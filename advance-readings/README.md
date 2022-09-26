# Advance Readings

In advance of the design workshop, all participants produced a one-or-two page advance reading to be shared with the other attendees on either:

* A specific problem that they wanted to solve with a web-of-trust solution, and why current solutions (PGP or CA-based PKI) can't address the problem?
* A specific solution related to the web-of-trust that you'd like others to use or contribute to?

If you will be attending Rebooting the Web of Trust Fall 2022 in The Hague, Netherlands, please upload your advance readings to this directory with a pull request.

## Pull Request Submission

To add a paper, create a pull request to this repo with your contribution (preferably as an .md file, but if you can't, as a PDF), along with updates to the README.md in this folder. Please also include a byline with contact information in the paper itself.

Please also enter your paper _twice_ in this README file, once in the topical listing (adding a new category describing your topic, if necessary) and one in the alphabetical listing. Please be sure to include the full URL for your paper in the README, so that we can copy it to the main page URL and have it still correctly link.

If you don't know how to submit a pull request, please instead submit an issue.

## Request RWOT11 discount code

To those who have submitted an Advance Readings paper, RWOT11 offers a steep discount on the ticket price for participation to the event. Please obtain your discount code as follows.
* Copy the link to your Pull Request (see previous section)
* Email to [questions@weboftrust.info](mailto:questions@weboftrust.info), paste the link to the Pull Request and ask for the discount code

Please make sure to make your Pull Request Submission BEFORE you buy the tickets for RWOT11, in order to apply your discount code.

## Primer Listing

These primers overview major topics which are likely to be discussed
at the design workshop. If you read nothing else, read these. (But
really, read as much as you can!)

* [Advance Reading Primer](./advance-reading-primer.md) — About the advance reading papers
* [RWOT Primer](./rwot-primer.md) — How the design workshop works
* [DID Primer](./did-primer.md) — Decentralized Identifiers ([extended version](./did-primer-extended.md) also available)
* [Functional Identity Primer](./functional-identity-primer.md) — A different way to look at identity
* [Verifiable Credentials Primer](./verifiable-credentials-primer.md) — the project formerly known as Verifiable Claims
* [Glossary of Terms](./glossary-primer.md) — a brief dictionary of technical terms used at RWOT
* [Data Generator](./data-generator.md) — a data-generator for SSI

## Topical Listing

_Please add a level three header (`###`) for your paper's topic if it's not there already, then link it in the form:_

```
[name](link)
   * by [author](mailto:if desired)
   * One to two sentence synopsis or quote
   * #hashtags for topics
```

### [A Human Rights Approach to Digital Identity Protocols](./A%20Human%20Rights%20Approach%20to%20Digital%20Identity%20Protocols.md)
   * by [Adrian Gropper, MD](mailto:agropper@healthurl.com), Patient Privacy Rights, Austin, Texas
   * A novel approach to digital identity protocols is presented that gives market power to the human subject of identity-based interactions through their ability to choose a delegate.
   * #Delegation  #HumanRights #DID #VerifiableCredentials #w3c #GNAP

### [A Minimal Approach to Linked Trust with Uncertainty](./a-minimal-approach-to-linked-trust-with-uncertainty.md)
   * by [Golda Velez](mailto:gvelez17@gmail.com), Cooperation.org, Tucson, Arizona
   * A pragmatic approach to enabling any observer to add to the linked trust ecosystem through observed claims. In particular applications to human rights and accountability, and the importance of broad adoption in heterogeneous
domains in order to resist bad actors and provide aggregate privacy.
   * #Adoption #HumanRights #AI #risk #trust #hybrid #VerifiableCredentials

### [Accessible self sovereign identity](./accessible-self-sovereign-identity.md)
   * by [Andrew Slack](mailto:andrew.slack@sicpa.com), SICPA, Switzerland
   * and [Victor Martinez](mailto:victor.martinezk@sicpa.com), SICPA, Switzerland
   * The experience and security of any system operated by people depends on the information conveyed through user interfaces, the response of the users, and the interpretation of their actions. Existing interaction patterns in verifiable credential wallets tend towards visual-centric models and rely on inconsistent representations of data. This paper explores design patterns to manage and exchange verifiable data in more accessible ways.
   * #Accesability #VerifiableCredentials

### [Advanced DIDComm Messaging - A modern DIDComm based chat protocol](./advanced-didcomm-messaging.md)
  * by [Karim Stekelenburg](mailto:karim@animo.id), Animo Solutions, The Netherlands
  * Leveraging DIDComm to create a modern chat protocol that can compete with commonly used chat applications like WhatsApp and Telegram.
  * #DIDComm #protocol #messaging #chat

### [AI & Metaverse - How to trust our digital twin?](./ai-and-metaverse.md)
   * by [Zaïda Rivai](mailto:zaida.rivai@danubetech.com), Danube Tech Gmbh, Vienna
   * A proposal of critical ethical issues in the emerging technology AI & metaverse. What are the most important (ethical) issues regarding trust, AI and metaverse? How could we solve them? How could we fight bias fed in AI algorithms used for the metaverse or how to solve the intellectual property problem in the metaverse?
   * #ai #metaverse #trust #ethics

### [An exploration into Verifiable Group Credentials](./group-credentials.md)
   * by [Lohan Spies](mailto:lohan.spies@iohk.io), IOHK/DIDx, Hong Kong/South Africa
   * A proposal to explore the concept of verifiable group credentials.
   * #VerifiableCredentials #GroupCredentials

###  [Analysis of hybrid wallet solutions - Implementation options for combining x509 certificates with DIDs and VCs](./hybrid_wallet_solutions_x509_DIDs_VCs.md)
   * by [Carsten Stöcker](mailto:carsten.stoecker@spherity.com), Spherity GmbH
   * and [Christiane Wirrig](mailto:christiane.wirrig@spherity.com), Spherity GmbH
   * The EU Commission&#39;s proposal for review of the eIDAS Regulation from 2021 has opened strong expectations for a deep change in traditional identity models.  The EU might endorse a hybrid solution consisting of x509 certificates and decentralized PKI using DID/VC. This paper provides various options to address different implementation alternatives in combining x509 and DID/VC approaches.
   * #did, #eIDAS, #x509, #hybrid-wallets

###  [AnonCreds: ~~Ledger~~ VDR Agnostic Authentic Data Specification and Roadmap](./anoncreds-ledger-agnostic-spec.md)
   * by [Stephen Curran](mailto:swcurran@cloudcompass.ca), Cloud Compass Computing Inc., Canada
   * Adding details to the roadmap of the AnonCreds Specification Working Group
     about the use of AnonCreds with even more ledgers/VDRs, and the next
     version of the AnonCreds specification (and open source implementations),
     likely to be based on BBS+ Signatures.
   * #DIDComm, #credentials, #privacy, #zkp, #DIDs, #DIDMethods

### [Audited DIDComm connections](./audited-didcomm.md)
  * by [Fabrice Rochette](mailto:f@2060.io), 2060.io
  * A discussion of how to make audited and intermediated DIDComm connections
  * #DIDComm #protocol #messaging #chat

### [Authorized Issuer Lists](./authorized-issuer-lists.md)
  * by [Manu Sporny](mailto:msporny@digitalbazaar.com), Digital Bazaar, USA
  * A way of publishing a list of authorized issuers to enable Verifiers to bootstrap into trusted ecosystems.
  * #VerifiableCredentials #w3c #trust #registries

### [BTCR From First Principles](./btcr-from-first-principles.md)
   * by [Kate Sills](mailto:katelynsills@gmail.com), Digital Contract Design
   * This paper compares did:btcr v0.1 to a naive, off-chain version in terms of
     vulnerabilities to a few identified attacks.
   * #did:btcr #did #registry

### [Caching in DID Resolution](./caching-in-did-resolution.md)
* by [Markus Sabadello](mailto:markus@danubetech.com), Danube Tech, Austria
* Some thoughts on how to add and control caching in DID Resolution processes.
* #did #did-resolution

### [CESR adapter for sophisticated multisig](https://hackmd.io/GbQO3p6QTge-8eQMGuMaeQ)
   * by [Henk van Cann](mailto:h.vancann@blockchainbird.org), Blockchainbird.org, The Netherlands
   * Bridge Keep wallet of KERI / ACDC and the more sophisticated solutions at BCC for keeping secrets secret. At the same time: study and work towards KERI, CESR and ACDC supporting sophisticated multisignature schemes.
   * #SeedTool #KERI #CESR #ACDC #KEEP #ToIP #BCC
   
### [Classy DIDs](./classy-dids.md)
  * by [Shaun Conway](mailto:shaun@ixo.foundation), [ixo](https://ixo.world)
  * Differentiating classes of DIDs for different applications, based on property sets and how these influence behaviours relating to the identified subject
  * #JSON-LD #DIDs

### [Collaborative Seed Recovery: A New Methodology for Smart Custody](collaborative-seed-recovery-csr.md)
   * by Christopher Allen, Shannon Appelcline & Wolf McNally, Blockchain Commons
   * Personally held digital assets are very vulnerable to accidental loss. This reading outlines solutions to date and looks at plans for a collaborative seed recovery architecture.
   * #recovery #seed

### [Combining eIDAS High device binding with unlinkability](./combining-eIDAS-High-with-unlinkability.md)
   * by [Sietse Ringers](mailto:mail@sietseringers.net)
   * Strong device binding using ECDSA in order to achieve eIDAS High may be combined with unlinkability in SSI systems at the cost of introducing a TTP which deals with the linkability introduced by ECDSA.
   * #ssi #eidas #credentials #privacy #zkp

### [Comparing Credential Formats](./Comparing_Credential_Formats.md)
   * by [Dr. Andre Kudra](mailto:a.kudra@esatus.com), esatus AG, Germany
   * Credential Formats analyzed and compared by an international expert group
   * #Credentials #Formats #Signature #Revocation #Key-Management

### [Comparison Of Wallet Security Architectures](./comparing-wallet-security-architectures.md)
   * by [Paul Bastian](mailto:paul.bastian@bdr.de), Bundsedruckerei GmbH, Germany
   * Categorizing and analyzing potential Wallet Security Architectures
   * #ssi #Wallet #Credentials #Key-Management #Holder-Authentication #revocation #recovery #privacy

### [Continuous Authentication and Authorization using Verifiable Credentials](./authentication-and-authorization-using-verifiable-credentials.md)
   * by [Nikos Fotiou](mailto:fotiou@aueb.gr), Athens University of Economics and Business
   * Verifiable Credentials for expressing user capabilities, issued using OAuth 2.0, and used for accessing HTTP-based resources that abide by the Zero-Trust principle.
   * #IAA, #VerifiableCredentials, #ZTA

### [Creative Brief RWOT Animation Project.](./Creative%20Brief%20RWOT%20Animation%20Project.pdf)
   * by [Erica Connell](mailto:erica@legreq.com), Legendary Requirements
   * Let's produce a ~1-minute animation that tells the story of DIDs and
   RWOT. Working with collaborators from RWOT11, we will develop creative
   ideas and set the framework for the realization of a brief, stop-motion
   animated short.
   * #RWOTAnimation #DIDs #changetheworld #attendRWOT

### [Credentialing-enabled Zero Trust Architecture for supply chains](./credentialing_enabled_ZTA_for_supply_chains.md)
   * by [Carsten Stöcker](mailto:carsten.stoecker@spherity.com), Spherity GmbH
   * and [Christiane Wirrig](mailto:christiane.wirrig@spherity.com), Spherity GmbH
   * ZTA is an important design philosophy to establish security mechanisms at the API layer of each individual IT resource for increasing API Endpoint Security. This paper discusses how credentials can enable ZTA mechanisms to secure ERP systems for supply chain use cases.
   * #ABAC, #API-Endpoint-Security, #Authorisation, #Credentials, #SupplyChain, #Wallets, #ZTA

### [Data exchange agreements - Making data transactions trustworthy, auditable and immutable](./data-exchange-agreements--automating-lawfulness-to-data-tranactions.md)

   * by [Lal Chandran](mailto:lal@igrant.io) (iGrant.io, Sweden) and Fredrik Linden (MyData, Sweden)
   * A novel approach to building lawful, human-centric and scalable data spaces, making data transactions trustworthy, auditable and immutable via data exchange agreements. It provides a suite of tools that enable automated agreement handling for data exchange between a Data Source (DS) and Data Using Service (DUS). The proposed approach brings in the requisite trust and governance to establish a ubiquitous data exchange marketplace while empowering individuals to be in control of their data. Automated agreement handling is required for a scalable and regulatory-compliant data marketplace (data space). All organisations need to ensure that they are on the right side of the law (e.g. the GDPR) when consuming personal data (risk management) and to establish the digital trust needed for individuals to say yes to sharing their data.
   * #eSSIF-Lab #SSI-ecosystem #dataagreeents #rightdata #dataexchangeagreements #gdpr #privacybydesign #wallet #dataspace #datamarketplace

### [Decentralized revocation of Verifiable Credentials](./Decentralized-revocation-of-Verifiable-Credentials.md)
   * by [Andrea Scorza, LTO Network](mailto:andrea@ltonetwork.com), [Arnold Daniels, LTO Network](mailto:arnold@ltonetwork.com)
   * #Revocation #VerifiableCredentials #StatusList #Cryptography #bitstring #blockchain #LTO #Sovrin

### [Defining a BIP 322 Signature Suite](./bip322-signature-suite.md)
   * by [Will Abramson](mailto:will@legreq.com), Legendary Requirements, work funded by Digital Contract Design
   * Let's make BIP 322 smart signatures a usable verification method for Verifiable Credential use cases.

### [DID Connect, connecting people, devices and applications via DID and Verifiable Credentials](./did-connect.md)
  * by [Robert Mao](mailto:rob@arcblock.io), ArcBlock, United States
  * DID Connect is a suite of RESTful APIs, UX components and SDK that provide a framework for DID interactions, connecting people, devices and applications via DID and Verifiable Credentials.
  * #connect #application #framework #VerifiableCredentials #UX

### [DID Fluidity](./did-fluidity.md)
  * by [Juan Caballero](mailto:jcaballero@centre.io), Centre.io, Berlin/United States
  * It would be great if a group of researchers and/or coordinators across DID methods could write lightweight micro-implementation guide covering cross-DID-method capabilities, anchored in properties defined in the DID data model and/or traits (see other paper below). This could be folded in as a section of the official W3C implementation guide at a later date if appropriate.
  * #documentation #crosschain #crossmethod #portability #metawallet #DIDextensions

### [Did Resources for SSI - address ALL requirements via DIDs](./did-resources.md)
   * by [Mirko Mollik](mailto:mollik@trustcerts.de)
   * DIDs allow us today to request the public keys to validate signature from a distributed verifiable data registry. Why not addressing all required resources like that, but independent from one specific vdr?
   * #did #vdr #resources

### [DID Torrent](./DID_torrent.md)
   * by [Vinay Vasanji](mailto:vinay.vasanji@pm.me)
   * A proposal to specify a p2p DID Method using the BitTorrent DHT, and a consumer use-case to drive its large scale adoption.
   * #DIDs #DIDmethods #p2p #peertopeer #applications #wallet

### [DID Traits](./did-traits.md)
   * by [Charles Cunningham](mailto:charles.cunningham@spruceid.com) and [Wayne Chang](mailto:wayne@spruceid.com), Spruce Systems, Inc., Berlin/New York
   * A proposal for characterising and categorising DID methods by supported feature sets to evaluate technical suitability for different use cases, applications and environments.
   * #dids #didmethods #identitymanagement #applications #devx

### [Discovery Handshake](./discovery-handshake.md)
   * by [Snorre Lothar von Gohren Edwin](mailto:snorre@diwala.io), Diwala, Uganda/Oslo
   * A proposal to reason about bringing your own wallet to the table.
   * #discover #protocols #wallet

### [DKMS for SSI](./dkms-for-ssi.md)
   * by [Philippe Page](mailto:philippe.page@humancolossus.org)
   * DKMS-4-SSI is driven by the need of security for a Dynamic Data Economy. By design DDE transactions take place in a Zero-Trust environement and relies on assymetric cryptography (public/private keys) to create/use/verify self-addressing idenitfiers (SAID).
   * #eSSIF-Lab #SSI-ecosystem #key-management #keri #cesr

### [Dynamic & Decentralized Reputation for the Web of Trust: What We Can Learn from the World of Sports, Tinder, and Netflix](dynamic-decentralized-reputation-web-of-trust.md)
   * by [Ankur Banerjee](https://twitter.com/ankurb)
   * A discussion on the potential drawbacks of proof-of-authority and soul-bound tokens (SBTs), with an alternative system that could be constructed using Elo rating systems used in the world of sports and web services.
   * #reputation #trust #scoring

### [Elision, Redaction, and Noncorrelation in Smart Documents](elision-redaction-correlation-smart-documents.md)
   * by Wolf McNally, Christopher Allen, Shannon Appelcline, Blockchain Commons
   * An introduction to the `Envelope` data structure and its novel approach to facilitating the construction and transformation of “smart documents”, including native facilities for encryption, signing, elision (redaction), sharding, and noncorrelation.
   * #VerifiableCredentials #identity #sharding #signing
   
### [Enabling SSI for NFC, IoT and other smart devices](./Enabling%20SSI%20for%20NFC%2C%20IoT%20and%20other%20smart%20devices.md)
   * By [Caspar Roelofs](mailto:caspar@gimly.io) and Carlos Fontana, Gimly, the Netherlands
   * An exploration of technical requirements, limitations and solutions to implement SSI with low-computational smart devices and low bandwith data-transmission such as NFC smartcards, IoT devices, NFC, BLE communication.
   * #NFC #IoT #BLE #DIDComm #Inclusion 

### [Enhancing DID Privacy through shared Credentials using Merkle trees of DIDs and Claims with multiple presentation proofs](./Enhancing_DID_Privacy_through_shared_Credentials.md)
   * by [Frédéric Martin](mailto:frederic.martin@mydid.com), myDID SA
   * by [Imad El Aouny](mailto:imad.elaouny@mydid.com), myDID SA
   * A proposal to enhance DID privacy and reduce possible correlations 
   * #Privacy #DID #VerifiableCredentials #Wallet #Communication

### [Enhancing DIDComm messaging for mobile environments](./enhancing-didcomm-for-mobile-environments.md)
   * by [Ariel Gentile](mailto:a@2060.io)
   * An exploration on different needs to make DIDComm-based mobile wallets interoperable and aware of the constraints given by mobile environments
   * #DIDComm #protocol #messaging #Mobile #communications

### [eSSIF-Lab: Towards a European SSI ecosystem](./eSSIF-Lab%20-%20Towards%20a%20European%20SSI%20ecosystem.md)
   * by [Oskar van Deventer](mailto:oskar.vandeventer@tno.nl), TNO, Netherlands
   * Overview of the eSSIF-Lab SSI ecosystem. "eSSIF-Lab is a 7 M€, three-year (2019-2022), European-Commission-funded program that has been sponsoring start-ups, SMEs and innovators to develop open-source SSI components, SSI products and SSI services."
   * #eSSIF-Lab #SSI-ecosystem #Europe

### [Generalizing Secure Scuttlebutt for Data Integrity](./ssb-di.md)
   * by [Charles E. Lehner](mailto:charles.lehner@spruceid.com), Spruce Systems, Inc., New York
   * A proposal for generalizing the Secure Scuttlebutt system for DIDs and Data Integrity.
   * #VerifiableCredentials #SecureScuttlebutt

### [Identified communications - SSI and internet communications or internet communications and SSI](./SSI%20and%20internet%20communications%20or%20internet%20communications%20and%20SSI.md)
  * by [Alex Blom](alexander.blom@bloqzone.com), Bloqzone, Netherlands
  * Examining different solutions to the problem of identified communications
  * #SIP #DIDComm #chat #communications

### [Identity and Trust in a Co-operative Ecosystem](./Identity%20and%20Trust%20in%20a%20Co-operative%20Ecosystem.md)
   * by [Nick Meyne](nick.meyne@smtngood.eu) from [Co-op Credentials](https://coopcreds.com/)
   * Systemic approaches to the design of a digital identity and trust network for a co-operative ecosystem
   * #identity, #trust, #community, #platform_co-operatives, #ecosystems, #systemic_design

### [Identity Bridge: Verifiable Credentials from European Digital IDs](./identity-bridge.md)
   * by [Fabio Tagliaferro](mailto:fabio.tagliaferro@univr.it), Commercio.Network & University of Verona, Italy
   * Leverage the power of national European identities to obtain SSI credentials, starting from the Italian SPID ecosystem.
   * #VerifiableCredentials #Europe #SPID #Italy #SSI

### [Identity Net: Building an identity net through self-authenticated data graphs](./identity-net.md)
   * by [Christopher Chung](chris@violet.co)
   * An emergent identity mesh built from authenticated data points
   * #webs-of-trust #data #authentication #community #network

### [Multi-dimensional reputation systems using Webs of Trust](./Multi-dimensional%20reputation%20systems%20using%20webs-of-trust.md)
   * by [Oliver Klingefjord](mailto:hello@replabs.xyz), Replabs, Berlin.
   * A proposal for a novel multi-dimensional reputation system framework for social media using language models and webs of trust.
   * #Reputation #Webs-of-trust #Trust-networks

### [On-Chain DIDs](./on-chain-dids.md)
   * by [Martin Riedel](mailto:martin@identity.org), Identity.com
   * Evaluating DID (Document) State on-chain and the challenges around nomenclatures and spec-compliance.
   * #dids #didmethods #identitymanagement #applications

### [Reducing Correlation: To What Degree is it Necessary?](./reducing-correlation.md)
   * by [Brent Zundel](mailto:brent.zundel@avast.com), Avast s.r.o.
   * A proposal for a conversation about whether reducing correlation is necessary during credential exchange.
   * #VerifiableCredentials #HolderBinding #Zero-knowledge-proofs #ZKP

### [Rendering Verifiable Credentials](./rendering-verifiable-credentials.md)
  * by [Manu Sporny](mailto:msporny@digitalbazaar.com), Digital Bazaar, USA
  * A Verifiable Credential extension to support rendering using graphics, audio, or braille.
  * #VerifiableCredentials #w3c #a11y

### [Revisiting Usefulness of Centralized System for Establishing Trust](./revisiting-usefulness-of-centrailzed-system.md)
   * by [Shigeya Suzuki](mailto:shigeya@wide.ad.jp), Ph.D, Project Professor, Graduate School of Media and Governance, Keio University, Japan
   * Using DNS as root of trust with help of ICANN's virtualized decentralized governance mechanism
   * #RootOfTrust #DNS #DNSSEC #ICANN #VirtualizedDecentralization #MultistakeholderGovernance
### [Revocation and VC](./revocation-and-vc.md)
   * by [Ahamed Azeem](mailto:azeem.ahamed@danubetech.com), Danube Tech, Austria.
   * A discussion about revocation methods used in SSI and VC and describes a suitable approach for privacy-preserving revocation.
   * #Revocation #VC #RevocationLists2020 #IndyRevocationn

### [Self Custody Risk Analysis](./self-custody-risk-analysis.md)
   * by [Eric Schuh](mailto:eric@legreq.com), Legendary Requirements, USA
   * A software framework to enable the choice of how to self custody digital assets
   * #recovery #wallet #threat-model

### [Social Wallet Recovery](./social-wallet-recovery.md)
  * by [Timo Glastra](mailto:timo@animo.id), Animo Solutions, The Netherlands
  * Social recovery of wallet data and keys by leveraging sharding.
  * #recovery #wallet #sharding

### [Societal impacts of SSI technologies](./societal-impacts.md)
  * by [Amy Guy](mailto:rwot@rhiaro.co.uk)
  * How can we make it easier to ask the hard questions about the work we do?
  * #ethics #SSI-ecosystem #community

### [Spendability of Currency: Citizen Report](./spendability-of-currency.md)
   * by [Will Abramson](mailto:wip.abramson@gmail.com), Legendary Requirements, UK
   * How easy is it to spend cash around the world these days? Let's find out, by actively attempting to and recording the results.

### [SSI data Generator](./data-generator.md)
   * by [Moritz Schlichting](mailto:moritz@animo.id), Animo Solutions, Utrecht, The Netherlands
   * A data generator for SSI interactions and mocking
   * #eSSIF-Lab #SSI-ecosystem #Europe #Data #Generator #tools

### [Standardization Overview](./standardization-overview.md)
   * by [Maaike van Leuken](mailto:maaike.vanleuken@tno.nl), TNO, Eindhoven, The Netherlands
   * An overview of SSI standardization
   * #eSSIF-Lab #Standardization

### [Trust Registries – Enhancing Interoperability and preventing Phishing/MITM Attacks](./Trust-Registries.md)

   * by [Isaac Henderson Johnson Jeyakumar](mailto:isaac-henderson.johnson-jeyakumar@iat.uni-stuttgart.de), University of Stuttgart, Germany & [Michael Kubach](mailto:michael.kubach@iao.fraunhofer.de), Fraunhofer IAO, Germany.
   * A proposal for a Trust Registry concept to enhance interoperability and prevent Phishing/MITM attacks in different components of the SSI Ecosystem.
   * #TrustRegistry #TRAIN #trustworthiness #SSI #eSSIF-Lab

### [Trusted Crypto Asset Framework](./trusted-crypto-asset.md)

* by: [Belsy Yuen](mailto:belsy@nymlab.it), [Elena Chachkarova](elena@nymlab.it), [Egidio Casati](mailto:egidio.casati@nymlab.it)
* A proposal for a decentralised trust framework powering regulated crypto assets
* #crypto-asset #ssi #regulated-deFi #kYC #smart-contract-wallet #on-chain-verifier

### [Unravelling Web of Trust](./UnravellingTrust.md)
  * by [Ian Grigg](mailto:iang@iang.org)
  * By way of anecdotes, an exploration as to why WoT didn't work, and why Trust is harder. A request for more anecdotes to shed light on the way forward.
  * #WOT #web-of-trust #trust #community

### [Using MultiBase Anchors within a Personally-Issued Endorsement Credential to Corroborate Attributes in an Existing Issued Credential](./endorsements.md)
* by Phillip D. Long, Dmitri Zagidulin, Kerri Lemoie
* A proposal for a Verifiable Endorsements mechanism for VCs.

### [Validation - The Missing Link](./validation-the-missing-link.md)
  * by [Rieks Joosten](mailto:rieks.joosten@tno.nl), TNO, Netherlands
  * In order to adopt VCs (or SSI technology), we need to explore what individual parties need *apart* from what's already part of VCs (e.g.: proofs), and how such needs can (also) be accommodated.
  * #validation #verification #sovereignty

### [Verifiable Credentials Holder Binding](./verifiable-credentials-holder-binding.md)
   * by [Oliver Terbu](mailto:oliver.terbu@spruceid.com), Spruce Systems, Inc., Berlin/New York
   * A proposal how to define a flexible and deterministic approach to verify the binding between the holder and the credential subject of the verifiable credential which is a blindspot of the W3C Verifiable Credentials Data Model 1.0 standard today.
   * #VerifiableCredentials #HolderBinding #2FA #Biometrics #Delegation

### [Verifiable Identifiers ](./verifiable-identifers.md)
   * by [Joe Andrieu](mailto:joe@legreq.com), Legendary Requirements, Ventura, CA, USA
   * *A Best Practice for Decentralized Identifiers* Verifiable Identifiers (VIDs) are a DID best practice for platform-independent, privacy-agile, cryptographic verification of actions taken on behalf of that identifier.
   * #DID #VID #IID #best-practice

### [Verifier Universal Interface](./vui-primer.md)
   * by [Daniel Moledo ](mailto:daniel@gataca.io)
   * VUI (Verifier Universal Interface) specification proposal to achieve interoperability for the verification process: that is, to eliminate a possible vendor lock-in between any wallet and any verifier tool.
   * #VerifiableCredentials #Verifier

### [Words Matter: A Rethink of Current SSI Terminology](./words-matter-a-rethink-of-current-terminology.md)
   * by [Ana Goessens](mailto:ana@animo.id)
   * Continuing the conversation on the topics surrounding SSI, using methods from commercial branding to semantic philosophy.
   * #Terminology #Semantics

### [ZKPs with zkSNARKs in a DIDComm ecosystem](./zkp-with-zksnarks-in-a-didcomm-ecosystem.md)
- by [Berend Sliedrecht](mailto:berend@animo.id), Animo, The Netherlands
- A proposal on working with zkSNARKs within the verifiable credential space
- #VerifiableCredentials #ZKP #zksnark

### ... more ...

## Alphabetical Listing

_Please also enter your paper alphabetically in the form:_

```
* [Paper Name](link)
```

* [A Human Rights Approach to Digital Identity Protocols](./A%20Human%20Rights%20Approach%20to%20Digital%20Identity%20Protocols.md)
* [A Minimal Approach to Linked Trust with Uncertainty](./a-minimal-approach-to-linked-trust-with-uncertainty.md)
* [Accessible self sovereign identity](./accessible-self-sovereign-identity.md)
* [Advanced DIDComm Messaging - A modern DIDComm based chat protocol](./advanced-didcomm-messaging.md)
* [AI & Metaverse - How to trust our digital twin?](./ai-and-metaverse.md)
* [An exploration into Verifiable Group Credentials](./group-credentials.md)
* [Analysis of hybrid wallet solutions - Implementation options for combining x509 certificates with DIDs and VCs](./hybrid_wallet_solutions_x509_DIDs_VCs.md)
* [AnonCreds: ~~Ledger~~ VDR Agnostic Authentic Data Specification and Roadmap](./anoncreds-ledger-agnostic-spec.md)
* [Audited DIDComm](./audited-didcomm.md)
* [Authorized Issuer Lists](./authorized-issuer-lists.md)
* [BTCR From First Principles](./btcr-from-first-principles.md)
* [Caching in DID Resolution](./caching-in-did-resolution.md)
* [CESR adapter for sophisticated multisig](./CESR-adapter-for-sophisticated-multisig.md)
* [Classy DIDs](./classy-dids.md)
* [Collaborative Seed Recovery: A New Methodology for Smart Custody](./collaborative-seed-recovery-csr.md)
* [Combining eIDAS High device binding with unlinkability](./combining-eIDAS-High-with-unlinkability.md)
* [Comparing Credential Formats](./Comparing_Credential_Formats.md)
* [Continuous Authentication and Authorization using Verifiable Credentials](./authentication-and-authorization-using-verifiable-credentials.md)
* [Creative Brief RWOT Animation Project](./Creative%20Brief%20RWOT%20Animation%20Project.pdf)
* [Credentialing-enabled Zero Trust Architecture for supply chains](./credentialing_enabled_ZTA_for_supply_chains.md)
* [Data exchange agreements - Making data transactions trustworthy, auditable and immutable](./data-exchange-agreements--automating-lawfulness-to-data-tranactions.md)
* [Decentralized revocation of Verifiable Credentials](./Decentralized-revocation-of-Verifiable-Credentials.md)
* [Defining a BIP 322 Signature Suite](./bip322-signature-suite.md)
* [DID Connect, connecting people, devices and applications via DID and Verifiable Credentials](./did-connect.md)
* [DID Fluidity](./did-fluidity.md)
* [Did Resources for SSI - address ALL requirements via DIDs](./did-resources.md)
* [DID Torrent](./DID_torrent.md)
* [DID Traits](./did-traits.md)
* [Discovery Handshake](./discovery-handshake.md)
* [DKMS for SSI](./dkms-for-ssi.md)
* [Dynamic & Decentralized Reputation for the Web of Trust: What We Can Learn from the World of Sports, Tinder, and Netflix](dynamic-decentralized-reputation-web-of-trust.md)
* [Elision, Redaction, and Noncorrelation in Smart Documents](elision-redaction-correlation-smart-documents.md)
* [Enabling SSI for NFC, IoT and other smart devices](./Enabling%20SSI%20for%20NFC%2C%20IoT%20and%20other%20smart%20devices.md)
* [Enhancing DID Privacy through shared Credentials using Merkle trees of DIDs and Claims with multiple presentation proofs](./Enhancing_DID_Privacy_through_shared_Credentials.md)
* [Enhancing DIDComm messaging for mobile environments](./enhancing-didcomm-for-mobile-environments.md)
* [eSSIF-Lab: Towards a European SSI ecosystem](./eSSIF-Lab%20-%20Towards%20a%20European%20SSI%20ecosystem.md)
* [Generalizing Secure Scuttlebutt for Data Integrity](./ssb-di.md)
* [Identified communications - SSI and internet communications or internet communications and SSI](./SSI%20and%20internet%20communications%20or%20internet%20communications%20and%20SSI.md)
* [Identity and Trust in a Co-operative Ecosystem](./Identity_and_Trust_for_Coops.md)
* [Identity Bridge: Verifiable Credentials from European Digital IDs](./identity-bridge.md)
* [Identity Net: Building an identity net through self-authenticated data graphs](./identity-net.md)
* [Multi-dimensional reputation systems using Webs of Trust](./Multi-dimensional%20reputation%20systems%20using%20webs-of-trust.md)
* [On-Chain DIDs](./on-chain-dids.md)
* [Reducing Correlation: To What Degree is it Necessary?](./reducing-correlation.md)
* [Rendering Verifiable Credentials](./rendering-verifiable-credentials.md)
* [Revisiting Usefulness of Centralized System for Establishing Trust](./revisiting-usefulness-of-centrailzed-system.md)
* [Revocation and VC](./revocation-and-vc.md)
* [Self Custody Risk Analysis](./self-custody-risk-analysis.md)
* [Social Wallet Recovery](./social-wallet-recovery.md)
* [Societal impacts of SSI technologies](./societal-impacts.md)
* [Spendability of Currency](./spendability-of-currency.md)
* [SSI data generator](./data-generator.md)
* [Standardization Overview](./standardization-overview.md)
* [Trust Registries – Enhancing Interoperability and preventing Phishing/MITM Attacks](./Trust-Registries.md)
* [Trusted Crypto Asset Framework](./trusted-crypto-asset.md)
* [Unravelling Web of Trust](./UnravellingTrust.md)
* [Using MultiBase Anchors within a Personally-Issued Endorsement Credential to Corroborate Attributes in an Existing Issued Credential](./endorsements.md)
* [Validation - The Missing Link](./validation-the-missing-link.md)
* [Verifiable Credentials Holder Binding](./verifiable-credentials-holder-binding.md)
* [Verifier Universal Interface](./vui-primer.md)
* [Words Matter: A Rethink of Current SSI Terminology](./words-matter-a-rethink-of-current-terminology.md)
* [ZKPs with zkSNARKs in a DIDComm ecosystem](./zkp-with-zksnarks-in-a-didcomm-ecosystem.md)
* ... more ...

## RWOT10 Papers

You may also want to consult the papers from [RWOT10](https://github.com/WebOfTrustInfo/rwot10-buenosaires/blob/master/topics-and-advance-readings/README.md), as that design workshop was cancelled due to COVID.
