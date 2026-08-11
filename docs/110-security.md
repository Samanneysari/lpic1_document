# Topic 110: Security

Security is a continuous process: inventory, reduce exposure, authenticate, authorize, update, monitor, back up and test recovery.

## 110.1 Security administration

### Find special-permission files

```bash
sudo find / -xdev -type f \( -perm -4000 -o -perm -2000 \) -print
```

| Expression | Meaning |
|---|---|
| `/` | Starts at root |
| `-xdev` | Does not descend into other mounted filesystems |
| `-type f` | Regular files only |
| `\(...\)` | Groups the OR conditions for the shell and `find` |
| `-perm -4000` | All setuid bits in this mask are set |
| `-perm -2000` | All setgid bits in this mask are set |

Compare results with the package database and a known baseline. A setuid file is not automatically malicious, but it increases privilege and must be justified, patched and protected from modification.

### Password and account policy

```bash
sudo passwd alice
sudo chage -l alice
sudo chage -m 1 -M 90 -W 14 alice
sudo passwd -S alice
```

`/etc/shadow` stores password hashes and aging fields, not plaintext passwords. Root-readable hashes still require protection because offline guessing is possible. Use long unique passwords, MFA where available and secure recovery procedures.

### Discover listening services

```bash
sudo ss -lntup
sudo lsof -nP -i
sudo nmap -sT -sV 127.0.0.1
```

| Command | Viewpoint |
|---|---|
| `ss` | Kernel socket table on the host |
| `lsof -i` | Processes with Internet sockets |
| `nmap` | Network scan from the scanning host's viewpoint |

Only scan systems and networks you are authorized to test. A loopback scan does not prove external reachability because firewall and bind addresses matter.

### Limits

The shell can show and set resource limits:

```bash
ulimit -a
ulimit -n
```

PAM limits are commonly configured in `/etc/security/limits.conf` and `/etc/security/limits.d/*.conf`:

```text
@developers soft nofile 4096
@developers hard nofile 8192
```

systemd services use unit settings such as `LimitNOFILE=`. PAM limits do not automatically control every system service.

### Login auditing

```bash
who
w
last -a | head
lastlog | head
```

`who` shows current sessions, `w` adds activity/load, `last` reads login history, and `lastlog` reports each account's most recent login when supported. Logs can be incomplete after rotation, deletion or tampering; forward critical audit data centrally.

### sudo and su

Use `visudo` to edit sudoers safely:

```bash
sudo visudo
sudo -l
sudo -u www-data id
su - alice
```

Example narrow rule:

```sudoers
%webops ALL=(root) /usr/bin/systemctl reload nginx.service
```

Avoid broad wildcard commands and `NOPASSWD` without risk analysis. Many permitted programs can invoke shells or edit arbitrary files. Put local rules in `/etc/sudoers.d/` with appropriate ownership/mode and validate with `visudo -cf`.

`su - alice` starts a login-like environment for Alice; `su alice` preserves more of the current environment. Authentication and logging differ from sudo.

### Find users of resources

```bash
sudo fuser -v /srv/data
sudo lsof /srv/data/file
sudo fuser -n tcp 22
```

These help identify processes preventing unmounts or using a port.

## 110.2 Host security

### Reduce attack surface

Inventory units and sockets:

```bash
systemctl --type=service --state=running
systemctl list-sockets --all
sudo ss -lntup
```

Disable an unnecessary service only after confirming dependencies and access impact:

```bash
sudo systemctl disable --now example.service
systemctl is-enabled example.service
systemctl is-active example.service
```

Masking is stronger and prevents normal activation:

```bash
sudo systemctl mask example.service
```

Use masking only when intentional; it can break dependent software.

### Login controls

- `/etc/nologin` can prevent non-root logins through cooperating login programs.
- `/usr/sbin/nologin` or `/bin/false` is commonly assigned to service accounts that do not need shells.
- A locked password does not disable public-key, token or service-specific authentication.
- Remove or restrict obsolete services such as Telnet, FTP and r-services when secure alternatives exist.

### inetd/xinetd and systemd sockets

Legacy super-servers activate services on connection. Configuration may appear in `/etc/xinetd.conf` and `/etc/xinetd.d/`. systemd socket activation uses `.socket` units:

```bash
systemctl list-sockets --all
systemctl cat example.socket
```

Disabling a service unit may not prevent its socket from activating it; inspect both.

On older SysVinit systems, enabled services may be represented by scripts under
`/etc/init.d/`, runlevel links and policy in `/etc/inittab`. Do not assume that
`systemctl` is the only activation path when auditing a legacy host.

### TCP wrappers awareness

`/etc/hosts.allow` and `/etc/hosts.deny` controlled access for applications linked with TCP-wrapper support. Many modern services no longer support this mechanism. Do not assume these files protect a service; verify application support and use its own access controls plus firewall policy.

### Patch and verify

Use trusted signed repositories, apply supported security updates, remove abandoned packages and reboot when kernel or foundational updates require it. Test recovery and maintain backups outside the host.

## 110.3 Secure data and communications with encryption

### SSH trust model

An SSH server has host keys identifying the server. A user can authenticate with a private key while the corresponding public key is stored in `~/.ssh/authorized_keys` on the server.

On first connection, verify the host-key fingerprint through a trusted channel before accepting it. `known_hosts` protects against silent server substitution on later connections.

Per-user trust is normally stored in `~/.ssh/known_hosts`; a system-wide file
may be `/etc/ssh/ssh_known_hosts`. Server private/public host-key pairs are
normally under `/etc/ssh/`, for example `ssh_host_ed25519_key` and
`ssh_host_ed25519_key.pub`. Protect private host keys and regenerate duplicated
template keys before exposing a clone.

### Create and use a key

```bash
ssh-keygen -t ed25519 -a 100 -C 'alice-admin'
ssh-keygen -lf "$HOME/.ssh/id_ed25519.pub"
eval "$(ssh-agent -s)"
ssh-add "$HOME/.ssh/id_ed25519"
ssh-copy-id alice@server.example.net
ssh alice@server.example.net
```

| Part | Meaning |
|---|---|
| `-t ed25519` | Selects Ed25519 key type |
| `-a 100` | Increases KDF rounds used to protect the private-key file |
| `-C` | Adds a comment for identification |
| `ssh-agent` | Holds decrypted private-key material for the session |
| `ssh-add` | Adds the key after passphrase entry |

Use a passphrase for human-operated private keys and an agent to avoid repeated entry. Automation keys should be narrowly authorized and protected with platform-appropriate secret controls.

RSA and ECDSA are also recognized by the objective. DSA is obsolete and should not be deployed even though historical filenames may appear in an exam list.

### Client configuration

`~/.ssh/config`:

```sshconfig
Host lab-web
    HostName server.example.net
    User alice
    IdentityFile ~/.ssh/id_ed25519
    IdentitiesOnly yes
```

Protect it:

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/config ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub
```

### Validate server configuration

OpenSSH server configuration is commonly `/etc/ssh/sshd_config` plus included drop-ins.

```bash
sudo sshd -t
sudo sshd -T | less
sudo systemctl reload sshd
```

Some Debian-family services are named `ssh` instead of `sshd`. Always validate before reload and keep an existing remote session open during changes.

### SSH tunnels

Local forwarding:

```bash
ssh -N -L 127.0.0.1:15432:db.internal:5432 alice@gateway.example.net
```

Connections to local port 15432 travel through SSH and are opened from the gateway toward `db.internal:5432`.

Remote forwarding:

```bash
ssh -N -R 127.0.0.1:18080:localhost:8080 alice@gateway.example.net
```

Dynamic SOCKS forwarding:

```bash
ssh -N -D 127.0.0.1:1080 alice@gateway.example.net
```

| Option | Meaning |
|---|---|
| `-N` | Do not run a remote command |
| `-L` | Local listening forward |
| `-R` | Remote listening forward |
| `-D` | Dynamic SOCKS proxy |

Bind forwarding listeners to loopback unless remote access is deliberately required and protected. Server policy can restrict forwarding.

X11 forwarding uses `ssh -X` or trusted `ssh -Y` as discussed in Topic 106.

### GnuPG concepts

GnuPG uses public-key cryptography for encryption and signatures. A public key can be shared. A private key must remain secret. A revocation certificate provides a way to mark a key unusable if compromised or retired.

```bash
gpg --full-generate-key
gpg --list-keys
gpg --list-secret-keys
gpg --output public-key.asc --armor --export user@example.net
gpg --output revoke.asc --gen-revoke user@example.net
```

Store the revocation certificate securely and separately.

Encrypt and decrypt:

```bash
gpg --encrypt --recipient user@example.net --output secret.txt.gpg secret.txt
gpg --decrypt --output secret.restored.txt secret.txt.gpg
```

Sign and verify:

```bash
gpg --armor --detach-sign package.tar.gz
gpg --verify package.tar.gz.asc package.tar.gz
```

Verification proves that the signature matches a key. You must separately establish that the key belongs to the intended person or project.

GnuPG state is normally under `~/.gnupg`; `gpg-agent` can cache private-key operations. Protect the directory and backups.

## Lab 110: Harden and verify a lab SSH service

1. Record listening sockets and the SSH bind address.
2. Capture the server host-key fingerprint through the VM console.
3. Create a passphrase-protected client key.
4. Add it to `ssh-agent` and install only the public key.
5. Verify the server fingerprint on connection.
6. Inspect effective sshd configuration with `sshd -T`.
7. Create a loopback-only local tunnel and test it.
8. Review authentication logs.
9. Remove the lab authorization and stop the agent.

Do not disable password authentication until key access and console recovery have been proven.

## Exercises

1. **110-Q1:** Write a `find` expression for setuid and setgid regular files on one filesystem.
2. **110-Q2:** Why does a loopback Nmap scan not prove external exposure?
3. **110-Q3:** Contrast `sudo` and `su -`.
4. **110-Q4:** Why may disabling a service unit be insufficient when a socket unit exists?
5. **110-Q5:** What security property does `known_hosts` provide?
6. **110-Q6:** Explain local, remote and dynamic SSH forwarding.
7. **110-Q7:** Contrast GPG encryption and signing.
8. **110-Q8:** Why is successful signature verification insufficient without key-owner verification?

Answers are in [the answer key](../exercises/answers.md#topic-110-answers).

## Official reading

- [OpenSSH manual pages](https://www.openssh.com/manual.html)
- [GnuPG manual](https://www.gnupg.org/documentation/manuals/gnupg/)
- [systemd security-related manuals](https://www.freedesktop.org/software/systemd/man/latest/)
