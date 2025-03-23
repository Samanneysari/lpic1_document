# Linux Lpic 1
## Operating System
An operating system (OS) is the vital software that powers up your computer and keeps it running smoothly. Picture it as the conductor of an orchestra, directing all the parts of your machine—like the processor, memory, and storage—so they work together without missing a beat. Without this software, your computer would just be a collection of lifeless hardware, unable to run apps or follow your instructions.

At its heart, the OS is the behind-the-scenes organizer. It juggles tasks like deciding which program gets attention from the CPU, keeping your files in order, and making sure everything hums along without tripping over itself. Plus, it’s what lets you actually use your computer, whether that’s through a friendly screen with icons and windows or a text-based setup where you type commands.

Simply put, the operating system is the backbone that makes your computer work for you. It ties your hardware to your apps, manages all the moving pieces, and keeps things flowing so you can do what you need to do.
## Firmware
Firmware is the software on your hardware that runs it; Think of it as a built-in OS or driver for your hardware. Motherboards need some firmware to be able to work too.
Firmware is a type of software that lives in hardware. Software is any program or group of programs run by a computer.
```
sudo dmidecode -t bios
```
## BIOS
BIOS is like your computer’s morning wake-up routine. Imagine when you turn on your computer—it doesn’t just start working instantly, right? It needs a moment to get ready, kind of like how you might stretch or grab a coffee when you wake up.
So, BIOS is a tiny little program that lives on a chip inside your computer. When you hit the power button, it’s the first thing that jumps into action. It’s like the computer’s personal assistant, checking to make sure everything’s okay—like the keyboard, mouse, and screen—and making sure they’re all connected and ready to work together.
Once it’s done with that quick check, BIOS says, “Alright, everything looks good!” and passes the job over to the operating system (you know, like Windows or macOS). That’s the main software that lets you do all the fun stuff—browsing the internet, playing games, or typing up a document.
## UEFI
UEFI stands for Unified Extensible Firmware Interface. It’s the newer, improved version of BIOS. Like BIOS, UEFI runs when you turn on your computer and checks the hardware. But it does this faster, so your computer starts up more quickly. UEFI can work with larger hard drives (perfect for storing lots of files) and has extras like Secure Boot. Secure Boot checks that only trusted software runs at startup, helping protect your computer from viruses or malware. UEFI is also easier to update and often has a nicer interface (sometimes even with mouse support!).
### Key Differences Between BIOS and UEFI
* **`Speed`**: UEFI boots your computer faster than BIOS.
* **`Storage`**: UEFI supports bigger hard drives; BIOS has limits and struggles with modern sizes.
* **`Security`**: UEFI has Secure Boot to block bad software; BIOS doesn’t.
* **`Look and Feel`**: UEFI can have a graphical interface; BIOS is usually plain text and harder to navigate.
## Bootloader
A bootloader is a small but essential program that runs when you turn on your computer. Its main job is to find the operating system (like Windows, macOS, or Linux) on your hard drive and load it into the computer’s memory. Once the operating system is loaded, it takes control, allowing you to use your computer.
Think of the bootloader as the starting whistle in a race. When you press the power button, your computer doesn’t know what to do on its own—it needs a guide. The bootloader acts as that guide, getting the operating system ready to run.
* **`GRUB`**: Commonly used for Linux.
* **`Windows Boot Manager`**: Used for Windows
## Boot Process
### 1. Power On
The power supply sends electricity to the motherboard, which "wakes up" the system and starts the boot process.
### 2. BIOS or UEFI Initialization
BIOS: Runs a Power-On Self-Test (POST) to check essential hardware like the CPU, RAM, and storage devices.
UEFI: Does a similar hardware check but faster, with added features like Secure Boot to ensure only trusted software runs.
* **`Purpose`**: Confirms that all critical hardware is functioning before moving forward.
### 3. Bootloader Activation
For BIOS, it looks in the Master Boot Record (MBR) on the storage device.
For UEFI, it checks the EFI System Partition (ESP).
* **`Purpose`**:Prepares the system to load the operating system by finding the bootloader.
### 4. Bootloader Execution
Examples include GRUB (common for Linux) or Windows Boot Manager (for Windows).
If there’s only one OS, it skips the menu and moves forward automatically.
* **`Purpose`**: Allows you to choose an operating system (if applicable) and starts loading it.
### 5. Operating System Loading
The kernel is the core of the operating system, responsible for managing hardware and software interactions.
The bootloader hands control over to the kernel to begin the OS startup.
* **`Purpose`**: Begins the process of getting the operating system up and running.
### 6. Kernel Initialization
It sets up hardware drivers (e.g., for your graphics card, network adapter, etc.).
It mounts the root file system, which contains all the necessary files for the OS to operate.
* **`Purpose`**: Prepares the system to handle applications and services.
### 7. System Services and User Interface
Services like networking, printing, and security systems are launched.
Depending on the OS, either a graphical user interface (GUI) or a command-line interface (CLI) appears.
* **`Purpose`**: Makes the computer fully functional and ready for interaction.
### 8. Login Screen or Desktop
The operating system is now completely loaded and operational.
You can log in and start using the computer.
* **`Purpose`**: The system is ready for you to work, browse, or do whatever you need!
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
## Init
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
### Kernel Madules
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

## Shadowing
In Linux, shadowing is a security feature that stores user passwords in a separate file (/etc/shadow) instead of the publicly readable /etc/passwd file. This prevents unauthorized users from accessing password hashes.
* Before Shadowing: Password hashes were stored in /etc/passwd, which was world-readable.
* After Shadowing: Passwords are moved to /etc/shadow, which only root can access.
* /etc/shadow contains hashed passwords, expiration settings, and account policies.
* Improves security by preventing regular users from reading password hashes.

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
## stat 

stat is a command-line tool that reveals the status of a file or directory by displaying its key attributes. These attributes include:

* File permissions
* Ownership (user and group)
* File size
* Timestamps (access, modification, and change times)
* Inode number
* Number of hard links
* Device and filesystem information

Unlike commands like `ls`, which provide a summary of file properties, `stat` offers a more comprehensive and structured view of a file's metadata.

```
stat example.txt
```
* **`File`**: The name of the file or directory.
* **`Size`**: The size of the file in bytes (e.g., 1024 bytes).
* **`Blocks`**: The number of disk blocks allocated to the file.
* **`IO Block`**: The size of each block on the filesystem (e.g., 4096 bytes).
* **`regular file`**: The type of the file (e.g., regular file, directory, symbolic link).
* **`Device`**: The device number where the file resides (in hexadecimal and decimal).
* **`Inode`**: The inode number, a unique identifier for the file on the filesystem.
* **`Links`**: The number of hard links pointing to this file.
* **`Access`**: The file's permissions in octal (0644) and symbolic (-rw-r--r--) notation.
* **`Uid`**: The user ID and username of the file's owner.
* **`Gid`**: The group ID and group name of the file's owner.
* **`Access`**: The last time the file was accessed (read).
* **`Modify`**: The last time the file's content was modified.
* **`Change`**: The last time the file's metadata (e.g., permissions) was changed.
* **`Birth`**: The creation time of the file (not always available on all filesystems).

## Package Management
Package management involves tools and systems that install, update, and remove software packages (precompiled programs and their dependencies).

### Debian-Based (e.g., Ubuntu):
* **`dpkg`**: Low-level tool for handling .deb packages.
* **`apt`**: High-level tool for managing packages and repositories.
### Red Hat-Based (e.g., CentOS, Fedora):
* **`rpm`**: Low-level tool for handling .rpm packages.
* **`yum or dnf`**: High-level tools for managing packages and repositories (dnf is the newer version of yum).

#### Update

The update command refreshes your system’s list of available packages and their versions by syncing with the repositories you’ve configured. It updates the local package database but does not install or modify any software on your system.

```
sudo apt update
```
#### Upgrade
The upgrade command updates all currently installed packages to their latest versions based on the repository data (which requires a prior update). It downloads and installs newer versions of software already on your system but does not add new packages or remove existing ones.

```
sudo apt upgrade
```
#### Install
The install command adds a specific package (or packages) to your system that isn’t currently installed. It downloads the package and its dependencies and sets them up. If the package is already installed, install can sometimes be used to reinstall it or upgrade it to a specific version (with additional options).
```
sudo apt install htop
```

| Command  | Purpose                               | Affects Installed Software? | Adds New Packages? | Requires Update First? |
|----------|---------------------------------------|----------------------------|---------------------|------------------------|
| update   | Syncs package list with repositories | No                         | No                  | N/A                    |
| upgrade  | Updates all installed packages       | Yes (updates versions)     | No                  | Yes                    |
| install  | Installs a specific new package      | Yes (adds new software)    | Yes                 | No (but recommended)   |

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

### 6. umask
The umask command in Linux sets the default permissions for new files and directories you create. It acts like a filter, determining which permissions are not granted by default, ensuring your files and folders start with the right level of access.
* **`Files`**: start with maximum permissions of 666 (read and write for owner, group, and others).
* **`Directories`** start with 777 (read, write, and execute for all).
* **`The umask value`** (a three-digit number, e.g., 022) masks out specific permissions.

#### Example: umask 022
##### New files: 666 - 022 = 644 (rw-r--r--)
* **`Owner`**: read/write
* **`Group/Others`**: read only

##### New directories: 777 - 022 = 755 (rwxr-xr-x)
* **`Owner`**: full access
* **`Group/Others`**: read and execute
#### Checking and Setting umask
##### Check current umask: Output might be 0022 (leading zero is optional).
```
umask
```

##### Set a new umask: Files become 664 (rw-rw-r--), directories 775 (rwxrwxr-x), allowing group write access.
```
umask 002
```


## Networking

Networking refers to the tools and techniques used to manage network interfaces, test connectivity, and monitor network activity on a Linux system.

* **`ifconfig`**: Displays and configures network interfaces (older tool, often replaced by ip).
* **`ip`**: Modern tool for managing network interfaces, routes, and more.
* **`netstat`**: Shows network statistics, connections, and routing tables (partly replaced by ss).
* **`ping`**: Tests connectivity to another host.
* **`traceroute`**: Traces the path packets take to a destination.

### Examples

1. View Network Interfaces with ifconfig:
```
ifconfig
```
2. List Interfaces with ip:
```
ip addr
```
3. Check Active Connections with netstat:
```
netstat -tulnp
```
4. Test Connectivity with ping:
```
ping -c 4 google.com
```
5. Trace a Route with traceroute: Shows the hops between your system and google.com.
```
traceroute google.com
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
11. **`join`**: Combines lines from two files based on a common field.
   - **Example**: Join two files (`file1.txt` and `file2.txt`) on their first column
```
join file1.txt file2.txt
```
12. **`split`** : Breaks a file into smaller pieces.
    - **Example**: Split bigfile.txt into 100-line chunks, named part-
```
split -l 100 bigfile.txt part-
```
13. **`tac`** : Displays a file’s lines in reverse order (opposite of cat).
   - **Example**: Reverse the lines of notes.txt
```
tac notes.txt
```
14. **`tee`** : Sends output to both a file and the screen (or another command).
   - **Example**: Save ls output to a file while displaying it
```
ls -l | tee output.txt
```
15. **`whereis`** : Locates the binary, source, and manual page files for a command.
   - **Example**: Find where bash is installed
```
whereis bash
```
16. **`shutdown`**: Safely powers off, reboots, or halts the system with a specified time and optional message.
   - **Example**: Shut down the system immediately.
```
shutdown -h now
```
   - **Example**: reboot in 10 Minutes with a Message
```
shutdown -r +10 "System rebooting for maintenance"
```
17. **`uname -r`**: Displays the kernel release version of the Linux system.
   - **Example**: 
```
uname -r 
```
18. **`hostnamectl`**: Manages and displays system hostname and related information.
   - **Example**: 
```
hostnamectl
```
   - **Example**: set hostname
```
sudo hostnamectl set-hostname newname
```
19. **`expr`**: Evaluates expressions and performs basic arithmetic or string operations.
   - **Example**: 
```
expr 5 + 3
```
20.  **`export`**: The export command in Linux is used to make variables available to other programs or processes that you run from your current shell session. In simpler terms, it’s like giving a variable a "passport" so it can travel beyond the shell you’re working in and be used by other commands, scripts, or applications you launch.
   - **Example**: 
```
export NAME="Alice"
echo "My name is $NAME"
```
21. **`whatis`**: Displays a one-line description of a command from its manual page.
   - **Example**: 
```
whatis ls
```
22. **`uniq`**: Filters out duplicate lines from sorted input or a file.
   - **Example**: 

```
echo -e "apple\napple\nbanana" | uniq
```
23. **`join`**: Combines lines from two files based on a common field.
   - **Example**: 
* File1 (f1.txt): 1 apple
* File2 (f2.txt): 1 red
```
join f1.txt f2.txt
```
24. **`uptime`**: Shows how long the system has been running and current load averages.
   - **Example**: 
```
uptime
```
## Services
### 1. What is a Service?
A service, often called a daemon, is a program that runs in the background, independent of any terminal or user session. Unlike interactive applications, services start automatically (often at boot) and don’t need user input to function. A long-running process that delivers a specific function, such as handling network requests or logging system events.

### 2. How Services Are Managed: Init Systems
Services are controlled by the init system, the first process started by the Linux kernel during boot (with process ID 1). The init system oversees starting, stopping, and managing all other processes, including services. Two primary init systems are used in Linux:

* **`SysVinit`**: The traditional init system found in older distributions.
* **`systemd`**: The modern init system adopted by most current distributions (e.g., Ubuntu, Fedora, CentOS).

### 3. Managing Services with systemd
systemd is the modern init system that has largely replaced SysVinit. It manages services through units (e.g., .service files) and provides a consistent command-line tool, systemctl.

#### Start a Service:
```
sudo systemctl start service_name
```
#### Stop a Service:
```
sudo systemctl stop service_name
```
#### Restart a Service:
```
sudo systemctl restart service_name
```
#### Enable a Service (auto-start on boot):
```
sudo systemctl enable service_name
```
#### Disable a Service (prevent auto-start):
```
sudo systemctl disable service_name
```
#### Check Service Status:
```
sudo systemctl status service_name
```

### 4. Key Differences Between SysVinit and systemd

| Feature         | SysVinit                          | systemd                              |
|----------------|----------------------------------|--------------------------------------|
| **Control Command** | `/etc/init.d/service_name action` | `systemctl action service_name`      |
| **Service Files**   | Scripts in `/etc/init.d/`    | Unit files (e.g., `/etc/systemd/system/`) |
| **Boot Process**    | Sequential startup          | Parallel startup (faster)            |
| **Logging**        | Stored in `/var/log/`        | Managed by `journald` (view with `journalctl`) |
| **Dependencies**   | Manually defined in scripts  | Automatically managed by unit files  |

### 5. Monitoring and Troubleshooting Services
#### 5.1 Checking Service Status
```
sudo systemctl status service_name
```
#### 5.2 Viewing Service Logs
```
sudo journalctl -u apache2
```
## system log

System logs are records of events and activities on a Linux system. They help administrators monitor performance, troubleshoot issues, and detect security problems. Logs are typically stored as text files and managed by a logging service.

### Key Logging Tools and Files
* **`/var/log`**: The default directory where most log files are stored.
* **`syslog or rsyslog`**: A common logging daemon that collects and writes log messages to files.
* **`journalctl`**: A tool for viewing logs managed by systemd’s journal system (modern Linux distributions).
### Common Log Files
* **`/var/log/syslog or /var/log/messages`**: General system logs (varies by distribution).
* **`/var/log/auth.log or /var/log/secure`**: Authentication-related logs (e.g., login attempts).
* **`/var/log/kern.log`**: Kernel-related messages.
* **`/var/log/dpkg.log`**: Logs for Debian-based package management (e.g., apt).

#### Examples

1. Viewing the Last 10 Lines of a Log File:
```
tail -n 10 /var/log/syslog
```

2. Monitoring Logs in Real-Time:
```
tail -f /var/log/auth.log
```
3. Using journalctl to View All Logs:
```
journalctl
```
4. Filtering Logs by Service:
```
journalctl -u sshd
```
5. Use grep to search logs:
```
grep "error" /var/log/syslog
```

## Archive and Compress
Archiving and compression are key skills in Linux for managing files—whether you’re trying to save space, bundle files together, or share them with others. In this section, we’ll explore what archiving and compression mean, and dive into tools like zip, gzip, and unzip.

* **Archiving**: This is when you combine multiple files or directories into a single file—like putting everything into one big box. Examples include .tar or .zip files. It’s great for organizing or transferring files.
* **Compression**: This shrinks a file’s size to save space, kind of like vacuum-sealing that box. Some tools do both archiving and compression, while others focus just on compression.

1. **zip**:  is a tool that both archives and compresses files or directories into a .zip file. It’s widely used because .zip files are compatible with many systems (Linux, Windows, etc.).


- **Example**: Compress a Single File:
```
zip notes.zip notes.txt
```
- **Example**: Compress multiple Files: Bundles file1.txt and file2.txt into backup.zip
```
zip backup.zip file1.txt file2.txt
```
- **Example**: Compress a Directory: -r (recursive) includes all files and subdirectories in documents/ into docs.zip.
```
zip -r docs.zip documents/
```
2. **gzip**: compresses individual files, replacing them with a .gz version. Unlike zip, it doesn’t archive multiple files into one—it works on one file at a time. Reduces file size and adds a .gz extension, deleting the original unless specified otherwise.
- **Example**: Compress a file and Keep the Original
```
gzip -k log.txt
```
- **Example**: Compress with Maximum Compression:
```
gzip -9 bigfile.txt
```
3. **unzip**: extracts files from a .zip archive, decompressing them and restoring the original files or directories. Reads the .zip file and unpacks its contents to your current directory (or a specified location).

- **Example**: Unpacks all files from backup.zip into the current directory.
```
unzip backup.zip
```
- **Example**: Extract to a Specific Folder
```
unzip docs.zip -d myfolder/
```
4. **Archive**: Since gzip only compresses single files, it’s often paired with tar for archiving multiple files
- **Example**: Create a .tar.gz (tar and gzip)
```
tar -czf archive.tar.gz documents/
```
- **Example**: Extract a .tar.gz
```
tar -xzf archive.tar.gz
```
## Wildcards
Wildcards (also known as "globbing") in Linux are special characters used to represent or match other characters in filenames or commands. They allow you to work with multiple files at once without typing each name individually, acting like a search filter directly in your terminal. Wildcards are processed by the shell (e.g., Bash), not the commands themselves. When you use a wildcard, the shell expands it into a list of matching files before passing them to the command.

There are three main wildcards in Linux:

* 1. *(Asterisk): The * wildcard matches any number of characters, including zero. It’s the most flexible and widely used wildcard. It can match part of a filename or an entire filename
- **Example**: List all .txt files:
```
ls *.txt
```
- **Example**: List all files starting with "log":
```
ls log*
```

* 2. ? (Question Mark): matches exactly one character—any character, but only one. It’s useful when you know the length of a filename but not the exact characters
- **Example**: List two-letter files:
```
ls ??
```

* 3. (Square Brackets) []: let you specify a set or range of characters to match at a specific position. You can list individual characters (e.g., [abc]) or a range (e.g., [a-c] for a, b, or c).
- **Example**: List files starting with "a", "b", or "c"
```
ls [abc]*
```
- **Example**: List files with a digit in the second position
```
ls ?[0-9].txt
```
- **Example**: List files ending with "a" or "b":
```
ls *.[ab]
```
- **Example**: List files starting with "data", followed by one character, ending with ".txt"
```
ls data?.txt
```
- **Example**: Copy Multiple Files
```
cp *.txt backup/
```
- **Example**: Lists all .log files in /var/log
```
ls /var/log/*.log
```
## Swap memory 
is an essential component of Linux systems that helps manage memory efficiently. It acts as a backup when the physical RAM (Random Access Memory) is fully utilized, allowing the system to continue running smoothly. In this document, we’ll explore what swap memory is, why it’s important, how to set it up, and how to manage and monitor it effectively.

Swap memory, also known as swap space, is a designated area on a hard drive (or other storage devices) that the operating system uses as an extension of the physical RAM. When the system runs low on available RAM, it moves inactive or less frequently used data from RAM to the swap space. This process is called swapping, and it frees up RAM for more critical tasks.

* Swap Partition: A dedicated partition on the disk reserved for swap.
* Swap File: A file within an existing filesystem that serves as swap space.

Swap memory is slower than physical RAM because disk access times are much higher than memory access times. However, it provides a crucial safety net to prevent the system from running out of memory.

Swap memory serves several key purposes:

1. Prevents Memory Exhaustion: When RAM is full, swap allows the system to continue running by temporarily storing less-used data on the disk.
2. Supports Hibernation: Swap is used to save the contents of RAM when the system enters hibernation mode.
3. Improves Multitasking: By moving inactive processes to swap, the system can handle more concurrent processes than the physical RAM alone would allow.
4. Manages Memory Pressure: Swap helps the system manage memory more efficiently, especially in environments with limited RAM.

Without swap, the system could freeze, crash, or terminate processes unexpectedly when RAM is fully consumed.

### Setting Up Swap Memory
There are two primary ways to set up swap in Linux: using a swap partition or a swap file. Both methods achieve the same goal, but they differ in flexibility and setup complexity.

1. Swap Partition

A swap partition is a dedicated section of the hard drive set aside exclusively for swap. It’s typically created during the Linux installation process, but you can also add one later.


   * 1.1 Create the Partition: Use a tool like fdisk, gdisk, or parted to create a new partition. Set the partition type to "Linux swap" (type 82 in fdisk).
```
sudo fdisk /dev/sda
```

Press n to create a new partition, choose a partition number, and specify the size.

Press t to set the type to 82 (Linux swap).
* 1.2 Format the Partition: Use mkswap to prepare the partition for swap usage
```
sudo mkswap /dev/sdaX
```
* 1.3  Activate the Swap Partition: Use swapon to enable the swap space.
```
sudo swapon /dev/sdaX
```
2. Swap File
A swap file is a file within an existing filesystem that is used as swap space. It’s more flexible than a partition because it doesn’t require repartitioning the disk.

* 2.1 Create the File: Use dd to create a file of the desired size. For example, to create a 1GB swap file:
```
sudo dd if=/dev/zero of=/swapfile bs=1M count=1024
```
* 2.2 Set Permissions: Ensure only root can access the swap file.
```
sudo chmod 600 /swapfile
```
* 2.3 Format the File: Use mkswap to set up the file as swap.
```
sudo mkswap /swapfile
```
* 2.4 Activate the Swap File: Use swapon to enable it.
```
sudo swapon /swapfile
```
3. Activating Swap Automatically at Boot

To ensure that your swap space (partition or file) is activated automatically when the system boots, you need to add an entry to the /etc/fstab file.

* 3.1 Find the UUID of the swap partition:
```
sudo blkid /dev/sdaX
```
* 3.2 Add the following line to /etc/fstab:
```
UUID=your-uuid-here none swap sw 0 0
```
* 3.3 for aswap file:
```
/swapfile none swap sw 0 0
```
* 3.4 After editing /etc/fstab, you can test the configuration with:
```
sudo mount -a
```
#### Monitoring
Below is an example output of the free -h command, followed by a detailed explanation of each column. The free -h command displays memory usage information in a human-readable format on a Linux system.

* Example Output of free -h

| Type  | Total | Used | Free | Shared | Buff/Cache | Available |
|-------|-------|------|------|--------|------------|------------|
| **Mem:** | 7.7G | 1.2G | 5.5G | 0.0K | 1.0G | 6.3G |
| **Swap:** | 2.0G | 0.0K | 2.0G | - | - | - |

1. Mem Row (Physical RAM)
total

**Value**: 7.7G

**Meaning**: The total amount of physical RAM installed on the system.

**Explanation**: In this example, the system has 7.7 gigabytes of RAM available. This is the total capacity of physical memory, excluding any reserved by the hardware or kernel.

* 1.1used

**Value**: 1.2G

**Meaning**: The amount of RAM currently in use by running processes.

**Explanation**: Here, 1.2 gigabytes of RAM are actively being used by applications and the operating system. This does not include memory used for buffers or cache (explained later).

* 1.2 free

**Value**: 5.5G

**Meaning**: The amount of RAM that is currently unused and immediately available for new processes.

**Explanation**: In this case, 5.5 gigabytes of RAM are free. However, in modern Linux systems, free memory might appear low because unused RAM is often utilized for caching to improve performance.

* 1.3 shared

**Value**: 0.0K

**Meaning**: The amount of RAM used by shared memory segments, accessible by multiple processes.

**Explanation**: Shared memory is typically used for inter-process communication (IPC). In this example, no memory (0 kilobytes) is allocated for shared segments, which is common unless specific applications require it.

* 1.4 buff/cache

**Value**: 1.0G

**Meaning**: The amount of RAM used for buffers and cache.

**Buffers**: Temporary storage for data being transferred, such as between disk and RAM.

**Cache**: Storage for frequently accessed data (e.g., file system cache) to speed up retrieval.

Here, 1.0 gigabyte is used for these purposes. This memory can be quickly reclaimed by the system if new processes need it, so it’s not permanently "taken."

* 1.5 available

**Value**: 6.3G

**Meaning**: The amount of RAM available for starting new applications without needing to use swap.

**Explanation**: This is a more practical indicator of usable memory than the "free" column. It includes free memory (5.5G) plus memory that can be freed from buffers and cache. In this case, 6.3 gigabytes are available, showing the system has ample memory for new tasks.

1. Swap Row (Swap Space)
The Swap row has fewer columns, focusing on swap space (disk-based virtual memory):

* 2.1 total

**Value**: 2.0G

**Meaning**: The total amount of swap space allocated on the disk.

Explanation: This system has 2.0 gigabytes of swap space, which acts as an overflow when physical RAM is full.

* 2.2 used

**Value**: 0.0K

**Meaning**: The amount of swap space currently in use.

**Explanation**: Here, no swap space (0 kilobytes) is being used, indicating that the system isn’t relying on slower disk storage, which is good for performance.

* 2.3 free

**Value**: 2.0G

**Meaning**: The amount of swap space that is currently unused.

**Explanation**: All 2.0 gigabytes of swap are free, meaning the system has not needed to use swap yet.


## Process
In Linux, a process is an instance of a running program. It includes the program’s code, its data (like variables), and the system resources it uses, such as memory, CPU time, and open files. Every process is assigned a unique identifier called a Process ID (PID), which the operating system uses to track and manage it. Processes are fundamental to how Linux operates, and knowing how to view, monitor, manage, and terminate them is essential for system administration or everyday use

A process can be in one of several states, which describe what it’s doing at any given time. You’ll see these states when viewing processes (e.g., in the S column of ps output):

* **`R (Running)`**: The process is currently executing on the CPU.
* **`S (Sleeping)`**: The process is waiting for an event, like user input or a timer.
* **`D (Uninterruptible Sleep)`**: The process is waiting for I/O (e.g., disk or network) and cannot be interrupted.
* **`Z (Zombie)`**: The process has finished, but its parent hasn’t cleaned up its exit status.
* **`T (Stopped)`**: The process has been paused, usually by a signal like Ctrl+Z.

### viewing processes

1. ps - Process Snapshot

The ps command gives you a static list of processes at a given moment.

Basic Usage:
```
ps
```

Output:

| PID  | TTY   | TIME     | CMD  |
|------|-------|---------|------|
| 1234 | pts/0 | 00:00:00 | bash |
| 5678 | pts/0 | 00:00:00 | ps   |

Explanation:

**`PID`**: Process ID.

**`TTY`**: Terminal associated with the process.

**`TIME`**: Total CPU time used.

**`CMD`**: The command or program running.

- **Example**: Displays processes owned by a specific user.
```
ps -u username
```
- **Example**: Shows every process on the system.
```
ps -e
```
2. Top

top shows a dynamic, real-time view of processes, sorted by resource usage (CPU by default).

```
top
```
* **`PID`**: Process ID.
* **`USER`**: Owner of the process.
* **`%CPU`**: CPU usage percentage.
* **`%MEM`**: Memory usage percentage.
* **`COMMAND`**: The program name.

* Press q to exit.
* Press k and enter a PID to kill a process.
* Press u to filter by user.

3. htop
htop is a more user-friendly alternative to top, with colors, mouse support, and a better interface.

```
htop
```
* Use arrow keys to select a process.
* Press F9 to send a signal (e.g., terminate).
* Press F5 to see processes in a tree view.

### Managing Processes

1. Running in the Background
Starts a process without tying up your terminal.

```
sleep 100 &
```
2. Bringing to the Foreground
Moves a background process to the foreground

```
fg %1
```
### Killing a process
To stop a process, you send it a signal. Common signals include SIGTERM (graceful stop) and SIGKILL (forceful stop).

1. kill - Send Signal by PID
```
kill 1234
```
Sends SIGTERM to PID 1234, asking it to exit cleanly.

2. Forceful Kill:
```
kill -9 1234
```
3. pkill - Kill by Name or Attribute
Targets processes by name or other properties.
```
pkill -f firefox
```
4. killall - Kill All by Name

```
killall firefox
```
### nice
The nice command is a utility in Linux that allows you to launch a process with a modified scheduling priority, known as its nice value. The nice value is a number that tells the system how "nice" a process should be to others—essentially, how much CPU time it should get relative to other processes. A lower nice value means higher priority (more CPU time), while a higher nice value means lower priority (less CPU time).

* **`-20`**: Highest priority (the process gets the most CPU time).
* **`0`**: Default priority (most processes start here unless changed).
* **`19`**: Lowest priority (the process gets the least CPU time).

Think of nice values like a politeness scale:

* A process with -20 is "rude" and demands CPU time first.
* A process with 19 is "very nice" and lets others go ahead.

* **`Negative Values (-20 to -1)`**: These give higher priority, but only the root user (superuser) can set them.
* **`Positive Values (0 to 19)`**: These lower the priority, and any user can set them.
* **`Relative Nature`**: Nice values don’t set exact CPU percentages—they influence how the scheduler favors one process over another.

For example, a process with a nice value of 10 will yield CPU time to one with 0, but both will still run, depending on system load.

- **Example**: Launches ffmpeg (a video encoder) with a nice value of 10, reducing its CPU priority so other tasks aren’t slowed down.

```
nice -n 10 ffmpeg -i input.mp4 output.mp4
```
- **Example**: Run a Command with Higher Priority (Root Only): 
```
sudo nice -n -5 important_task.sh
```

- **Example**: Check a Process’s Nice Value: 3955
```
ps -o pid,ni -p 3955
```

- **Example**: Lower the Priority of a Running Process: Changes the nice value of process ID 5678 to 15, reducing its priority.
```
renice -n 15 -p 5678
```

#### Points

* A regular user can only change the nice value between 0 and +19.
(In Linux, the nice value determines the priority of a process. Higher nice values mean lower priority.)

* Only the root user can set a process's nice value to a negative number.
(Negative nice values increase the priority of a process, allowing it to get more CPU time.)

* A regular user cannot increase the priority of a process. This means if a user changes a process's nice value from 0 to 4, they cannot later change it back to 2 (a lower nice value) because it would increase the priority.
(Only root can lower the nice value, which effectively raises the process priority.)

* Process priority becomes relevant only when there is contention, meaning when multiple processes are competing for system resources.
(If there is no resource contention, nice values have no practical effect because all processes get enough CPU time.)

## Hard Links and Soft Links in Linux

In Linux, links provide a way to reference files or directories from multiple locations without duplicating the data. There are two main types of links: `hardlinks` and `softlinks` (symbolic links). Understanding their differences and use cases is essential for effective file management, whether you’re organizing files, performing backups, or administering a system.

### 1. What is a Link?
A link is a pointer to a file or directory. It allows you to access the same data using multiple filenames, making file management more efficient without creating redundant copies.

* **`Hard Link`**: A direct reference to the file’s data on the disk.
* **`Soft Link (Symlink)`**: A reference to another filename, which then points to the data.

### 2. Hard Links
A hard link is an additional name for an existing file. It directly references the file’s data via its inode—a data structure in the filesystem that stores metadata (like permissions and ownership) and points to the file’s data blocks on the disk. When you create a hard link, both the original filename and the new hard link point to the same inode and data.

Key Characteristics of Hard Links:

* **`Same Inode`**: The hard link and the original file share the same inode number.
* **`No "Original" File`**: There’s no distinction between the original and the hard link—they’re equal references to the same data.
* **`Filesystem Limitation`**: Hard links can only be created within the same filesystem.
* **`Files Only`**: Hard links are typically for files, not directories (though root users can link directories, it’s rare and not recommended).
* **`Data Persistence`**: The data remains on the disk as long as at least one hard link exists. Deleting one link doesn’t affect the others or the data.

* Use the ln command without options:

```
ln report.txt report_backup.txt
```
Now, report.txt and report_backup.txt are two names for the same file. Editing one changes the other because they share the same data.


* Use ls -i to display inode numbers
```
ls -i report.txt report_backup.txt
```
### 3. Soft Links (Symbolic Links)
A soft link (or symbolic link) is a special type of file that points to another file or directory by its path. Unlike a hard link, a soft link doesn’t reference the data directly—it points to the target’s filename, which then resolves to the data. This makes symlinks more flexible but also prone to becoming "broken" if the target is moved or deleted.

Key Characteristics of Soft Links:

* **`Separate Inode`**: The symlink has its own inode, distinct from the target file’s inode.
* **`Cross-Filesystem Support`**: Symlinks can point to files or directories on different filesystems, including network locations.
* **`Directories Allowed`**: Symlinks can link to both files and directories.
* **`Broken Links`**: If the target file or directory is deleted or moved, the symlink becomes broken and points to nothing.
* **`Permissions`**: The symlink’s permissions are independent, but access to the target is governed by the target’s permissions.

- **Example**: file
```
ln -s report.txt report_link
```
- **Example**: directory
```
ln -s /var/log logs
```
Now, logs is a symlink to /var/log. You can use cd logs to access /var/log.


* Use ls -l to view the link and its target:
```
ls -l report_link
```
### 4. Key Differences Between Hard Links and Soft Links

| Feature            | Hard Link                          | Soft Link (Symlink)                |
|--------------------|----------------------------------|------------------------------------|
| **Inode**         | Shares the same inode as the original | Has its own inode                  |
| **Points To**     | Directly to the data blocks      | To the filename (path)            |
| **Cross Filesystems** | No, limited to the same filesystem | Yes, can span filesystems          |
| **Can Link Directories** | No (generally)                 | Yes                                |
| **Effect of Deleting** | Data persists if other hard links exist | Becomes broken if target is deleted |
| **Permissions**   | Same as the original file       | Independent, but target controls access |
| **Usage**         | Multiple names for the same file | Flexible references, shortcuts    |

## Cron Jobs in Linux
A cron job is a scheduled task in Linux that runs automatically at specified times or intervals. Managed by the cron daemon (a background service), cron jobs are widely used to automate repetitive tasks such as backups, system maintenance, or sending reports. This document provides everything you need to understand and implement cron jobs.
A cron job is a command or script scheduled to execute at specific times without manual intervention. It’s a time-based job scheduler that helps automate tasks, making it an essential tool for system administration.

* Backing up files or databases
* Clearing temporary files or logs
* Sending automated emails or notifications
* Running system updates or health checks

### 1. How Cron Works
The cron daemon (crond) runs continuously in the background, checking crontab (cron table) files for scheduled tasks. Each user can have their own crontab, and there’s a system-wide crontab for root-level tasks.

### 2. Cron Schedule Format
A cron job is defined by a line in the crontab file with six parts:

Five time fields: Minute, Hour, Day of the Month, Month, Day of the Week
Command: The task to execute

```
* * * * * command_to_run
| | | | |
| | | | +-- Day of the week (0-6) (Sunday=0 or 7)
| | | +---- Month (1-12)
| | +------ Day of the month (1-31)
| +-------- Hour (0-23)
+---------- Minute (0-59)
```
* **(`*`)**: Every (e.g., every minute, every hour)
* **`Numbers`**: Specific values (e.g., 5 for 5th minute)
* **`Ranges`**: Use - (e.g., 1-5 for Monday to Friday)
* **`Lists`**: Use , (e.g., 0,15,30,45 for every 15 minutes)
* **`Steps`**: Use / (e.g., */10 for every 10 minutes)

### 3. Setting Up Cron Jobs
Use the crontab command to create or manage cron jobs.

#### Edit Crontab:Opens the crontab file in your default editor.
```
crontab -e
```
#### List Cron Jobs: Shows your current cron jobs.
```
crontab -l
```
#### Remove All Cron Jobs: Deletes your entire crontab.
```
crontab -r
```
#### Edit Another User’s Crontab (as root):
```
sudo crontab -e -u username
```
### 4. Writing Cron Job Entries
Here are practical examples of cron job schedules:

#### Run a Script Daily at 2:30 AM:
```
30 2 * * * /path/to/script.sh
```
* Minute: 30
* Hour: 2
* Day/Month/Week: * (every)

#### Run a Command Every 15 Minutes:
```
*/15 * * * * /path/to/command
```
* Minute: */15 (every 15 minutes)
* Others: * (every)

#### Backup Database Every Sunday at Midnight:
```
0 0 * * 0 /usr/bin/mysqldump -u user -p password dbname > /backup/db.sql
```
* Minute: 0
* Hour: 0
* Day of Week: 0 (Sunday)

#### Run a Job on the 1st and 15th of Every Month at 8:00 AM:
```
0 8 1,15 * * /path/to/report.sh
```
* Minute: 0
* Hour: 8
* Day of Month: 1,15










