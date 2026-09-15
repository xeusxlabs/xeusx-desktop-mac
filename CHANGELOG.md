# Changelog

All notable changes to the public **Xeusx for macOS** client are recorded here.
Each release lists what changed, the bundled **Orb server agent** version, and the
**SHA-256** of the signed `Xeusx+.dmg` so you can verify your download. The in-app
updater checks the same checksum and a cryptographic signature before installing.

## Xeusx+ 26.1.4+145 — 2026-09-15

- Improved TUIC provisioning and surfaced firewall setup failures.
- Improved XHTTP H2 compatibility for CDN-fronted servers.
- Preserved native macOS styling and strengthened release-build validation.

SHA-256 (`Xeusx+.dmg`): `deee8fa036d27a5109de1c37b9e6dc053fafb8ac438df329444a8be61c704636`

Orb server agent: `26.1.4+142`

## Xeusx+ 26.1.4+143 — 2026-09-14

- Fixed connection failures on IPv6-enabled networks when large country-based Traffic Rules are configured.
- Improved connection, protocol switching, and disconnect responsiveness by batching route setup and cleanup.
- The app now waits for route setup to finish before reporting a connection, preventing unnecessary automatic failover during startup.

SHA-256 (`Xeusx+.dmg`): `0e27127cbdfe63b08d72461fc72e7900cd8b82054a5d664cf82f90639b0b41c7`

Orb server agent: `26.1.4+140`

## Xeusx+ 26.1.3+142 — 2026-09-02

**Breaking change:** Legacy users continue to work after the update but cannot be migrated automatically to the new decentralized cluster-wide server and user management model. To migrate, create a new server cluster, recreate each legacy user as an access profile, and share a new Xeusx token.

**New:**

- **One access profile. One encrypted token.** Create an access profile for each authorized user, then grant or revoke access across the servers in your cluster. Each profile uses a single encrypted Xeusx token, while approved connections stay synchronized across the user’s enrolled devices.
- **Fleet-wide or server-specific access.** Grant an access profile access to every current and future Orb-managed server in the cluster, or restrict it to an explicit server list. With server-specific access, newly added servers remain unavailable until you explicitly grant access.
- **Device-level control.** View and revoke devices enrolled under an access profile, and set a maximum device limit. Each enrolled device receives its own revocable connection identity, helping limit exposure if a token is copied or compromised.
- **Traffic Rules Sharing.** Export Traffic Rules to `.xeusx` files and open them on any supported Xeusx device to preview the rules before importing. If the file also contains a Xeusx token, the connection and its Traffic Rules are imported together in one step.

SHA-256 (`Xeusx+.dmg`): `045eb793abfc426e8d70f3114264a9c94a25c239ee8b202da34c3f9e6378a442`

Orb server agent: `26.1.4+140`

## Xeusx+ 26.1.2+3 — 2026-07-14

- **[Beta] Orb Optical Token sharing:** Display a short-lived visual token that another Xeusx device can scan directly. For device-to-device setup, connection data stays offline and never passes through email, cloud storage, messaging services, or a Xeusx-operated relay.
- **Bulk import:** Paste one or more Xeusx connection tokens from the clipboard, or import multiple `.xeusx` files in a single operation. This streamlines multi-server setup and reduces repetitive input and configuration errors.
- **Help and Diagnostics:** A new Settings section brings support, the changelog, diagnostic controls, and local logs together in one place.
- **Appearance controls:** Choose System, Light, or Dark mode. System follows macOS automatically, while Light and Dark keep the interface fixed to your preferred appearance.

SHA-256 (`Xeusx+.dmg`): `4f1ca26afc3c77487c9351132f7c1e744625562f194157efcd220bb78f4bd17a`

Orb server agent: `26.1.2+3`

## Xeusx+ 26.1.2+2 — 2026-07-09

- Improved the stability of client app updates.

SHA-256 (`Xeusx+.dmg`): `8e6ca49163c912bbc20b4912b5a055c8116588fead43091bc0839b5a1d011b20`

Orb server agent: `26.1.2+3`

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
