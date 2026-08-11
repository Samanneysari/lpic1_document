# Topic 107: Administrative Tasks

## 107.1 User and group administration

### Account databases

| File | Purpose | Important fields |
|---|---|---|
| `/etc/passwd` | User identity and login metadata | name, UID, GID, comment, home, shell |
| `/etc/shadow` | Protected password hash and aging fields | hash, last change, minimum, maximum, warning, expiry |
| `/etc/group` | Group membership and GID | name, password placeholder, GID, members |
| `/etc/gshadow` | Protected group administration data | group password/admin/member data |
| `/etc/skel` | Templates for newly created home directories | shell startup files and local defaults |

Use `getent` rather than reading local files exclusively when systems may use LDAP or another name service:

```bash
getent passwd alice
getent group developers
id alice
```

### Create a user explicitly

Defaults vary by distribution and `/etc/login.defs`, `/etc/default/useradd` or tool configuration. State important choices:

```bash
sudo useradd --create-home --shell /bin/bash --comment 'Alice Example' alice
sudo passwd alice
id alice
getent passwd alice
```

| Option | Meaning |
|---|---|
| `--create-home` / `-m` | Creates the home and copies skeleton files when applicable |
| `--shell` / `-s` | Sets login shell |
| `--comment` / `-c` | Sets the GECOS/comment field |

`useradd alice` alone does not have identical home-directory and private-group behavior on all distributions.

### Modify membership safely

```bash
sudo groupadd developers
sudo usermod --append --groups developers alice
id alice
```

Group lists use commas when supplied as one option value:

```bash
sudo usermod -aG developers,operators alice
```

Using `-G` without `-a` replaces supplementary membership with the specified list. A user may need to start a new login session before new membership affects processes.

### Locking and disabling

```bash
sudo passwd -l alice
sudo passwd -u alice
sudo usermod -L alice
sudo usermod -U alice
sudo chage -E 0 alice
```

Lowercase `usermod -u` changes UID; uppercase `-U` unlocks the password. Locking a password does not necessarily block SSH keys or other authentication. Account expiration, shell policy and access services must be considered when disabling all login methods.

Inspect aging:

```bash
sudo chage -l alice
sudo chage -M 90 -W 14 alice
```

### Delete carefully

```bash
sudo userdel alice
sudo userdel --remove alice
sudo groupdel developers
```

`--remove` attempts to remove the home and mail spool. Search for files owned by the UID and preserve required business data before deletion.

Modify group metadata:

```bash
sudo groupmod --new-name platform developers
```

### System and limited accounts

Service accounts normally have no interactive password, a non-login shell and narrowly scoped file access:

```bash
sudo useradd --system --home-dir /var/lib/example \
    --create-home --shell /usr/sbin/nologin example-svc
```

Paths and default UID ranges vary. Do not run network services as root merely for convenience.

## 107.2 Schedule administrative jobs

### User crontab

```bash
crontab -e
crontab -l
crontab -r -i
```

A user crontab entry has five time fields followed by the command:

```cron
15 2 * * 1-5 /usr/local/bin/report >>/home/alice/report.log 2>&1
```

| Field | Value | Meaning |
|---|---|---|
| minute | `15` | At minute 15 |
| hour | `2` | At 02:00 |
| day of month | `*` | Every day of month |
| month | `*` | Every month |
| day of week | `1-5` | Monday through Friday |

Cron has a limited environment. Use absolute paths, protect files, make scripts executable and log output. Do not place passwords in the command line.

System `/etc/crontab` and files in `/etc/cron.d` include an additional username field. Periodic directories may include `/etc/cron.daily`, `/etc/cron.weekly`, and related paths.

Cron implementations store per-user crontabs below a protected spool such as
`/var/spool/cron/` or `/var/spool/cron/crontabs/`. Do not edit spool files
directly; use `crontab -e` so locking, ownership and syntax handling are applied.

Access may be controlled with `/etc/cron.allow`, `/etc/cron.deny`, `/etc/at.allow`, and `/etc/at.deny`; exact precedence and defaults are implementation-specific, so read the local manuals.

### One-time `at` jobs

```bash
printf '%s\n' '/usr/local/bin/report' | at 23:30
atq
at -c JOB_NUMBER
atrm JOB_NUMBER
```

`atq` lists queued jobs, `at -c` displays a queued job and `atrm` removes it. The `atd` service must be running.

### systemd timers

`/etc/systemd/system/example-report.service`:

```ini
[Unit]
Description=Generate example report

[Service]
Type=oneshot
ExecStart=/usr/local/bin/report
```

`/etc/systemd/system/example-report.timer`:

```ini
[Unit]
Description=Run example report daily

[Timer]
OnCalendar=*-*-* 02:15:00
Persistent=true
RandomizedDelaySec=5m

[Install]
WantedBy=timers.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now example-report.timer
systemctl list-timers --all
systemctl status example-report.timer
journalctl -u example-report.service
```

`Persistent=true` can trigger a missed calendar run after downtime. `RandomizedDelaySec` spreads load. Verify the service manually before enabling the timer.

Run a transient timer:

```bash
systemd-run --user --on-active=5m /usr/bin/printf 'timer fired\n'
```

## 107.3 Localisation and internationalisation

Locale controls language, sorting, numeric formats, dates and character classes.

```bash
locale
locale -a
printf '%s\n' "$LANG" "$LC_ALL"
LC_ALL=C sort names.txt
```

`LANG` supplies a default. Individual `LC_*` variables override categories. `LC_ALL` overrides all categories and is useful temporarily for predictable script parsing; avoid setting it globally without reason.

UTF-8 is a Unicode encoding. ASCII covers a smaller character set. ISO-8859 families are older single-byte encodings. Convert a known source encoding with:

```bash
iconv -f ISO-8859-1 -t UTF-8 input.txt > output.txt
```

Specify the correct source encoding; guessing can corrupt text.

### Time zones

```bash
timedatectl
timedatectl list-timezones | less
sudo timedatectl set-timezone Asia/Baku
date
readlink -f /etc/localtime
```

Time zone data is under `/usr/share/zoneinfo`. Systems may also maintain `/etc/timezone`. `TZ` can override the time zone for one process:

```bash
TZ=UTC date
```

`tzselect` is an interactive helper that suggests a `TZ` value; by itself it
does not necessarily change the system-wide time zone. Use the distribution's
supported method, such as `timedatectl set-timezone`, for persistent host
configuration.

## Lab 107: Account and timer lifecycle

1. Create a lab group and user with explicit home and shell settings.
2. Add two supplementary groups and verify them.
3. Configure password aging and inspect it.
4. Lock the password and explain which login methods may remain.
5. Write a oneshot service that creates a timestamped report.
6. schedule it with a timer five minutes in the future.
7. Verify execution from the journal.
8. Disable/remove the timer and remove the lab account safely.

## Exercises

1. **107-Q1:** Why is `getent` preferable to only grepping `/etc/passwd`?
2. **107-Q2:** What dangerous difference exists between `usermod -u` and `usermod -U`?
3. **107-Q3:** What happens if `usermod -G` is used without `-a`?
4. **107-Q4:** Why should cron jobs use absolute paths?
5. **107-Q5:** Contrast a user crontab and `/etc/crontab`.
6. **107-Q6:** What does `Persistent=true` mean in a calendar timer?
7. **107-Q7:** Explain the precedence of `LANG`, category-specific `LC_*`, and `LC_ALL`.

Answers are in [the answer key](../exercises/answers.md#topic-107-answers).

## Official reading

- Local manuals: `useradd(8)`, `usermod(8)`, `chage(1)`, `crontab(5)`, `at(1)`
- [systemd.timer](https://www.freedesktop.org/software/systemd/man/latest/systemd.timer.html)
- [systemd-run](https://www.freedesktop.org/software/systemd/man/latest/systemd-run.html)
