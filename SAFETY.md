# Command Safety Checklist

Linux administration commands can destroy data or interrupt access. This checklist applies to every lab in the repository.

## Before changing disks or filesystems

```bash
lsblk -f
findmnt
sudo blkid
```

- Confirm the device name, size and filesystem.
- Confirm it is a disposable lab disk.
- Unmount a filesystem before destructive formatting or offline repair.
- Never copy `/dev/sda`, `/dev/vda` or `/dev/nvme0n1` from an example without checking your own system.
- Snapshot the VM and back up important data.

Commands such as `fdisk`, `parted`, `mkfs`, `mkswap`, `wipefs`, `dd`, `fsck -y`, `xfs_repair`, and `lvremove` require special care.

## Before editing boot or mount configuration

Back up the file and validate it:

```bash
sudo cp --archive /etc/fstab /etc/fstab.before-lab
sudo findmnt --verify --verbose
```

For GRUB, generate configuration only with the distribution's supported command and inspect errors before rebooting.

## Before changing networking or SSH remotely

- Keep the current session open.
- Schedule a rollback when practical.
- Add the new configuration before removing the old one.
- Validate SSH configuration with `sshd -t` before reload.
- Verify firewall rules do not block your management address.

## Secrets

- Do not place passwords in shell history, process arguments, Git, cron entries or screenshots.
- Use secret files with restrictive permissions, an agent, a keyring or a secrets manager.
- A password lock does not necessarily disable SSH public-key access.
- Never share a private SSH or GPG key.

## Privilege

Use an unprivileged account for normal work and `sudo` only for the command that needs privilege. Read a command before executing it; `sudo` does not make an unsafe command safe.

## Recovery rule

If output differs from the guide, stop and investigate. Do not keep adding commands in the hope that one will work.
