# How to Use This Guide

## What LPIC-1 tests

LPIC-1 validates distribution-neutral Linux administration. It is not limited to Ubuntu, Debian, Red Hat, or SUSE. You must recognize both modern tools and legacy tools explicitly named in the official objectives.

Exam 101 focuses on architecture, installation, packages, GNU/Unix commands, devices and filesystems. Exam 102 focuses on shells, graphical interfaces, administrative work, services, networking and security.

## How each example is written

Commands use this format:

```bash
command --option argument
```

Then the guide explains each part:

| Part | Meaning |
|---|---|
| `command` | Program being executed |
| `--option` | Changes the program's behavior |
| `argument` | The object on which the program operates |

Lines beginning with `$` in displayed output represent an unprivileged shell prompt. Lines beginning with `#` represent a root prompt. Do not type the prompt itself.

## Build a safe lab

Use snapshots and disposable virtual disks. Before a storage command, verify the target at least twice:

```bash
lsblk -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINTS,MODEL
findmnt
```

`lsblk` lists block devices. `-o` selects explicit columns. `findmnt` shows mounted filesystems. If a target contains important data or is mounted, stop.

Use example hostnames and addresses reserved for documentation:

- Domains: `example.com`, `example.net`, `example.org`
- IPv4 documentation networks: `192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24`
- IPv6 documentation prefix: `2001:db8::/32`

## Distribution differences

Where commands differ, the guide labels them:

| Family | Examples | Package tools | Common service names |
|---|---|---|---|
| Debian | Debian, Ubuntu | `dpkg`, `apt`, `apt-get` | `ssh`, `cron` |
| RPM/Red Hat | RHEL, Rocky, AlmaLinux, Fedora | `rpm`, `dnf`, legacy `yum` | `sshd`, `crond` |
| SUSE | openSUSE, SLES | `rpm`, `zypper` | `sshd`, `cron` |

Always inspect the local manual before assuming an option exists:

```bash
man command
command --help
```

## The verification habit

After every change, verify the desired state. For example:

```bash
sudo systemctl enable --now ssh
systemctl is-enabled ssh
systemctl is-active ssh
```

| Line | Purpose |
|---|---|
| `enable --now` | Enables future boot startup and starts the service now |
| `is-enabled` | Verifies boot-time enablement |
| `is-active` | Verifies current runtime state |

Verification is part of the task, not an optional extra.

## Study method

For every objective:

1. Read the theory.
2. Re-type examples instead of copying them blindly.
3. Predict the output before pressing Enter.
4. Run the lab.
5. Break the configuration deliberately in a snapshot.
6. Diagnose and repair it.
7. Complete the exercises.

## Exam command awareness

LPIC objectives include commands that may be deprecated in daily administration, such as `ifconfig`, `netstat`, `route`, and TCP wrappers. Learn what they do for the exam, but prefer modern tools such as `ip`, `ss`, NetworkManager and systemd mechanisms in real systems.
