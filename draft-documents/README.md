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

## [Scalable anywise DIDComm](https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/draft-documents/scalable-anywise-didcomm.md)

> _Abstract:_ Currently DIDComm1 does not properly handle scalable multi-party well. This paper gives an overview of the current work that has been done in this field and proposes a new solution based on using a network of "repurposed" mediators with onion-like routing. The current work that has been done in this field includes the following: DRAFT Aries-rfc 0748: N-wise DID Exchange2, ThreadSync Protocol3, ThreadParticipant Protocol4 and Gossyp5. Our proposed solution is a mesh network of mediators who obfuscate the route and allow for a concealed participants list. The group will also share a common group key pair (public, private) which will be used for the end-to-end encryption. The mediators and their layered-encryption will use their own did:peer keypair. Another proposition we would like to add is a new type of service called: broadcaster. This broadcaster will be able to do heavy lifting for mobile agents in terms of networking and processing power. A single message can be sent to the broadcaster and it will broadcast the message further to the actual recipients.

## [Selective Correlation](https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/draft-documents/selective-correlation.md)

> _Abstract:_ The goal of this paper is to enable decision makers, particularly non-technical ones, to gain a nuanced grasp of correlation. We will explore the concept of selective correlation, introduce a threat model, and propose a framework within which policies such as data minimization can be successfully actualized. We will strive to do so in plain English, but with some rigor. This will enable readers of this paper to better understand correlation best practices, to adopt correct approaches for their use cases, and to assess techniques that enable these best practices.

## [A specification for ledger-agnostic AnonCreds](https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/draft-documents/specification-for-ledger-agnostic-anoncreds.md)

> _Abstract:_ AnonCreds are a novel means of providing digitally verifiable data that is privacy-preserving and tamper-proof (for SSI). Currently, AnonCreds are coupled to Hyperledger Indy, however the underlying cryptographic logic is based on the Hyperledger Ursa library and henceforth uncoupled to any specific ledger. Many real-world use-cases for SSI implementations come with using multiple and different types of ledgers for the same user domain. For instance, a country could use verifiable credentials based on ledger A for issuing a driving license and certificate of citizenship, whilst using ledger B for banking-related matters. The ability to anchor AnonCreds related objects (schemas, credential definitions, etc..) on theoretically any ledger, is the goal of this proposal. The outcome is an AnonCreds specification describing how to use AnonCreds in a ledger agnostic way, based on the current Hyperledger Indy implementation, with modifications/shortcomings that describe possible extensions and updates to the current speicfication (such as removing the binding to CL signatures, or the revocation scheme).

## [The Codependency of Trust & Community](https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/draft-documents/the-codependency-of-trust-and-community.md)

> _Abstract:_ In this paper for RWoT we propose a model of trust and community that draws on thinking in complementary disciplines such as Physics and Mathematics (Theory of Explanation), Biology (Autopoeisis) and Social Sciences (social systems). We offer a definition of trust by studying the way that it manifests between individuals and communities. We derive a conceptual model of trust by identifying key events between individuals that determine trust within a particular context and use the model to describe how larger societal structures can be built from the composition of individual trust.

## [Excerpting Known Issuer/Verifier Registers](https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/draft-documents/title-tbd-issuer-verifier-list.md)

> _Abstract:_ This work will focus on how a party or its agent can decide whether or not to engage with a counterparty in a transaction. This document first does a survey of prior art related to trust frameworks and technologies to collect the current state of the art. It then extracts requirements from each of these works. It discusses the work at two levels, technical solutions and governance. It then attempts to summarize a data model that can support the requirements. The paper then proposes multiple serializations of the data model, including but not limited to Verifiable Credentials, DNSSEC, and blockchain-based serializations, that could then be incubated and sent onto the standards track at global standards setting organizations.

## [W3C Verifiable Credentials Holder Binding Specification](https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/draft-documents/verfiable-credentials-holder-binding.md)

> _Abstract:_ The W3C Verifiable Credentials Data Model does not define how to bind the W3C Verifiable Credential to the W3C Verifiable Presentation, so that the Verifier can verify that the holder of the verifiable presentation is the rightful or intended holder of the verifiable credential. Verifying a verifiable presentation does not include verifying the binding between the verifiable credential subject and the verifiable presentation holder. There is no normative reference for any existing approach.

> For these reasons, this paper describes a mechanism and a data model that allows Holders and/or Issuers to indicate how the rightfulness of the presentment can be verified at the time of presentment. Binding multiple Verifiable Credentials to a Holder should be possible. The W3C Verifiable Credentials Data Model 1.1 specification which is essentially equivalent to no guidance on the Holder Binding is provided. This mechanism is fully backward compatible with existing verifiable credentials and verifiable presentations. This paper does not mandate a specific form of holder binding or W3C Verifiable Credential proof type or format. Instead it provides a framework for Issuers, Holders and Verifiers to provide guidance on how Holder Binding can be checked deterministically according to their intentions.

## [Composable Credentials](https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/draft-documents/verifiable-endorsements-from-linked-claims.md)

> _Abstract:_ The Verifiable Credential ecosystem has encountered several use cases that require a third-party assertion, or an endorsement of an existing object (another VC, a PDF, a webpage, etc). Whether it is product reviews, endorsements of self-created credentials, academic paper reviews, or some other general purpose third party assertion, these use cases have several requirements in common. Each use case may also require a domain-specific set of fields.

> We propose a minimal format for Linked Claims that will allow each use case of 3rd party assertions to be represented as a set of LinkedClaims.

> Further, we propose to demonstrate the ability to compose several LinkedClaims into a single domain-specific credential, specifically a Verifiable Endorsement, that will satisfy the domain requirements of the likely users.

> This approach will enable rich shared datasets to inform trust decisions, while satisfying the requirements of domain-specific end users. If time permits a sample score can be built over the linked claim dataset.
