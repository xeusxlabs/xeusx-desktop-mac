# Changelog

All notable changes to the public **Xeusx for macOS** client are recorded here.
Each release lists what changed, the bundled **Orb server agent** version, and the
**SHA-256** of the signed `Xeusx+.dmg` so you can verify your download. The in-app
updater checks the same checksum and a cryptographic signature before installing.

## Xeusx+ 26.3.1+49 — 2026-09-25

### Design improvements

- Refined native Liquid Glass styling for macOS 27, with a more consistent appearance across Settings, Traffic Rules, and Orb.
- Aligned Residential Proxy dropdown colors with Settings for a cohesive look in Light and Dark modes.

SHA-256 (`Xeusx+.dmg`): `6a08b9d10b0dddd1441a3cd4f8b28771983af19b180a0c930b23bdac880b680e`

Orb server agent: `26.3.0+32`

## Xeusx+ 26.3.0+48 — 2026-09-25

> [!IMPORTANT]
> After updating Xeusx+, open **Orb** and select **Update all** before configuring the new providers. Update the iOS client too, then synchronize each authorized user's connections.

### New

- **Decodo residential routing** — Use a certificate-verified HTTPS gateway, country targeting, and named sticky sessions without a configured port inventory. Authorized macOS and iOS users can select Decodo in **Connect → Residential Proxy** after server qualification and synchronization.
- **Bright Data residential routing** — Adds a certificate-verified HTTPS gateway and named sessions with fixed-peer and blocked-fallback controls. Activation requires the account and zone to pass every connection, forwarding, and encrypted-DNS check.
- **Excluded provider ports** — Reserve individual ports or ranges for other applications across an account's gateways. Protection covers allocation, setup checks, routing, rotation, and cleanup; conflicting active assignments must be retired first.

### Fixed

- Recover from an interrupted residential status read by reconnecting once to the same verified server, with clearer SSH and provider-permission diagnostics.
- Preserved valid residential sessions across routine cluster authorization updates while continuing to enforce revocation and allowance changes.

**Residential routing requirements:** Supply your own provider account and enable user access in Orb. The current integration forwards **HTTPS and supported encrypted DNS over IPv4**. Geonode supports DoH and DoT; Decodo and Bright Data support DoH. Unsupported traffic within the selected scope stays blocked, and an unavailable exit never causes that scope to fall back to another route.

**Bright Data qualification:** Some account or zone policies permit test websites but block literal-IP forwarding or DoH. Orb withholds activation until those required checks pass on each assigned server. Provider statistics do not override qualification, and successful qualification does not guarantee access to every website.

**HTTPS website content stays encrypted between your device and the website**, including website login credentials, cookies, and page contents, when the website's certificate is correctly verified. Decodo and Bright Data also encrypt the server-to-provider connection; the provider itself still sees connection metadata.

See [Residential proxy routing](https://github.com/xeusxlabs/xeusx-desktop-mac#residential-proxy-routing) for provider-specific setup, session behavior, accounting, and restrictions.

SHA-256 (`Xeusx+.dmg`): `0b762a22d2092c1441b183d29f5f4814d9dfb402e039432ec5bb88ec21db08f5`

Orb server agent: `26.3.0+32`

## Xeusx+ 26.3.0+39 — 2026-09-24

> [!IMPORTANT]
> After updating Xeusx+, open **Orb** and select **Update all** to install the bundled server improvements.

### New

- **Residential proxy routing** — Configure Geonode residential routing in Orb, including entry gateways, exit countries, and per-user data allowances. Authorized users can choose their residential exit in **Connect → Residential Proxy**.
- **Sticky-session controls** — Keep the same residential session or request a new one, with clearer port availability, usage information, and renewal controls.
- **Connection security details** — Detailed Logs now show observed transport encryption and authentication results, with unavailable information clearly marked.

### Improved

- More consistent native sheets, settings controls, and clickable connection details.
- More reliable fleet updates, removal of unavailable servers, and user access synchronization.

### Fixed

- Restored synchronization of profiles and residential proxy options over TUIC and Hysteria2 connections.
- Fixed DNS and residential session recovery issues that could require a manual VPN reconnect.

**Residential routing requirements:** A separately configured Geonode account and access enabled in Orb are required. This release supports **HTTPS and encrypted DNS over IPv4** through residential exits. UDP, IPv6, and other unsupported traffic within the selected scope remain blocked. Traffic in that scope also stays blocked if the residential exit becomes unavailable.

**HTTPS website content stays encrypted between your device and the website.** With the website's certificate correctly verified, Geonode and network observers cannot read website login credentials, cookies, page contents, or transaction details carried over HTTPS. Encrypted DNS retains its separate TLS protection to the selected resolver.

> [!WARNING]
> **Geonode proxy credentials and connection metadata are exposed.** The current integration uses a plain HTTP CONNECT connection from your VPN server to Geonode, without TLS to the proxy itself. Anyone able to monitor that connection can read the **Geonode proxy username and password** and destination IP/port; destination hostnames may also be visible. Traffic timing and volume remain observable.

SHA-256 (`Xeusx+.dmg`): `7ec0ac44241b80ba360c7f6e2a0e884dc93491b7acd87850ba4dba0b9ab50874`

Orb server agent: `26.3.0+25`

## Xeusx+ 26.2.0+6 — 2026-09-18

### New

- **Choose your DNS resolver** — Select Cloudflare, Quad9, AdGuard DNS, or a custom resolver in Traffic Rules, with clear descriptions of each provider and its filtering options.
- **Encrypted DNS by default** — DNS over HTTPS is now the default, with certificate-verified DNS over TLS and advanced UDP/TCP options available when needed.
- **Encrypted DNS forwarding on managed servers** — Orb-managed servers now use encrypted upstream DNS while preserving existing filtering preferences.

### Improved

- **DNS stays inside the VPN path** — Managed public DNS traffic follows the selected VPN route in both routing modes, including when Traffic Rules are disabled.
- **Faster DNS resolution** — Bounded connection reuse, caching, and request coalescing reduce unnecessary DNS work and improve responsiveness.
- **Automatic filter updates** — Blocking lists now refresh on a dedicated verified schedule without relying on cron.

### Fixed

- Resolved DNS transport concurrency issues that could affect reconnects and clean shutdown.



Open **Orb** in Xeusx+ and select **Update all** to complete server maintenance. Existing profiles and credentials are preserved — **no token reimport is required**.

SHA-256 (`Xeusx+.dmg`): `6464fdca9b8decff48e23df8a373f4d270eaeca1a7459dbfe43c6cda09905a49`

Orb server agent: `26.2.0+5`

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
