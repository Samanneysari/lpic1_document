# Topic 106: User Interfaces and Desktops

## 106.1 Install and configure X11

### X11 architecture

In X11 terminology, the X server controls displays and input devices. X clients are applications that request drawing and input services. The client and server can be on different machines, which explains the network-oriented naming.

```text
keyboard/mouse -> X server -> display
                    ^
                    |
              X client programs
```

The `DISPLAY` environment variable identifies a display:

```bash
printf '%s\n' "$DISPLAY"
```

A common local value is `:0`. A value can include host, display and screen components such as `hostname:10.0`.

### Components

| Component | Job |
|---|---|
| X server | Hardware input/output and drawing services |
| Display manager | Graphical login, for example GDM, SDDM or LightDM |
| Window manager | Places and decorates windows |
| Desktop environment | Integrated session such as GNOME, KDE Plasma or Xfce |
| X client | Application connected to the X server |

### Configuration

Modern Xorg usually auto-detects hardware. Static configuration may be stored in:

- `/etc/X11/xorg.conf`
- `/etc/X11/xorg.conf.d/*.conf`

Example keyboard override:

```text
Section "InputClass"
    Identifier "system-keyboard"
    MatchIsKeyboard "on"
    Option "XkbLayout" "us"
EndSection
```

Validate names against local Xorg documentation before deploying. A broken graphical configuration can leave the text console available for recovery.

Useful inspection:

```bash
loginctl list-sessions
loginctl show-session "$XDG_SESSION_ID" -p Type -p Name -p Remote
journalctl -b | grep -Ei 'xorg|wayland|display-manager'
```

`~/.xsession-errors` may exist on some desktop/session combinations but is not universal.

### X access control

`xhost` changes server access rules. Commands such as `xhost +` disable meaningful access control and are unsafe.

```bash
xhost
xauth list
```

`xauth` manages X authentication cookies. SSH X11 forwarding normally handles authentication automatically:

```bash
ssh -X user@host
ssh -Y user@trusted-host
```

`-X` requests untrusted X11 forwarding. `-Y` requests trusted forwarding and should be limited to a trusted server. The SSH server and client must permit forwarding.

### Wayland awareness

Wayland is a newer display protocol and architecture. A Wayland compositor combines display server and window-compositing responsibilities. XWayland allows many X11 applications to run inside a Wayland session. Do not assume an X11-specific tool fully controls a Wayland session.

## 106.2 Graphical desktops and remote access

Major environments include GNOME, KDE Plasma and Xfce. They provide panels, settings, file managers and session components but can use different display managers and window managers.

Remote session technologies named by the objective:

| Technology | Description |
|---|---|
| X11 forwarding | Forwards individual X applications, commonly through SSH |
| XDMCP | Legacy remote graphical login protocol; normally unsuitable on untrusted networks without protection |
| VNC | Shares or creates a remote graphical desktop using the RFB protocol |
| RDP | Remote Desktop Protocol, supported by Linux servers/clients such as xrdp and FreeRDP |
| SPICE | Remote display protocol common in virtualization environments |

Prefer encrypted and authenticated transport. A remotely reachable desktop service increases attack surface and should be firewalled, patched and monitored.

Identify the current desktop/session:

```bash
printf 'desktop=%s session=%s type=%s\n' \
    "${XDG_CURRENT_DESKTOP:-unknown}" \
    "${DESKTOP_SESSION:-unknown}" \
    "${XDG_SESSION_TYPE:-unknown}"
```

## 106.3 Accessibility

Accessibility enables users with visual, hearing, motor or cognitive needs to operate the system. Technologies include:

- high-contrast and large-text themes
- screen readers
- Braille displays
- screen magnifiers
- on-screen keyboards
- sticky, slow, bounce and toggle keys
- mouse keys and alternative pointing methods
- gestures and voice recognition

Accessibility is not merely cosmetic. It must be available at login where required, survive upgrades, work with the selected desktop and be tested with the actual user's workflow.

Common desktop settings are managed through the desktop's accessibility panel. GNOME systems may expose selected settings through `gsettings`, but schema names and availability vary:

```bash
gsettings list-schemas | grep -i accessibility
```

Use graphical settings or supported management policies rather than changing unknown keys blindly.

## Lab 106: Inspect a graphical session

On a VM with a desktop:

1. Identify the display manager service.
2. Determine whether the session uses X11 or Wayland.
3. Display `DISPLAY` and relevant XDG variables.
4. Locate Xorg configuration directories.
5. List X authentication cookies without sharing their values.
6. Enable one accessibility feature, verify it, then restore the previous setting.
7. Compare X11 forwarding, VNC and RDP for one administrative scenario.

## Exercises

1. **106-Q1:** In X11, why is the program controlling the physical display called the server?
2. **106-Q2:** Contrast a display manager, window manager and desktop environment.
3. **106-Q3:** Why is `xhost +` dangerous?
4. **106-Q4:** What is XWayland?
5. **106-Q5:** Name five accessibility technologies included in the objective.

Answers are in [the answer key](../exercises/answers.md#topic-106-answers).

## Official reading

- [X.Org documentation](https://www.x.org/wiki/Documentation/)
- [Wayland documentation](https://wayland.freedesktop.org/docs/html/)
- [OpenSSH manual pages](https://www.openssh.com/manual.html)
