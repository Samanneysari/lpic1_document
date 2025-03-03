# Linux Lpic 1
## Operating System
An operating system (OS) is system software that manages computer hardware, and software resources, and provides common services for computer programs. It sits on top of the hardware and manages the resources when other software (Sometimes called an userspace program) asks for it.
## Firmware
Firmware is the software on your hardware that runs it; Think of it as a built-in OS or driver for your hardware. Motherboards need some firmware to be able to work too.
Firmware is a type of software that lives in hardware. Software is any program or group of programs run by a computer.
## BIOS
BIOS is like your computer’s morning wake-up routine. Imagine when you turn on your computer—it doesn’t just start working instantly, right? It needs a moment to get ready, kind of like how you might stretch or grab a coffee when you wake up.
So, BIOS is a tiny little program that lives on a chip inside your computer. When you hit the power button, it’s the first thing that jumps into action. It’s like the computer’s personal assistant, checking to make sure everything’s okay—like the keyboard, mouse, and screen—and making sure they’re all connected and ready to work together.
Once it’s done with that quick check, BIOS says, “Alright, everything looks good!” and passes the job over to the operating system (you know, like Windows or macOS). That’s the main software that lets you do all the fun stuff—browsing the internet, playing games, or typing up a document.
## UEFI
UEFI stands for Unified Extensible Firmware Interface. It’s the newer, improved version of BIOS. Like BIOS, UEFI runs when you turn on your computer and checks the hardware. But it does this faster, so your computer starts up more quickly. UEFI can work with larger hard drives (perfect for storing lots of files) and has extras like Secure Boot. Secure Boot checks that only trusted software runs at startup, helping protect your computer from viruses or malware. UEFI is also easier to update and often has a nicer interface (sometimes even with mouse support!).
## Key Differences Between BIOS and UEFI
### Speed: UEFI boots your computer faster than BIOS.
### Storage: UEFI supports bigger hard drives; BIOS has limits and struggles with modern sizes.
### Security: UEFI has Secure Boot to block bad software; BIOS doesn’t.
### Look and Feel: UEFI can have a graphical interface; BIOS is usually plain text and harder to navigate.
## Bootloader
A bootloader is a small but essential program that runs when you turn on your computer. Its main job is to find the operating system (like Windows, macOS, or Linux) on your hard drive and load it into the computer’s memory. Once the operating system is loaded, it takes control, allowing you to use your computer.
Think of the bootloader as the starting whistle in a race. When you press the power button, your computer doesn’t know what to do on its own—it needs a guide. The bootloader acts as that guide, getting the operating system ready to run.
### GRUB: Commonly used for Linux.
### Windows Boot Manager: Used for Windows
## Boot Process
### 1. Power On
The power supply sends electricity to the motherboard, which "wakes up" the system and starts the boot process.
### 2. BIOS or UEFI Initialization
BIOS: Runs a Power-On Self-Test (POST) to check essential hardware like the CPU, RAM, and storage devices.
UEFI: Does a similar hardware check but faster, with added features like Secure Boot to ensure only trusted software runs.
#### Purpose: Confirms that all critical hardware is functioning before moving forward.
### 3. Bootloader Activation
For BIOS, it looks in the Master Boot Record (MBR) on the storage device.
For UEFI, it checks the EFI System Partition (ESP).
#### Purpose: Prepares the system to load the operating system by finding the bootloader.
### 4. Bootloader Execution
Examples include GRUB (common for Linux) or Windows Boot Manager (for Windows).
If there’s only one OS, it skips the menu and moves forward automatically.
#### Purpose: Allows you to choose an operating system (if applicable) and starts loading it.
### 5. Operating System Loading
The kernel is the core of the operating system, responsible for managing hardware and software interactions.
The bootloader hands control over to the kernel to begin the OS startup.
#### Purpose: Begins the process of getting the operating system up and running.
### 6. Kernel Initialization
It sets up hardware drivers (e.g., for your graphics card, network adapter, etc.).
It mounts the root file system, which contains all the necessary files for the OS to operate.
#### Purpose: Prepares the system to handle applications and services.
### 7. System Services and User Interface
Services like networking, printing, and security systems are launched.
Depending on the OS, either a graphical user interface (GUI) or a command-line interface (CLI) appears.
#### Purpose: Makes the computer fully functional and ready for interaction.
### 8. Login Screen or Desktop
The operating system is now completely loaded and operational.
You can log in and start using the computer.
#### Purpose: The system is ready for you to work, browse, or do whatever you need!
## Root
refers to the highest level of access or control within the system. It’s a fundamental concept that appears in several key areas, each with its own specific meaning
#### 1. Root as a Superuser
#### 2. Root as a filesystem root
#### 3. root as root's home directiory
#### 4. root as a group
## Directories
The Filesystem Hierarchy Standard (FHS) is a set of guidelines that defines the structure and organization of files and directories in Unix-like operating systems, such as Linux. Its primary goal is to ensure consistency across different distributions, making it easier for users, administrators, and software to locate and manage files in a predictable way.
Below is a comprehensive list of the main directories in Linux, along with their definitions:
* **/**: The root directory, serving as the top-level directory of the file system hierarchy. All other directories and files reside under this directory.
* **/bin**: Contains essential user command binaries (executable files) such as ls, cp, and mv, which are necessary for basic system operation and accessible to all users.
*  **/boot**: Holds static files required for booting the system, including the Linux kernel and bootloader configuration files (e.g., GRUB).
*  **/dev**: Stores device files that represent hardware devices (e.g., disks, printers, or terminals). In Linux, these files allow programs to interact with hardware as if they were regular files.
* **/etc**: Contains host-specific system configuration files, such as settings for applications, services, and the operating system itself (e.g., /etc/passwd for user account information).
* **/home**: Houses individual home directories for each user (e.g., /home/username), where users store personal files and user-specific configuration settings.
* **/lib**: Provides essential shared libraries and kernel modules that programs rely on to function, offering reusable code and routines.
* **/media**: Serves as a mount point for removable media, such as USB drives, CDs, or DVDs, which are automatically mounted here when inserted.
* **/mnt**: Acts as a mount point for temporarily mounted file systems, often used for manually mounting devices like external hard drives or network shares.
* **/opt**: Stores add-on or optional software packages, typically third-party applications that are not part of the default system installation.
* **/proc** : A virtual file system that provides information about running processes and kernel resources, generated dynamically by the system (e.g., /proc/cpuinfo for CPU details).
* **/root**: The home directory for the root user (the system’s superuser), distinct from the /home directory used by regular users.
* **/sbin**: Contains essential system binaries used for administrative tasks, such as fdisk or reboot, typically reserved for the system administrator.
* **/srv**: Holds data for services provided by the system, such as files served by web or FTP servers, though its usage varies by distribution.
* **/tmp**: A directory for temporary files created by applications or users, often cleared automatically upon system reboot.
* **/usr**: A secondary hierarchy containing user-related programs and data, with subdirectories like /usr/bin (user binaries), /usr/lib (libraries), and /usr/share (shared data).
*  **/var**: Stores variable data files that change during system operation, such as log files (/var/log), mail spools, and other persistent temporary files.
  
These directories form the backbone of the Linux file system, ensuring a standardized structure across different distributions. While additional directories like /sys (for kernel and device information) or /run (for runtime data) may appear in modern systems, the ones listed above are the core directories defined by the FHS. Note that the exact contents or usage of some directories may vary slightly depending on the specific Linux distribution.
## User and Group Management
* **New User**
```
sudo useradd saman
```
* **New Group**
```
sudo groupadd realmadrid
```
* **delete user**
```
sudo userdel saman
```
* **to determine the current username of the user logged in**
```
whoami
```
* **sets and changes passwords for users**
```
sudo passwd saman
```
* **Assign multiple sub group to a user** 
```
sudo usermod -aG group1.group2.group3 saman
```
* **Lock Password**
```
usermod -L saman
```
* **Unlock Password**
```
usermod -u saman
```
* **Lock User**
```
passwd -l saman
```
* **Unlock User**
```
passwd -u saman
```

### When you use useradd saman: 
* **1. Check if there is any user like saman in /etc/passwd**
* **2. Assign first free UID to the user**
* **3. Create a group with the same username and Assign first free GID**
* **4. join user saman to the group saman**
* **5. make a directory with the same username under /home**
* **6. user will be the owner of the home directory and set permission**
* **7. copy all the files from route /etc/skel/ to the home directory of the user and set permission**
* **8. in the route /var/spool/mail/... a file will make with the same username**
* **9. in the route /etc/passwd a record will add with the same username**
### When you use groupadd saman:
* **1. Check if there is not any group like saman in the route /etc/passwd**
* **2. Assign first free GID to the group**
* **3. add a new record in the route /etc/passwd with the same group name**
### Man Useradd
* **-d** : the new user will be created using HOME_DIR as the value for the user's login directory. The default is to append the LOGIN
           name to BASE_DIR and use that as the login directory name. If the directory HOME_DIR does not exist, then it will be created
           unless the -M option is specified.
* **-m** : Create the user's home directory if it does not exist. The files and directories contained in the skeleton directory (which can
           be defined with the -k option) will be copied to the home directory. By default, if this option is not specified and CREATE_HOME is not enabled, no home directories are created.
* **-s** : sets the path to the user's login shell. Without this option, the system will use the SHELL variable specified in
           /etc/default/useradd, or, if that is as well not set, the field for the login shell in /etc/passwd remains empty.
* **-u** : The numerical value of the user's ID. This value must be unique, unless the -o option is used. The value must be non-negative.
           The default is to use the smallest ID value greater than or equal to UID_MIN and greater than every other user.
* **-c** : Any text string. It is generally a short description of the account, and is currently used as the field for the user's full
           name.

### Shadowing
##### In Linux, shadowing is a security feature that stores user passwords in a separate file (/etc/shadow) instead of the publicly readable /etc/passwd file. This prevents unauthorized users from accessing password hashes.
##### Before Shadowing: Password hashes were stored in /etc/passwd, which was world-readable.
##### After Shadowing: Passwords are moved to /etc/shadow, which only root can access.
##### /etc/shadow contains hashed passwords, expiration settings, and account policies.
##### Improves security by preventing regular users from reading password hashes.

## ls
The ls command in Linux is used to list the contents of a directory. It displays files and directories with various details depending on the options used
* **Syntax**
```
ls [OPTIONS] [DIRECTORY]
```
#### Options
* **ls** → Lists files and directories in the current directory.

* **ls -l** → Displays detailed information (permissions, owner, size, and timestamp).

* **ls -a** → Shows hidden files (files starting with .)

* **ls -h** → Displays file sizes in human-readable format.

* **ls -R** → Lists contents recursively, including subdirectories.

* **ls -t** → Sorts files by modification time (newest first).

* **ls -S** → Sorts files by size (largest first).

* **ls -1** → Lists one file per line.
## Common Commands
* **pwd** : displays the full path of the current directory.
```
pwd
```
* **touch** : is used to create empty files or update timestamps of existing files
```
touch f1
```
* **cd** : is used to change directory
```
cd /var/
```
* **file** : is used to specify the type of file
```
file saman.text
```
* **mkdir** : is used to create directories in the current pwd
```
mkdir real
```
* **cp** : is used to copy files or directories from one location to another.
```
cp [option] [source][destination]
cp -r /mft/f1.text /home/saman
```
* **mv** : moves or renames files and directories.
```
cp [option] [source][destination]
mv file1 newfile  # Renames file1 to newfile
mv file1 /home/user/  # Moves file1 to /home/user/
```
* **rm** : deletes files or directories.
```
rm file1 → Deletes file1.

rm -r dir1 → Deletes directory dir1 and its contents.

rm -i file1 → Prompts before deletion.
```
* **su -** : switch user to root , run home directory system script & variables
```
su - root
```
* **su** : switch user to root, without run home directory system script
```
su root
```
* **echo** : add message to a file 
```
echo "salam" > f1.text
```
* **cat** : reading files
```
cat f1.text
```

## alias
An alias in Linux is a shortcut for a command or a group of commands, allowing users to create custom, simplified command names for frequently used commands.
```
alias name='command'
```
```
alias ll='ls -lah'
```
* **Removing an Alias**
```
unalias ll
```
* **Making Aliases Permanent**
```
echo "alias ll='ls -lah'" >> ~/.bashrc
source ~/.bashrc
```
## Permission
In Linux, file and directory permissions determine who can read, write, or execute a file. Understanding these permissions is essential for managing security and access control.
### 1. File Permission Types
Each file and directory has three types of permissions:
* **Read (r)**: Allows viewing the file contents or listing directory contents. 4
* **Write (w)**: Allows modifying the file or adding/removing files in a directory. 2
* **Execute (x)**: Allows running a file (if it's a script or program) or accessing a directory. 1

Permissions are assigned to three categories:
* **Owner (u)**: The user who owns the file.
* **Group (g)**: A group of users with shared access.
* **Others (o)**: All other users on the system.

### 2. Viewing File Permissions

To check file permissions, use:
```
ls -l filename
```
Example output:
```
-rw-r--r--  1 user group  1024  Mar 2 10:00  file.txt
```
* **The first character (- or d)** indicates a file (-) or directory (d).

* **The next three (rw-)** are owner permissions (read and write).

* **The next three (r--)**  are group permissions (read-only).

* **The last three (r--)** are others’ permissions (read-only).

### 3. Changing Permissions with chmod

The **chmod** command is used to modify permissions.

#### 3.1 Symbolic Mode
Adds execute permission for the owner

      chmod u+x file.sh

Removes write permission for the group

      chmod g-w file.txt

Grants read permission to others

      chmod o+r file.txt

Sets specific permissions

      chmod u=rwx,g=rx,o=r file.txt


### 4. Changing Ownership with chown and chgrp

4.1 Changing File Owner (chown)

Change owner

      chown newuser file.txt 

Change owner and group

      chown newuser:newgroup file.txt 

### 5. Sticky bit
The sticky bit is a special permission that prevents users from deleting files they do not own in a shared directory. This is commonly used in directories like /tmp

#### 5.1 To enable the sticky bit on a directory:

      chmod +t /shared_folder/

#### 5.2 Checking the Sticky Bit

      ls -ld /shared_folder/

If set, you will see a t at the end of the permissions:

      drwxrwxrwt  10 root root  4096 Mar 2 10:00 /shared_folder/

### journalctl
The journalctl command is a utility used to view messages from the systemd journal. The systemd journal collects status and error messages from the boot process, the kernel, and all systemd-managed services.

* View all messages in the systemd journal.
* List boot IDs for each system boot.
* View messages associated with a particular boot instance using the -b option along with a boot instance ID.
* Display only kernel messages using the -k option

### Init
The init (or systemd) is the initialization daemon and can be considered the "mother of all processes". It is the first process started by the kernel. For systems using SysVinit or Upstart, the init daemon is named init, while for systemd systems, it's named systemd. When the Linux kernel starts, the initialization process (init or systemd) has a parent process ID (PPID) of 0 and a PID of 1. Once started, init is responsible for launching processes configured to start at boot time, such as the login shell (getty or mingetty process), and for managing services

* **SysVinit** : A traditional init system created for UNIX System V in the early 1980s. It starts and stops services based on runlevels. Control files are located at /etc/init.d/.
* **Upstart** : Improved handling of dependencies between services and could substantially improve system startup time. It is not concerned with runlevels, but with system events. Job definition files are located in the /etc/init directory.
* **Systemd** : Used by the latest versions of Fedora and RHEL. It manages services, sockets, devices, mount points, swap areas, and other unit types. It is concerned with runlevels, but they are called target units
```
systemctl --version
```
The systemd init system uses units to manage various aspects of the system. A unit is a group consisting of a name, a type, and a configuration file focused on a particular service or action. Systemd has 12 unit types. Here are some of them, drawing on the sources and our conversation history


* **Service**: Manages daemons on a Linux server. Service unit names end with .service.
* **Target**: Groups other units together. Target unit names end with .target. Systemd uses target units instead of runlevels.
* **Automount** : Automatically mounts filesystems.
* **Device**: Represents a device.
* **Mount**: Defines mount points.
* **Path**
* **Snapshot**
* **Socket**
* **scope**
* **slice**
* **swap**
* **timer**
```
systemctl list-units
```
### kernel madules
A Linux Kernel Module (LKM) is a piece of code that can be dynamically loaded and unloaded into the Linux kernel without requiring a system reboot. These modules extend the functionality of the kernel, allowing it to support new hardware, filesystems, and features without modifying the core system.
* **Modularity**: New functionalities can be added to the kernel as needed.
* **Resource Optimization**: Modules are only loaded when required, reducing system overhead.
* **Flexibility**: No need to recompile or restart the system to add/remove features.
* **Ease of Maintenance**: Modules can be updated or replaced without affecting the running kernel.

Listing Loaded Modules
```
lsmod
```
Loading a Module
```
sudo modprobe module_name
```
unload a module from the kernel
```
sudo rmmod module_name
```
### Runlevel
A runlevel in Linux defines the operational state of the system. It determines which services and processes are running. Runlevels are pre-defined modes in which the system can operate, such as single-user mode, multi-user mode, or graphical mode.
Each runlevel has a specific purpose, and switching between runlevels allows administrators to control the behavior of the system.

| Runlevel | Description                     | Purpose                          |
|----------|---------------------------------|----------------------------------|
| 0        | Halt                            | Shuts down the system           |
| 1        | Single-user mode                | Maintenance mode                 |
| 2        | Multi-user mode (no network)    | Basic multi-user mode            |
| 3        | Multi-user mode with networking | Full CLI-based multi-user mode   |
| 5        | Graphical mode (GUI)            | Multi-user mode with GUI support |
| 6        | Reboot                          | Restarts the system              |

* Some Linux distributions (e.g., Red Hat-based systems) follow this traditional runlevel system.

* Modern systemd-based distributions (such as Ubuntu and newer Fedora versions) use targets instead of runlevels.

To find out the current runlevel of your Linux system, use:
```
runlevel
```
#### Runlevels in systemd (Modern Linux Distributions)

| Traditional Runlevel | systemd Target      |
|----------------------|---------------------|
| 0                    | poweroff.target     |
| 1                    | rescue.target       |
| 2, 3                 | multi-user.target   |
| 5                    | graphical.target    |
| 6                    | reboot.target       |

Checking Current Runlevel (Target) in systemd:
```
systemctl get-default
```
## Partitioning
Partitioning is the process of dividing a hard drive into separate sections, called partitions. Think of it like splitting a big room into smaller rooms, where each room can have its own purpose. In Linux, partitioning is an important step when setting up a system because it helps you organize your data and manage how your hard drive is used.
In Linux, there are a few types of partitions you need to know about:

* **Primary Partitions**: These are the main sections of your hard drive. You can have up to four primary partitions on a single drive.
* **Extended Partitions**: If you need more than four partitions, you can create an extended partition. This acts like a container that holds extra partitions inside it.
* **Logical Partitions**: These are the extra partitions you create inside an extended partition. They let you go beyond the four-partition limit.

#### Partitioning Methods

When you partition a hard drive in Linux, you’re not just splitting it into sections—you’re also choosing a partitioning method (or scheme) that defines how the partitions are organized and stored on the disk. The two primary methods are MBR (Master Boot Record) and GPT (GUID Partition Table). Each has its own strengths, limitations, and use cases. Let’s dive into what they are and how they work
1. MBR (Master Boot Record)
MBR is the older, traditional partitioning method, dating back to the 1980s. It stores partition information in the first sector of the disk (the "master boot record").

The MBR contains a small boot loader and a partition table that can define up to 4 primary partitions.
If you need more than 4, you can create an extended partition, which acts as a container for additional logical partitions.
Limits:
* Maximum disk size: 2 terabytes (due to 32-bit addressing).
* Maximum partitions: 4 primary, or more with logical partitions inside an extended one.
* Tools: Managed with fdisk or sfdisk.
* Use Case: Common on older systems or legacy hardware with BIOS (not UEFI).
* A disk might have /dev/sda1 (primary), /dev/sda2 (primary), and /dev/sda5 (logical inside an extended partition).

2. GPT (GUID Partition Table)
GPT is the modern partitioning method, designed to overcome MBR’s limitations. It’s part of the UEFI (Unified Extensible Firmware Interface) standard.

Uses globally unique identifiers (GUIDs) to define partitions.
Stores partition data in multiple locations on the disk for redundancy.
Supports up to 128 partitions by default (and more with adjustments).

* Maximum disk size: 9.4 zettabytes (about 9.4 billion terabytes), far beyond current hardware limits.
* Requires UEFI firmware (though some BIOS systems can boot GPT with extra setup).
* Tools: Managed with gdisk, parted, or sfdisk.
* Use Case: Standard for modern systems, large drives, and UEFI-based computers.
* A disk might have /dev/sda1 (EFI system partition), /dev/sda2 (root), and so on, up to 128 partitions.

## Quick Reference: Partitioning Methods in Linux

| Method    | Max Disk Size | Max Partitions     | Boot Support | Tool Example | Use Case            |
|-----------|---------------|--------------------|--------------|--------------|---------------------|
| MBR       | 2 TB          | 4 primary (+logical)| BIOS         | `fdisk`      | Older systems, small disks |
| GPT       | 9.4 ZB        | 128 (default)      | UEFI         | `gdisk`      | Modern systems, large disks |



#### 1. To create partitions in Linux, you can use a tool called **fdisk**
```
sudo fdisk /dev/sda
```
* sudo: Gives you permission to make changes.
* /dev/sda: This is your hard drive (it might be /dev/sdb or something else on your system).

#### 2. Create a New Partition:
* Press n and hit Enter to make a new partition.
* Choose p for a primary partition.
* Pick a number (1-4) for your partition.
* Set the size by choosing starting and ending points. (You can usually just press Enter to use the defaults and fill the space.)

To see what partitions are already on your system, you can use these commands:
```
sudo fdisk -l
```
a simple tree view of your drives and partitions
```
lsblk
```
#### File system
After creating partitions, they aren’t ready to use yet—you need to format them with a file system. A file system defines how data is stored, organized, and retrieved on the partition. In Linux, popular file systems include ext4, XFS, and Btrfs. Formatting is the process of applying a file system to a partition, making it ready to store files.

A file system is like a blueprint for how data is arranged on a partition. It manages files, directories, and permissions, ensuring that the operating system can read and write data efficiently.
* **ext4** : The most common and reliable choice for general use. It’s the default for many Linux distributions.
* **XFS** : Great for handling large files and high-performance storage needs.
* **Btrfs** : Offers advanced features like snapshots and data integrity checks, useful for more complex setups

To format a partition with a file system, you can use the mkfs (make file system) command. Here’s how to format a partition as ext4:

* 1. Identify Your Partition: Make sure you know the correct partition name, such as /dev/sda1. You can check this with lsblk or sudo fdisk -l.
* 2. Format the Partition: Run the following command:
```
sudo mkfs.ext4 /dev/sda1
```
After formatting, you can verify the file system’s integrity using the fsck (file system check) command:
```
sudo fsck /dev/sda1
```
If fsck reports that the file system is "clean," everything is in order.


#### Mounting
Once a partition is formatted with a file system, it’s ready to store data—but you still need to mount it to access it. Mounting attaches the file system to a directory (like /mnt/data), making it part of the Linux directory structure so you can read and write files.
Mounting is the process of linking a file system to a specific directory, called a mount point. Once mounted, you can access the files on that partition through the mount point directory.
To mount a partition temporarily (until the next reboot), use the mount command:
```
sudo mount /dev/sda1 /mnt
```
For the mount to persist across reboots, you need to add an entry to the /etc/fstab file:
```
sudo vim /etc/fstab
```
Add a Line for Your Partition:
```
UUID=xxxx /mnt ext4 defaults 0 2
```
* UUID=xxxx: Replace xxxx with the UUID of your partition (you can find it with blkid /dev/sda1).
* /mnt: The mount point.
* ext4: The file system type.
* defaults: Standard mount options.
* 0 2: Settings for backup and file system check order.

After editing /etc/fstab, you can mount the partition with:
```
sudo mount -a
```
#### Unmounting a File System
When you no longer need access to the file system, you can unmount it using the umount command:
```
sudo umount /mnt
```
This detaches the file system from the mount point, making the partition inaccessible until it’s mounted again.


## Argument
In Linux, when you type a command into the terminal, it’s often made up of several parts: the command itself and its arguments. Arguments are additional pieces of information you provide to tell the command what to do or what to work on. Understanding arguments is a key skill for using the Linux command line effectively
Arguments are the words or symbols that follow a command, separated by spaces. They can be:

* **Options/Flags** : Modify how the command behaves (e.g., -l in ls -l).
* **Operands** : Specify what the command should act on (e.g., /boot in ls /boot).

In programming terms (like in shell scripts), arguments are numbered starting from 0:

* **Argument 0** : The command itself.
* **Argument 1, 2, etc.** : The options or operands that follow.

```
ls -l /boot
```
* **ls** : The command (argument 0). It lists directory contents.
* **-l** : An option (argument 1). It tells ls to use a long, detailed listing format.
* **/boot** : An operand (argument 2). It specifies the directory to list.

## Files
In Linux, everything is treated as a file—whether it’s a document, a directory, or even a piece of hardware. However, these "files" come in different types, each serving a unique purpose. Understanding these file types is essential for navigating and managing a Linux system effectively. Let’s explore the main types of files you’ll encounter.
You can use the ls -l command to see a file’s type. The first character in the output tells you what kind of file it is. For example:
```
ls -l
```

| File Type         | Symbol | Example             | Purpose                          |
|-------------------|--------|---------------------|----------------------------------|
| Regular File      | `-`    | `notes.txt`         | Stores data (text, binaries)     |
| Directory         | `d`    | `/home`             | Organizes other files            |
| Symbolic Link     | `l`    | `python -> python3` | Points to another file           |
| Block Device      | `b`    | `/dev/sda`          | Represents block-based devices   |
| Character Device  | `c`    | `/dev/tty`          | Represents character-based devices |
| Named Pipe        | `p`    | `mypipe`            | Inter-process communication      |
| Socket            | `s`    | `mysqld.sock`       | Network/local communication      |


## Addressing
In Linux, when you navigate the filesystem or specify the location of a file or directory, you use paths. A path is like an address that tells the system where to find something. There are two main types of paths: absolute and relative. Understanding the difference is key to working efficiently in the terminal.
1. Absolute Paths
   * Definition: An absolute path provides the full, exact location of a file or directory, starting from the root directory (/).
   * How It Works: It doesn’t depend on your current location in the filesystem—it always begins with / and lists every directory down to the target.
   * When to Use: Use absolute paths when you need to be specific, regardless of where you are in the system.
```
cat /home/user/documents/notes.txt
```
2. Relative Paths
   * Definition: A relative path describes the location of a file or directory based on your current working directory (where you are in the filesystem). It doesn’t start with /.
   * How It Works: It uses your current position as a starting point and moves from there, often using special symbols like . (current directory) or .. (parent directory).
   * When to Use: Use relative paths for convenience when working within your current directory or nearby locations.

      If you’re in /home/user:

      ../backup: Refers to /home/backup (one level up from /home/user).

      If you’re in /etc:

      ./passwd: Refers to /etc/passwd (. means "here").

#### Special Symbols in Relative Paths

. (Dot): Represents the current directory.

Example:

  runs a script in your current directory.

```
 ./script.sh
 ```

.. (Double Dot): Represents the parent directory (one level up).

Example:

 refers to a file in the directory above your current one.

 ```
 ../file.txt
 ```

 | Type           | Symbol/Start | Example                  | Description                          |
|----------------|--------------|--------------------------|--------------------------------------|
| Absolute Path  | Starts with `/` | `/home/user/notes.txt` | Full path from root directory        |
| Relative Path  | No `/` at start | `notes.txt`, `../backup` | Path relative to current directory   |

## A Toolbox of Commands

1. **`grep`**: Searches for text patterns in files or input.
   - **Example**: Find lines with "error" in a log.
```
     grep "error" log.txt
```

2. **`tail`** : Displays the last lines of a file (default: 10)
   - **Example** : View the last 5 lines of a log
```
      tail -n 5 log.txt
```
3. **`nl`** : Numbers the lines of a file or input.
   - **Example**: Number all lines in a file
```
nl notes.txt
```
4. **`less`** : Shows file contents one page at a time for scrolling.
   - **Example**: View a large file
```
less bigfile.txt
```
5. **`more`** : Similar to less, but simpler—displays text one screen at a time.
   - **Example**: Read a file page by page
```
more log.txt
```
6. **`head`** : Shows the first lines of a file (default: 10).
   - **Example**: See the first 3 lines of a file
```
head -n 3 notes.txt
```
7. **`sort`** : Sorts lines of text alphabetically or numerically.
   - **Example**: Sort a list of names
```
sort names.txt
```
8. **`wc`**: Counts lines, words, or characters in a file or input.
   - **Example**: Count lines in a file
```
wc -l log.txt
```
9. **`sed`**: Stream editor for modifying text (e.g., replace, delete).
   - **Example**: Replace "old" with "new" in a file.
```
sed 's/old/new/g' text.txt
```
10. **`find`**: Searches for files or directories in a filesystem.
   - **Example**: Find all .txt files in /home
```
find /home -name "*.txt"
```
   - **Example**: Find all files in / that size is between 10 and 50 MB
```
find / -size +10M -size -50M
```
   - **Example**: Find all files in / that change time is less than 30 min ago
```
find / cmin -30
```







