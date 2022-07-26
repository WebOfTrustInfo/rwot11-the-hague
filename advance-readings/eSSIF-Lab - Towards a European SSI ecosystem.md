[eSSIF-Lab: Towards a European SSI ecosystem](./eSSIF-Lab - Towards a European SSI ecosystem.md)

   * by [Oskar van Deventer](mailto:oskar.vandeventer@tno.nl), TNO, Netherlands
   * Overview of the eSSIF-Lab SSI ecosystem
   * #eSSIF-Lab #SSI-ecosystem #Europe



This is a proposed collaborative paper to be completed at [RWOT 2022](https://rwot11.eventbrite.com/), Den Haag, Netherlands, 26-30 September. Advance reading: see [here](https://github.com/WebOfTrustInfo/rwot11-the-hague/tree/master/advance-readings).



# eSSIF-Lab: Towards a European SSI ecosystem

Oskar van Deventer (TNO), eSSIF-Lab subgrantees (to be invited)

## Summary

eSSIF-Lab is a 7 M€, three-year (2019-2022), European-Commission-funded program that has been sponsoring start-ups, SMEs and innovators to develop open-source SSI components, SSI products and SSI services. A total of 54 eSSIF-Lab subgrantees has developed a wide variety of SSI solutions, which have been  interop-tested with other eSSIF-Lab subgrantees and innovators outside the program, which have been contributed to standardisation in W3C, Aries, DIF, OIDC and other, and which have been commercially deployed in the European market. Many eSSIF-Lab subgrantees have managed to secure external investments, and a few have even been involved in mergers & acquisitions. Many of the eSSIF-Lab outputs are available in the form of well-documented open-source code, ready for deployment. This includes SSI wallet infrastructure, SDKs for SSI wallets, SSI-standards-compliant API libraries, tooling for SSI trust infrastructure, tooling for SSI-based mandating/delegation and several other. Other eSSIF-Lab outputs are commercial propositions including SSI applications for educational credentials, for the health sector, for e-government and other.

This RWOT paper provides a selection of impactful eSSIF-Lab subgrantee projects, and provides pointers how to download or use these results for your own SSI projects.

## 1. Introduction: SSI and eSSIF-Lab

Self-Sovereign Identity (SSI) does not need any introduction in the context of RWOT [1]. People are encouraged to read primers on SSI e.g. here: [2], [3], [4], [5].

eSSIF-Lab [6] (European Self-Sovereign-Identity-Framework Laboratory) is part of of the Next Generation Internet (NGI) programme, organised by the European Commission in the context of the Horizon 2020 Research and Innovation Actions [7] funding. eSSIF-Lab was partly modeled after the Silicon Valley Innovation Programme [8] (SVIP) of the American Deparment of Homeland Services. **<u>*< ... more about eSSIF-Lab, its consortium, its goverance, budgets, numbers, etcetera ... >*</u>** 

eSSIF-Lab booklet [9]

Relation with EBSI-ESSIF [10]

## 2. eSSIF-Lab subgrantee project results

**<u>*< ... To be discussed whether a further structuring is useful, e.g. one subsection for library projects, another for SSI wallets, etcetera ... >*</u>**

### 2.1 Automated data agreements by iGrant.io (Sweden)

The ADA project [11] builds a fully auditable digital infrastructure that enables sustainable use, reuse and exchange of personal data to enable advanced digitalisation enforced via Data Agreements. A Data Agreement records the conditions for an organisation to process personal data following privacy regulations (e.g. GDPR) captured as a signed receipt given to an individual and to organisations wishing to record their personal data processing. The receipt acts as evidence, demonstrates a higher level of accountability, and is based on standard schemas. The accountability is further enhanced by directly integrating the Data Agreement with the input from a risk assessment, e.g. Data Protection Impact Assessment.

Once created, the Data Agreement is integrated into SSI-based workflows, resulting in an easy-to-adopt and automated solution for data exchange, making every transaction trustworthy, auditable and immutable.

The Data Agreement specification is openly available [12] and implemented over DIDComm protocol, integrated into Aries and EBSI (European Blockchain Service Infrastructure) presentation exchanges. 

### 2.2 eSSIF-Lab subgrantee project SSI-NFC Bridge
  With self-sovereign identity - DIDs and VCs - we finally are able to add the identity and authentication layer that had been missing since the inception of the internet. At Gimly we are bridging the digital and physical worlds, leveraging SSI in combination with NFC capabilities of smartcards and mobile devices to bring trust and transparency back into our digital as well as physical interactions. 

Our aim is to enable self-sovereign identity for both online and offline identification, authorization, and access management, with a decreased dependency on the use of personal smartphones. Example use cases may include private health records, eID cards with eIDAS compliant signatures, eMobility, or enterprise employee authorisations, access management, and transactions.

The bridge is designed blockchain and did-method agnostic to allow for easy integration of SSI smartcards in any SSI solution. The smartcards hold an NFC microchip with an EAL6+ grade secure element for authentication and signing with their embedded DID and can be used for sovereign storage and selective disclosure of verifiable credentials. The first smartcards to be supported are Tangem made-for-blockchain NFC cards, and we are collaborating with Tangem on the release of a fully open sourced NFC chip preventing any vendor lock-in in future. In addition, the SSI-NFC firmware will also be available for licensing to be implemented in client's own existing smartcard provider.

### 2.3 eSSIF-Lab subgrantee project Trust-over-IP Trust Registry by Trinsic Europe Ltd. (England)
  The Trust Registry project provides an open-source, Trust-over-IP spec-compliant governance model to enable the easier bootstrapping of SSI ecosystems. The primary use case for a Trust Registry is to enable a governance authority to permission the rules of a given ecosystem--specifically, which issuers are authoritative for which kinds of credentials.
  Our work provides an extension to the Verifiable Credentials Data Model (VC). This extension is interoperable with existing processors of VCs in such a way that it doesn't deviate or break existing implementations, but allows systems that can understand Trust Registry types to interpret the data using this model.
  The architectural approach taken is microservice based, which means it's designed to be compatible with any SSI codebase that wants to encorporate governance. The repository is complete with quickstart tutorials, APIs, and other developer-friendly tooling to encourage adoption. 

### 2.4 eSSIF-Lab subgrantee project TRAIN (TRust mAnagement INfrastructure) by Fraunhofer IAO, Germany.
  TRAIN provides an open-source Trust Management Infrastructure that allows to verify the trustworthiness of involved parties in the SSI Ecosystem. e.g. is the issuer trustworthy (is it a real bank or just a fake bank).
  
TRAIN aims to add a Trust-Component to the ESSIF-Framework, which enables the discovery and verification of credential issuers, as well as the definition, consideration, and verification of eIDAS compliance (including LoAs) of involved parties. TRAIN provides a decentralized framework for the publication and querying of trust information. It makes use of the Internet Domain Name System (DNS) with its existing global infrastructure, organization, governance and security standards to achieve the trust discovery process. The trust list used by TRAIN also follows the ETSI standard by which interoperability across different trust infrastructures can be achieved.
  
An illustrative interoperability use case for the European Health Insurance Card (EHIC) has been realized and demonstrated with SICPA SA and Validated ID. The latest draft of OpenID Connect for Verifiable Presentations (OIDC4VC) contains informative implementation guidelines describing how issuers, holders and verifiers can utilise the TRAIN trust scheme approach. 

### 2.5 eSSIF-Lab subgrantee project ZeroTrustVC (Enabling Zero Trust architectures using OAuth2.0 and Verifiable Credentials) by AUEB, Greece
The project Enabling Zero Trust Architectures using OAuth2.0 and Verifiable Credentials (ZeroTrustVC) aims at providing tools for implementing Authentication and Authorization for HTTP-based resources. The project considers HTTP-based resources accessed through a web browser and its goal is to enable continuous user authentication and authorization, as required by the Zero Trust security principle. To this end, it leverages Verifiable Credentials to encode user capabilities and it specifies VC issuance and usage flows based on standard OAuth 2.0.

From a high-level perspective, ZeroTrustVC is an access control solution that relies on widely used standards, composed of a VC issuer, a VC verifier, and a Client module.

The VC issuer is an OAuth 2.0 authorization server extended with VC issuing capabilities. Issued VCs are encoded as JWT and signed using JWS, improving compatibility and integration with existing tools. ZeroTrustVC consider VCs that describe the capabilities of a client over a protected resource. Additionally, ZeroTrustVC VC issuer maintains a VC revocation list.

The VC verifier is an HTTPS proxy that intercepts the communication between a client and an HTTP(S)-based protected resource. The VC verifiers is able to verify the validity, the status, and the ownership of a VC. Additionally, the VC verifier acts as a policy enforcement point by validating whether or not a VC can be used for executing a particular request over a protected resource.

The client module is a VC wallet implemented as a browser extension, executed by a real world user that interacts with the VC issuer standard OAuth 2.0 flows. Additionally, the client module can transparently inject VCs and the appropriate proofs of possessions into HTTP requests towards protected resources.  

Open source tools for managing the lifecycle of VCs are available at the [project homepage](https://mm.aueb.gr/projects/zerotrustvc) [14]. 

### 2.6 eSSIF-Lab subgrantee project "Adding SSI to internet communications" by Bloqzone
One of the things people enjoy the most about the internet, is that it enables them to talk to others remotely almost without limit.
Unfortunately, remotely often means that parties are not sure who they are communicating with. 

Adding SSI to internet communications (SSIComms for short), resulting in seamless identified communications, is the solution to this problem. 

SSIComms makes use of two protocols: DIDComm, central to SSI, and SIP, equally central to internet comunications and an SSIComms session between Alice and Bob involves 4 major steps:

1. First, Alice and Bob start a SIP session, for instance by Alice calling Bob using the SIP protocol.
2. Then, after Bob answers, he and Alice establish a DIDComm connection by Bob sending Alice an out-of band-message. As a means of transport, Bob chooses the active SIP session between him and Alice, and sends Alice the message as an encrypted SIP message.
3. With the DIDComm connection in place, they can now use DIDComm to exchange credentials.
4. The credentials proven to be satisfactory, Bob and Alice continue their SIP session and exchange voice, video or text messages.

SSIComms differs from existing SSI/DIDComm based applications in that it focuses on internet communications sessions with both participants behind a firewall. Under these circumstances, DIDComm by itself does not suffice to add an identity layer.

### 2.7 eSSIF-Lab subgrantee project "SSI Java Libraries" by Danube Tech
Danube Tech has been working on open-source Java implementations of various decentralized identity
build blocks for several years.

This includes the following libraries:
[jsonld-common-java](https://github.com/decentralized-identity/jsonld-common-java),
[did-common-java](https://github.com/decentralized-identity/did-common-java),
[key-formats-java](https://github.com/danubetech/key-formats-java/),
[ld-signatures-java](https://github.com/weboftrustinfo/ld-signatures-java),
[verifiable-credentials-java](https://github.com/danubetech/verifiable-credentials-java),
[cborld-java](https://github.com/danubetech/cborld-java).

These libraries are being used by various SSI solution providers and
in DID/VC-based projects across the EU and beyond. For example, see the
[EBSI4Austria](https://medium.com/@markus.sabadello/report-from-ebsi4austria-b79c0ed8ab8d)
and [Transatlantic SSI Interop](https://medium.com/@markus.sabadello/transatlantic-ssi-interop-52bac6be8dfe) projects.

## 3. SSI standardisation and interop testing

< ... Further structuring to be discussed ... >

### 3.1 Data Agreement standards and Interop

The Data Agreement schema is standardised as part of ISO 27560 and driven via DIF (Decentralized Identity Foundation) Data Agreement WG [13]. The DIF workgroup will further investigate standardising the DID:mydata introduced as part of the Automated Data Agreement project by iGrant.io (Sweden).

### 3.2 Standard/interop YYY

### 3.3 Standard/interop ZZZ

## 4. Conclusions

## 5. References

[1] https://rwot11.eventbrite.com/ 

[2] [The Path to Self-Sovereign Identity (lifewithalacrity.com)](http://www.lifewithalacrity.com/2016/04/the-path-to-self-soverereign-identity.html)

[3] [Self-Sovereign Identity - the good, the bad and the ugly; May 2019 | TNO](https://blockchain.tno.nl/blog/self-sovereign-identity-the-good-the-bad-and-the-ugly/)

[4] [rwot11-the-hague/advance-readings at master · WebOfTrustInfo/rwot11-the-hague (github.com)](https://github.com/WebOfTrustInfo/rwot11-the-hague/tree/master/advance-readings)

[5] **<u>*< ... more SSI references ... >*</u>**

[6] [eSSIF-Lab | eSSIF-Lab: Help Shape a Safe and Secure Next Generation InternetT GENERATION INTERNET](https://essif-lab.eu/)

[7] [h2020-wp1820-annex-d-ria_en.pdf (europa.eu)](https://ec.europa.eu/research/participants/data/ref/h2020/other/wp/2018-2020/annexes/h2020-wp1820-annex-d-ria_en.pdf)

[8] [SVIP | Homeland Security (dhs.gov)](https://www.dhs.gov/science-and-technology/svip)

[9] [essif booklet 22 (essif-lab.eu)](https://essif-lab.eu/wp-content/uploads/2022/03/essif-booklet-22-1.pdf)

[10] [High-level scope (ESSIF) - EBSI Documentation - (europa.eu)](https://ec.europa.eu/digital-building-blocks/wikis/pages/viewpage.action?pageId=379913698)

[11] Automated Data Agreement by iGrant.io, avaialble at: https://essif-lab.eu/automated-data-agreements-to-simplify-ssi-work-flows-by-igrant-io/

[12] Automated Data Agreement specification, available at: https://github.com/decentralised-dataexchange/automated-data-agreements/blob/main/docs/data-agreement-specification.md

[13] DID Data Agreement WG: https://github.com/decentralized-identity/data-agreement

[14] ZeroTrustVC project homepage, available at https://mm.aueb.gr/projects/zerotrustvc
