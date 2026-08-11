# Topic 109: Networking Fundamentals

## 109.1 Internet protocol fundamentals

### Layers and encapsulation

For LPIC-1, focus on practical TCP/IP behavior:

| Layer idea | Examples | Unit commonly discussed |
|---|---|---|
| Application | DNS, HTTP, SSH, SMTP | Message/data |
| Transport | TCP, UDP | Segment/datagram |
| Internet | IPv4, IPv6, ICMP | Packet |
| Link | Ethernet, Wi-Fi | Frame |

An application writes data to a socket. The transport layer identifies endpoints with ports. IP provides addressing and routing. The link layer delivers the next local hop. At the receiver, headers are processed in reverse.

### TCP, UDP and ICMP

| Protocol | Main behavior | Typical use |
|---|---|---|
| TCP | Connection-oriented byte stream with sequencing, acknowledgments, retransmission and flow/congestion control | SSH, HTTP(S), SMTP |
| UDP | Connectionless datagrams without built-in delivery or ordering guarantees | DNS queries, NTP, real-time traffic |
| ICMP | Network control and diagnostic messages | Errors, reachability, IPv6 neighbor discovery |

TCP reliability does not mean the application transaction succeeded, and UDP does not mean packets are always lost. Applications select behavior appropriate to their protocol.

### IPv4 addressing and CIDR

An IPv4 address has 32 bits. A prefix length says how many leading bits identify the network.

Example: `192.0.2.130/26`

- `/26` mask: `255.255.255.192`
- block size in final octet: 64
- network: `192.0.2.128`
- traditional broadcast: `192.0.2.191`
- typical usable host range: `192.0.2.129`–`192.0.2.190`

Compute with an installed tool rather than guessing:

```bash
ipcalc 192.0.2.130/26
```

Private IPv4 ranges:

- `10.0.0.0/8`
- `172.16.0.0/12`
- `192.168.0.0/16`

Loopback is `127.0.0.0/8`. Link-local automatic addressing is `169.254.0.0/16`. Public routing policy is separate from the mathematical validity of an address.

### IPv6 basics

IPv6 addresses have 128 bits and use hexadecimal groups. Leading zeros in a group can be omitted; one longest run of zero groups can be compressed with `::` once.

| Prefix/type | Purpose |
|---|---|
| `::1/128` | Loopback |
| `fe80::/10` | Link-local; interface scope is often required |
| `fc00::/7` | Unique local range |
| `2000::/3` | Current global unicast allocation space |
| `ff00::/8` | Multicast |

IPv6 has no broadcast; multicast and Neighbor Discovery provide related functions. A normal LAN prefix is commonly `/64`. IPv6 uses ICMPv6 for essential functions, so indiscriminately blocking ICMPv6 breaks networking.

### Traffic and routes

A host determines whether the destination is on-link using its address and prefix. For an off-link destination it selects a route, commonly the default route, and sends the frame to the next-hop router. Routers repeat a route lookup until the packet reaches its destination or fails.

### Common ports

The exam expects common TCP and UDP associations. `/etc/services` is a local name-to-port database, not proof that a service is running.

| Port | Service | Common transport |
|---:|---|---|
| 20/21 | FTP data/control | TCP |
| 22 | SSH | TCP |
| 23 | Telnet | TCP |
| 25 | SMTP | TCP |
| 53 | DNS | UDP and TCP |
| 80 | HTTP | TCP |
| 110 | POP3 | TCP |
| 123 | NTP | UDP |
| 139 | NetBIOS session | TCP |
| 143 | IMAP | TCP |
| 161/162 | SNMP queries/traps | UDP commonly |
| 389 | LDAP | TCP/UDP possibilities; TCP common |
| 443 | HTTPS | TCP; modern HTTP/3 uses QUIC over UDP |
| 465 | Message submission over implicit TLS | TCP |
| 514 | Syslog or legacy remote shell depending transport/context | UDP commonly for syslog, TCP for shell |
| 636 | LDAPS | TCP |
| 993 | IMAPS | TCP |
| 995 | POP3S | TCP |

Memorize service, port and expected transport, but verify implementation documentation.

## 109.2 Persistent network configuration

### Host identity and resolver files

| File | Purpose |
|---|---|
| `/etc/hostname` | Persistent local hostname on many systems |
| `/etc/hosts` | Static local name/address mappings |
| `/etc/nsswitch.conf` | Lookup-source order for databases such as `hosts` and `passwd` |
| `/etc/resolv.conf` | Resolver configuration or link to a resolver manager's generated file |

Inspect and set the hostname with the supported systemd tool where available:

```bash
hostname
hostnamectl status
sudo hostnamectl set-hostname lab-client.example.net
```

`hostname` prints the current kernel hostname. `hostnamectl status` includes
persistent and transient hostname information. `set-hostname` changes host
identity and can affect prompts, logs and services; use an approved name and
verify `/etc/hosts` or DNS separately.

Example hosts lookup policy:

```text
hosts: files dns
```

This normally checks `/etc/hosts` before DNS. Other sources such as `resolve`, `mdns`, `myhostname` or LDAP may appear.

### NetworkManager with nmcli

List devices and profiles:

```bash
nmcli device status
nmcli connection show
nmcli --fields GENERAL,IP4,IP6 device show
```

Create a static IPv4 profile for a lab interface named `ens192`:

```bash
sudo nmcli connection add type ethernet ifname ens192 con-name lab-static \
    ipv4.method manual ipv4.addresses 192.0.2.10/24 \
    ipv4.gateway 192.0.2.1 ipv4.dns '192.0.2.53 192.0.2.54' \
    ipv6.method disabled
```

Activate and verify:

```bash
sudo nmcli connection up lab-static
ip address show dev ens192
ip route
nmcli device show ens192
```

Every setting line explained:

| Setting | Meaning |
|---|---|
| `type ethernet` | Ethernet profile |
| `ifname ens192` | Binds profile to this interface name |
| `con-name lab-static` | Human-readable profile name |
| `ipv4.method manual` | Static IPv4 configuration |
| `ipv4.addresses` | Address and prefix |
| `ipv4.gateway` | Default gateway candidate |
| `ipv4.dns` | Resolver addresses |
| `ipv6.method disabled` | Disables IPv6 for this lab profile; do not do this as a generic fix |

Changing networking remotely can disconnect you. Use VM console, keep the old profile and prepare rollback.

DHCP profile example:

```bash
sudo nmcli connection modify lab-static ipv4.method auto \
    ipv4.addresses '' ipv4.gateway '' ipv4.dns ''
```

### Wi-Fi awareness

```bash
nmcli radio wifi
nmcli device wifi list
nmcli device wifi connect 'LAB-SSID' --ask
```

`--ask` avoids placing the Wi-Fi password directly in shell history. Profile secret storage must still be protected.

### systemd-networkd awareness

systemd-networkd uses files such as `/etc/systemd/network/*.network`. Example:

```ini
[Match]
Name=enp1s0

[Network]
Address=192.0.2.20/24
Gateway=192.0.2.1
DNS=192.0.2.53
```

Do not let multiple network managers control the same interface. Legacy `ifup` and `ifdown` are exam terms and operate distribution-specific interface configuration.

## 109.3 Basic network troubleshooting

Use a layered method:

1. Physical/link: interface present, carrier, errors?
2. Address: correct address and prefix?
3. Route: on-link and default routes correct?
4. Local socket/firewall: service listening and allowed?
5. Reachability: gateway and remote IP?
6. Name resolution: correct lookup result?
7. Application/TLS: protocol-level success?

### Modern iproute2 commands

```bash
ip -br link
ip -br address
ip route show
ip -6 route show
ip route get 198.51.100.10
ip neigh show
```

`ip route get` asks the kernel which route, source and interface it would use without sending an application request.

Temporary lab address and route:

```bash
sudo ip address add 192.0.2.30/24 dev ens192
sudo ip link set ens192 up
sudo ip route add default via 192.0.2.1 dev ens192
```

These changes are not normally persistent and can disrupt connectivity. Do not add a second default blindly.

### Sockets

```bash
ss -lntup
ss -tn state established
```

| Option | Meaning |
|---|---|
| `-l` | Listening |
| `-n` | Numeric addresses/ports |
| `-t` | TCP |
| `-u` | UDP |
| `-p` | Process information when permitted |

### Reachability and path

```bash
ping -c 4 192.0.2.1
ping -6 -c 4 2001:db8::1
traceroute 198.51.100.10
tracepath 198.51.100.10
```

A failed ping does not prove the host is down; ICMP echo may be filtered. Test the actual application port too.

```bash
nc -vz 198.51.100.20 22
printf 'hello\n' | nc -N 192.0.2.20 9000
```

Netcat options vary between implementations. Read `nc(1)` locally.

### Legacy net-tools

Recognize equivalents:

| Legacy | Modern preference |
|---|---|
| `ifconfig -a` | `ip address` and `ip link` |
| `route -n` | `ip route` |
| `netstat -lntup` | `ss -lntup` |

The names `ping6`, `traceroute6`, and `tracepath6` may be separate commands or
compatibility links on older systems. Modern implementations commonly accept
`ping -6`, `traceroute -6`, and `tracepath -6`; learn both forms for exam
recognition and check the local manual.

Learn legacy output for the exam, but use iproute2 for current administration.

## 109.4 Client-side DNS

### What happens after a user enters a name

For an application resolving `www.example.com`:

1. The application calls the system resolver.
2. Name Service Switch policy in `/etc/nsswitch.conf` decides lookup sources and order.
3. A static `/etc/hosts` entry may answer first.
4. A local stub such as systemd-resolved may consult cache and per-link policy.
5. A configured recursive resolver receives the query.
6. If not cached, the recursive resolver follows DNS delegation from root to TLD to authoritative servers.
7. The answer and TTL return to the client and may be cached.
8. The application selects an address, opens a transport connection and continues its protocol, for example a TLS handshake and HTTP request.

DNS returns data; it does not itself establish the TCP connection or prove the destination is trustworthy.

### Query tools

```bash
getent ahosts www.example.com
host www.example.com
dig www.example.com A
dig www.example.com AAAA
dig @192.0.2.53 www.example.com A
dig +trace www.example.com
```

| Tool | Best use |
|---|---|
| `getent` | Tests the system's configured NSS lookup path |
| `host` | Simple DNS queries |
| `dig` | Detailed DNS query and response fields |
| `dig @server` | Queries one chosen DNS server directly |
| `dig +trace` | Performs an iterative delegation trace from root; behavior differs from the normal stub path |

Important DNS response ideas:

- `NOERROR` can contain an answer or an empty answer.
- `NXDOMAIN` means the queried name does not exist according to DNS.
- `SERVFAIL` means the resolver could not complete the answer, perhaps because of upstream or DNSSEC failure.
- An answer from `dig @server` but failure from `getent` suggests local NSS/stub configuration rather than authoritative data alone.

### systemd-resolved awareness

```bash
resolvectl status
resolvectl query www.example.com
resolvectl statistics
sudo resolvectl flush-caches
```

`/etc/resolv.conf` may be a symbolic link managed by systemd-resolved, NetworkManager or another service. Do not overwrite generated files without identifying their owner.

### Troubleshooting sequence

```bash
getent hosts target.example.com
grep '^hosts:' /etc/nsswitch.conf
cat /etc/resolv.conf
resolvectl status 2>/dev/null
dig target.example.com
dig @configured-resolver target.example.com
```

Also verify UDP/TCP port 53 reachability where policy permits and compare expected authoritative data.

## Lab 109: Diagnose name-to-service connectivity

1. Record interfaces, addresses and routes.
2. Predict the route to a test address with `ip route get`.
3. Test the gateway and one remote IP.
4. Inspect listening sockets.
5. Resolve a domain through `getent`, `host` and `dig`.
6. Compare the results and explain why they can differ.
7. Query a specific resolver.
8. Test one real service port with `nc`.
9. Document the failure layer for three instructor-provided faults: wrong prefix, missing default route and broken resolver.

## Exercises

1. **109-Q1:** Contrast TCP, UDP and ICMP.
2. **109-Q2:** Calculate network and broadcast for `198.51.100.77/27`.
3. **109-Q3:** Why must ICMPv6 not be blocked indiscriminately?
4. **109-Q4:** Which files control hostname, static host entries, lookup order and resolver configuration?
5. **109-Q5:** Write commands to show addresses, routes, selected route and listening TCP sockets.
6. **109-Q6:** Why can ping fail while HTTPS still works?
7. **109-Q7:** Contrast `getent hosts` with `dig`.
8. **109-Q8:** Explain the resolution path from application to authoritative DNS.

Answers are in [the answer key](../exercises/answers.md#topic-109-answers).

## Official reading

- [iproute2 documentation](https://wiki.linuxfoundation.org/networking/iproute2)
- [NetworkManager documentation](https://networkmanager.dev/docs/)
- Local manuals: `ip(8)`, `ss(8)`, `nsswitch.conf(5)`, `resolv.conf(5)`, `dig(1)`
