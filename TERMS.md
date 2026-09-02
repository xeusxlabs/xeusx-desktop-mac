# Xeusx Terms of Use

**Last updated: July 17, 2026**

These Terms of Use (**"Terms"**) govern your download, installation, and use of **Xeusx for macOS**, including the public **Xeusx+** build (**"Xeusx"** or the **"app"**). By downloading, installing, or using Xeusx, you agree to these Terms. If you do not agree, do not download, install, or use Xeusx.

These Terms work together with the **[License](LICENSE.md)**, which governs your rights in the software, and the **[Privacy Policy](PRIVACY.md)**, which explains how the app handles information. If these Terms conflict with the License about software-licensing rights, the License controls for that issue.

## 1. What Xeusx is

Xeusx is a native macOS app that connects your Mac to private, self-hosted VPN servers using one encrypted Xeusx token assigned to your authorized access. For these Terms, an **"Authorized Server"** is a compatible server that you own, administer, or have express permission to use. The term describes your authority to use the server; it does not mean Xeusx Labs has reviewed, approved, or certified it. The token represents the Xeusx connections assigned to that access and keeps them synchronized. The public **Xeusx+** build includes the Connect client and **Orb**, a built-in server manager that can provision and operate your own Authorized Servers over SSH from the app.

Xeusx is **not** a VPN subscription, hosted VPN service, internet service provider, cloud relay, bandwidth provider, exit-node provider, managed security service, server-hosting company, or server administrator for you. The developer does not provide VPN servers, network access, exit locations, bandwidth, user accounts, app-usage analytics, or a backend that your app reports to. Xeusx also does not discover, recommend, broker, certify, sell, or provide access to third-party VPN services.

The developer does not host, operate, configure, secure, monitor, or manage any Authorized Server for you, including servers you set up or manage with Orb. Orb runs on your Mac, acts on your instructions, and uses the server addresses and credentials you provide.

## 2. Eligibility and requirements

To use Xeusx, you need a compatible Mac running **macOS 14 or later** and a valid Xeusx token and passphrase assigned to your authorized access. To provision or manage servers with Orb, you also need a supported Ubuntu Linux server you own or are authorized to administer, with SSH access to it, and you are responsible for complying with your hosting provider's terms.

You must be legally able to enter into these Terms and legally permitted to use VPN, proxy, encryption, and server-management software — and to operate or administer a server — in the places that apply to you.

Possession of a Xeusx token does not by itself establish authorization. You are responsible for confirming that every token and server is assigned to access you are entitled to use and for preventing unauthorized disclosure of credentials.

## 3. License and official downloads

Xeusx is free to download and use as an unmodified official build, but it is proprietary software. Your rights to the app are governed by the **[License](LICENSE.md)**.

You may download official builds from official Xeusx distribution channels. You may share links to official download locations. You may not redistribute, mirror, re-upload, repackage, resell, rebrand, modify, reverse engineer, or create derivative versions of the app except as expressly allowed by the License or by a separate written agreement from the developer.

## 4. Your infrastructure and access credentials

Xeusx acts only on the server addresses, access credentials, and configuration you import or create. The developer does not operate, configure, monitor, supervise, validate, review, or secure any Authorized Server. This applies equally to servers you provision or manage with Orb: you remain responsible for every server Orb touches.

You are solely responsible for:

- your Authorized Servers, tokens, configuration, routing choices, and traffic;
- provisioning, configuring, updating, securing, monitoring, backing up, and operating any server you set up or manage with Orb;
- complying with your hosting provider's terms and acceptable-use policy;
- the access profiles, credentials, links, and QR codes you create, assign, export, revoke, or otherwise make available within a deployment you control;
- verifying that every server and credential you use is authorized;
- securing your device, server, credentials, passphrases, SSH keys, administrative keys, and hosting account;
- complying with laws that apply to you, your access profiles, your traffic, and your servers; and
- any activity that occurs through your use of Xeusx or your server infrastructure.

If an Authorized Server is administered by another party, that party may process connection metadata or maintain server-side logs. Its practices are independent from Xeusx Labs and are not governed by these Terms.

Orb lets you create access profiles across a server fleet and scope each profile to all current and future managed servers or only selected servers. When selected access is used, a new server is unavailable until it is added to that profile. An access profile is part of your server configuration; it is not a Xeusx Labs account, subscription, or managed service.

One encrypted Xeusx token represents the Xeusx connections assigned to an access profile and keeps them synchronized. Removing server access remains effective on the server even before the device receives a later synchronization update. Only the connected Authorized Server is contacted during synchronization; requests are not sent to a Xeusx developer account or VPN backend.

Synchronization is event-driven and may occur after relevant connection, app, system, or network events, or when you choose **Sync**. There is no periodic server-synchronization timer or continuous background polling loop. Checks do not run while the privacy vault is locked, and automatic checks are deferred without a suitable tunnel. The **[Privacy Policy](PRIVACY.md)** describes these requests in more detail.

## 5. Acceptable use

You agree to use Xeusx only for lawful, authorized, and responsible purposes. You must not use Xeusx to:

- violate any applicable law, regulation, court order, contract, hosting-provider rule, or third-party right;
- gain unauthorized access to any system, account, network, device, or service;
- provision, administer, modify, or access any server you do not own or are not authorized to manage;
- attack, disrupt, overload, scan without authorization, or interfere with any system, network, or service;
- distribute malware, phishing content, spam, botnet traffic, credential theft tools, exploit kits, or other harmful content;
- infringe intellectual-property, privacy, publicity, or other rights;
- evade sanctions, export controls, law-enforcement orders, court orders, or legal restrictions;
- conceal or facilitate criminal activity;
- operate a paid, hosted, resale, managed, or public VPN/proxy service using Xeusx without a separate written agreement; or
- tamper with app security, signing, update verification, integrity checks, privacy protections, anti-tamper mechanisms, or server-management restrictions.

VPN, proxy, encryption, telecommunications, server-administration, and server-hosting rules vary by jurisdiction and may change. You are responsible for determining whether your use of Xeusx is lawful where you are located and where your traffic, servers, or authorized users may be located. Do not use Xeusx where it is restricted or prohibited.

## 6. Updates and availability

The developer may provide updates, patches, release artifacts, update manifests, or new builds at its discretion. The developer may change, suspend, or discontinue Xeusx or any feature at any time. The developer has no obligation to provide support, maintenance, compatibility, security fixes, updates, hosting, or continued availability.

For security, you are responsible for downloading Xeusx from official locations, verifying releases when appropriate, and keeping your copy up to date. You are also responsible for keeping your own servers and dependencies secure and current.

## 7. Third-party services and components

Xeusx may interact with or rely on third parties, including GitHub for official downloads and update delivery, Apple operating-system services, your hosting provider, any independently administered Authorized Server you choose to use, optional routing-rule sources you configure, operating-system package repositories, and bundled third-party or open-source components.

Those third parties are independent from the developer and are governed by their own terms, privacy policies, and licenses. The developer is not responsible for third-party services, infrastructure, content, logs, availability, security, or data practices.

## 8. Privacy

The app is designed to avoid developer-operated accounts, analytics, advertising, telemetry, and traffic collection. The **[Privacy Policy](PRIVACY.md)** explains what the app stores locally, what optional network requests it may make, and what independently controlled infrastructure and service providers may process when you download updates, connect to an Authorized Server, or use Orb to administer servers.

## 9. No emergency or high-risk use

Xeusx is not designed for emergency services, life-safety systems, critical infrastructure, military use, nuclear facilities, medical devices, air traffic control, or any environment where failure, interruption, blocking, misrouting, leakage, compromise, server misconfiguration, or loss of connectivity could lead to death, personal injury, property damage, environmental damage, or severe business loss. You must not rely on Xeusx as your only means of communication, security, compliance, administration, or access.

## 10. No warranty

XEUSX IS PROVIDED **"AS IS"** AND **"AS AVAILABLE"** WITHOUT WARRANTY OF ANY KIND, WHETHER EXPRESS, IMPLIED, STATUTORY, OR OTHERWISE, INCLUDING WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE, NON-INFRINGEMENT, SECURITY, ACCURACY, AVAILABILITY, ERROR-FREE OPERATION, UNINTERRUPTED OPERATION, CORRECT SERVER CONFIGURATION, OR THAT XEUSX WILL MEET YOUR REQUIREMENTS.

NO VPN, PROXY, SERVER-MANAGEMENT, OR SECURITY SOFTWARE CAN GUARANTEE ANONYMITY, COMPLETE SECURITY, UNINTERRUPTED ACCESS, CORRECT CONFIGURATION, SUCCESSFUL OPERATION ON EVERY NETWORK, OR LAWFUL USE IN EVERY JURISDICTION. YOU USE XEUSX AT YOUR OWN RISK.

Some jurisdictions do not allow certain warranty exclusions, so some exclusions may not apply to you.

## 11. Limitation of liability

TO THE MAXIMUM EXTENT PERMITTED BY LAW, THE DEVELOPER AND ITS SUPPLIERS SHALL NOT BE LIABLE FOR ANY INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL, EXEMPLARY, PUNITIVE, OR ENHANCED DAMAGES, OR FOR ANY LOSS OF PROFITS, REVENUE, BUSINESS, DATA, USE, GOODWILL, REPUTATION, OPPORTUNITY, OR OTHER INTANGIBLE LOSSES, ARISING OUT OF OR RELATED TO XEUSX, ORB, YOUR SERVER, YOUR TRAFFIC, YOUR CONFIGURATION, THESE TERMS, OR THE LICENSE, UNDER ANY THEORY OF LIABILITY, WHETHER CONTRACT, TORT, STRICT LIABILITY, NEGLIGENCE, STATUTE, OR OTHERWISE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

BECAUSE XEUSX IS PROVIDED AT NO CHARGE, THE DEVELOPER'S TOTAL AGGREGATE LIABILITY FOR ALL CLAIMS ARISING OUT OF OR RELATED TO XEUSX, THESE TERMS, OR THE LICENSE SHALL NOT EXCEED **ONE U.S. DOLLAR (US $1)** OR THE MINIMUM AMOUNT REQUIRED BY APPLICABLE LAW, WHICHEVER IS GREATER.

Some jurisdictions do not allow certain limitations of liability, so some limitations may not apply to you.

## 12. Indemnification

To the maximum extent permitted by law, you agree to defend, indemnify, and hold harmless the developer and its suppliers, contributors, officers, directors, employees, contractors, and agents from and against any claims, demands, losses, liabilities, damages, fines, penalties, costs, and expenses, including reasonable attorneys' fees, arising out of or related to:

- your use or misuse of Xeusx;
- your use or misuse of Orb or any server-management function;
- your server infrastructure, configuration, tokens, access profiles, hosting account, or traffic;
- your violation of these Terms, the License, or applicable law;
- your violation of any third-party right; or
- any content, data, or activity transmitted through your use of Xeusx or your server.

## 13. Export controls and sanctions

You must comply with all applicable export-control, import-control, sanctions, anti-boycott, and restricted-party laws and regulations. You may not use, download, export, re-export, transfer, or provide Xeusx in violation of those laws or for prohibited end uses.

## 14. Termination

These Terms begin when you first download, install, or use Xeusx and continue until terminated. They terminate automatically without notice if you breach them. Upon termination, you must stop using Xeusx and remove it from your devices. Sections 3 through 7 and 9 through 18 survive termination.

## 15. Changes to these Terms

The developer may update these Terms from time to time. Material changes will be reflected here with a new "Last updated" date. Continued use of Xeusx after updated Terms are posted means you accept the updated Terms, unless applicable law requires a different process.

## 16. Trademarks and no affiliation

Xeusx and related names, logos, and marks are trademarks of their respective owner. Apple, macOS, Mac, Touch ID, GitHub, and other third-party names are used only for identification and remain the property of their respective owners. Xeusx is not affiliated with, endorsed by, sponsored by, or derived from Apple Inc., GitHub, Inc., Microsoft Corporation, or any other third party.

## 17. General

If any provision of these Terms is held unenforceable, the remaining provisions remain in effect, and the unenforceable provision will be enforced to the maximum extent permitted by law. The developer's failure to enforce any provision is not a waiver. These Terms, together with the **[License](LICENSE.md)** and **[Privacy Policy](PRIVACY.md)**, are the entire agreement between you and the developer regarding your use of Xeusx and supersede any prior or contemporaneous understandings on that subject.

## 18. Contact

**Support email:** [support@xeusx.com](mailto:support@xeusx.com)

For private support, legal, privacy, security, or rights-related matters, use
**Contact Support** inside the app or email
[support@xeusx.com](mailto:support@xeusx.com). These are the preferred channels
for confidential or sensitive communications.

For non-sensitive support requests and bug reports, use the public Xeusx for
macOS issue tracker:
<https://github.com/xeusxlabs/xeusx-desktop-mac/issues>.

GitHub issues are public. Do not include connection tokens, passphrases, private
keys, full server addresses, bearer credentials, SSH credentials, personal
information, or unredacted diagnostic logs in a public issue.
