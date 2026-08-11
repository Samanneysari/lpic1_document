# Topic 101: System Architecture

This chapter covers every objective in Topic 101. It extends the introductory hardware, firmware, boot and systemd explanations in [`LPic1.md`](../LPic1.md) without replacing them.

## 101.1 Determine and configure hardware settings

### The hardware-to-userspace path

Linux discovers hardware through firmware tables and device buses. The kernel loads a suitable driver, exposes information through virtual filesystems, and creates device nodes that programs can use.

| Location | Purpose | Example |
|---|---|---|
| `/proc` | Runtime process and kernel views | `/proc/cpuinfo`, `/proc/meminfo`, `/proc/cmdline` |
| `/sys` | Structured kernel device and driver model | `/sys/class/net`, `/sys/block` |
| `/dev` | Device nodes used for I/O | `/dev/sda`, `/dev/nvme0n1`, `/dev/tty` |

These directories are interfaces to kernel data. Most files in `/proc` and `/sys` are generated dynamically and do not occupy normal disk space.

### Firmware settings

BIOS and UEFI initialize hardware and select a boot path. Common settings include boot order, virtualization support, storage-controller mode, Secure Boot, integrated peripherals, hardware clock and power behavior.

UEFI is a firmware standard, not a guarantee that every machine boots faster. Secure Boot verifies signatures in the boot chain; it does not replace operating-system patching or malware protection.

Inspect firmware information:

```bash
sudo dmidecode --type bios
test -d /sys/firmware/efi && echo UEFI || echo BIOS-or-compatibility-mode
```

| Part | Meaning |
|---|---|
| `dmidecode` | Reads DMI/SMBIOS tables supplied by firmware |
| `--type bios` | Limits output to BIOS/firmware information |
| `test -d` | Succeeds if the specified directory exists |
| `&&` | Runs the next command only if the test succeeded |
| `\|\|` | Runs the final command if the test failed |

### Storage device types

| Type | Typical Linux name | Important point |
|---|---|---|
| SATA/SAS/SCSI disk | `/dev/sda` | Partitions commonly appear as `/dev/sda1` |
| NVMe disk | `/dev/nvme0n1` | Partitions appear as `/dev/nvme0n1p1` |
| Virtual disk | `/dev/vda` or `/dev/sda` | Name depends on the virtual controller |
| Optical media | `/dev/sr0` | Usually read through a filesystem |
| USB storage | often `/dev/sdX` | Device letter can change after reconnecting |

Never identify a disk by name alone before a destructive operation. Compare size, model, serial, filesystem and mount points.

### Hardware discovery commands

```bash
lspci -nnk
lsusb -t
lsblk -o NAME,MAJ:MIN,SIZE,TYPE,FSTYPE,MOUNTPOINTS,MODEL
lscpu
free -h
```

| Command | What it shows |
|---|---|
| `lspci -nnk` | PCI devices, numeric IDs and the kernel driver in use |
| `lsusb -t` | USB devices arranged by bus topology |
| `lsblk -o ...` | Selected block-device properties |
| `lscpu` | CPU architecture and topology |
| `free -h` | Physical and swap memory in human-readable units |

`free` memory being low is not automatically a problem. Linux uses otherwise idle RAM for cache. The `available` column is usually more useful than `free` when estimating memory available to new applications.

### Kernel modules

A module adds kernel functionality at runtime. Use `modprobe` for normal administration because it resolves dependencies; `insmod` and `rmmod` operate on a specific module file or module and do not provide the same dependency handling.

```bash
lsmod
modinfo loop
sudo modprobe loop
sudo modprobe -r loop
```

| Part | Meaning |
|---|---|
| `lsmod` | Lists currently loaded modules |
| `modinfo loop` | Displays metadata and parameters for the `loop` module |
| `modprobe loop` | Loads the module and required dependencies |
| `modprobe -r loop` | Requests dependency-aware removal |

Persistent module requests can be placed in `/etc/modules-load.d/*.conf`. Module options can be placed in `/etc/modprobe.d/*.conf`. A module may refuse removal while it is in use.

### udev and D-Bus

`udev`, normally provided by `systemd-udevd`, receives kernel device events and manages device nodes, permissions and stable links. D-Bus is a message bus that lets system and desktop processes communicate; services such as NetworkManager use it.

```bash
udevadm info --query=all --name=/dev/sda
udevadm monitor --kernel --udev
busctl list
```

Do not copy `/dev/sda` blindly; substitute an existing device. `udevadm monitor` waits for events, so press `Ctrl+C` to stop it.

## 101.2 Boot the system

### Boot sequence

1. Firmware performs hardware initialization.
2. Firmware selects a boot entry or boot device.
3. A boot manager such as GRUB loads the kernel and initial RAM filesystem.
4. The kernel initializes memory, CPUs and drivers, then mounts the temporary root in the initramfs.
5. Initramfs discovers the real root filesystem and switches to it.
6. The kernel starts PID 1, normally systemd on current distributions.
7. PID 1 starts units required by the selected target.
8. Login services and applications become available.

The initramfs is a small temporary userspace used before the real root filesystem is available. It commonly contains storage, encryption, RAID or LVM tools and drivers needed to find root.

### Inspect the current boot

```bash
cat /proc/cmdline
dmesg --level=err,warn
journalctl -b
journalctl -b -1
systemd-analyze critical-chain
```

| Command | Purpose |
|---|---|
| `cat /proc/cmdline` | Shows kernel parameters used for this boot |
| `dmesg --level=err,warn` | Filters the kernel ring buffer to warnings and errors |
| `journalctl -b` | Shows messages from the current boot |
| `journalctl -b -1` | Shows the previous boot when persistent journal data exists |
| `critical-chain` | Shows time-critical systemd activation dependencies |

Access to some kernel and journal data may require root.

### Temporary boot parameters

At the GRUB menu, select an entry and press `e` to edit it temporarily. Find the line beginning with `linux` and append a parameter. `Ctrl+X` or `F10` commonly boots the edited entry. The change normally applies to one boot only.

Examples you should recognize:

| Parameter | Meaning |
|---|---|
| `systemd.unit=rescue.target` | Request rescue mode for this boot |
| `ro` | Initially mount root read-only |
| `quiet` | Reduce normal boot messages |

Do not disable security controls merely to hide a boot error. Diagnose the error from the journal and repair its cause.

### SysVinit, systemd and Upstart

SysVinit starts scripts arranged by runlevel, traditionally under `/etc/init.d` and `/etc/rc?.d`. systemd manages typed units and dependencies. Upstart was an event-based init system used by older releases; awareness of it is sufficient for LPIC-1.

Legacy SysVinit systems can define the default runlevel and process actions in
`/etc/inittab`. systemd system units are commonly supplied under
`/usr/lib/systemd/system/` (or `/lib/systemd/system/` on some layouts), while
administrator-created units and overrides belong under `/etc/systemd/system/`.
Do not edit vendor unit files in `/usr/lib`; use an override or a unit under
`/etc/systemd/system/` so package upgrades do not erase the change.

PID 1 can be identified with:

```bash
ps -p 1 -o pid,comm,args
readlink /sbin/init
```

## 101.3 Runlevels, boot targets, shutdown and reboot

### Runlevels are distribution-dependent

Traditional meanings are conventions, not universal guarantees. Debian historically treated runlevels 2 through 5 similarly, while many RPM-based systems used 3 for multi-user text mode and 5 for graphical mode.

| Runlevel | Common traditional meaning | Common systemd target |
|---:|---|---|
| 0 | Halt/power off | `poweroff.target` |
| 1 or `s` | Single-user/rescue | `rescue.target` |
| 2–4 | Multi-user; exact meaning varies | `multi-user.target` |
| 5 | Graphical multi-user | `graphical.target` |
| 6 | Reboot | `reboot.target` |

### Manage systemd targets

```bash
systemctl get-default
sudo systemctl set-default multi-user.target
sudo systemctl isolate rescue.target
systemctl list-dependencies graphical.target
```

| Operation | Effect |
|---|---|
| `get-default` | Displays the target selected for future normal boots |
| `set-default` | Changes the default target for future boots |
| `isolate` | Starts the requested target and stops units not required by it |
| `list-dependencies` | Displays target dependencies |

`isolate` can stop networking and graphical sessions. Do not run it over a remote connection unless you have console access and a recovery plan.

SysV-compatible commands you should recognize include `runlevel`, `init 3`, and `telinit 3`. On systemd systems they may be compatibility links.

### Notify users and shut down safely

```bash
wall "Maintenance begins in 10 minutes"
sudo shutdown -r +10 "Scheduled maintenance"
sudo shutdown -c
```

| Part | Meaning |
|---|---|
| `wall` | Writes a message to logged-in terminals |
| `shutdown -r` | Schedules a reboot |
| `+10` | Performs it in ten minutes |
| `shutdown -c` | Cancels a pending shutdown |

Immediate alternatives include `systemctl reboot`, `systemctl poweroff`, `reboot`, and `poweroff`. A clean shutdown gives services time to stop and filesystems time to flush data.

`acpid` reacts to ACPI events such as a power-button press on systems that use it. On current systemd systems, `systemd-logind` also handles power-related events.

## Lab 101: Trace one boot

1. Record firmware mode.
2. Record `/proc/cmdline`.
3. Identify PID 1.
4. list kernel warnings for the current boot.
5. Find the default target and its dependencies.
6. Select one device from `lspci -nnk` and record its driver.
7. Write a short boot sequence using evidence from your machine.

Do not change the default target in this lab unless you have VM console access.

## Exercises

1. **101-Q1:** Explain the difference between `/dev`, `/proc`, and `/sys`.
2. **101-Q2:** Why is `modprobe` normally preferred to `insmod`?
3. **101-Q3:** Which command shows the kernel command line used in the current boot?
4. **101-Q4:** Why is the meaning of runlevel 2 not identical on every distribution?
5. **101-Q5:** Write commands that warn users, schedule a reboot in 15 minutes, and cancel it.
6. **101-Q6:** A system reaches GRUB but cannot find its encrypted root filesystem. Which early-boot component should you investigate first, and why?

Answers are in [the answer key](../exercises/answers.md#topic-101-answers).

## Official reading

- [LPI Topic 101 objectives](https://www.lpi.org/our-certifications/exam-101-102-objectives/)
- [Linux kernel documentation](https://docs.kernel.org/)
- [systemd bootup manual](https://www.freedesktop.org/software/systemd/man/latest/bootup.html)
- [systemctl manual](https://www.freedesktop.org/software/systemd/man/latest/systemctl.html)
