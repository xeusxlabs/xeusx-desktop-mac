# Changelog

All notable changes to the public **Xeusx for macOS** client are recorded here.
Each release lists what changed, the bundled **Orb server agent** version, and the
**SHA-256** of the signed `Xeusx+.dmg` so you can verify your download. The in-app
updater checks the same checksum and a cryptographic signature before installing.

## Xeusx+ 26.1.2+1 — 2026-07-09

- Added Orb-managed mux controls for constrained hosts and low-concurrency networks, improving Shadowsocks reliability and throughput under provider limits.
- Faster protocol health detection and failover with low-latency pre-probing and traffic-flow recovery, so automatic switching moves from blocked to reachable protocols according to Settings preferences.
- Improved Orb server setup and upgrade reliability across Ubuntu 22, 24, and 26.

SHA-256 (`Xeusx+.dmg`): `63bddf45f582a357379e494629e5eb87877abb597c6dd3bc041482a877fb6cc3`

Orb server agent: `26.1.2+3`

## Xeusx+ 26.1.1+2 — 2026-07-07

First public availability of **Xeusx+ for macOS**: the **Connect** client and the built-in **Orb** server manager.

- Native macOS **menu-bar** VPN client for private, self-hosted VPN infrastructure.
- Built-in **Orb** server manager for provisioning and operating self-hosted Xeusx VPN servers over SSH.
- **Encrypted token import** with local unlock and verification on the user's Mac.
- **No account or telemetry requirement** for the app client.
- **Multiple connection methods** served through one embedded engine and selectable automatically where supported by the imported server profile.
- **Automatic failover** across available connection methods and servers, backed by health monitoring and reconnect behavior.
- **Always-on kill switch** designed to fail closed across reconnects, failover, rule changes, and updates.
- **Touch ID / Mac password privacy lock** and device-local Keychain storage for connection material.
- **Server identity verification** designed to reject swapped or impersonated VPN servers.
- **Smart routing** with full-VPN or split routing and presets for ad, tracker, and known-malicious-site blocking where configured.
- **Local devices stay reachable** by default for common LAN use cases such as printers, AirPlay, NAS, and local network resources.
- **Signed and checksum-verified updater** with rollback-protection design.
- **Guided server provisioning with Orb** — provision a complete self-hosted Xeusx VPN on a supported Ubuntu Linux server you control or are authorized to administer, then operate it from the app.
- **Server administration over SSH** — a device-minted, scoped admin key with pinned host identity; setup credentials are used for enrollment and not retained afterward where supported, management is limited to defined Xeusx operations, and there is no developer admin backend.
- **User and fleet management** — add or remove users, mint shareable encrypted tokens and QR codes, manage multiple servers, and push updates to one or all of them.
- **Per-server controls** — toggle available connection methods, ad and tracker blocking, multiplexing, automatic server recovery, and scheduled operating-system and component updates.

SHA-256 (`Xeusx+.dmg`): `81734f0a3f9baa2187db34f4fc46925918a71b33b3eb879b09c087bce90125b6`

Orb server agent: `26.1.1+15`
