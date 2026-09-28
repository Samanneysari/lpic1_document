# Topic 104: Devices, Linux Filesystems and the FHS

> [!CAUTION]
> Partitioning, formatting and repair commands can destroy data. Use a VM snapshot and a separate disposable lab disk. Replace example device names only after checking `lsblk -f` and `findmnt`.

## 104.1 Create partitions and filesystems

### Device naming and partition tables

Linux represents storage as block devices. A partition table describes regions of a disk; a filesystem organizes files inside a partition or logical volume.

A **block device** reads and writes numbered chunks of data, typically a disk. Its **logical block size** is the unit exposed for addressing by the device; a filesystem also has its own allocation block size. These are related but need not be identical. In `dd bs=1M`, `bs` is the size per copy operation, not proof of the disk's physical sector size. A **partition** is a named region of a disk. A **partition table** records the regions; **MBR** is an older table format, while **GPT** supports more entries and includes backup metadata. Neither format creates files by itself. `fdisk` edits the partition table; `mkfs.ext4` creates a filesystem in a chosen region. Finally, `mount` connects that filesystem to a directory in the Linux tree.

Read-only inspection, one command per line:

```bash
lsblk -o NAME,SIZE,TYPE,LOG-SEC,PHY-SEC,PTTYPE,FSTYPE,MOUNTPOINTS
```

`lsblk` shows block devices; `-o` selects columns. `LOG-SEC` and `PHY-SEC` are logical and physical sector sizes, `PTTYPE` is the partition-table type, `FSTYPE` is the filesystem type, and `MOUNTPOINTS` shows where it is attached. A blank field is possible and does not by itself indicate a broken disk.

```bash
stat -f .
```

`stat` inspects metadata; `-f` requests information about the filesystem containing `.` rather than one file; the output can include filesystem block-size fields. Distinguish the filesystem's block size from the device sector sizes shown by `lsblk` and from `dd`'s chosen copy size.

```bash
sudo fdisk -l
```

`sudo` requests privileged execution under local policy; `fdisk` is the partition-table tool; `-l` **lists** disks and partitions without editing them. Starting interactive `fdisk /dev/...` is a different operation; writing changes there can destroy access to data. Match model, size and identifier before any lab write.

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

**Swap** is disk-backed space the kernel may use for memory pages it does not need in RAM right now; it is far slower than RAM and is not a substitute for sufficient memory. In the example, `mkswap -L LABSWAP` writes a swap signature and label on the selected disposable partition; `swapon` enables that exact partition; `swapon --show` verifies active swap; `swapoff` disables it. Never use `mkswap` on a partition containing files you need.

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

An **inode** is a filesystem record containing a file's metadata, such as ownership, permissions, size and data locations. A directory maps a **name** to an inode number. An inode number is unique within one filesystem, not globally across the machine. A hard link gives the same inode another name. Some filesystems represent or account for metadata differently, but these concepts explain ordinary Unix file operations. `df` reports free/used space for a mounted filesystem; `du` walks files reachable from a path and adds their allocated usage. They can differ because of metadata, snapshots, deleted files still open by a process or inaccessible paths.

```bash
df -h .
```

`df` reports filesystem capacity; `-h` uses readable units; `.` selects the filesystem containing your current directory.

```bash
du -sh .
```

`du` walks your current directory; `-s` gives one summary and `-h` uses readable units. This is usage under the directory, not the whole disk's free space.

```bash
stat hello.txt
```

`stat` displays metadata for the named file, including inode number, allocated blocks, ownership and timestamps. Create `hello.txt` in the [practice area](00-linux-foundations.md#4-your-first-shell-session) first. `Access` (atime) is last recorded read, `Modify` (mtime) is the last content modification, and `Change` (ctime) is the last **inode-status** change, including a content or permission change. **ctime is not creation time**. Some filesystems show `Birth` for creation; access-time updates may be deferred or disabled by mount policy.

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

The directory used for attachment is a **mount point**. Before mounting, `/mnt/labdata` is just a directory; after mounting, paths below it refer to the attached filesystem. Files previously visible beneath that directory can be hidden until unmounting. `lsblk` shows devices and mount points; `findmnt` shows the active mount relationship. A filesystem type such as ext4 describes how files are organized; mounting makes that organization accessible at a path.

```bash
sudo mkdir -p /mnt/labdata
sudo mount /dev/vdb1 /mnt/labdata
findmnt /mnt/labdata
sudo umount /mnt/labdata
```

In the lab block above, `mkdir -p` makes the mount-point directory, `mount` attaches `/dev/vdb1` there, `findmnt` verifies the active attachment, and `umount` detaches it. These commands are **separate lines**: check that the example partition exists, contains the expected filesystem and is disposable before running `mount`. Read-only `findmnt /` is safe to try on your current system without attaching anything.

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

systemd mount units end in `.mount`; the unit name is derived from the escaped
mount path, so `/srv/data` becomes `srv-data.mount`. systemd also generates
mount units from `/etc/fstab`. Inspect them with:

```bash
systemctl status srv-data.mount
systemd-escape --path --suffix=mount /srv/data
```

## 104.5 Permissions and ownership

### Permission model

Regular files contain ordinary data. A directory maps names to files. A symbolic link stores a target path. A block device represents block-oriented I/O; a character device handles a stream of bytes; a FIFO (named pipe) passes a stream between processes; a socket is a communication endpoint. The first character of `ls -l` commonly shows `-`, `d`, `l`, `b`, `c`, `p` or `s` respectively. A hard link is an additional name for a file, not a separate file type.

```bash
ls -ld . /dev/null
```

`ls` lists metadata; `-l` gives the detailed type/permission string; `-d` shows the directory entry `.` itself. Expect `d` for `.` and normally `c` for the character device `/dev/null`.

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

Practice on a file you own, created in your [practice directory](00-linux-foundations.md#4-your-first-shell-session):

```bash
chmod 640 hello.txt
```

`chmod` changes permission bits; `640` gives the owner read/write (`6`), the group read (`4`) and others no access (`0`); `hello.txt` is the target. `ls -l hello.txt` verifies the result. The owner can normally change the mode of their own file.

```bash
stat -c '%U:%G %a %n' hello.txt
```

`stat` reads metadata; `-c` selects a format; `%U` is owner name, `%G` group name, `%a` octal mode and `%n` filename. This command does not change anything.

In a disposable VM, an administrator can change ownership with `sudo chown alice:developers hello.txt`: `sudo` requests permission to run as root, `chown` changes ownership, `alice:developers` sets user and group, and `hello.txt` is the target. The account and group must exist. Replacing them with names from another machine will fail; changing ownership can also remove your own ability to edit the file.

### Special bits

| Bit | Symbol | Typical effect |
|---|---|---|
| setuid | `u+s`, numeric 4xxx | Executable runs with file owner's effective UID when supported |
| setgid (SGID) | `g+s`, numeric 2xxx | Executable uses file group; directory makes new entries inherit its group |
| sticky | `+t`, numeric 1xxx | Shared directory restricts deletion/rename to permitted owners/root |

On a writable shared directory, the **sticky bit** lets users create files but stops one ordinary user from deleting or renaming another user's entries merely because the directory is writable. It does not encrypt files or make their contents private. `/tmp` is a common example. The directory's other permissions still apply.

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

Deleting one hard-link name leaves the content reachable through the other name until all links are removed and no process still holds the file open. A symbolic link can point across filesystems and can become dangling when its target path disappears.

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

Linux uses **one directory tree** beginning at `/`, even when files come from several disks. A slash separates path components: `/home/alice/report.txt` names a file under `home`, then `alice`. `/` is the root directory; `/root` is the root account's home and means something different. `ls /` lists top-level names; `cd /etc` changes your shell into the configuration directory; `pwd` confirms your current location. The Filesystem Hierarchy Standard (FHS) describes conventional uses for important directories, though distributions can differ.

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
