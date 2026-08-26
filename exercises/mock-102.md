# LPIC-1 102-500 Mock Exam A

This original practice exam follows the official version 5.0 objective weights:
each objective contributes exactly its published weight in questions. It is not
an LPI question dump or a prediction of live items.

- Time limit: **90 minutes**
- Questions: **60**
- Points: **1 per question**
- Materials: closed book for the first attempt
- Fill-in answers: command/file names only unless the question says otherwise

Record uncertain answers; do not open the [answer key](mock-102-answers.md)
until the timer ends.

## Topic 105: Shells and Shell Scripting

### Objective 105.1 (questions 1–4)

1. For an interactive Bash login shell, which user file is considered first?
   - A. `~/.bashrc`
   - B. `~/.bash_profile`
   - C. `~/.bash_logout`
   - D. `/etc/skel/.profile`

2. What is the defining effect of `. settings.sh` or `source settings.sh`?
   - A. It runs the file in a child shell.
   - B. It executes the file in the current shell.
   - C. It only checks syntax.
   - D. It exports every variable automatically.

3. Why is placing `.` at the beginning of root's `PATH` dangerous?
   - A. It disables shell builtins.
   - B. A writable current directory can supply a misleading command first.
   - C. It prevents absolute paths.
   - D. It clears aliases.

4. Changes made under `/etc/skel/` normally affect which accounts?
   - A. Every existing account immediately
   - B. Only root
   - C. Future home directories created with skeleton processing
   - D. Only systemd services

### Objective 105.2 (questions 5–8)

5. What is the first line `#!/bin/bash` called?
   - A. Here document
   - B. Shebang
   - C. Shell trap
   - D. Function prototype

6. Which expansion forwards all script arguments while preserving each original
   argument boundary?
   - A. `$*`
   - B. `"$@"`
   - C. `$#`
   - D. `$$`

7. In `backup && verify || alert`, when is `verify` attempted?
   - A. Only after `backup` succeeds
   - B. Only after `backup` fails
   - C. Always
   - D. Only when `alert` succeeds

8. Why is a setuid Bash script not a suitable privilege mechanism on Linux?
   - A. Bash cannot read arguments.
   - B. Interpreted setuid scripts are generally ignored due to security/race problems.
   - C. Scripts cannot be owned by root.
   - D. `chmod` cannot set execute bits on scripts.

## Topic 106: User Interfaces and Desktops

### Objective 106.1 (questions 9–10)

9. In X11 terminology, which component controls the physical display and input
   devices?
   - A. X client
   - B. X server
   - C. Window decoration
   - D. Desktop application only

10. Which pair manages X authentication cookies and names the target display?
    - A. `xauth` and `DISPLAY`
    - B. `xhost +` and `PATH`
    - C. `Wayland` and `EDITOR`
    - D. `XDMCP` and `LANG`

### Objective 106.2 (question 11)

11. Which protocol is commonly associated with virtualization-console remote
    display?
    - A. SPICE
    - B. NTP
    - C. LDAP
    - D. SMTP

### Objective 106.3 (question 12)

12. Which feature controls automatic repeated-key input caused by holding a key
    down?
    - A. Sticky keys
    - B. Repeat-key settings
    - C. Screen magnifier
    - D. Braille display

## Topic 107: Administrative Tasks

### Objective 107.1 (questions 13–17)

13. Why is `getent passwd alice` preferable to only grepping `/etc/passwd`?
    - A. It changes the account database.
    - B. It follows NSS and can include directory services.
    - C. It prints password hashes.
    - D. It creates the user's home.

14. Which command appends `alice` to supplementary group `developers` without
    replacing existing supplementary groups?
    - A. `usermod -G developers alice`
    - B. `usermod -aG developers alice`
    - C. `groupmod -a alice developers`
    - D. `useradd -G developers alice`

15. What remains possible after only locking a user's password?
    - A. Nothing can authenticate as that account.
    - B. SSH public-key or other non-password authentication may still work.
    - C. The user's UID is deleted.
    - D. Every running process is terminated.

16. Fill in the command used to inspect and configure password aging:
    `__________`

17. Which service-account choice is normally safest when interactive login is
    unnecessary?
    - A. UID 0 with `/bin/bash`
    - B. No password and a non-login shell with narrow file access
    - C. Shared administrator password
    - D. World-writable home directory

### Objective 107.2 (questions 18–21)

18. How many time fields appear before the command in a normal user crontab?
    - A. 4
    - B. 5
    - C. 6
    - D. 7

19. What extra field appears in `/etc/crontab` compared with a user crontab?
    - A. Kernel version
    - B. Username to run as
    - C. Exit code
    - D. Time zone database path

20. Which command removes a queued `at` job?
    - A. `atq`
    - B. `atrm`
    - C. `crontab -r`
    - D. `systemctl cancel`

21. What does `Persistent=true` in a systemd calendar timer do?
    - A. Runs the service continuously.
    - B. May trigger a missed event after the timer becomes active again.
    - C. Prevents the timer from being disabled.
    - D. Writes output to `/etc/crontab`.

### Objective 107.3 (questions 22–24)

22. Which locale variable overrides every individual `LC_*` category?
    - A. `LANG`
    - B. `LC_ALL`
    - C. `TZ`
    - D. `DISPLAY`

23. Why is `LC_ALL=C command` useful in a script?
    - A. It requests predictable C-locale output/sorting for that command.
    - B. It converts every file to ASCII.
    - C. It changes the system time zone.
    - D. It enables Unicode fonts.

24. Which command converts known ISO-8859-1 input to UTF-8?
    - A. `locale -f ISO-8859-1 -t UTF-8 file`
    - B. `iconv -f ISO-8859-1 -t UTF-8 input >output`
    - C. `tzselect ISO-8859-1 UTF-8`
    - D. `date --unicode file`

## Topic 108: Essential System Services

### Objective 108.1 (questions 25–27)

25. Which command copies the running system clock to the hardware clock while
    treating the RTC as UTC?
    - A. `date --rtc`
    - B. `hwclock --systohc --utc`
    - C. `timedatectl set-ntp true`
    - D. `ntpdate --hardware`

26. Which UDP port is normally used by NTP?
    - A. 53
    - B. 110
    - C. 123
    - D. 514

27. Which command displays Chrony source state?
    - A. `chronyc sources -v`
    - B. `ntpd -q sources`
    - C. `date --peers`
    - D. `hwclock --sources`

### Objective 108.2 (questions 28–31)

28. In a classic syslog selector, what does `*.warning` normally match?
    - A. Warning only
    - B. Warning and more urgent severities
    - C. Less urgent messages only
    - D. Kernel messages only

29. Which location normally makes systemd journal data survive reboot?
    - A. `/run/log/journal/`
    - B. `/tmp/journal/`
    - C. `/var/log/journal/`
    - D. `/etc/journal/`

30. Fill in the `journalctl` option used to read a copied journal directory:
    `journalctl __________=/mnt/recovery/var/log/journal`

31. Which command checks a logrotate policy without performing rotation?
    - A. `logrotate --debug /etc/logrotate.conf`
    - B. `logrotate --delete /etc/logrotate.conf`
    - C. `logger --rotate-test`
    - D. `journalctl --rotate-only`

### Objective 108.3 (questions 32–34)

32. After editing `/etc/aliases`, which command normally rebuilds the alias
    database?
    - A. `mailq`
    - B. `newaliases`
    - C. `postfix -forward`
    - D. `sendmail -bp`

33. Which per-user file requests local mail forwarding when supported?
    - A. `~/.mailrc`
    - B. `~/.forward`
    - C. `~/.aliases`
    - D. `~/.postfix`

34. What does `mailq` normally display through an MTA compatibility layer?
    - A. User inbox messages
    - B. Mail transfer queue
    - C. DNS MX records
    - D. CUPS jobs

### Objective 108.4 (questions 35–36)

35. Which command lists a printer queue using the LPD-compatible interface?
    - A. `lpq`
    - B. `lprm`
    - C. `newaliases`
    - D. `atq`

36. Which command removes a configured CUPS queue named `lab-printer`?
    - A. `lprm lab-printer`
    - B. `lpadmin -x lab-printer`
    - C. `cancel -p lab-printer`
    - D. `cupsd --delete lab-printer`

## Topic 109: Networking Fundamentals

### Objective 109.1 (questions 37–40)

37. What is the network address of `192.0.2.77/27`?
    - A. `192.0.2.0`
    - B. `192.0.2.32`
    - C. `192.0.2.64`
    - D. `192.0.2.77`

38. Which service normally uses TCP port 22?
    - A. DNS
    - B. SSH
    - C. NTP
    - D. IMAP

39. Which protocol provides an ordered byte stream with retransmission?
    - A. ICMP
    - B. UDP
    - C. TCP
    - D. ARP

40. Which statement about IPv6 is correct?
    - A. It uses broadcast for Neighbor Discovery.
    - B. Link-local addresses are within `fe80::/10`.
    - C. Every LAN must use `/128`.
    - D. ICMPv6 can be blocked entirely without effect.

### Objective 109.2 (questions 41–44)

41. Which file controls the source order for hostname resolution?
    - A. `/etc/services`
    - B. `/etc/nsswitch.conf`
    - C. `/etc/hostname`
    - D. `/etc/fstab`

42. Which command lists NetworkManager connection profiles?
    - A. `nmcli connection show`
    - B. `ip profile list`
    - C. `hostnamectl connections`
    - D. `ifup --show`

43. Which Wi-Fi connection option avoids placing a password directly in shell
    history?
    - A. `nmcli device wifi connect SSID --ask`
    - B. `nmcli device wifi connect SSID password SECRET`
    - C. `echo SECRET | nmcli history`
    - D. `ifup --password SECRET`

44. Where are systemd-networkd `.network` files commonly stored?
    - A. `/etc/systemd/network/`
    - B. `/etc/NetworkManager/keys/`
    - C. `/var/spool/network/`
    - D. `/usr/share/hosts/`

### Objective 109.3 (questions 45–48)

45. Which command asks the kernel which route/source/interface it would use for
    `198.51.100.10`?
    - A. `ip route get 198.51.100.10`
    - B. `route add 198.51.100.10`
    - C. `traceroute --kernel 198.51.100.10`
    - D. `ss route 198.51.100.10`

46. Which command shows listening TCP and UDP sockets numerically with process
    information when permitted?
    - A. `ss -lntup`
    - B. `ip -br address`
    - C. `ping -a`
    - D. `hostname -i`

47. Why can `ping` fail while HTTPS works?
    - A. HTTPS never uses IP.
    - B. ICMP echo may be filtered while TCP 443 is allowed.
    - C. DNS disables ICMP automatically.
    - D. A default route is unnecessary for HTTPS.

48. Which legacy command corresponds most closely to `ip route`?
    - A. `ifconfig`
    - B. `route`
    - C. `netstat -i` only
    - D. `host`

### Objective 109.4 (questions 49–50)

49. Which command tests the system's configured NSS path rather than DNS alone?
    - A. `dig`
    - B. `host`
    - C. `getent hosts name`
    - D. `traceroute name`

50. `dig @192.0.2.53 app.example` succeeds but `getent hosts app.example`
    fails. Which local file should be inspected first for lookup-source order?
    - A. `/etc/nsswitch.conf`
    - B. `/etc/services`
    - C. `/etc/shadow`
    - D. `/etc/cups/cupsd.conf`

## Topic 110: Security

### Objective 110.1 (questions 51–53)

51. Which `find` test selects files with the setuid bit set?
    - A. `-perm -4000`
    - B. `-perm -0400`
    - C. `-uid +4000`
    - D. `-mode setuid`

52. Which tool safely validates `/etc/sudoers` syntax while editing?
    - A. `sudo -l`
    - B. `visudo`
    - C. `su -`
    - D. `ulimit`

53. Which command displays currently logged-in users plus activity and load?
    - A. `lastlog`
    - B. `w`
    - C. `chage`
    - D. `fuser`

### Objective 110.2 (questions 54–56)

54. In the shadow-password model, where are protected password hashes normally
    stored?
    - A. `/etc/passwd`
    - B. `/etc/shadow`
    - C. `/etc/nologin`
    - D. `/etc/hosts.deny`

55. A disabled systemd service starts when a connection arrives. What should be
    checked?
    - A. Its `.socket` unit
    - B. Only `/etc/resolv.conf`
    - C. The user's umask
    - D. The hardware clock

56. Why must `/etc/hosts.allow` not be assumed to protect every modern service?
    - A. TCP wrappers apply only to applications built/configured to use them.
    - B. It controls UDP only.
    - C. It is a printer configuration file.
    - D. It is always generated from DNS.

### Objective 110.3 (questions 57–60)

57. What security purpose does `known_hosts` serve after trustworthy enrollment?
    - A. It stores user private keys.
    - B. It detects unexpected SSH server host-key changes.
    - C. It grants sudo access.
    - D. It encrypts local files.

58. Which SSH option creates a local SOCKS proxy?
    - A. `-L`
    - B. `-R`
    - C. `-D`
    - D. `-X`

59. What does a valid GPG signature establish after the signer's key identity
    has been verified?
    - A. Confidentiality of plaintext
    - B. Integrity and use of the corresponding signing private key
    - C. Secure deletion
    - D. Compression ratio

60. Fill in the command that loads a private key into a running SSH agent:
    `__________`

## Readiness interpretation

- 54–60: strong result; review every uncertain or guessed answer
- 48–53: close, but repair weak objectives before booking
- Below 48: return to the mapped chapters and labs

This threshold is a study heuristic, not LPI's confidential scoring method.
