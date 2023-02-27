# Rebooting the Web of Trust XI (Fall 2022) Final Papers

_This is a listing for the RWOT9 papers to date. [Several more](../draft-documents/README.md) are in process._

## [*Composing Credentials via LinkedClaims and Cryptographic Binding*](composable-credentials.pdf) [(Text)](composable-credentials.md)

#### by Phillip D. Long, Dmitri Zagidulin, and Golda Velez

> The Verifiable Credential (VC) ecosystem has encountered several use cases that require a third-party assertion, or a linked claim to an existing object (another VC, a PDF, a web page, etc). Whether it is product reviews, linked claims of self-created credentials, provenance of academic paper reviews, or some other general purpose third-party assertion, these use cases have several requirements in common. Each use case may also require a domain-specific set of fields.

> We propose a minimal format for connecting (and optionally cryptographically binding) credentials that will allow each use of third-party assertions to be represented as a set of LinkedClaims. Such a data set will enable verifiers to evaluate the credibility of claims, including those sourced from outside the Verifiable Credential ecosystem.

> Further, we propose to demonstrate the ability to compose several Verifiable Credentials into a single domain-specific credential using the LinkedClaim vocabulary that will satisfy the domain requirements of the likely users.

> This approach will enable rich shared datasets to inform trust decisions while satisfying the requirements of domain-specific end users. One of the intentions of LinkedClaims Verifiable Credentials is to give individuals the agency to make such claims about themselves and others on their own terms.

## [*Identifier Binding: defining the Core of Holder Binding*](identifier-binding.pdf) [(Text)](identifier-binding.md)

#### by Paul Bastian, Rieks Joosten, Zaïda Rivai, Oliver Terbu, Snorre Lothar von Gohren Edwin, Antonio Antonino, Nikos Fotiou, Stephen Curran, and Ahamed Azeem

> The [*W3C Verifiable Credentials Data Model(VCDM)*](https://www.w3.org/TR/vc-data-model/) specifies **Verifiable Credentials (VCs)**[^1] as a collection of **claims** that are **issued** by a single **party**, and **Verifiable Presentations (VPs)** as a collection of **claims** that a **holder** can construct from different **VCs** issued by different **parties**. Over the last year(s), various issues have been raised that revolve around what has been called 'holder binding'. The term 'holder binding' itself isn't clearly defined, and is in fact quite contentious. This paper seeks to come to grips with this discussion. Our first contribution is the specification of a terminology, which is intended to help readers understand what we mean to say without requiring them to make assumptions about such meanings (as is often the case in discussions about 'holder binding'). Our second contribution is an analysis of a (fictitious) use-case that suggests that **verifiers** typically do not need to know who the **holder** is (i.e. who has presented the **claims** to be **verified**). This analysis shows that **verifiers** need capabilities to (a) learn which **entity** is the **subject** of a particular **claim**, and (b) to know whether or not two **subject identifiers** refer to the same **entity** or to different **entities**. Also, they may need assurances regarding the **party** on whose behalf the **component** that has electronically presented the claims, has been using those capabilities. Our third contribution is a proposal for the syntax and semantics of a new property that can be used in (different parts of) **VCs**/**VPs**, that will provide **verifiers** with such capabilities.

## [*Linking Credentials with Data Exchange Agreements through Secured Inclusive Interfaces*](data-exchange-agreements-with-oca.pdf) [(Text)](data-exchange-agreements-with-oca.md)

#### by  Lal Chandran, Lotta Lundin, Fredrik Lindén,  Philippe Page,  Paul Knowles,  Víctor Martínez Jurado,  Andrew Slack

> On the need to link verifiable credentials with the right to use data in a secure, inclusive user interaction.

> In this collaborative work from RWOT11, we revisit the issue of patient data exchange in a setting requiring cross-border, multi jurisdiction, and inclusive access to all participants. A fundamental problem in developing large-scale real-world solutions based on verifiable credentials is keeping the simplicity of usage for individuals in different contexts without sacrificing security.

> We aim to highlight selected technical challenges and outline how the DEXA and OCA protocols contribute to scalable solutions.

## [*Taking out the CRUD: Five Fabulous DID Attacks*](taking-out-the-crud-five-fabulous-did-attacks.pdf) [(Text)](taking-out-the-crud-five-fabulous-did-attacks.md)
#### by Shannon Appelcline, Cihan Saglam, Kate Sills, Carsten Stöcker

> Decentralized identity solutions, such as DID methods, tend to be designed to protect against certain attacks, but the purpose of that design usually is not explicitly stated in any architectural description or threat documentation. In particular, some DID methods have costly on-chain requirements that must have had a reasoning behind their requirement. We can today see that these DID methods were purposefully shaped, but it’s not clear why such decisions were made. The purpose of this paper is to describe a few colorful attacks on DID methods so that we can better understand what threats a system might be vulnerable to.

> Although we derived the examples in this paper by examining current DID methods, we believe these attack vectors are more general, even for systems not using DIDs. The goal is to support engineers and developers who are developing decentralized identity solutions to safeguard their work and make it secure and compliant.

## [*Verifiable Issuers & Verifiers*](verifiable-issuers-and-verifiers.pdf) [(Text)](verifiable-issuers-and-verifiers.md)
#### by Manu Sporny, Oskar van Deventer, Isaac Henderson Johnson Jeyakumar, Shigeya Suzuki, Konstantin Tsabolov, Line Kofoed, Rieks Joostena

> Enabling anyone to share information about the Issuers and Verifiers for whom they assure trust

> This work focuses on how a party or its agent can decide whether or not to engage with a counterparty in a transaction. The purpose of this work is to enable the sharing of a list of Verifiable Issuers and Verifiers in a way that is useful to a particular transaction. A set of use cases provide examples where verification of an Issuer ("Is that diploma from a recognized university?") or Verifier ("Should the wallet block an unauthorized Verifier?") is needed. The studied prior art highlights various solutions to verify Issuers and Verifiers and identifies a lack of standards. Important contributions from this paper include a unified set of requirements, a data model, and multiple serializations of the data model --- including but not limited to Verifiable Credentials, DNSSEC, and blockchain-based serializations --- that could then be incubated and sent onto the standards track at global standards setting organizations.

