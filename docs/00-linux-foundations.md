# Linux Foundations: Start Here If You Are New to Computers

Read this before Topic 101 if words such as *program*, *memory*, or *operating system* are new to you. Later chapters teach the commands in exam depth. This chapter explains the parts that those chapters assume you already know.

## 1. What a computer runs

**Hardware** is the physical equipment. The CPU follows instructions; RAM holds data and running programs temporarily; a disk or SSD retains files after power is off. A **program** is instructions stored on a device. A **process** is a running instance of a program. Two processes can run the same program at once.

An **operating system (OS)** manages hardware and gives programs common services, such as files, memory, networking and access control. **Linux** strictly names the kernel: the central program that manages these services. People also say “Linux” for a whole usable OS built around that kernel. A **distribution** (or *distro*) packages the kernel with tools, libraries, an installer, package manager, configuration and updates. Ubuntu and Debian are two different distributions using the Linux kernel.

An application does not normally write directly to a disk controller. It asks the kernel to open or write a file through a **system call**. The kernel checks permissions and asks an appropriate **driver** to operate the hardware. A driver is code that understands a particular device or device family; some drivers are loadable kernel modules.

**Firmware** is software stored in a device's nonvolatile storage. The computer's motherboard firmware starts before Linux, initializes enough hardware to boot, and selects a boot program. Other devices, such as network cards, can also have firmware. Firmware is software, but it is neither the Linux kernel nor an ordinary Linux application. **BIOS** is an older PC firmware interface; **UEFI** is the modern firmware interface. A PC may offer a compatibility mode. Neither BIOS nor UEFI is a Linux distribution.

## 2. Where Linux and GNU came from

Unix was a family of operating systems developed starting in the late 1960s. Its ideas shaped later systems, including a tree of files, small programs that can be combined, and multiple user accounts. In 1983 Richard Stallman announced the **GNU** project to build a free Unix-like operating system. “Free software” here refers to the freedom to run, study, change and share software, not necessarily a price of zero. GNU developed tools such as Bash, GCC and coreutils. In 1991 Linus Torvalds began the Linux kernel. GNU tools and the Linux kernel are often combined into a working system; some people call this combination **GNU/Linux**. Distributions can also include much software from other projects. The kernel, the GNU project and a particular distro are three different things.

Common distribution families:

| Family | Examples | Typical package tools | What changes for a learner |
|---|---|---|---|
| Debian | Debian, Ubuntu | `apt`, `dpkg` | Package format and repository commands |
| Red Hat / RPM | Fedora, RHEL, Rocky Linux, AlmaLinux | `dnf`, `rpm` | Package commands, names and some configuration defaults |
| SUSE | openSUSE, SUSE Linux Enterprise | `zypper`, `rpm` | Package and administration conventions |
| Independent | Arch Linux, Alpine Linux | `pacman`, `apk` respectively | Different packaging and defaults |

These are examples, not a ranking. LPIC-1 expects skills across distributions, especially Debian and RPM families. The kernel concepts, path notation and many shell commands transfer between them.

## 3. From power button to login

1. **Power and firmware:** the CPU begins executing motherboard firmware. BIOS or UEFI initializes hardware and chooses a boot entry. A Power-On Self-Test (POST) is an early hardware check; details vary by machine.
2. **Bootloader:** on many Linux installations, GRUB selects and loads a Linux kernel and an **initramfs** into RAM. In UEFI mode, firmware loads an EFI program from the EFI System Partition (ESP). In legacy BIOS mode, the boot path usually starts with code on the selected disk. A menu need not appear.
3. **Kernel:** the kernel initializes memory, devices and drivers. Its early messages are kept in a **kernel ring buffer**, a finite in-memory message area. When full, older messages can be overwritten; `dmesg` displays messages still available. This is not a permanent archive.
4. **Temporary root:** the initramfs is a small temporary filesystem with tools and drivers that help locate and unlock the real root filesystem, when needed. The startup code switches to the real root.
5. **Init / PID 1:** the kernel starts the first userspace process, called **init** and assigned process ID (**PID**) 1. On many current distributions this is `systemd`. It starts services, mounts and login facilities. Older systems may use SysVinit; a **runlevel** is its named operating mode. systemd uses **targets** to group units for similar purposes.
6. **Login:** a console or graphical login lets a user start a session. A **shell** such as Bash can accept typed commands.

Do not confuse the kernel ring buffer with the system journal: `journalctl` reads logs collected by the logging service, while `dmesg` reads kernel messages. Permissions and persistence vary.

Try these read-only commands on a running Linux VM:

```bash
cat /proc/cmdline
```

`cat` prints a file; `/proc/cmdline` is a virtual file showing the kernel arguments used for this boot. Your disk's ordinary files do not contain this changing value.

```bash
ps -p 1 -o pid,comm,args
```

`ps` lists process information; `-p 1` selects PID 1; `-o pid,comm,args` chooses the displayed columns. Look for the name of your init process.

```bash
dmesg | tail -n 10
```

`dmesg` reads available kernel messages; `|` passes its output to `tail`; `-n 10` prints the last ten lines. Some systems require `sudo dmesg` or restrict this information. The output is not necessarily the first ten boot events.

Topic [101.1 and 101.2](101-system-architecture.md) explains device discovery, D-Bus, the boot chain and logging in more detail.

## 4. Your first shell session

A **terminal** displays text input and output. A **shell** interprets commands you type in it. A **path** identifies a file or directory. `/` is the root of the directory tree; `/home/alice` is an absolute path; `notes.txt` is relative to your current directory. `.` means the current directory and `..` its parent. The account named `root` is a privileged user; `/` is a directory, and `/root` is usually root's home directory.

Create a harmless practice area as your normal user, one line at a time:

```bash
pwd
```

`pwd` prints your current working directory. It does not change directories.

```bash
mkdir -p "$HOME/lpic-practice"
```

`mkdir` makes a directory; `-p` also makes missing parents and accepts an existing directory; `$HOME` is your home-directory variable. Quotes keep a path containing spaces together.

```bash
cd "$HOME/lpic-practice"
```

`cd` changes the current shell's directory to the practice area. A successful `cd` normally prints nothing; run `pwd` to verify.

```bash
echo 'Hello, Linux' > hello.txt
```

`echo` prints text; `>` redirects that output to `hello.txt`, creating or replacing the file. Do not redirect to a file you want to keep unchanged.

```bash
ls -l
```

`ls` lists directory entries; `-l` adds type, permissions, owner, size and modification time. `ll` is **not** a universal Linux command: on some installations it is an alias for `ls -l` or `ls -alF`, and on others it does not exist. `type ll` tells you what your shell would run.

```bash
cp hello.txt copy.txt
```

`cp` copies the contents to a new file. The original stays in place. Without `-i`, an existing destination may be overwritten; practice only with throwaway files.

```bash
mv copy.txt moved.txt
```

`mv` renames or moves the file. `copy.txt` is no longer at that old name; `moved.txt` now is.

```bash
rm -i moved.txt
```

`rm` removes the named directory entry; `-i` asks first. A shell removal does not normally go to a recycle bin. Never try an unfamiliar recursive removal on real data.

For `touch`, text viewers, wildcard matching and archives, continue with [Topic 103](103-gnu-unix-commands.md). For disks, mounts, permissions and the directory tree, continue with [Topic 104](104-devices-filesystems-fhs.md).

## 5. People and permissions

Each process runs with an identity. A **user** has a user ID (UID), and a **group** has a group ID (GID). A user has one primary group and can belong to supplementary groups. File permissions describe access for the owner, group and others. `root` is the privileged account, conventionally UID 0. **`sudo` is a command, not a kind of user**: when policy permits, it runs a specified command with another identity, often root's. An ordinary user allowed by that policy may be called a *sudoer*. A password prompt is not proof that every command is authorized.

```bash
id
```

`id` prints your UID, primary GID and group memberships. Use it to observe the current account without changing anything.

```bash
groups
```

`groups` prints group names for your current account; `groups alice` asks about an account named `alice`, if it exists. Membership alone does not explain every access rule; file permissions and other policies also matter.

Read [Topic 107](107-administrative-tasks.md) for account changes and [Topic 110](110-security.md#sudo-and-su) for sudo policy. Use `sudo` only for the specific lab command that needs privilege.

## Sources for the history

- [GNU project's initial announcement (1983)](https://www.gnu.org/gnu/initial-announcement.html)
- [GNU project overview](https://www.gnu.org/gnu/about-gnu.html)
- [Linux kernel documentation: introduction and 1991 beginnings](https://www.kernel.org/doc/html/v6.6/process/1.Intro.html)
