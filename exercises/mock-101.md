# LPIC-1 101-500 Mock Exam A

This original practice exam follows the official version 5.0 objective weights:
each objective contributes exactly its published weight in questions. It is not
an LPI question dump or a prediction of live items.

- Time limit: **90 minutes**
- Questions: **60**
- Points: **1 per question**
- Materials: closed book for the first attempt
- Fill-in answers: command/file names only unless the question says otherwise

Record uncertain answers; do not open the [answer key](mock-101-answers.md)
until the timer ends.

## Topic 101: System Architecture

### Objective 101.1 (questions 1–2)

1. Which virtual filesystem presents the kernel's structured device model?
   - A. `/etc`
   - B. `/sys`
   - C. `/home`
   - D. `/opt`

2. Which command both identifies a PCI device's numeric ID and shows its bound
   kernel driver?
   - A. `lsusb -t`
   - B. `lsmod -a`
   - C. `lspci -nnk`
   - D. `modprobe -l`

### Objective 101.2 (questions 3–5)

3. Put the components in normal boot order:
   - A. kernel → firmware → bootloader → initramfs → PID 1
   - B. firmware → bootloader → kernel/initramfs → real root → PID 1
   - C. bootloader → firmware → PID 1 → kernel → real root
   - D. firmware → PID 1 → bootloader → kernel → initramfs

4. Which command shows messages only from the current systemd boot?
   - A. `journalctl -b`
   - B. `dmesg -c`
   - C. `last reboot`
   - D. `systemctl get-default`

5. Fill in the file that exposes the kernel command line used for the current
   boot: `__________`

### Objective 101.3 (questions 6–8)

6. Which command changes the default systemd target for future boots?
   - A. `systemctl isolate multi-user.target`
   - B. `systemctl set-default multi-user.target`
   - C. `systemctl enable rescue.target`
   - D. `telinit multi-user.target`

7. What is the main operational risk of `systemctl isolate rescue.target` over
   SSH?
   - A. It rewrites the partition table.
   - B. It can stop networking and terminate the remote session.
   - C. It permanently changes the default target.
   - D. It disables the kernel module loader.

8. Which sequence warns users, schedules a reboot in ten minutes and then
   cancels it?
   - A. `write reboot; reboot +10; reboot -c`
   - B. `wall 'reboot'; shutdown -r +10; shutdown -c`
   - C. `mesg y; init 6 +10; init -c`
   - D. `notify-send reboot; systemctl reboot +10; systemctl cancel`

## Topic 102: Linux Installation and Package Management

### Objective 102.1 (questions 9–10)

9. Which statement about a separate `/home` partition is correct?
   - A. It is automatically an independent backup.
   - B. It can separate capacity and mount policy but shares the disk's failure domain.
   - C. It is mandatory for UEFI.
   - D. It prevents root from reading user files.

10. Which order correctly describes LVM layering before a filesystem is made?
    - A. LV → VG → PV
    - B. VG → PV → LV
    - C. PV → VG → LV
    - D. PV → LV → VG

### Objective 102.2 (questions 11–12)

11. Which GRUB 2 file is normally generated and should not be the primary file
    edited by an administrator?
    - A. `/etc/default/grub`
    - B. `/etc/grub.d/40_custom`
    - C. `/boot/grub/grub.cfg`
    - D. `/etc/fstab`

12. In a UEFI system, firmware normally loads an EFI executable from which
    partition type?
    - A. BIOS boot partition
    - B. Linux swap partition
    - C. EFI System Partition
    - D. LVM physical volume

### Objective 102.3 (question 13)

13. Fill in the command that prints the shared-library dependencies of a trusted
    dynamic executable: `__________`

### Objective 102.4 (questions 14–16)

14. Which command finds the installed Debian package that owns `/bin/bash`?
    - A. `dpkg -L /bin/bash`
    - B. `dpkg -S /bin/bash`
    - C. `apt-cache depends /bin/bash`
    - D. `dpkg-reconfigure /bin/bash`

15. What does `apt update` do?
    - A. Installs every available upgrade.
    - B. Refreshes repository metadata.
    - C. Reconfigures installed packages.
    - D. Verifies every installed file.

16. Which tool can search package contents for a file in a Debian package that
    is not installed, after its index is prepared?
    - A. `apt-file search`
    - B. `dpkg -S`
    - C. `apt remove`
    - D. `dpkg --verify`

### Objective 102.5 (questions 17–19)

17. Which RPM query reports the installed package owning a path?
    - A. `rpm -ql PATH`
    - B. `rpm -qf PATH`
    - C. `rpm -V PATH`
    - D. `rpm -K PATH`

18. What does output from `rpm -V package` prove by itself?
    - A. The host is compromised.
    - B. Selected installed attributes differ from package metadata.
    - C. The RPM signature is invalid.
    - D. Every dependency is installed.

19. Which command family normally resolves repository dependencies for an
    RPM-based system?
    - A. `rpm2cpio`
    - B. `ldconfig`
    - C. DNF/YUM or Zypper
    - D. `dpkg`

### Objective 102.6 (question 20)

20. Which item must normally be unique after cloning a Linux VM template?
    - A. `/etc/services`
    - B. D-Bus machine ID and SSH host keys
    - C. `/usr/bin/bash`
    - D. Package-manager cache format

## Topic 103: GNU and Unix Commands

### Objective 103.1 (questions 21–24)

21. Which quoting form prevents variable expansion and preserves all characters
    until the closing quote?
    - A. Double quotes
    - B. Single quotes
    - C. Backticks
    - D. Parentheses

22. Which command can identify whether `cd` is a builtin and show all `python`
    command resolutions?
    - A. `which`
    - B. `locate`
    - C. `type`
    - D. `whereis`

23. After `course=LPIC1`, what makes the value available to subsequently
    started child processes?
    - A. `set course`
    - B. `export course`
    - C. `env course`
    - D. `source course`

24. Fill in the common Bash history file in a user's home directory:
    `__________`

### Objective 103.2 (questions 25–26)

25. Why can `uniq file` leave duplicate lines in its output?
    - A. It compares only adjacent lines.
    - B. It ignores lowercase characters.
    - C. It reads only standard input.
    - D. It requires numeric input.

26. Which command prints decompressed `archive.xz` content to standard output
    without replacing the source file?
    - A. `unxz archive.xz`
    - B. `xzcat archive.xz`
    - C. `tar -xf archive.xz`
    - D. `split archive.xz`

### Objective 103.3 (questions 27–30)

27. Which `find` expression selects regular files larger than 10 MiB?
    - A. `-type d -size 10M`
    - B. `-type f -size +10M`
    - C. `-file -gt 10M`
    - D. `-name +10M`

28. Which pipeline preserves arbitrary filename boundaries?
    - A. `find . | xargs sha256sum`
    - B. `find . -print | xargs -n0 sha256sum`
    - C. `find . -type f -print0 | xargs -0 sha256sum`
    - D. `find . -spaces | xargs sha256sum`

29. Which `tar` option selects xz compression?
    - A. `z`
    - B. `j`
    - C. `J`
    - D. `Z`

30. In `dd if=source.img of=copy.img`, what does `of=` name?
    - A. Input format
    - B. Output file
    - C. Offset field
    - D. Open flags only

### Objective 103.4 (questions 31–34)

31. Which descriptor is standard error?
    - A. 0
    - B. 1
    - C. 2
    - D. 3

32. What is the effect of `command >out 2>&1`?
    - A. stdin and stdout go to `out`.
    - B. stdout and stderr go to `out`.
    - C. Only stderr goes to `out`.
    - D. `out` is appended, not truncated.

33. Which command copies its input to both stdout and a file?
    - A. `tee`
    - B. `paste`
    - C. `split`
    - D. `xargs`

34. Which utility converts records received on stdin into command arguments?
    - A. `tr`
    - B. `xargs`
    - C. `od`
    - D. `nl`

### Objective 103.5 (questions 35–38)

35. Which shell command lists jobs started from the current shell?
    - A. `ps`
    - B. `jobs`
    - C. `top`
    - D. `watch`

36. Which signal should normally be attempted before SIGKILL?
    - A. SIGSTOP
    - B. SIGCHLD
    - C. SIGTERM
    - D. SIGCONT

37. Which command selects an exact process name before terminating it?
    - A. `pkill -TERM -x name`
    - B. `killall -9 '*name*'`
    - C. `kill -f name`
    - D. `ps -kill name`

38. Which tool provides a detachable interactive terminal session?
    - A. `nohup` only
    - B. `screen` or `tmux`
    - C. `free`
    - D. `uptime`

### Objective 103.6 (questions 39–40)

39. What is the usual default nice value of a normally created process?
    - A. -20
    - B. -1
    - C. 0
    - D. 19

40. An unprivileged user's process has nice value 10. Which requested change
    normally requires privilege because it raises scheduling priority?
    - A. 10 → 15
    - B. 10 → 19
    - C. 10 → 5
    - D. No change ever requires privilege

### Objective 103.7 (questions 41–43)

41. Which ERE matches a line containing exactly `yes` or `no`?
    - A. `^(yes|no)$`
    - B. `^[yes|no]$`
    - C. `*(yes,no)*`
    - D. `^yes+no$`

42. Which command treats `.*` as literal characters rather than a regex?
    - A. `grep -E '.*' file`
    - B. `grep -F '.*' file`
    - C. `grep -v '.*' file`
    - D. `sed '.*' file`

43. What does `sed 's/old/new/g' file` do by default?
    - A. Modifies `file` in place.
    - B. Prints transformed text with every match on a line replaced.
    - C. Replaces only filenames.
    - D. Deletes matching lines.

### Objective 103.8 (questions 44–46)

44. In vi Normal mode, which command yanks the current line?
    - A. `dd`
    - B. `yy`
    - C. `p`
    - D. `i`

45. Which vi command quits and discards unsaved changes?
    - A. `:wq`
    - B. `ZZ`
    - C. `:q!`
    - D. `:w!`

46. Which environment variable commonly selects the default text editor?
    - A. `DISPLAY`
    - B. `PAGER`
    - C. `EDITOR`
    - D. `SHELLLEVEL`

## Topic 104: Devices, Linux Filesystems and FHS

### Objective 104.1 (questions 47–48)

47. Which tool is specifically focused on GPT partition tables?
    - A. `gdisk`
    - B. `mkswap`
    - C. `tune2fs`
    - D. `xfs_db`

48. Which Btrfs feature creates independently mountable filesystem tree roots
    without being a disk partition?
    - A. Logical partition
    - B. Subvolume
    - C. Inode table
    - D. Swap extent

### Objective 104.2 (questions 49–50)

49. `df -h` shows free blocks but file creation fails with “No space left on
    device.” What should be checked next?
    - A. `df -i`
    - B. `ldd`
    - C. `lsmod`
    - D. `grub-mkconfig`

50. Which command performs a no-modify XFS repair diagnostic?
    - A. `fsck -y device`
    - B. `xfs_repair -n device`
    - C. `xfs_fsr -w device`
    - D. `mke2fs -n device`

### Objective 104.3 (questions 51–53)

51. Which `/etc/fstab` field controls filesystem-check order?
    - A. First
    - B. Third
    - C. Fifth
    - D. Sixth

52. Which identifier is normally safer than `/dev/sdb1` for a persistent fstab
    entry?
    - A. PID
    - B. UUID
    - C. UID
    - D. PCI bus number

53. What is the systemd mount-unit name for `/srv/data`?
    - A. `srv/data.mount`
    - B. `/srv/data.mount`
    - C. `srv-data.mount`
    - D. `data@srv.mount`

### Objective 104.5 (questions 54–56)

54. What does mode `2770` set on a directory?
    - A. setuid and world read
    - B. setgid with owner/group full access
    - C. sticky bit with world full access
    - D. no special bit

55. With requested file mode 666 and umask 027, what mode normally results?
    - A. 640
    - B. 650
    - C. 639
    - D. 777

56. Which command changes only a file's group owner?
    - A. `chmod`
    - B. `chgrp`
    - C. `umask`
    - D. `groupset`

### Objective 104.6 (questions 57–58)

57. Which property is true of a hard link?
    - A. It can cross filesystems.
    - B. It has a different inode from its target.
    - C. It is another name for the same inode.
    - D. It always becomes dangling when another name is deleted.

58. Which command creates a symbolic link named `current` to `release-2`?
    - A. `ln release-2 current`
    - B. `ln -s release-2 current`
    - C. `cp -s current release-2`
    - D. `link --soft current release-2`

### Objective 104.7 (questions 59–60)

59. Why can `locate report.conf` show a file that no longer exists?
    - A. It searches shell history.
    - B. It uses a periodically refreshed database.
    - C. It follows only symbolic links.
    - D. It reads package metadata only.

60. Under the FHS, where should host-specific system configuration normally
    reside?
    - A. `/etc`
    - B. `/srv`
    - C. `/run`
    - D. `/opt/bin`

## Readiness interpretation

- 54–60: strong result; review every uncertain or guessed answer
- 48–53: close, but repair weak objectives before booking
- Below 48: return to the mapped chapters and labs

This threshold is a study heuristic, not LPI's confidential scoring method.
