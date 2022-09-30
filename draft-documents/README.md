# RWOT11 Draft Documents

Thanks to everyone who contributed to RWOT11. The following are the papers that are currently in process:

## [**Composing Credentials via Links and Cryptographic Binding**](https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/draft-documents/composable-credentials.md)

> _Abstract:_ The Verifiable Credential ecosystem has encountered several use cases that require a third-party assertion, or an endorsement of an existing object (another VC, a PDF, a webpage, etc). Whether it is product reviews, endorsements of self-created credentials, provenance of academic paper reviews, or some other general purpose third party assertion, these use cases have several requirements in common. Each use case may also require a domain-specific set of fields.

> We propose a minimal format for connecting credentials that will allow each use case of 3rd party assertions to be represented as a set of LinkedClaims.

> Further, we propose to demonstrate the ability to compose several LinkedClaims into a single domain-specific credential, specifically a Verifiable Endorsement, that will satisfy the domain requirements of the likely users.

> This approach will enable rich shared datasets to inform trust decisions, while satisfying the requirements of domain-specific end users. If time permits a sample score can be built over the linked claim dataset.
 
## [**Credential Profile Comparison**](https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/draft-documents/credential-profile-comparison.md)

> _Abstract:_ The artifact created is a comparison matrix for the wide variety of credential formats and their related signing algorithms, revocation mechanisms, and key management systems (collectively referred to as credential profiles), and an application guideline for using the matrix to conduct own assessments of such profiles. The RWOT11 session continues the work kicked off in an IIWXXIV session in April 2022 and worked on offline afterwards. It is a second iteration of the overview of credentials, with validated attributes and categories and further content added. A discussion of the different credential profiles will follow later and is not subject of the work at RWOT11.

> The list contains commonly discussed profiles like W3C Verifiable Credentials, AnonCreds, ISO-standard Mobile Driving License (mDL) but also legacy technologies like X.509 for comparison.

## [**Data exchange agreements over OCA for an accessible, scalable and auditable data exchange ecosystem**](https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/draft-documents/data-exchange-agreements-with-oca.md)

> _Abstract:_ This paper is a collaborative project at the 11th Rebooting of Web of Trust (RWOT) workshop in The Hague in September 2022. We present the Data Exchange Agreement (DEXA) protocol suite that enables human-centric automated agreement handling for data exchange between a Data Source (DS) and a Data Using Service (DUS). It helps organisations to be transparent and legitimate in their data usage while leveraging data in a scalable manner as part of a data ecosystem. Furthermore, the DEXA protocol brings in the requisite trust and governance to establish a ubiquitous data exchange space while empowering individuals to be in control of their data. All organisations need to ensure that they are on the right side of the law (e.g. the GDPR) when consuming personal data (risk management) and to establish the digital trust needed for individuals to say yes to sharing their data.

> Using OCA (Overlay Capture Architecture) in DEXA ensures cross-border data exchange across multiple jurisdictions while addressing accessibility concerns.

> In our scenario, a healthcare provider in Sweden could leverage the protocol to publish the availability of their prescriptions, in Swedish, in a cross-border healthcare data space. A Pharmacy in Zurich could sign up to read the prescription in German and issue a generic medicine to Fredrik. The use of OCA enables language localisation and ensures Fredrik, who is visually impaired, can understand the Data Agreement presented by the Pharmacy during the transaction. All transactions are auditable, and Fredrik is issued a receipt with a warning in Swedish for the possible adverse effects of taking the medicine.

## [did:merkle](https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/draft-documents/did-merkle.md)

> _Abstract:_ One Time Merkle Proofs for less correlatable credentials ?

> One Time Revealable Credentials ?

> Group credentials offer an opportunity for privacy preserving verification of group membership. We want to issue the exact same VC to all members of a group so that each VC reveals no information about who is a member of the group. We propose to do this by issuing a VC with subject id of the merkle root of cryptographic identifiers controlled by various group members. Upon presentation of that VC to a Verifier, group membership can be verified by testing that the cryptographic id that signs the VP is in the merkle tree. We create a did:merkle and merkleProof proof type so that the VC is issued to did:merkle and the VP includes TWO proofs. One is the traditional tamper-evident signature. The second is the merkleProof. For additional correlation protection, the issuer may include multiple cryptographic ids for each recipient, allowing recipients to use different proofs with different verifiers. This solution is cryptosuite agnostic and does not depend on novel cryptography such as group signatures.

> NOTE: More about anti-correlation, or at least that its the two parts together (group membership and multiple proofs per member)

## [Identity Threats](https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/draft-documents/identity-threats.md)

> _Abstract:_ Decentralized identity solutions, such as DID methods, tend to be designed to protect against certain attacks, but the purpose of that design is not usually explicitly stated in any architectural description or threat documentation. In particular, some DID methods have costly on-chain requirements. We can today see that these DID methods were purposefully shaped, but it's not clear why such decisions were made. The purpose of this paper is to list attacks on DID methods so that we can better understand what threats a system might be vulnerable to (or not).

> Although we focused on specific DID methods, we believe these attack vectors are more general, even for systems not using DIDs. The goal is support engineers and developers who are developing decentralized identity solutions to safeguard their work and make it secure and compliant.

## [Is This DID Method Ready to be Endorsed?](https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/draft-documents/is-my-did-method-ready-to-endorse.md)

> _Abstract:_ How do we educate someone tasked with implementing a DID Method in an application?

> Deciding to implement or support a DID Method for a given application requires an evaluation of whether the DID Method reaches the level of a proper standard with support for the relevant features.

> The existing Rubric provides a number of criteria and metrics, however they cover a broad set of interests oriented towards a user of a DID Method. All stakeholders first have a narrower question of whether a DID Method is sufficiently well standardized along various axes.

> Additionally, certain kinds of DID methods are simply unsuitable for particular applications and usage patterns, whether it be because of regulations or technological requirements/restrictions. Non-domain-expert stakeholders of every kind would benefit from a simplified set of considerations and guidelines when choosing a set of DID Methods to support.

## [On-Chain identity verification design patterns](https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/draft-documents/on-chain-verifications.md)

> _Abstract:_ On August 8th, 2022, the US Department of Treasury brought regulation against a decentralized application (dApp) for the very first time, by bringing the liability for interactions with OFAC-sanctioned entities to ALL Eethereum wallets that interacted with the Tornando Cash on chain mixer.

> This is a once-in-a-lifetime opportunity to leverage on-chain digital identity as a way to anticipate the regulation trajectory and unlock adoption of decentralized applications (including decentralized finance) with sophisticated compliance and reporting/auditing strategies.

> In this paper we want to analyze different on-chain credential  / proof verification as part of a process for validating transactions involving digital assets (i.e. “DeFi transactions”).

> Our analysis includes solutions with different privacy strategies, ranging from on-chain tokenized identities (i.e. “Soul-Bbound Tokens”) to on-chain validation of Proofs derived from AanonCreds.
 
## [Rendering Verifiable Credentials](https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/draft-documents/rendering-vcs-snapshot-9-27-22.md)

> _Abstract:_ In the Verifiable Credentials ecosystem, wallets and verifiers have expressed a strong preference for consistent rendering mechanisms because they will simplify the implementation of applications that are safe and easy to use. Several specifications have proposed credential rendering methods for a specific set of use-cases, but no interoperable scheme has emerged across use-cases. In this paper, the authors survey existing methods and propose a unified data model for rendering hints, renderer descriptions, and security considerations to keep in mind when using them.
