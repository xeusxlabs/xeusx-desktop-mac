# Xeusx Privacy Policy

**Last updated: September 24, 2026**

This Privacy Policy explains how **Xeusx for macOS**, including the public **Xeusx+** build (**"Xeusx"** or the **"app"**), handles information. Xeusx is a self-hosted VPN client and server manager that stores local connection and server-administration material under your control. Optional residential-proxy setup also delivers provider credentials to the servers you select, as described below.

For this Policy, an **"Authorized Server"** is a compatible server that you own, administer, or are expressly authorized to use. The term describes your authority to use the server; it does not mean Xeusx Labs has reviewed, approved, or certified it. Xeusx does not provide a server directory, access marketplace, brokerage service, or developer-operated VPN network.

## At a glance

- **No accounts.** Xeusx has no sign-up, login, user profile, or developer account system.
- **No developer VPN backend.** Xeusx connects your Mac to an Authorized Server, not to a developer-operated VPN service.
- **No developer traffic visibility.** The developer does not operate a relay or exit server for your VPN traffic.
- **No tracking or telemetry.** The app does not include third-party advertising, analytics, behavioral tracking, usage telemetry, crash reporting to the developer, or a license server that reports app use to the developer.
- **Local secrets.** Connection material is stored locally in macOS Keychain. The import passphrase is used transiently in memory and is not stored by the app.
- **Orb server management stays local too.** If you use Orb to run your own servers, Xeusx creates or uses server-management material on your Mac, keeps it in your local Keychain vault where applicable, and connects directly to your servers. The developer runs no admin backend and receives none of this.
- **Optional residential providers are independent.** If your operator enables residential routing, the configured provider receives the authentication and connection information needed to carry that traffic. Xeusx Labs does not supply the provider account or receive that information.
- **Independent infrastructure may process ordinary request data.** GitHub may receive your IP address when you download the app or when the app checks for updates, and your hosting provider may process server-related data. If an Authorized Server is administered by another party, that party may process VPN connection and synchronization-request metadata under its own policies.

## 1. Information the developer does not collect through the app

The app does not collect, transmit to the developer, or sell personal information. The app does not include developer-operated accounts, advertising identifiers, analytics SDKs, behavioral profiling, usage telemetry, crash reporting to the developer, install counting, connection counting, server counting, or a developer-operated license server.

The app does not send browsing history, DNS queries, VPN traffic, imported tokens, passphrases, server lists, server credentials, SSH keys, connection logs, or app-usage statistics to the developer.

## 2. Information stored on your device

When you import one encrypted Xeusx token, Xeusx decodes it locally and stores your connection material in a device-local macOS Keychain vault. Depending on your server configuration, this may include server addresses, access-profile entries, protocol profiles, server-issued artifacts, synchronization credentials, server labels, routing preferences, and related connection settings.

An access profile represented by a Xeusx token can include all current and future servers in a fleet, or only selected servers. With selected access, a new server remains unavailable until it is added to that profile. An access profile is connection configuration within the selected server environment; it is not a Xeusx Labs account, subscription, or managed service.

Xeusx also stores ordinary app preferences locally, such as selected options and UI settings.

If you use **Orb**, Xeusx also stores server-management material locally on your Mac. This may include the list of servers you manage, server labels, SSH host identity information, setup state, update settings, access-management metadata, and a scoped administrative SSH key used to manage Xeusx operations on your servers. The key is generated or enrolled on your Mac and is used to connect from your Mac to servers you manage; it is not sent to the developer.

When you configure a residential provider in Orb, its credentials are saved in the protected local vault and delivered to the selected managed servers for provider authentication. Those provider credentials are not included in users' exported connection profiles. Provider settings, sticky-port assignments, per-user allowances and usage state are also retained as needed to operate the feature.

Any setup password, SSH credential, or server alias you provide during first-time setup is used for the setup flow and key enrollment. Xeusx is designed not to retain setup passwords after enrollment where the supported setup flow allows password removal or replacement with a scoped key. You can rotate or revoke management keys and remove managed servers when supported by the app and your server configuration.

Detailed logging, if available and enabled by you, is local to your Mac. Logs are not sent to the developer by the app. Logs are intended not to include your import passphrase, full connection strings, or private keys, but you should review any log before sharing it with anyone.

Your import passphrase is used only transiently in memory to decode a pasted token. The app is designed not to write the passphrase to disk, Keychain, logs, or developer systems.

## 3. Network connections the app may make

Apart from carrying your VPN traffic, the app may make the following outbound connections:

1. **VPN tunnel.** When you connect, Xeusx routes traffic to the Authorized Server you selected. That server is owned or administered by you, or is one you are expressly authorized to use; it is not provided by the developer.
2. **Official updates.** Xeusx may fetch a signed update manifest and release artifact from GitHub or another official distribution location. These requests do not include your imported VPN secrets, but ordinary web request data such as IP address, user agent, time, and requested file may be visible to the third-party host.
3. **Connection synchronization.** Xeusx may update your connection material through an active VPN tunnel using server-issued credentials. These requests go to the connected Authorized Server, not to the developer.
4. **Optional routing rule-set updates.** If you enable downloadable rule sets, blocklists, or geo data, Xeusx may fetch those files from the sources you configure or approve, on the schedule you choose.
5. **Orb server administration.** If you manage servers with Orb, the app opens SSH connections from your Mac directly to those servers. These connections go to servers you control or are authorized to manage, not to the developer, and are intended for defined Xeusx management operations rather than general-purpose server administration.
6. **Hosting-provider or operating-system traffic.** Your server, hosting provider, operating system, package repositories, and security-update sources may create their own logs or network requests outside the app's control.
7. **Optional residential proxies.** Orb uses the configured provider's HTTPS management API to manage provider settings, sessions and usage. Selected residential traffic travels through your Authorized Server to that provider. These requests use the operator-supplied provider account, not a Xeusx Labs account.

Xeusx does not phone home to a developer-operated app-usage backend.

### 3.1 Connection synchronization

Xeusx can check for updated connection and access information through the active VPN tunnel using certificate-pinned HTTPS. Only the connected server is contacted; the app does not use a public synchronization endpoint or contact each server separately.

Synchronization is event-driven. A check may run:

- when the VPN tunnel connects;
- after the privacy vault is unlocked or you return to Xeusx after it was inactive, if a suitable tunnel is available;
- after the Mac wakes, if the tunnel remained available or reconnects;
- after the Mac's underlying network changes, if a suitable tunnel is available;
- after you confirm a new or updated Xeusx token;
- once after certain connection failures if an existing tunnel path remains available; or
- when you choose **Sync**.

There is no periodic server-synchronization timer or continuous background polling loop. An unlocked, connected session that remains otherwise idle does not self-refresh until a later event or manual **Sync**. Checks do not run while the privacy vault is locked. If no suitable tunnel is available, an automatic check is deferred until a later successful connection.

The connected Authorized Server receives the server-issued identifiers and credentials needed to authenticate synchronization. If that server is administered by another party, that party may process the request time and ordinary HTTPS and VPN-connection metadata. Xeusx Labs does not receive this information.

This synchronization is separate from official app-update checks, optional routing-data downloads on a schedule you choose, and Orb server-maintenance schedules.

### 3.2 Residential proxy routing

Residential routing is optional and requires an independently supplied provider account and operator-enabled access. The provider may process its account credentials, requested locations, session identifiers, destination metadata, connection times and traffic volume. Your managed servers maintain the authorization and usage state needed to enforce residential allowances. These are operational records for your configured infrastructure, not developer telemetry.

The current Geonode adapter uses an unencrypted HTTP proxy connection from the VPN server to the provider. Proxy credentials and destination metadata are visible on that hop. Application HTTPS and the selected encrypted DNS retain their TLS protection; unsupported traffic in the residential scope stays blocked. The provider's processing is independent from Xeusx Labs and is subject to its own terms and privacy practices.

## 4. Authorized servers and hosting infrastructure

Xeusx is designed primarily for server infrastructure you own or administer. It does not discover, recommend, broker, certify, or sell access to third-party VPN services.

If you choose an Authorized Server administered by another party, that party controls the server and may process connection metadata such as your source IP address, connection times, traffic volume, destination metadata visible at the server, and server-side logs. Its privacy and security practices are independent from Xeusx Labs and are not governed by this Privacy Policy. Only use tokens and servers for which you have express authorization.

If you use Orb to provision or manage a server, your hosting provider may process account, billing, IP address, server, disk, snapshot, network, abuse, and operational data under its own terms and privacy policy. Xeusx does not control your hosting provider.

## 5. GitHub and other distribution hosts

Official downloads and updates may be hosted on GitHub or another official distribution provider. When you download files or when the app checks for updates, the host may process ordinary request information under its own privacy policy and terms. The developer does not control that third party's processing.

## 6. macOS permissions and local security

- **Local Authentication / Touch ID / Mac password:** used to unlock your local vault. Biometric checks are performed by macOS; Xeusx does not receive or store biometric data.
- **Administrator approval:** the first connection may require macOS administrator approval to install or activate a privileged helper needed to create and manage the VPN interface. This is a local authorization flow.
- **SSH / server administration:** Orb requires SSH access to servers you own or are authorized to administer.
- **Network access:** required to establish the VPN tunnel, check for updates, synchronize connections, fetch optional rule-set data, and — when you use Orb — administer your own servers over SSH.
- **Keychain:** used to store connection material and server-management material locally on your Mac.

## 7. Security design and limits

Xeusx is designed with local token import, Keychain storage, server identity verification, update verification, scoped server-administration keys, and an always-on kill switch. These protections help reduce common risks, but no app can guarantee complete security, anonymity, uninterrupted connectivity, correct server configuration, or successful operation on every network.

A VPN protects the connection path between your Mac and your selected server. It does not make you anonymous by itself, does not control websites or apps you use, does not protect against every tracking method, and does not guarantee that network filtering, blocking, monitoring, or traffic analysis will be defeated.

Orb helps you administer servers, but you remain responsible for server hardening, hosting-provider security, credentials, access profiles, updates, firewall rules, backups, and compliance.

## 8. Children's privacy

Xeusx is not directed to children and does not knowingly collect personal information from children through the app.

## 9. International use

Xeusx is self-hosted software that runs on your Mac and connects to the Authorized Server you choose. Because the app does not send app-usage data to a developer-operated backend, the developer does not receive your app-usage data through Xeusx. Third-party hosts, your hosting provider, any party administering an Authorized Server you do not administer, package repositories, and optional sources you configure may process data in other jurisdictions under their own policies.

## 10. Your choices and control

You can control Xeusx data by managing it on your device. You can remove saved servers in the app, disable optional update checks or rule-set downloads where settings allow, delete local logs, remove managed servers, rotate or revoke server-management keys where supported, remove the app, and remove related Keychain items from your Mac.

You should keep your token, passphrase, Mac account, server credentials, SSH keys, and server administrator access secure. Anyone with access to those items may be able to use or modify your VPN connection or server.

## 11. Third-party and open-source components

Xeusx may include third-party and open-source components governed by their own licenses and notices. Those notices are provided with the app or accompanying materials.

## 12. Changes to this policy

The developer may update this Privacy Policy from time to time. Material changes will be reflected here with a new "Last updated" date. Continued use of Xeusx after an updated policy is posted means you accept the updated policy, unless applicable law requires a different process.

## 13. Contact and communications

You may contact Xeusx Labs through **Contact Support** inside the app or by
email at [support@xeusx.com](mailto:support@xeusx.com). Use one of these private
channels for privacy questions, complaints, rights requests, security matters,
or any message containing personal information or other sensitive details.

For non-sensitive support requests and bug reports, use the public Xeusx for
macOS issue tracker:
<https://github.com/xeusxlabs/xeusx-desktop-mac/issues>.

If you communicate through GitHub, GitHub processes your account name, message,
and associated metadata under its own policy. Public issues are visible to
others. Do not include connection tokens, passphrases, private keys, bearer
credentials, SSH credentials, full server addresses, personal information, or
unredacted diagnostic logs in a public issue.

Information you voluntarily provide through a support channel is used only to
respond, maintain security and functionality, enforce legal rights, or comply
with law. A support, privacy, security, or legal communication may be retained
for as long as reasonably necessary for those purposes, subject to applicable
law and, for GitHub communications, GitHub's controls.

---

See also: **[Terms of Use](TERMS.md)** and **[License](LICENSE.md)**.
