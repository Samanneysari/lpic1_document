# Topic 104: Devices, Linux Filesystems and the FHS

> [!CAUTION]
> Partitioning, formatting and repair commands can destroy data. Use a VM snapshot and a separate disposable lab disk. Replace example device names only after checking `lsblk -f` and `findmnt`.

## 104.1 Create partitions and filesystems

### Device naming and partition tables

Linux represents storage as block devices. A partition table describes regions of a disk; a filesystem organizes files inside a partition or logical volume.

```bash
lsblk -o NAME,PATH,SIZE,TYPE,PTTYPE,FSTYPE,MOUNTPOINTS
sudo fdisk -l
```

`PTTYPE` can reveal `dos`/MBR or `gpt`. Names differ by device: `/dev/vdb1`, `/dev/sdb1`, and `/dev/nvme1n1p1` can all be first partitions.

Tools named by the objective:

| Tool | Normal role |
|---|---|
| `fdisk` | Interactive MBR and modern GPT partitioning |
| `gdisk` | GPT-focused interactive partitioning |
| `parted` | Scriptable/interactive partitioning with size units |

Before changing anything:

```bash
lsblk -f
findmnt
sudo blkid
```

### Filesystem creation

After confirming that `/dev/vdb1` is disposable and unmounted:

```bash
sudo mkfs.ext4 -L LABDATA /dev/vdb1
```

| Part | Meaning |
|---|---|
| `mkfs.ext4` | Creates an ext4 filesystem |
| `-L LABDATA` | Assigns a filesystem label |
| `/dev/vdb1` | Target partition; existing data is overwritten |

Recognize these constructors:

```bash
mkfs.ext2
mkfs.ext3
mkfs.ext4
mkfs.xfs
mkfs.vfat
mkfs.exfat
```

The required package and available options vary by distribution. XFS is a journaling filesystem designed for scalability. VFAT/exFAT are useful for interoperability but do not provide normal Unix ownership and permission semantics like ext4 or XFS.

### Btrfs awareness

Btrfs supports features such as subvolumes, checksums, transparent compression and multi-device filesystems. A subvolume is not the same thing as a disk partition. Basic inspection:

```bash
sudo btrfs filesystem show
sudo btrfs subvolume list /mountpoint
```

These require Btrfs tools and an appropriate mounted filesystem.

### Swap

For a confirmed disposable partition:

```bash
sudo mkswap -L LABSWAP /dev/vdb2
sudo swapon /dev/vdb2
swapon --show
sudo swapoff /dev/vdb2
```

`mkswap` writes a swap signature, `swapon` activates it, and `swapoff` deactivates it. A swap entry in `/etc/fstab` is activated with `swapon --all`, not `mount -a`.

## 104.2 Maintain filesystem integrity

### Space and inode monitoring

```bash
df -hT
df -i
du -sh /var/* 2>/dev/null
```

| Command | Meaning |
|---|---|
| `df -hT` | Mounted filesystem capacity and type |
| `df -i` | Inode consumption |
| `du -sh` | Summarizes space reachable under each argument |

A filesystem can report “no space left” because blocks are full or because inodes are exhausted.

### Offline repair principle

Do not run a modifying filesystem check on a mounted writable filesystem. Stop services, unmount it and ensure you selected the correct device. The root filesystem usually requires rescue/recovery boot for offline repair.

Ext-family tools:

```bash
sudo e2fsck -f /dev/vdb1
sudo tune2fs -l /dev/vdb1
```

`fsck` is a front end that selects an appropriate checker. `e2fsck` handles ext2/3/4. `mke2fs` creates ext filesystems, and `tune2fs` inspects or changes selected ext filesystem parameters.

XFS tools:

```bash
sudo xfs_repair -n /dev/vdb1
sudo xfs_db -r /dev/vdb1
```

`xfs_repair -n` performs a no-modify diagnostic pass. XFS does not use `fsck` in the same way as ext filesystems. `xfs_fsr` reorganizes files to improve layout; it is not a general corruption repair command.

Always read the local manual and maintain a verified backup. A repair tool can discard unrecoverable metadata to make a filesystem consistent.

## 104.3 Control mounting and unmounting

Mounting attaches a filesystem to the single Linux directory tree.

```bash
sudo mkdir -p /mnt/labdata
sudo mount /dev/vdb1 /mnt/labdata
findmnt /mnt/labdata
sudo umount /mnt/labdata
```

The command is `umount`, not `unmount`. An unmount can fail when a process has an open file or working directory there:

```bash
sudo fuser -vm /mnt/labdata
sudo lsof +f -- /mnt/labdata
```

### `/etc/fstab`

Prefer stable identifiers such as UUID or labels over changeable device letters.

```fstab
UUID=11111111-2222-3333-4444-555555555555 /srv/data ext4 defaults,nofail 0 2
```

Fields:

| Position | Meaning |
|---:|---|
| 1 | Source device, UUID or label |
| 2 | Mount point |
| 3 | Filesystem type |
| 4 | Comma-separated options |
| 5 | Legacy dump field |
| 6 | Filesystem-check order; root commonly `1`, other checked filesystems `2`, disabled `0` |

Safe edit workflow:

```bash
sudo cp --archive /etc/fstab /etc/fstab.before-lab
sudoedit /etc/fstab
sudo findmnt --verify --verbose
sudo mount -a
findmnt /srv/data
```

`mount -a` processes mountable fstab entries but does not activate swap entries. A bad fstab can disrupt boot, so keep console or recovery access.

Useful options include `ro`, `rw`, `noexec`, `nosuid`, `nodev`, `noauto`, `user`, `users`, and `nofail`. Their effect depends on filesystem and context; they are layers of risk reduction, not universal security barriers.

For a removable filesystem that a non-root user may mount manually, an
administrator can create a narrowly scoped entry such as:

```fstab
LABEL=LABUSB /media/labusb vfat noauto,user,nodev,nosuid 0 0
```

`noauto` keeps `mount -a` from mounting it. `user` permits the user who mounts
it to unmount it, whereas `users` permits any user to unmount it. The mount
point must already exist and the policy must match the local threat model.

systemd can represent mounts as `.mount` units and automatically generates units from `/etc/fstab`.

## 104.5 Permissions and ownership

### Permission model

```text
-rwxr-x--- 1 alice developers 1200 Jan 1 12:00 deploy.sh
```

The first character is file type. The next groups are permissions for owner, group and others.

| Permission | File | Directory |
|---|---|---|
| `r` | Read contents | List names |
| `w` | Modify contents | Create/delete/rename entries when traversal is also allowed |
| `x` | Execute as a program | Traverse/search the directory |

### Change ownership and modes

```bash
sudo chown alice:developers deploy.sh
sudo chgrp developers deploy.sh
chmod u=rwx,g=rx,o= deploy.sh
chmod 750 deploy.sh
```

Octal values are sums: read 4, write 2, execute 1. `750` means owner 7 (`rwx`), group 5 (`r-x`), others 0.

### Special bits

| Bit | Symbol | Typical effect |
|---|---|---|
| setuid | `u+s`, numeric 4xxx | Executable runs with file owner's effective UID when supported |
| setgid | `g+s`, numeric 2xxx | Executable uses file group; directory makes new entries inherit its group |
| sticky | `+t`, numeric 1xxx | Shared directory restricts deletion/rename to permitted owners/root |

```bash
sudo install -d -o root -g developers -m 2775 /srv/team
chmod 1777 /tmp-example
```

Setuid scripts are generally not honored safely on Linux; setuid executables require careful auditing.

### umask

The umask removes permission bits from an application's requested mode. It is not best understood as simple decimal subtraction.

```bash
umask
umask 027
touch new-file
mkdir new-directory
```

With a typical requested file mode of 666 and directory mode of 777, umask 027 commonly produces file mode 640 and directory mode 750. Applications can request more restrictive modes.

## 104.6 Hard and symbolic links

A hard link is another directory entry for the same inode. A symbolic link is a separate file containing a path to a target.

```bash
printf 'data\n' > original.txt
ln original.txt hard-link.txt
ln -s original.txt symbolic-link.txt
ls -li original.txt hard-link.txt symbolic-link.txt
```

| Property | Hard link | Symbolic link |
|---|---|---|
| Inode | Same as target | Own inode |
| Crosses filesystems | No | Yes |
| Can normally target directory | Hard links to directories are prohibited in normal Linux administration | Yes |
| Target removed | Data remains while another hard link exists | Link becomes dangling |

Relative symbolic targets are resolved relative to the directory containing the symbolic link, not the shell's current directory at access time.

## 104.7 Find and place system files

### FHS overview

| Path | Purpose |
|---|---|
| `/etc` | Host-specific system configuration |
| `/var` | Variable data such as logs, caches, spools and application state |
| `/usr` | Shareable, mostly read-only userland programs and data |
| `/bin`, `/sbin`, `/lib` | Essential paths; often symlinks into `/usr` on merged-usr systems |
| `/home` | Normal user home directories |
| `/root` | Root user's home directory |
| `/tmp` | Temporary files, often cleared according to local policy |
| `/run` | Volatile runtime state since boot |
| `/opt` | Add-on application software |
| `/srv` | Data served by this system |
| `/mnt` | Temporary administrator mounts |
| `/media` | Removable media mount points |

### Find commands and files

```bash
type -a passwd
command -v passwd
whereis passwd
find /usr/share/man -type f -name 'passwd*'
locate '/passwd'
```

`locate` searches a database, so very new or removed files may not be reflected until `updatedb` refreshes it. `/etc/updatedb.conf` controls exclusions on implementations that use it.

## Lab 104: Disposable filesystem

Using a dedicated empty virtual disk:

1. Prove which device is disposable with `lsblk` and `findmnt`.
2. Create a GPT and one partition using one approved partitioning tool.
3. Create an ext4 filesystem with label `LABDATA`.
4. Mount it temporarily and verify it.
5. Create files and inspect block and inode consumption.
6. Add a UUID-based fstab entry with `nofail`.
7. Validate fstab before reboot.
8. Unmount it and perform a read-only or non-modifying filesystem check.
9. Remove the fstab lab entry before deleting the VM disk.

Have an instructor or experienced administrator review the selected device before the formatting step.

## Exercises

1. **104-Q1:** Why is `/dev/vdb1` only an example and never safe to assume?
2. **104-Q2:** Contrast `df` and `du`.
3. **104-Q3:** Why must an ext filesystem normally be unmounted before repair?
4. **104-Q4:** Explain all six fields in an fstab entry.
5. **104-Q5:** Calculate the symbolic permissions represented by `2750`.
6. **104-Q6:** Why is umask not simply decimal subtraction?
7. **104-Q7:** What survives when the original filename of a hard-linked file is deleted?
8. **104-Q8:** Why can `locate` return stale results?

Answers are in [the answer key](../exercises/answers.md#topic-104-answers).

## Official reading

- [util-linux](https://www.kernel.org/pub/linux/utils/util-linux/)
- [Linux man-pages](https://www.kernel.org/doc/man-pages/)
- [Filesystem Hierarchy Standard](https://refspecs.linuxfoundation.org/fhs.shtml)
