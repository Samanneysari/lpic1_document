# LPIC-1 Answer Key

Use these answers to correct reasoning, not merely to count correct choices. Equivalent commands may be valid when they preserve safety and intended behavior.

## Topic 101 answers

1. **101-Q1:** `/dev` contains device nodes used for I/O; `/proc` exposes process and kernel runtime views; `/sys` exposes the structured device/driver model and kernel attributes.
2. **101-Q2:** `modprobe` resolves dependencies and uses module configuration. `insmod` inserts one module file directly.
3. **101-Q3:** `cat /proc/cmdline`.
4. **101-Q4:** SysV runlevel meanings are conventions implemented by each distribution. Debian historically configured 2–5 similarly, while RPM distributions commonly distinguished 3 and 5.
5. **101-Q5:** `wall 'Reboot in 15 minutes'`; `shutdown -r +15 'Scheduled reboot'`; cancel with `shutdown -c`.
6. **101-Q6:** Investigate the initramfs first because it must contain the drivers and userspace tools needed to unlock and locate the real root filesystem before normal userspace starts.

## Topic 102 answers

1. **102-Q1:** Partitions on one disk share the same physical failure domain. Deletion, controller failure, disk failure or theft can affect all of them. A backup is a tested independent copy.
2. **102-Q2:** A PV is LVM-initialized storage, a VG pools one or more PVs, and an LV allocates virtual block storage from a VG.
3. **102-Q3:** It is generated and can be overwritten. Edit source files such as `/etc/default/grub` and `/etc/grub.d/*`, then regenerate with the distribution's tool.
4. **102-Q4:** `ldd /bin/cp`, used only on a trusted executable.
5. **102-Q5:** `apt update` refreshes repository metadata. `apt upgrade` installs eligible newer package versions using that metadata.
6. **102-Q6:** Debian: `dpkg -S /path`. RPM: `rpm -qf /path`.
7. **102-Q7:** Examples: machine ID, SSH host keys, hostname, MAC-bound network configuration, DHCP leases, cloud-init instance state and application secrets.

## Topic 103 answers

1. **103-Q1:** Single quotes preserve content literally. Double quotes preserve one argument while allowing variable and command substitution.
2. **103-Q2:** `uniq` operates on adjacent duplicate lines. Use `sort file | uniq` or `sort -u file` when equal lines are separated.
3. **103-Q3:** `find /etc -type f -name '*.conf' -mtime -7 -print`.
4. **103-Q4:** `2>&1` duplicates stderr to stdout's current destination. In `cmd >out 2>&1`, both go to `out`; in `cmd 2>&1 >out`, stderr remains at stdout's old destination.
5. **103-Q5:** A glob is expanded by the shell to pathnames; a regex is interpreted by a text-processing program to match text.
6. **103-Q6:** SIGTERM.
7. **103-Q7:** `if=` selects input and `of=` selects output. Reversing them can overwrite the source or a disk.
8. **103-Q8:** In Normal mode: `dd`, `u`, `/server`, Enter, then `:wq` and Enter.

## Topic 104 answers

1. **104-Q1:** Device enumeration depends on the machine and can change. It could be absent, disposable, or contain critical data; prove identity with size, model, filesystem and mounts.
2. **104-Q2:** `df` reports filesystem-wide allocation from filesystem metadata. `du` walks directory entries and totals reachable file usage; deleted-open files, sparse files and permissions can make results differ.
3. **104-Q3:** Modifying metadata while the mounted filesystem is changing can produce inconsistent observations and corruption. Use an offline check unless the filesystem/tool explicitly supports online operation.
4. **104-Q4:** Source, mount point, filesystem type, options, dump field, filesystem-check order.
5. **104-Q5:** setgid plus owner `rwx`, group `r-x`, others `---`: symbolic `u=rwx,g=rx,o=,g+s`.
6. **104-Q6:** The kernel clears masked bits from a requested mode using bit operations. Applications can request modes other than the common 666/777 starting values.
7. **104-Q7:** The inode and data remain accessible through every remaining hard link until link count reaches zero and no process holds the file open.
8. **104-Q8:** It queries a periodically refreshed database rather than walking the live filesystem.

## Topic 105 answers

1. **105-Q1:** Bash considers `~/.bash_profile`, then `~/.bash_login`, then `~/.profile`, stopping at the first readable one. A selected file may source `~/.bashrc` explicitly.
2. **105-Q2:** An alias is simple interactive text substitution. A function is shell code that accepts arguments, variables and control flow.
3. **105-Q3:** `"$@"` expands each original argument as a separate word, preserving spaces and empty arguments.
4. **105-Q4:** `if [ "$#" -eq 1 ] && [ -f "$1" ] && [ -r "$1" ]; then ...; fi`.
5. **105-Q5:** It makes a pipeline's status reflect a failing component instead of only the final command, subject to shell rules.
6. **105-Q6:** Linux generally ignores setuid on scripts due to interpreter/race security problems. Use narrow sudo rules or a purpose-built helper.
7. **105-Q7:** A successful `exec command` replaces the shell process, so later script statements do not run.

## Topic 106 answers

1. **106-Q1:** It provides display/input services to client applications, possibly across a network; the physical screen is on the server side.
2. **106-Q2:** A display manager provides graphical login/session startup; a window manager places/decorates windows; a desktop environment integrates a full session and applications.
3. **106-Q3:** It broadly disables X server access control, potentially allowing other clients to observe input or manipulate the session.
4. **106-Q4:** XWayland is an X server compatibility layer that runs X11 clients within a Wayland environment.
5. **106-Q5:** Any five of screen reader, Braille display, magnifier, high contrast, large text, on-screen keyboard, sticky keys, slow keys, bounce keys, mouse keys, gestures or voice recognition.

## Topic 107 answers

1. **107-Q1:** `getent` follows Name Service Switch and can include local files, LDAP and other configured sources.
2. **107-Q2:** Lowercase `-u` changes UID. Uppercase `-U` unlocks the password.
3. **107-Q3:** It replaces the user's supplementary groups with the supplied list. `-aG` appends.
4. **107-Q4:** Cron has a limited/different PATH and working environment; absolute paths remove ambiguity and executable-hijacking risk.
5. **107-Q5:** User crontabs have five time fields and run as that user. `/etc/crontab` has an additional username field and is system-managed.
6. **107-Q6:** A missed calendar event may be triggered after the timer becomes active again, commonly after downtime.
7. **107-Q7:** `LANG` is the default, a category-specific `LC_*` overrides that category, and `LC_ALL` overrides every category.

## Topic 108 answers

1. **108-Q1:** The system clock is maintained by the running kernel; RTC persists in hardware; time zone converts instants for local display.
2. **108-Q2:** Multiple independent sources allow comparison, selection and resilience against an unavailable or inaccurate source.
3. **108-Q3:** `emerg`, `alert`, `crit`, `err`, `warning`, `notice`, `info`, `debug`.
4. **108-Q4:** `journalctl -b -u sshd.service -p warning` (use `ssh.service` where that is the actual unit). A single priority also includes more urgent messages.
5. **108-Q5:** Volatile journal data under `/run` is lost at reboot. Persistent data under `/var/log/journal` survives according to retention policy.
6. **108-Q6:** `newaliases` rebuilds the MTA alias database. `.forward` requests per-user forwarding when supported and permitted.
7. **108-Q7:** `lpq`/`lpstat` list; `cancel JOB_ID` or `lprm JOB_ID` removes an authorized job.

## Topic 109 answers

1. **109-Q1:** TCP is a reliable ordered byte stream; UDP sends independent datagrams without built-in delivery/order; ICMP carries control and diagnostic messages.
2. **109-Q2:** `/27` blocks are 32 addresses. 77 falls in 64–95: network `198.51.100.64`, broadcast `198.51.100.95`, typical hosts 65–94.
3. **109-Q3:** IPv6 depends on ICMPv6 for Neighbor Discovery, Path MTU discovery and control/error functions.
4. **109-Q4:** `/etc/hostname`, `/etc/hosts`, `/etc/nsswitch.conf`, `/etc/resolv.conf` respectively.
5. **109-Q5:** `ip -br address`; `ip route`; `ip route get ADDRESS`; `ss -lnt`.
6. **109-Q6:** Echo requests/replies can be filtered while TCP 443 is permitted and the web service works.
7. **109-Q7:** `getent hosts` tests the configured NSS path. `dig` makes a DNS query and bypasses non-DNS sources such as `/etc/hosts`.
8. **109-Q8:** Application resolver call → NSS order → files/local stub/cache → recursive resolver → root/TLD/authoritative delegation when uncached → answer/TTL back through caches → application opens its transport connection.

## Topic 110 answers

1. **110-Q1:** `find / -xdev -type f \( -perm -4000 -o -perm -2000 \) -print`.
2. **110-Q2:** It tests loopback from the same host; external firewall rules, routing and service bind addresses may produce a different result.
3. **110-Q3:** `sudo` runs approved commands under policy with per-command logging. `su -` changes identity and starts a login-like environment, commonly after target/root authentication depending policy.
4. **110-Q4:** A `.socket` unit can listen and activate the service on demand. Inspect and disable the socket where appropriate.
5. **110-Q5:** It records expected host public keys and warns when a server identity unexpectedly changes, reducing man-in-the-middle risk after trustworthy enrollment.
6. **110-Q6:** `-L` opens a local listener to a destination through the server; `-R` opens a listener on the remote side; `-D` creates a local SOCKS proxy.
7. **110-Q7:** Encryption provides confidentiality to intended private-key holders. Signing provides integrity and evidence that the signing private key was used.
8. **110-Q8:** A valid signature only links data to a key. You must establish through a trusted method that the key belongs to the intended signer.

## Mock assessment answers

### Part A

| Question | Answer | Explanation |
|---:|:---:|---|
| 1 | B | `/sys` is the structured kernel device model. |
| 2 | B | `modprobe` resolves dependencies. |
| 3 | B | `set-default` changes future normal boot target. |
| 4 | B | `dpkg -S` searches installed path ownership. |
| 5 | A | `rpm -V` verifies installed metadata/content attributes. |
| 6 | B | `>>` appends stdout. |
| 7 | B | Null delimiters preserve spaces, newlines and special characters. |
| 8 | C | SIGTERM normally permits cleanup. |
| 9 | C | `:wq` writes and quits. |
| 10 | D | Field six controls check order. |
| 11 | C | Leading 2 is setgid. |
| 12 | B | Quoted `$@` preserves argument boundaries. |
| 13 | A | `.bashrc` is the normal interactive Bash file. |
| 14 | B | Uppercase `-U` unlocks. |
| 15 | B | `getent` follows NSS. |
| 16 | A | `ip route get` performs a kernel route lookup. |
| 17 | D | `emerg` is severity 0 and most urgent. |
| 18 | B | `sshd -t` validates syntax/options. |
| 19 | A | `-L` is local forwarding. |
| 20 | B | A signature supports integrity/authenticity after key validation. |

### Part B

21. Inspect inode usage with `df -i`; also consider quotas and reserved blocks if inodes are not exhausted.
22. Existing processes retain their supplementary group list. Start a new login session; `newgrp` can start a shell with a selected group but is not identical to a full fresh login.
23. Inspect `hosts:` in `/etc/nsswitch.conf`, `/etc/hosts`, `/etc/resolv.conf`, local stub/systemd-resolved state and application sandboxing/cache.
24. Likely causes: limited PATH, different working directory, missing environment variables, permissions, non-executable script, shell differences, no TTY and unhandled output.
25. Keep the existing session; ensure console/rollback; back up config; make minimal change; run `sshd -t`; reload rather than restart; open a second connection and verify before closing the first.
26. Confirm PID/name, process state, logs, open files/locks, whether it is stuck in uninterruptible sleep, child processes and data-cleanup consequences.
27. Clients cannot distinguish clones and host-trust warnings become meaningless, enabling impersonation risk. Regenerate unique host keys through the distribution/template provisioning procedure and verify fingerprints.
28. `-y` automatically accepts potentially data-losing repairs, and modifying fsck on a mounted writable production filesystem can corrupt metadata. Use backup, downtime and offline diagnostics first.
29. No. Legitimate configuration changes produce verification differences. Investigate ownership, change control, package baseline and logs.
30. Inspect the corresponding `.socket` unit and other activation mechanisms.

### Part C

31. One solution:

```bash
cut -d: -f7 /etc/passwd | sort | uniq -c | sort -nr
```

32. One solution:

```bash
find /var/log -type f -size +10M -mtime -7 -print
```

33. Example:

```bash
#!/usr/bin/env bash
if [ "$#" -ne 1 ] || [ ! -d "$1" ]; then
    printf 'Usage: %s DIRECTORY\n' "$0" >&2
    exit 2
fi
find "$1" -maxdepth 1 -type f -printf '.' | wc -c
```

34. Example:

```fstab
UUID=11111111-2222-3333-4444-555555555555 /srv/data ext4 defaults,nofail 0 2
```

35. `journalctl -u sshd.service -p warning --since today`.

36. `nmcli connection show` followed by `nmcli --fields GENERAL,IP4,IP6 device show`.

37. Example:

```bash
ssh-keygen -t ed25519 -a 100 -C 'lab-key'
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
ssh-keygen -lf ~/.ssh/id_ed25519.pub
```

38. Example:

```bash
tar -czf project.tar.gz project/
tar -tzf project.tar.gz
sha256sum project.tar.gz
```

39. Inspect then terminate:

```bash
pgrep -a -x process-name
pkill -TERM -x process-name
```

40. `OnCalendar=*-*-* 03:30:00`. `Persistent=true` allows a missed event to run after the timer becomes active again.
