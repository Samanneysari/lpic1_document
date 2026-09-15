# LPIC-1 Version 5.0 Coverage Matrix

This matrix follows the currently published English LPIC-1 objectives for
exam codes `101-500` and `102-500`. It maps each objective's knowledge areas
and named files, terms and utilities to teaching evidence—not merely to a
chapter title.

The LPI utility lists are explicitly partial, so passing a string-presence
check is not the completion standard. A learner should understand the purpose,
important options, output and failure modes described in the linked section.

## Exam 101-500

### Topic 101: System Architecture

| Done | Objective and weight | Published knowledge-area coverage | Named scope covered | Evidence |
|---|---|---|---|---|
| [ ] | **101.1** Hardware settings (2) | Integrated peripherals; storage types; device resources; hardware-listing and USB tools; sysfs, udev and D-Bus | `/sys/`, `/proc/`, `/dev/`, `modprobe`, `lsmod`, `lspci`, `lsusb` | [101.1](docs/101-system-architecture.md#1011-determine-and-configure-hardware-settings), [LAB-101-1](labs/README.md#lab-101-1-hardware-inventory) |
| [ ] | **101.2** Boot the system (3) | Bootloader/kernel parameters; BIOS/UEFI-to-login sequence; SysVinit/systemd; Upstart awareness; boot logs | `dmesg`, `journalctl`, BIOS, UEFI, bootloader, kernel, initramfs, init, SysVinit, systemd | [101.2](docs/101-system-architecture.md#1012-boot-the-system), [LAB-101-2](labs/README.md#lab-101-2-boot-evidence) |
| [ ] | **101.3** Runlevels, targets, shutdown and reboot (3) | Set/change defaults; rescue/single-user mode; clean shutdown/reboot; user notification; process termination; acpid awareness | `/etc/inittab`, `/etc/init.d/`, `init`, `telinit`, `shutdown`, `systemctl`, `/etc/systemd/`, `/usr/lib/systemd/`, `wall`, acpid | [101.3](docs/101-system-architecture.md#1013-runlevels-boot-targets-shutdown-and-reboot), [LAB-101-3](labs/README.md#lab-101-3-targets-and-shutdown) |

### Topic 102: Linux Installation and Package Management

| Done | Objective and weight | Published knowledge-area coverage | Named scope covered | Evidence |
|---|---|---|---|---|
| [ ] | **102.1** Disk layout (2) | Allocate filesystems/swap; workload-based layout; boot constraints; LVM basics | `/`, `/var`, `/home`, `/boot`, ESP, swap, mount points, partitions, PV/VG/LV | [102.1](docs/102-installation-package-management.md#1021-design-hard-disk-layout), [LAB-102-1](labs/README.md#lab-102-1-disk-layout-design) |
| [ ] | **102.2** Boot manager (2) | Backup boot choices; GRUB Legacy install/configuration; GRUB 2 changes; bootloader interaction | `menu.lst`, `grub.conf`, `grub.cfg`, `grub-install`, `grub-mkconfig`, MBR | [102.2](docs/102-installation-package-management.md#1022-install-and-configure-a-boot-manager), [LAB-102-2](labs/README.md#lab-102-2-grub-inspection-and-recovery-plan) |
| [ ] | **102.3** Shared libraries (1) | Identify dependencies and library locations; configure loading/cache | `ldd`, `ldconfig`, `/etc/ld.so.conf`, `LD_LIBRARY_PATH` | [102.3](docs/102-installation-package-management.md#1023-manage-shared-libraries) |
| [ ] | **102.4** Debian packages (3) | Install/upgrade/remove; search installed and uninstalled file ownership; inspect version, contents, dependencies, integrity and state; APT awareness | `/etc/apt/sources.list`, `dpkg`, `dpkg-reconfigure`, `apt`, `apt-get`, `apt-cache`, `apt-file` | [102.4](docs/102-installation-package-management.md#1024-debian-package-management), [LAB-102-3](labs/README.md#lab-102-3-package-equivalence) |
| [ ] | **102.5** RPM/YUM/Zypper (3) | Install/reinstall/upgrade/remove; query metadata, dependency, integrity and signature state; file ownership/provision; DNF awareness | `rpm`, `rpm2cpio`, `/etc/yum.conf`, `/etc/yum.repos.d/`, `yum`, `dnf`, `zypper` | [102.5](docs/102-installation-package-management.md#1025-rpm-yum-dnf-and-zypper), [LAB-102-3](labs/README.md#lab-102-3-package-equivalence) |
| [ ] | **102.6** Virtualization guest (1) | VMs and system/application containers; IaaS compute/storage/networking; images; clone identity; integration drivers; cloud-init | VM, Linux/application container, guest drivers, SSH host keys, D-Bus machine ID | [102.6](docs/102-installation-package-management.md#1026-linux-as-a-virtualization-guest), [LAB-102-4](labs/README.md#lab-102-4-clone-identity-audit) |

### Topic 103: GNU and Unix Commands

| Done | Objective and weight | Published knowledge-area coverage | Named scope covered | Evidence |
|---|---|---|---|---|
| [ ] | **103.1** Command line (4) | Single commands/sequences; environment variables; history; commands inside/outside PATH | Bash, `echo`, `env`, `export`, `pwd`, `set`, `unset`, `type`, `which`, `man`, `uname`, `history`, `.bash_history`, quoting | [103.1](docs/103-gnu-unix-commands.md#1031-work-on-the-command-line), [LAB-103-1](labs/README.md#lab-103-1-command-line-and-filters) |
| [ ] | **103.2** Text filters (2) | Select, transform, combine, sort, count, checksum, split and decompress text streams | `bzcat`, `cat`, `cut`, `head`, `less`, `md5sum`, `nl`, `od`, `paste`, `sed`, SHA sums, `sort`, `split`, `tail`, `tr`, `uniq`, `wc`, `xzcat`, `zcat` | [103.2](docs/103-gnu-unix-commands.md#1032-process-text-streams-with-filters), [LAB-103-1](labs/README.md#lab-103-1-command-line-and-filters) |
| [ ] | **103.3** File management (4) | Individual/recursive copy, move and removal; simple/advanced globs; `find` by type/size/time and actions; tar/cpio/dd | `cp`, `find`, `mkdir`, `mv`, `ls`, `rm`, `rmdir`, `touch`, `tar`, `cpio`, `dd`, `file`, gzip/bzip2/xz families, globbing | [103.3](docs/103-gnu-unix-commands.md#1033-perform-basic-file-management), [LAB-103-2](labs/README.md#lab-103-2-files-and-archives) |
| [ ] | **103.4** Streams, pipes and redirects (4) | stdin/stdout/stderr; pipes; command output as arguments; simultaneous screen/file output | file descriptors, `>`, `>>`, `<`, `2>`, `2>&1`, pipe, `tee`, `xargs` | [103.4](docs/103-gnu-unix-commands.md#1034-streams-pipes-and-redirection), [LAB-103-1](labs/README.md#lab-103-1-command-line-and-filters) |
| [ ] | **103.5** Processes (4) | Foreground/background jobs; survive logout; monitor/select/sort; signals | `&`, `bg`, `fg`, `jobs`, `kill`, `nohup`, `ps`, `top`, `free`, `uptime`, `pgrep`, `pkill`, `killall`, `watch`, `screen`, `tmux` | [103.5](docs/103-gnu-unix-commands.md#1035-create-monitor-and-stop-processes), [LAB-103-3](labs/README.md#lab-103-3-jobs-and-processes) |
| [ ] | **103.6** Process priorities (2) | Default/inherited nice value; launch with priority; alter a running process | `nice`, `renice`, `ps`, `top` | [103.6](docs/103-gnu-unix-commands.md#1036-process-priorities), [LAB-103-3](labs/README.md#lab-103-3-jobs-and-processes) |
| [ ] | **103.7** Regular expressions (3) | BRE versus ERE; special characters, classes, quantifiers and anchors; filesystem/content search; delete/change/substitute | `grep`, `egrep`/`grep -E`, `fgrep`/`grep -F`, `sed`, `regex(7)` | [103.7](docs/103-gnu-unix-commands.md#1037-regular-expressions), [LAB-103-4](labs/README.md#lab-103-4-regex-and-vi) |
| [ ] | **103.8** Basic file editing (3) | vi modes/navigation; insert/edit/delete/yank/paste/search; other editors; default editor | `vi`, `/`, `?`, `h/j/k/l`, `i/o/a`, `d/p/y/dd/yy`, `ZZ`, `:w!`, `:q!`, `EDITOR`; Vim, Nano, Emacs | [103.8](docs/103-gnu-unix-commands.md#1038-basic-file-editing-with-vi), [LAB-103-4](labs/README.md#lab-103-4-regex-and-vi) |

### Topic 104: Devices, Linux Filesystems and FHS

| Done | Objective and weight | Published knowledge-area coverage | Named scope covered | Evidence |
|---|---|---|---|---|
| [ ] | **104.1** Partitions/filesystems (2) | MBR/GPT; ext2/3/4, XFS, VFAT, exFAT creation; Btrfs multi-device/compression/subvolumes; swap | `fdisk`, `gdisk`, `parted`, `mkfs*`, `mkswap` | [104.1](docs/104-devices-filesystems-fhs.md#1041-create-partitions-and-filesystems), [LAB-104-1](labs/README.md#lab-104-1-disposable-filesystem) |
| [ ] | **104.2** Filesystem integrity (2) | Verify integrity; monitor blocks/inodes; simple offline repair; ext and XFS distinctions | `du`, `df`, `fsck`, `e2fsck`, `mke2fs`, `tune2fs`, `xfs_repair`, `xfs_fsr`, `xfs_db` | [104.2](docs/104-devices-filesystems-fhs.md#1042-maintain-filesystem-integrity), [LAB-104-1](labs/README.md#lab-104-1-disposable-filesystem) |
| [ ] | **104.3** Mounting (3) | Manual/boot mounts; user-mountable removable media; labels/UUIDs; systemd mount units | `/etc/fstab`, `/media/`, `mount`, `umount`, `blkid`, `lsblk`, `.mount` units | [104.3](docs/104-devices-filesystems-fhs.md#1043-control-mounting-and-unmounting), [LAB-104-1](labs/README.md#lab-104-1-disposable-filesystem) |
| [ ] | **104.5** Permissions/ownership (3) | Regular/special files and directories; SUID/SGID/sticky; creation mask; group access | `chmod`, `umask`, `chown`, `chgrp` | [104.5](docs/104-devices-filesystems-fhs.md#1045-permissions-and-ownership), [LAB-104-2](labs/README.md#lab-104-2-permissions-and-collaboration) |
| [ ] | **104.6** Links (2) | Create/identify hard and symbolic links; copying versus linking; administration use | `ln`, `ls`, inode and link count | [104.6](docs/104-devices-filesystems-fhs.md#1046-hard-and-symbolic-links), [LAB-104-2](labs/README.md#lab-104-2-permissions-and-collaboration) |
| [ ] | **104.7** FHS and locating files (2) | Correct FHS placement; find files/commands; purpose of important directories | `find`, `locate`, `updatedb`, `whereis`, `which`, `type`, `/etc/updatedb.conf` | [104.7](docs/104-devices-filesystems-fhs.md#1047-find-and-place-system-files) |

Objective 104.4 was removed from version 5.0 and has no study requirement.

## Exam 102-500

### Topic 105: Shells and Shell Scripting

| Done | Objective and weight | Published knowledge-area coverage | Named scope covered | Evidence |
|---|---|---|---|---|
| [ ] | **105.1** Shell environment (4) | Login/new-shell variables and PATH; functions; skeleton directory; global/user profiles | `.`, `source`, `/etc/bash.bashrc`, `/etc/profile`, `env`, `export`, `set`, `unset`, Bash startup files, function, alias | [105.1](docs/105-shells-shell-scripting.md#1051-customize-the-shell-environment), [LAB-105-1](labs/README.md#lab-105-1-shell-environment) |
| [ ] | **105.2** Simple scripts (4) | sh loops/tests; substitution/status/chaining; conditional mail; shebang; location, ownership, execute and SUID handling | `for`, `while`, `test`, `if`, `read`, `seq`, `exec`, `\|\|`, `&&` | [105.2](docs/105-shells-shell-scripting.md#1052-write-and-customize-simple-scripts), [LAB-105-2](labs/README.md#lab-105-2-defensive-bash-script) |

### Topic 106: User Interfaces and Desktops

| Done | Objective and weight | Published knowledge-area coverage | Named scope covered | Evidence |
|---|---|---|---|---|
| [ ] | **106.1** X11 (2) | Architecture/configuration; keyboard override; display/window/desktop components; remote display access; Wayland awareness | `/etc/X11/xorg.conf`, `/etc/X11/xorg.conf.d/`, `~/.xsession-errors`, `xhost`, `xauth`, `DISPLAY`, X | [106.1](docs/106-user-interfaces-desktops.md#1061-install-and-configure-x11), [LAB-106-1](labs/README.md#lab-106-1-desktop-session) |
| [ ] | **106.2** Graphical desktops (1) | Major desktops; remote desktop/session protocols | KDE, GNOME, Xfce, X11, XDMCP, VNC, SPICE, RDP | [106.2](docs/106-user-interfaces-desktops.md#1062-graphical-desktops-and-remote-access), [LAB-106-1](labs/README.md#lab-106-1-desktop-session) |
| [ ] | **106.3** Accessibility (1) | Visual settings/themes and assistive technologies | high contrast/large print, screen reader, Braille, magnifier, on-screen keyboard, sticky/repeat/slow/bounce/toggle keys, mouse keys, gestures, voice recognition | [106.3](docs/106-user-interfaces-desktops.md#1063-accessibility), [LAB-106-1](labs/README.md#lab-106-1-desktop-session) |

### Topic 107: Administrative Tasks

| Done | Objective and weight | Published knowledge-area coverage | Named scope covered | Evidence |
|---|---|---|---|---|
| [ ] | **107.1** Users/groups (5) | Add/modify/remove users/groups; password/group databases; special-purpose/limited accounts | `/etc/passwd`, `/etc/shadow`, `/etc/group`, `/etc/skel/`, `chage`, `getent`, `groupadd/del/mod`, `passwd`, `useradd/del/mod` | [107.1](docs/107-administrative-tasks.md#1071-user-and-group-administration), [LAB-107-1](labs/README.md#lab-107-1-account-lifecycle) |
| [ ] | **107.2** Scheduling (4) | Manage cron/at; access controls; systemd timers | cron directories/spool, allow/deny files, `/etc/crontab`, `crontab`, `at`, `atq`, `atrm`, `systemctl`, `systemd-run` | [107.2](docs/107-administrative-tasks.md#1072-schedule-administrative-jobs), [LAB-107-2](labs/README.md#lab-107-2-three-schedulers) |
| [ ] | **107.3** Localisation (3) | Locale variables and predictable `LANG=C`; timezone configuration; encoding conversion | `/etc/timezone`, `/etc/localtime`, `/usr/share/zoneinfo/`, `LC_*`, `LC_ALL`, `LANG`, `TZ`, `locale`, `tzselect`, `timedatectl`, `date`, `iconv`, UTF-8/ISO-8859/ASCII/Unicode | [107.3](docs/107-administrative-tasks.md#1073-localisation-and-internationalisation) |

### Topic 108: Essential System Services

| Done | Objective and weight | Published knowledge-area coverage | Named scope covered | Evidence |
|---|---|---|---|---|
| [ ] | **108.1** System time (3) | System/RTC time; UTC hardware clock; timezone; ntpd/Chrony configuration; pool service; ntpq awareness | zone/time files, `/etc/ntp.conf`, `/etc/chrony.conf`, `date`, `hwclock`, `timedatectl`, `ntpd`, `ntpdate`, `ntpq`, `chronyc`, pool.ntp.org | [108.1](docs/108-essential-system-services.md#1081-maintain-system-time) |
| [ ] | **108.2** Logging (4) | rsyslog facilities/priorities/actions and remote roles; journal query/filter/persistence/size/vacuum/offline access; rsyslog-journal interaction; logrotate; alternatives | `/etc/rsyslog.conf`, `/var/log/`, `logger`, `logrotate`, journal files/config, `journalctl`, `systemd-cat`, syslog/syslog-ng | [108.2](docs/108-essential-system-services.md#1082-system-logging), [LAB-108-1](labs/README.md#lab-108-1-logs-and-rotation) |
| [ ] | **108.3** MTA basics (3) | Aliases, user forwarding, Postfix/Sendmail/Exim awareness | `~/.forward`, `newaliases`, `mail`, `mailq`, Sendmail emulation layer | [108.3](docs/108-essential-system-services.md#1083-mail-transfer-agent-basics) |
| [ ] | **108.4** Printing (2) | Local/remote CUPS; queues/jobs; general troubleshooting; job removal | `/etc/cups/`, CUPS tools, `lpr`, `lprm`, `lpq` plus `lp`, `lpstat`, `cancel`, `lpadmin` | [108.4](docs/108-essential-system-services.md#1084-manage-printers-and-printing) |

### Topic 109: Networking Fundamentals

| Done | Objective and weight | Published knowledge-area coverage | Named scope covered | Evidence |
|---|---|---|---|---|
| [ ] | **109.1** Protocol fundamentals (4) | Masks/CIDR and public/private IPv4; required ports/services; TCP/UDP/ICMP; IPv4/IPv6 differences and IPv6 basics | `/etc/services`, IPv4, IPv6, subnetting, TCP, UDP, ICMP; all listed ports | [109.1](docs/109-networking-fundamentals.md#1091-internet-protocol-fundamentals) |
| [ ] | **109.2** Persistent configuration (4) | Host TCP/IP; Ethernet/Wi-Fi with NetworkManager; systemd-networkd awareness | `/etc/hostname`, `/etc/hosts`, `/etc/nsswitch.conf`, `/etc/resolv.conf`, `nmcli`, `hostnamectl`, `ifup`, `ifdown` | [109.2](docs/109-networking-fundamentals.md#1092-persistent-network-configuration) |
| [ ] | **109.3** Troubleshooting (4) | Temporary interface/address and routing changes with iproute2; default route; layered debugging; legacy net-tools | `ip`, `hostname`, `ss`, ping/ping6, traceroute/traceroute6, tracepath/tracepath6, netcat, `ifconfig`, `netstat`, `route` | [109.3](docs/109-networking-fundamentals.md#1093-basic-network-troubleshooting), [LAB-109-1](labs/README.md#lab-109-1-layered-troubleshooting) |
| [ ] | **109.4** Client DNS (2) | Query remote DNS; local/remote resolver configuration; lookup order; diagnosis; systemd-resolved awareness | `/etc/hosts`, `/etc/resolv.conf`, `/etc/nsswitch.conf`, `host`, `dig`, `getent`, `resolvectl` | [109.4](docs/109-networking-fundamentals.md#1094-client-side-dns), [LAB-109-2](labs/README.md#lab-109-2-dns-path) |

### Topic 110: Security

| Done | Objective and weight | Published knowledge-area coverage | Named scope covered | Evidence |
|---|---|---|---|---|
| [ ] | **110.1** Security administration (3) | SUID/SGID audit; passwords/aging; port discovery; login/process/memory limits; login history; sudo basics | `find`, `passwd`, `fuser`, `lsof`, `nmap`, `chage`, `netstat`, `sudo`, `/etc/sudoers`, `su`, `usermod`, `ulimit`, `who`, `w`, `last` | [110.1](docs/110-security.md#1101-security-administration), [LAB-110-1](labs/README.md#lab-110-1-host-audit) |
| [ ] | **110.2** Host security (3) | Shadow passwords; disable unused services; TCP-wrapper awareness | `/etc/nologin`, passwd/shadow files, xinetd files, `systemd.socket`, SysV files, `hosts.allow`, `hosts.deny` | [110.2](docs/110-security.md#1102-host-security), [LAB-110-1](labs/README.md#lab-110-1-host-audit) |
| [ ] | **110.3** Encryption (4) | OpenSSH client and host keys; GnuPG key/config/revocation; encrypt/decrypt/sign/verify; local/remote/dynamic and X11 tunnels | `ssh`, `ssh-keygen`, `ssh-agent`, `ssh-add`, RSA/DSA/ECDSA/Ed25519 key filenames, `authorized_keys`, `ssh_known_hosts`, `gpg`, `gpg-agent`, `~/.gnupg/` | [110.3](docs/110-security.md#1103-secure-data-and-communications-with-encryption), [LAB-110-2](labs/README.md#lab-110-2-ssh-and-gpg) |

## Completion rule

Do not mark an objective complete after reading only. Mark it complete when you
can:

1. Explain each knowledge area without copying the guide.
2. Recognize the named files, terms and commands and interpret representative output.
3. Perform the linked lab safely and verify the result.
4. Diagnose at least one deliberate failure without random changes.
5. Answer the related chapter and mock-exam questions without the answer key.

This mapping covers the published objective scope. LPI does not publish the
live question bank, so no independent guide can promise every exact exam
question or every junior Linux interview question.
