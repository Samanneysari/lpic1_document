# LPIC-1 Exercises and Mock Assessment

Complete chapter questions first. This file adds mixed questions that require choosing between similar commands and reasoning about failures.

Do not open the [answer key](answers.md) until you have written your answer and confidence level.

## Part A: Multiple choice

1. Which directory primarily exposes the kernel device model?
   - A. `/etc`
   - B. `/sys`
   - C. `/home`
   - D. `/opt`

2. Which command loads a module while resolving dependencies?
   - A. `insmod`
   - B. `modprobe`
   - C. `lsmod`
   - D. `modinfo`

3. Which command changes the default systemd boot target?
   - A. `systemctl isolate`
   - B. `systemctl set-default`
   - C. `systemctl enable`
   - D. `telinit 0`

4. Which command finds the installed Debian package owning `/bin/ls`?
   - A. `dpkg -L /bin/ls`
   - B. `dpkg -S /bin/ls`
   - C. `apt show /bin/ls`
   - D. `apt-cache owns /bin/ls`

5. Which command verifies files from an installed RPM package?
   - A. `rpm -V package`
   - B. `rpm -K package`
   - C. `rpm -ql package`
   - D. `rpm2cpio package`

6. Which operator appends standard output?
   - A. `>`
   - B. `>>`
   - C. `2>`
   - D. `<`

7. Which expression safely preserves arbitrary filename boundaries between `find` and `xargs`?
   - A. `find . | xargs`
   - B. `find . -print0 | xargs -0`
   - C. `find . -print | xargs -n0`
   - D. `find . | xargs --spaces`

8. Which signal normally allows graceful cleanup?
   - A. SIGKILL
   - B. SIGSTOP
   - C. SIGTERM
   - D. SIGCHLD

9. Which vi command writes and quits?
   - A. `:q!`
   - B. `dd`
   - C. `:wq`
   - D. `/wq`

10. Which fstab field controls filesystem-check order?
    - A. First
    - B. Third
    - C. Fifth
    - D. Sixth

11. What does mode `2750` include?
    - A. Sticky bit
    - B. setuid
    - C. setgid
    - D. World write

12. Which expansion preserves separate script arguments?
    - A. `$*`
    - B. `"$@"`
    - C. `$#`
    - D. `$$`

13. Which file is normally a user interactive Bash configuration?
    - A. `~/.bashrc`
    - B. `/etc/fstab`
    - C. `~/.forward`
    - D. `/etc/aliases`

14. Which command unlocks a password with `usermod`?
    - A. `usermod -u user`
    - B. `usermod -U user`
    - C. `usermod -L user`
    - D. `usermod -G user`

15. Which utility tests the system's configured NSS name-resolution path?
    - A. `dig`
    - B. `getent`
    - C. `traceroute`
    - D. `ss`

16. Which command predicts the kernel route to `198.51.100.10`?
    - A. `ip route get 198.51.100.10`
    - B. `ss 198.51.100.10`
    - C. `route add 198.51.100.10`
    - D. `ip neigh flush 198.51.100.10`

17. Which syslog severity is most urgent?
    - A. `debug`
    - B. `warning`
    - C. `alert`
    - D. `emerg`

18. Which command validates sshd configuration without reloading it?
    - A. `ssh -T`
    - B. `sshd -t`
    - C. `ssh-keygen -t`
    - D. `systemctl status sshd`

19. What does `ssh -L` create?
    - A. Local port forwarding
    - B. Remote port forwarding
    - C. Dynamic forwarding only
    - D. X11 forwarding

20. What is the primary purpose of a GPG signature?
    - A. Hide plaintext from everyone
    - B. Demonstrate integrity and possession of the signing private key
    - C. Compress a file
    - D. Replace backups

## Part B: Short scenarios

21. A filesystem reports no free space, but `df -h` shows available blocks. What should you inspect next?

22. A user was added to a group but a running shell does not show membership. Explain why and give a safe remedy.

23. `dig @192.0.2.53 app.example.com` succeeds but `getent hosts app.example.com` fails. Name three local areas to inspect.

24. A cron command works interactively but fails from cron. List four likely causes.

25. An SSH configuration change is required on a remote server. Describe a safe change-and-verification sequence.

26. A process ignores SIGTERM. What should you inspect before using SIGKILL?

27. A cloned VM has the same SSH host-key fingerprint as its template. Explain the risk and required class of repair.

28. An administrator runs `fsck -y` on a mounted production filesystem. Identify both major problems.

29. `rpm -V` reports a changed configuration file. Does this prove compromise? Explain.

30. A service is disabled but still starts when a connection arrives. What systemd feature should you inspect?

## Part C: Practical tasks

31. Produce a sorted count of login shells from `/etc/passwd`.
32. Find regular files under `/var/log` larger than 10 MiB and modified in the last seven days without deleting them.
33. Create a Bash script that requires one directory, reports an error to stderr if invalid, and prints the number of regular files if valid.
34. Write an fstab entry using a placeholder UUID for ext4 mounted at `/srv/data`, with `defaults,nofail` and normal non-root check order.
35. Write a journal query for warnings and more urgent messages from `sshd.service` since today.
36. Write a NetworkManager command sequence that lists profiles and displays DNS/gateway data without changing the host.
37. Write commands to create a passphrase-protected Ed25519 key, load it into an agent and show its fingerprint.
38. Write commands to create a gzip-compressed tar archive, list it and calculate SHA-256.
39. Write an exact-name process lookup followed by graceful termination.
40. Write a systemd timer calendar expression for every day at 03:30 and explain `Persistent=true`.

## Scoring

- Multiple choice: 1 point each
- Scenarios: 3 points each
- Practical tasks: 4 points each
- Total: 90 points

Recommended readiness target: at least 80%, with no unsafe action in practical work. This score is for study planning and is not an LPI scoring model.
