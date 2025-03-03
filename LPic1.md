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
The Linux operating system organizes its files in a hierarchical structure known as the Filesystem Hierarchy Standard (FHS). Below is a comprehensive list of the main directories in Linux, along with their definitions:
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




