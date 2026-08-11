# Topic 102: Linux Installation and Package Management

## 102.1 Design hard disk layout

A disk layout should reflect workload, recovery needs, firmware, encryption, growth and backup strategy. Splitting data into filesystems can contain failures and apply different mount options, but every extra boundary also creates a capacity-planning decision.

### Common layout decisions

| Mount or area | Why it may be separate |
|---|---|
| `/` | Required root filesystem containing the operating system |
| `/boot` | Keeps kernels and boot files accessible to the boot loader |
| EFI System Partition | FAT-formatted partition used by UEFI firmware |
| `/var` | Contains changing data such as logs, caches, queues and databases |
| `/home` | Separates user data from the operating system |
| swap | Supports memory pressure and, when sized/configured appropriately, hibernation |

There is no universal swap size formula. Consider RAM, workload, crash dumps, hibernation and storage performance.

### MBR, GPT and boot mode

MBR uses a small legacy partition table and normally supports four primary entries, one of which may be an extended partition containing logical partitions. GPT supports many partitions and large disks. GPT is commonly paired with UEFI, but GPT can also be used as a data disk on BIOS systems, and GRUB can boot GPT on BIOS systems when a BIOS boot partition is provided.

### LVM basics

Logical Volume Manager adds an abstraction layer:

```text
disk/partition -> physical volume (PV) -> volume group (VG) -> logical volume (LV) -> filesystem
```

Key commands:

```bash
pvs
vgs
lvs
lsblk -f
```

These read-only commands show LVM and filesystem state. Creating or resizing LVM storage is covered in the safe storage lab because the commands can destroy data if a target is wrong.

### Design example

For a small server with one system disk and one application-data disk:

- EFI System Partition when booting with UEFI
- `/boot` if encryption or platform design requires it
- LVM-backed root filesystem
- separate logical volume for `/var/lib/application`
- swap based on measured need
- backups stored outside the server

A separate partition is not a backup. Failure of the underlying disk can affect all partitions.

## 102.2 Install and configure a boot manager

### GRUB Legacy and GRUB 2

LPIC-1 requires recognition of both generations.

| Generation | Configuration commonly seen |
|---|---|
| GRUB Legacy | `/boot/grub/menu.lst`, `/boot/grub/grub.conf` |
| GRUB 2 | generated `/boot/grub/grub.cfg` or `/boot/grub2/grub.cfg` |

Do not normally edit generated `grub.cfg` directly. Change the distribution's source configuration, often `/etc/default/grub` and scripts in `/etc/grub.d`, then regenerate it.

A recoverable design can keep an older known-good kernel entry, a rescue entry,
and bootable recovery media. On mirrored or multi-disk systems, boot-loader
installation and EFI boot entries must match the actual redundancy design;
having a copied `/boot` directory alone does not guarantee that firmware can
start from the alternate disk. Test the backup boot path during maintenance.

### Inspect GRUB safely

```bash
grub-install --version 2>/dev/null || grub2-install --version
grep '^GRUB_' /etc/default/grub
sudo grub-mkconfig -o /tmp/grub.cfg.test
```

RPM-based distributions may name the generator `grub2-mkconfig`. Generating to `/tmp` is a safe way to inspect syntax without replacing the active configuration.

### Installation concepts

`grub-install` installs boot-loader components to a device or EFI environment. The correct target and options depend on BIOS versus UEFI, architecture, mounted ESP and distribution packaging. Never copy a `grub-install /dev/sda` example onto an unknown machine. Confirm boot mode, disk layout and the distribution's recovery procedure first.

In UEFI, firmware loads an `.efi` executable from the EFI System Partition. In legacy BIOS boot, firmware begins execution through the selected boot disk's boot path. GRUB then loads its modules, configuration, kernel and initramfs.

### GRUB shell awareness

Useful GRUB commands include `ls`, `set`, `insmod`, `linux`, `initrd`, and `boot`. Device syntax such as `(hd0,gpt2)` is GRUB syntax, not a Linux `/dev` path.

## 102.3 Manage shared libraries

Shared libraries allow multiple programs to use common compiled code. Dynamic executables record required library names; the dynamic linker finds and maps those libraries at runtime.

```bash
file /bin/ls
ldd /bin/ls
ldconfig -p | head
```

| Command | Purpose |
|---|---|
| `file` | Identifies executable format and linkage information |
| `ldd` | Displays shared-library dependencies; use it only on trusted executables |
| `ldconfig -p` | Prints libraries known to the linker cache |

Typical library directories include `/lib`, `/usr/lib`, and architecture-specific subdirectories. Configuration can be stored in `/etc/ld.so.conf` and included files. Root refreshes the cache with:

```bash
sudo ldconfig
```

`LD_LIBRARY_PATH` temporarily adds search directories for a process:

```bash
LD_LIBRARY_PATH=/opt/example/lib /opt/example/bin/app
```

Avoid setting it globally without a strong reason; loading an unintended library can break software or create a security risk.

## 102.4 Debian package management

`dpkg` manages installed `.deb` packages. APT resolves repositories and dependencies at a higher level.

```bash
sudo apt update
apt list --upgradable
sudo apt install nginx
apt show nginx
dpkg -L nginx
dpkg -S /usr/sbin/nginx
```

| Line | Meaning |
|---|---|
| `apt update` | Refreshes repository metadata; it does not upgrade packages |
| `apt list --upgradable` | Lists packages for which a newer candidate exists |
| `apt install` | Resolves dependencies and installs the package |
| `apt show` | Shows repository package metadata |
| `dpkg -L` | Lists files installed by an installed package |
| `dpkg -S` | Finds the installed package owning a path |

Low-level operations:

```bash
sudo dpkg -i ./package.deb
dpkg-query -W 'nginx*'
dpkg --verify nginx
sudo dpkg-reconfigure tzdata
apt-cache policy nginx
apt-get --simulate upgrade
```

`dpkg -i` does not obtain missing dependencies by itself. `dpkg --verify`
compares selected installed-file metadata when the package records it; output
must be interpreted and is not a complete intrusion-detection system.
`apt-get` is the stable command-line-oriented APT interface commonly used in
scripts; `--simulate` calculates actions without applying them. Repository
definitions are commonly under `/etc/apt/sources.list` and
`/etc/apt/sources.list.d/`. Verify repository origin and signing configuration
before trusting packages.

To find a path in a package that is not installed, Debian-family systems can
use `apt-file` when the package and its index are available:

```bash
sudo apt install apt-file
sudo apt-file update
apt-file search '/usr/bin/example-name'
```

`dpkg -S` searches installed package ownership; `apt-file search` searches the
downloaded contents index, so their scopes are different.

Removal differs:

```bash
sudo apt remove package-name
sudo apt purge package-name
```

`remove` normally leaves package configuration managed as conffiles; `purge` removes those package configuration files too. User data is not guaranteed to be deleted.

## 102.5 RPM, YUM, DNF and Zypper

`rpm` is the low-level package database and file-format tool. DNF/YUM and Zypper use repositories and resolve dependencies.

### RPM queries and verification

```bash
rpm -q bash
rpm -qi bash
rpm -ql bash
rpm -qf /bin/bash
rpm -V bash
rpm -K ./package.rpm
sudo rpm -Uvh ./package.rpm
sudo rpm -e package-name
```

| Option | Meaning |
|---|---|
| `-q` | Query |
| `-i` with query | Display package information |
| `-l` | List files |
| `-f` | Find the owner of a file |
| `-V` | Verify installed files against package metadata |
| `-K` | Check package signatures/digests |

Verification differences require interpretation; they do not automatically mean compromise because configuration files can change legitimately.

`rpm -Uvh` installs or upgrades a local RPM and `rpm -e` removes an installed
package. Because low-level RPM does not resolve repository dependencies in the
same way as DNF/YUM or Zypper, prefer the distribution's repository manager for
normal administration.

### DNF and YUM

```bash
sudo dnf makecache
dnf info nginx
dnf repoquery --whatprovides '*/example-file'
sudo dnf install nginx
sudo dnf upgrade nginx
sudo dnf reinstall nginx
sudo dnf remove nginx
dnf history
```

`yum` may be a compatibility command backed by DNF on current RPM-based distributions. Know both names because the objective includes YUM and awareness of DNF.

Global YUM/DNF settings may be read from `/etc/yum.conf`, with repository files
normally under `/etc/yum.repos.d/`. `repoquery` functionality may require a
plugin package on some releases.

### Zypper

```bash
sudo zypper refresh
zypper search nginx
zypper info nginx
sudo zypper install nginx
sudo zypper update nginx
sudo zypper remove nginx
zypper repos
```

Repository configuration is commonly stored under `/etc/yum.repos.d/` on DNF/YUM systems. SUSE uses its own repository management through Zypper.

### Extract without installing

On RPM systems, `rpm2cpio` converts an RPM payload for extraction:

```bash
mkdir rpm-content && cd rpm-content
rpm2cpio ../package.rpm | cpio -idmv
```

This extracts into the current directory. Inspect paths and use a disposable directory.

## 102.6 Linux as a virtualization guest

A virtual machine emulates or exposes virtual hardware and runs its own kernel. A container isolates processes while normally sharing the host kernel. An IaaS instance commonly combines compute, virtual networking, block storage, metadata and an operating-system image.

A system image is a reusable filesystem or disk template used to create virtual
machines and cloud instances. A container image is a layered application
filesystem plus metadata; it does not normally contain a separate running
kernel. Images should be patched, scanned, versioned and prepared so that
instance-specific identity and secrets are generated at deployment time.

### Guest integration

Guest agents and optimized drivers can provide clean shutdown, time coordination, network/storage performance, IP reporting and snapshot support. Examples include QEMU guest agent, VMware tools and Hyper-V Linux integration services.

### Cloning safely

A template must not produce clones with the same identity or secret host keys. Depending on distribution and provisioning system, review:

- `/etc/machine-id`
- SSH host keys under `/etc/ssh/`
- DHCP leases
- persistent network rules and MAC-address matches
- hostname
- cloud-init instance state
- application secrets and logs

Do not delete identity files from a running production machine. Prepare templates using distribution and platform procedures, then verify that two test clones receive different machine IDs and SSH host-key fingerprints.

Inspect cloud-init:

```bash
cloud-init status --long
systemctl status cloud-init.service
ls -l /var/lib/cloud/instances
```

## Lab 102: Compare package families

On a Debian-family and an RPM-family VM:

1. Refresh repository metadata.
2. Find the package providing a chosen executable.
3. Display package metadata and installed files.
4. Install a harmless utility such as `tree`.
5. Verify which package owns its executable.
6. Remove it.
7. Record the equivalent command in each family.

Do not add third-party repositories for this lab.

## Exercises

1. **102-Q1:** Explain why a separate partition is not a backup.
2. **102-Q2:** What are PV, VG and LV in LVM?
3. **102-Q3:** Why should generated `grub.cfg` normally not be edited directly?
4. **102-Q4:** Which command lists the shared libraries required by `/bin/cp`?
5. **102-Q5:** Contrast `apt update` and `apt upgrade`.
6. **102-Q6:** Write Debian and RPM commands to find the installed package owning a file.
7. **102-Q7:** Name four identities or secrets that must be considered when cloning a Linux VM.

Answers are in [the answer key](../exercises/answers.md#topic-102-answers).

## Official reading

- [GNU GRUB manual](https://www.gnu.org/software/grub/manual/grub/)
- [Debian package management reference](https://www.debian.org/doc/manuals/debian-reference/ch02.en.html)
- [RPM documentation](https://rpm.org/docs/)
- [DNF documentation](https://dnf.readthedocs.io/)
- [Zypper documentation](https://documentation.suse.com/smart/systems-management/html/zypper/index.html)
