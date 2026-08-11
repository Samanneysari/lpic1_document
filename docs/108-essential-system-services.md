# Topic 108: Essential System Services

## 108.1 Maintain system time

### Three time concepts

| Concept | Description |
|---|---|
| System clock | Kernel-maintained time while Linux is running |
| Hardware clock (RTC) | Battery-backed clock that can persist while powered off |
| Time zone | Rules used to display an instant as local civil time |

Servers should normally keep the hardware clock in UTC and apply a time zone for display.

```bash
date --iso-8601=seconds
timedatectl status
sudo hwclock --show
```

Change time manually only when synchronization is deliberately disabled and the operational impact is understood:

```bash
sudo timedatectl set-ntp false
sudo timedatectl set-time '2026-08-11 12:00:00'
sudo hwclock --systohc --utc
```

Time jumps can affect logs, certificates, databases and distributed systems. Prefer synchronization.

### NTP and chrony

NTP estimates clock offset and network delay. A client exchanges timestamped packets with multiple sources and corrects its clock. UDP port 123 is normally used.

Chrony configuration is commonly `/etc/chrony.conf` or `/etc/chrony/chrony.conf`:

```text
pool pool.ntp.org iburst
makestep 1.0 3
rtcsync
```

| Directive | Meaning |
|---|---|
| `pool` | Uses multiple servers obtained from a pool name |
| `iburst` | Speeds initial measurements after startup |
| `makestep 1.0 3` | Allows stepping when offset exceeds 1 second during first three updates |
| `rtcsync` | Enables supported kernel RTC synchronization behavior |

Verify:

```bash
chronyc tracking
chronyc sources -v
timedatectl status
```

Traditional `ntpd` commonly uses `/etc/ntp.conf`. `ntpq -p` displays peers on implementations that provide classic ntpq. `ntpdate` performs a one-time adjustment and is legacy/deprecated in many modern deployments but remains an exam term.

Do not expose an unrestricted NTP server to untrusted networks. Apply vendor defaults and access controls.

## 108.2 System logging

### Syslog model

A syslog message has a facility and severity/priority. A selector routes matching messages to an action.

Common facilities include `auth`, `authpriv`, `cron`, `daemon`, `kern`, `mail`, `user`, and `local0` through `local7`.

Severities from most urgent to least urgent:

| Number | Name |
|---:|---|
| 0 | `emerg` |
| 1 | `alert` |
| 2 | `crit` |
| 3 | `err` |
| 4 | `warning` |
| 5 | `notice` |
| 6 | `info` |
| 7 | `debug` |

In a classic selector, `*.warning` normally includes warning and more urgent messages, not only warning.

Example rsyslog rule:

```text
authpriv.*    /var/log/secure-auth
local0.*      /var/log/example-app.log
```

Exact default files differ: Debian-family systems commonly use `/var/log/syslog` and `/var/log/auth.log`; RPM-family systems commonly use `/var/log/messages` and `/var/log/secure`.

`systemd-journald` collects structured journal records. rsyslog can read journal
or syslog input and route selected messages to traditional text files or remote
collectors. The exact handoff is distribution-configured, so duplicate or
missing messages must be investigated in both services. Classic `syslogd` and
`syslog-ng` are alternative logging implementations that may use different
configuration syntax.

Generate and inspect a test message:

```bash
logger -p local0.notice -t lpic-lab 'test message'
journalctl -t lpic-lab
```

### Remote logging

Traditional rsyslog forwarding syntax recognizes:

```text
*.*  @192.0.2.20:514
*.*  @@192.0.2.20:514
```

One `@` traditionally means UDP; two mean TCP. Production forwarding should use authenticated encryption where supported, queues, rate limits and restricted firewall rules. A central collector must explicitly load/configure its input module and listen address; do not expose it openly.

Validate rsyslog configuration before restart:

```bash
sudo rsyslogd -N1
sudo systemctl reload rsyslog
```

### systemd journal

```bash
journalctl -b
journalctl -u ssh.service
journalctl -p warning
journalctl --since 'today 08:00' --until 'today 10:00'
journalctl -f
journalctl --disk-usage
```

| Filter | Purpose |
|---|---|
| `-b` | Current boot |
| `-u` | Unit |
| `-p` | Priority range |
| `--since`, `--until` | Time range |
| `-f` | Follow new messages |

Persistent journal storage normally uses `/var/log/journal`; volatile storage uses `/run/log/journal`. Configure policy in `/etc/systemd/journald.conf` or preferably a drop-in under `/etc/systemd/journald.conf.d/`.

Example drop-in:

```ini
[Journal]
Storage=persistent
SystemMaxUse=500M
```

```bash
sudo systemctl restart systemd-journald
journalctl --disk-usage
sudo journalctl --vacuum-time=30d
```

Vacuuming deletes archived journal data and is irreversible. Retention must match incident-response and compliance needs.

Read an offline journal copied or mounted at `/mnt/recovery/var/log/journal`:

```bash
journalctl --directory=/mnt/recovery/var/log/journal
```

Send stdin to the journal:

```bash
printf 'example event\n' | systemd-cat -t lpic-lab -p info
```

### Log rotation

`logrotate` archives, compresses and removes old text logs according to policy. Global configuration is `/etc/logrotate.conf`; packages commonly add `/etc/logrotate.d/*`.

```text
/var/log/example-app.log {
    weekly
    rotate 8
    compress
    missingok
    notifempty
    create 0640 root adm
}
```

Test without rotating:

```bash
sudo logrotate --debug /etc/logrotate.conf
```

Some applications must reopen log files after rotation, using `postrotate` or native reopen mechanisms. Avoid `copytruncate` unless its small data-loss race is acceptable.

## 108.3 Mail Transfer Agent basics

An MTA transfers mail between queues and systems. Common MTAs include Postfix, Sendmail and Exim. LPIC-1 requires awareness and basic client-host forwarding/aliases, not full Internet mail-server deployment.

### Aliases

`/etc/aliases` can redirect local recipients:

```text
postmaster: root
root: admin@example.net
```

Rebuild the alias database:

```bash
sudo newaliases
```

### User forwarding

A user's `~/.forward` may contain a destination:

```text
admin@example.net
```

Permissions and MTA policy determine whether it is honored. Forwarding can leak sensitive system mail, create loops or expose addresses; use approved destinations.

### Client commands

```bash
printf 'test body\n' | mail -s 'LPIC test' root
mailq
sendmail -bp
```

`mailq` and `sendmail -bp` commonly display the MTA queue through a Sendmail-compatible command layer. A successful `mail` command does not prove remote delivery; inspect logs and queue state.

## 108.4 Manage printers and printing

CUPS provides a print scheduler, queues, filters and network printing. Configuration is under `/etc/cups`; administration may be available through `http://localhost:631` when enabled and allowed.

`/etc/cups/cupsd.conf` controls the scheduler and access policy. Queue data is
normally managed with CUPS tools rather than by editing generated files such as
`printers.conf` directly.

```bash
lpstat -t
lpstat -p -d
lpoptions -d printer-name
lp -d printer-name document.pdf
lpq -P printer-name
cancel JOB_ID
lprm JOB_ID
```

| Command | Purpose |
|---|---|
| `lpstat` | Shows scheduler, printer and queue state |
| `lpoptions -d` | Sets a default destination for the user |
| `lp` / `lpr` | Submits a job |
| `lpq` | Displays queue in LPD-compatible style |
| `cancel` / `lprm` | Removes an allowed queued job |

An administrator can create and remove a lab queue with `lpadmin`. The device
URI and driver/model depend on the real printer:

```bash
sudo lpadmin -p lab-printer -E \
    -v ipp://printer.example.net/ipp/print -m everywhere
lpstat -p lab-printer -l
sudo lpadmin -x lab-printer
```

| Part | Meaning |
|---|---|
| `-p lab-printer` | Selects the queue name |
| `-E` after `-p` | Enables the queue and accepts jobs in this command context |
| `-v` | Sets the printer device URI |
| `-m everywhere` | Requests driverless IPP Everywhere support when available |
| `-x` | Deletes the named queue, not the physical printer |

Use a real authorized printer URI and consult the installed CUPS manuals;
older printers may require a different model/PPD workflow.

Service troubleshooting:

```bash
systemctl status cups
journalctl -u cups
ss -ltnp | grep ':631'
```

Restrict printer administration and remote access. Do not expose the CUPS web interface broadly without authentication, TLS and firewall policy.

## Lab 108: Time and logs

1. Record system clock, RTC interpretation, time zone and synchronization state.
2. Identify active time sources with Chrony or the installed NTP implementation.
3. Send a tagged message with `logger`.
4. Find it by tag, time and priority in the journal.
5. Write a temporary rsyslog rule for `local0` in a lab VM.
6. Validate configuration before reload.
7. Create a logrotate policy for the lab file and test with `--debug`.
8. Remove the temporary rule and policy.

## Exercises

1. **108-Q1:** Contrast system clock, RTC and time zone.
2. **108-Q2:** Why should multiple NTP sources be used?
3. **108-Q3:** Order syslog severities from `emerg` to `debug`.
4. **108-Q4:** Write a journal query for SSH warnings from the current boot.
5. **108-Q5:** What is the difference between volatile and persistent journal storage?
6. **108-Q6:** What do `newaliases` and `.forward` do?
7. **108-Q7:** Which commands list and remove print jobs?

Answers are in [the answer key](../exercises/answers.md#topic-108-answers).

## Official reading

- [chrony documentation](https://chrony-project.org/documentation.html)
- [rsyslog documentation](https://www.rsyslog.com/doc/)
- [journalctl manual](https://www.freedesktop.org/software/systemd/man/latest/journalctl.html)
- [CUPS documentation](https://openprinting.github.io/cups/)
