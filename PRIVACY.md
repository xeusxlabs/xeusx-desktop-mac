# Xeusx Privacy Policy

**Last updated: July 7, 2026**

This Privacy Policy explains how **Xeusx for macOS**, including the public **Xeusx+** build (**"Xeusx"** or the **"app"**), handles information. Xeusx is a self-hosted VPN client and server manager designed so connection material and server-administration material stay on your Mac and under your control.

## At a glance

- **No accounts.** Xeusx has no sign-up, login, user profile, or developer account system.
- **No developer VPN backend.** Xeusx connects your Mac to your server, not to a developer-operated VPN service.
- **No developer traffic visibility.** The developer does not operate a relay or exit server for your VPN traffic.
- **No tracking or telemetry.** The app does not include third-party advertising, analytics, behavioral tracking, usage telemetry, crash reporting to the developer, or a license server that reports app use to the developer.
- **Local secrets.** Connection material is stored locally in macOS Keychain. The import passphrase is used transiently in memory and is not stored by the app.
- **Orb server management stays local too.** If you use Orb to run your own servers, Xeusx creates or uses server-management material on your Mac, keeps it in your local Keychain vault where applicable, and connects directly to your servers. The developer runs no admin backend and receives none of this.
- **Some third parties may see ordinary request data.** For example, GitHub may receive your IP address when you download the app or when the app checks for updates, your hosting provider may process server-related data, and your chosen server operator may see VPN connection metadata.

## 1. Information the developer does not collect through the app

The app does not collect, transmit to the developer, or sell personal information. The app does not include developer-operated accounts, advertising identifiers, analytics SDKs, behavioral profiling, usage telemetry, crash reporting to the developer, install counting, connection counting, server counting, or a developer-operated license server.

The app does not send browsing history, DNS queries, VPN traffic, imported tokens, passphrases, server lists, server credentials, SSH keys, connection logs, or app-usage statistics to the developer.

## 2. Information stored on your device

When you import a connection token, Xeusx decodes it locally and stores the resulting connection material in a device-local macOS Keychain vault. Depending on your server configuration, this may include server addresses, user entries, protocol profiles, server-issued artifacts, server labels, routing preferences, and related connection settings.

Xeusx also stores ordinary app preferences locally, such as selected options and UI settings.

If you use **Orb**, Xeusx also stores server-management material locally on your Mac. This may include the list of servers you manage, server labels, SSH host identity information, setup state, update settings, user-management metadata, and a scoped administrative SSH key used to manage Xeusx operations on your servers. The key is generated or enrolled on your Mac and is used to connect from your Mac to servers you manage; it is not sent to the developer.

Any setup password, SSH credential, or server alias you provide during first-time setup is used for the setup flow and key enrollment. Xeusx is designed not to retain setup passwords after enrollment where the supported setup flow allows password removal or replacement with a scoped key. You can rotate or revoke management keys and remove managed servers when supported by the app and your server configuration.

Detailed logging, if available and enabled by you, is local to your Mac. Logs are not sent to the developer by the app. Logs are intended not to include your import passphrase, full connection strings, or private keys, but you should review any log before sharing it with anyone.

Your import passphrase is used only transiently in memory to decode a pasted token. The app is designed not to write the passphrase to disk, Keychain, logs, or developer systems.

## 3. Network connections the app may make

Apart from carrying your VPN traffic, the app may make the following outbound connections:

1. **VPN tunnel.** When you connect, Xeusx routes traffic to the VPN server you selected. That server is operated by you or by someone you trust, not by the developer.
2. **Official updates.** Xeusx may fetch a signed update manifest and release artifact from GitHub or another official distribution location. These requests do not include your imported VPN secrets, but ordinary web request data such as IP address, user agent, time, and requested file may be visible to the third-party host.
3. **Optional server refresh.** If your server supports it, Xeusx may renew connection material over a protected request to your server using server-issued credentials. This request goes to your server, not to the developer.
4. **Optional routing rule-set updates.** If you enable downloadable rule sets, blocklists, or geo data, Xeusx may fetch those files from the sources you configure or approve, on the schedule you choose.
5. **Orb server administration.** If you manage servers with Orb, the app opens SSH connections from your Mac directly to those servers. These connections go to servers you control or are authorized to manage, not to the developer, and are intended for defined Xeusx management operations rather than general-purpose server administration.
6. **Hosting-provider or operating-system traffic.** Your server, hosting provider, operating system, package repositories, and security-update sources may create their own logs or network requests outside the app's control.

Xeusx does not phone home to a developer-operated app-usage backend.

## 4. Your server operator and hosting provider

Xeusx connects to a private VPN server that you or a third party operates. The server operator controls that server. Like any VPN server operator, they may be able to observe connection metadata, such as source IP address, connection times, traffic volume, destination metadata visible at the server, and server-side logs.

If someone else operates your server, their privacy and security practices are governed by them, not by this Privacy Policy. Only use tokens from a server operator you trust.

If you use Orb to provision or manage a server, your hosting provider may process account, billing, IP address, server, disk, snapshot, network, abuse, and operational data under its own terms and privacy policy. Xeusx does not control your hosting provider.

## 5. GitHub and other distribution hosts

Official downloads and updates may be hosted on GitHub or another official distribution provider. When you download files or when the app checks for updates, the host may process ordinary request information under its own privacy policy and terms. The developer does not control that third party's processing.

## 6. macOS permissions and local security

- **Local Authentication / Touch ID / Mac password:** used to unlock your local vault. Biometric checks are performed by macOS; Xeusx does not receive or store biometric data.
- **Administrator approval:** the first connection may require macOS administrator approval to install or activate a privileged helper needed to create and manage the VPN interface. This is a local authorization flow.
- **SSH / server administration:** Orb requires SSH access to servers you own or are authorized to administer.
- **Network access:** required to establish the VPN tunnel, check for updates, perform optional server refresh, fetch optional rule-set data, and — when you use Orb — administer your own servers over SSH.
- **Keychain:** used to store connection material and server-management material locally on your Mac.

## 7. Security design and limits

Xeusx is designed with local token import, Keychain storage, server identity verification, update verification, scoped server-administration keys, and an always-on kill switch. These protections help reduce common risks, but no app can guarantee complete security, anonymity, uninterrupted connectivity, correct server configuration, or successful operation on every network.

A VPN protects the connection path between your Mac and your selected server. It does not make you anonymous by itself, does not control websites or apps you use, does not protect against every tracking method, and does not guarantee that network filtering, blocking, monitoring, or traffic analysis will be defeated.

Orb helps you administer servers, but you remain responsible for server hardening, hosting-provider security, credentials, users, updates, firewall rules, backups, and compliance.

## 8. Children's privacy

Xeusx is not directed to children and does not knowingly collect personal information from children through the app.

## 9. International use

Xeusx is self-hosted software that runs on your Mac and connects to the server you choose. Because the app does not send app-usage data to a developer-operated backend, the developer does not receive your app-usage data through Xeusx. Third-party hosts, your server operator, your hosting provider, package repositories, and optional sources you configure may process data in other jurisdictions under their own policies.

## 10. Your choices and control

You can control Xeusx data by managing it on your device. You can remove saved servers in the app, disable optional update checks or rule-set downloads where settings allow, delete local logs, remove managed servers, rotate or revoke server-management keys where supported, remove the app, and remove related Keychain items from your Mac.

You should keep your token, passphrase, Mac account, server credentials, SSH keys, and server administrator access secure. Anyone with access to those items may be able to use or modify your VPN connection or server.

## 11. Third-party and open-source components

Xeusx may include third-party and open-source components governed by their own licenses and notices. Those notices are provided with the app or accompanying materials.

## 12. Changes to this policy

The developer may update this Privacy Policy from time to time. Material changes will be reflected here with a new "Last updated" date. Continued use of Xeusx after an updated policy is posted means you accept the updated policy, unless applicable law requires a different process.

## 13. Contact

Questions about this Privacy Policy can be raised through the project's official GitHub repository.

---

See also: **[Terms of Use](TERMS.md)** and **[License](LICENSE.md)**.
