# RWOT11: A credential profile comparison matrix to facilitate technical and non-technical decision making

## Authors
Andre Kudra*,
Torsten Lodderstedt,
Paul Bastian,
Mirko Mollik,
Maaike van Leuken,
Caspar Roelofs

## Note

The draft paper has been [moved to a new repository](https://github.com/vcstuff/credential-profile-comparison/blob/main/credential-profile-comparison.md), to allow anyone to open PRs and issues for edits, suggestions, questions or any other feedback.
## Abstract
In this paper, a *comparison matrix* for the wide variety of credential formats - such as [W3C Verifiable Credentials](https://w3c.github.io/vc-data-model/), [AnonCreds](https://anoncreds-wg.github.io/anoncreds-spec/), ISO-standard [Mobile Driving License (mDL)](https://www.iso.org/standard/69084.html) - and the various related signing algorithms, revocation mechanisms, and key management systems (collectively referred to as **credential profiles**) is introduced. The [credential profile comparison matrix](https://docs.google.com/spreadsheets/d/1Z4cYfjbbE-rABcfC-xab8miocKLomivYMUFibOh9BVo) is a living document that serves as an accessible resource for an in-depth evaluation of the technical requirements and their technical and non-technical implications for different use-cases and objectives. This paper introduces the rationale behind this matrix, the various properties that are included in the matrix and their definitions, and serves as an application guide on how to use the matrix for more informed technical and non-technical discussions and decision making.

This work is the outcome of a collaborative writing session during RWOT11 in September 2022, and continues the work kicked off in an IIWXXIV session in April 2022 and worked on offline afterwards. The work should be considered an iterative process, with the matrix being a living document that will require continuous updating while facilitating discussion among technical and non-technical experts.



## Keywords
Verifiable Credentials, Credential Format, Credential Profile, Signing Algorithm, Revocation Mechanism, Key Management, SSI Components, ToIP Layer 3, Comparison Matrix, Anoncreds, mDl, Zero Knowledge Proofs




## Introduction
There is an increasing agreement among technical experts as well as industry leaders and governmental agencies and regulators that Verifiable Credentials (VCs) are needed and a most useful means to enable broad digitalization. VCs allow for moving around data between parties under full control of data subjects securely and are increasingly discussed and implemented in both private and public industries.

Especially among technical experts, there appears to be a shared understanding of the advantages and disadvantages of various types of VCs. However, where technical specifications oftentimes refer to these VCs by a single common denomination, such as AnonCreds or W3C JSON-LD VC, a lot of technical and non-technical underpinnings, assumptions, and prerequisites remain inexplicit. 

So even among technical experts, discussions and technical decision-making often take place without a shared understanding of the full technical feature set and requirements underpinning those technical decisions. Without making these underpinnings explicit, such discussions can remain restricted and unable to cross technological and philosophical paradigms. This is problematic also for less technical stakeholders, such as business innovators, industry leaders or governmental institutions and regulators interested in VCs, who rely on technical expert guidence for their own strategic decision making. Thus, there is a need for accessible resources providing comprehensive definitions and in-depth comparisons of the wide variety of VCs and their underpinnings that can help in both technical and non-technical discussions and decision making. 

In this paper, we introduce the concept of *credential profiles* to acknowledge that VCs are used in a wide variety of configurations that include different credential formats, signing algorithms, revocation mechanisms, and key management systems. By comparing these profiles in a *credential profile matrix*, we provide an accessible resource for an in-depth evaluation of the technical requirements and their technical and non-technical implications for different use-cases and objectives.

As such, the matrix can serve as an tool to fulfill three functions for innovators, industry, developers, security researchers, and in general people that want to use credentials in their use cases:

1. an *education function*, i.e. it is a means for getting a better understanding of credentials and a wide variety of inherent aspects, some of them highly technical, others business and application related, and;
2. a *discussion facilitation function*, i.e. a concise and comprehensive repository of facts about credentials allowing and facilitating an objective comparison and discussion, and;
3. a *decision support function*, i.e. a tool for comparing properties and finding the right approach for a specific use case in question.


In this paper, we aim to describe the rationale behind the credential profile matrix, how it was constructed, and how it is intended to facilitate informed technical and non-technical decision making. This [introduction]() highlighted the need for a deeper and more accessible analysis of the various credential types and their technological underpinnings, requirements and implementations. In the [methodological section](#Methodology) section, we will briefly outline the process in constructing the profile comparison matrix and the methodological choices that were made in defining the targeted stakeholders. In the [results section](#Results), we will summarize the properties that have been included in the profile comparison matrix and their definitions. Finally, in the [discussion](#Discussion) we will highlight several preliminary lessons learned and outline a path to move this initiative forward.

## Methodology
For the creation of the credential profile matrix, a group of domain experts gathered first at the Internet Identity Workshop in its 34th incarnation (IIWXXIV) in Mountain View in April 2022. They kicked off with listing to experts for different VC types and formats, starting to gather data in a structured way, to ultimately be able to compare them in defined categories. This lead to a definition for credential profile: a configuration the credential format, signing algorithm, revocation algorithm and key management. These properties are then further drilled down, e.g. looking at technical traits like selective disclosure, crypto agility, or hardware support, and adoption criteria like standardization, technology readiness level, or implementation support. 

For example, what is typically refered to as AnonCreds resolves to the credential profile "AnonCreds + CL + Indy Revocation + did:indy + link secrets".

The work of the expert group has continued after the event in dedicated working sessions. At RWOT11 in September 2022 was used to work on both matrix in structure and context and the accompanying paper. For completeness and correctness, the comparison matrix will be validated within the SSI community. This implies that this application guideline is a living document, as we might encounter more interesting properties while validating the comparison matrix.

### Stakeholder Selection
The comparison matrix is meant to provide value to various stakeholder groups. The specific target groups and what benefit they will be able to draw from it are discussed below.
* Community experts. Thought leaders of the identity and trust services community get together to share their expert knowledge, collect and preserve it in a joint repository and entertain a discussion around it.
* Technology innovators. Those who are able and willing to follow the leading edge of the verifiable credential space can take more than a gut-based decision which technology to deploy in their innovation.
* Industry leaders. Decision takers on executive level who have a technical background and interested in the verifiable credential space can judge the relevance for their industry or business domain.
* Policymakers and regulators. Decisionmakers and their technically capable advisors can evaluate possible technologies and the implications of their implementation for their governmental use cases and mandates.
* Software developers. Highly technical audiences can dive deep into particular aspects of verifiable credentials and understand which properties they need to include in the application software they are creating.
* Security researchers. Security-oriented audiences can find out details of security mechanisms and cryptographic procedures in a credential profile, which is relevant for independent vetting of verifiable credentials.
* Others! Anyone considering deploying verifiable credentials in their use cases will gain rich insights into the matter and benefit from the expertise brought in by the content contributors and expert discussion outcomes.

### Scope
In the comparison matrix and this application guideline, with credential we mean digital credentials. Physical credentials are out of scope. The credential profile should also only include the most common credential profiles as we are making the comparison matrix. 

Our focus is on open source solutions, such that when conclusions based on the comparison matrix are made, it can also actually be used.

We only consider the properties of underlying technologies directly relevant to the credential profile and what those properties mean for the properties of the credential profile. Based on this criterium, we place exchange protocols out of scope, including the possibility for offline verification of credentials, as this is a property emerging from the exchange protocol. A property can also manifest itself on different levels of the ToIP technology stack, or on a governance level. In the comparison matrix, only the property on the credential profile level are considered.

> [To be discussed: add a definition/overview of he different aspects, e.g format, signing algorthim, ...?](/AqZvZR3rRcGg02oMrtFNaw)

The credential format and the signature algorithm are in scope, as the choice in these technologies directly impact the properties of the credential profile.
> [To be discussed: is revocation and key management in scope?](/AqZvZR3rRcGg02oMrtFNaw)


## Results
The [credential profile comparison matrix](https://docs.google.com/spreadsheets/d/1Z4cYfjbbE-rABcfC-xab8miocKLomivYMUFibOh9BVo) is maintained as a living spreadsheat in google sheets. In the following sections we will describe the properties in the comparison matrix. Some properties are present in various tables and will be discussed first.

### Common Properties
<!--explain why some properties emerge from signature/revoation algo-->
Various properties are applicable to different tables in the matrix. The properties will be discussed in the following sections.

#### Intellectual Property Rights
Information on the status of patents and knowledge of possible IP rights are important for the adoption of new technologies. The document lists the known status of existing or expired patents or links to the IPR Policies that were in effect for the creation of standards and specifications. The existence of IPR policies however does not guarantee the non-existence of patents from parties that were not involved in the process.

#### Specification

Specifications are essential for interoperability and security assessments. Whenever specifications are publicly available then a link should be provided.

#### Standardization
The standardization column describes under which standardization body 
and which working group the technology is standardized. It also described what the status of the standard is or which standards track is intended for the future of emerging technologies.

#### Implementation Support
For developers it is important to know to what extent the technology has been implemented. Therefore information is provided on which or how many software libraries are available. 

#### Technology Readiness Level

The Technology Readiness Level (TRL) is a measurement for the maturity of a technology developed by NASA. The values range from 1 to 9 with increasing values meaning increased maturity. In short these levels describe:
 - TRL 1: scientific research is beginning and those results are being translated into future research and development
 - TRL 2: basic principles have been studied and practical applications can be applied to those initial findings, little to no experimental proof of concept for the technology
 - TRL 3 : active research and design begin, often a proof-of-concept model is constructed
 - TRL 4 : proof-of-concept technology is ready, multiple component pieces are tested with one another
 - TRL 5 : technology is identified as a breadboard technology and must undergo more rigorous testing
 - TRL 6 : technology has a fully functional prototype or representational model
 - TRL 7 : technology requires that the working model or prototype be demonstrated in a space environment
 - TRL 8 : technology has been tested and "flight qualified" and it's ready for implementation into an already existing technology or technology system
 - TRL 9 : technology has been "flight proven" during a successful mission

More information on TRL can be found [here](https://www.nasa.gov/directorates/heo/scan/engineering/technology/technology_readiness_level).

The TRL of various technologies in the matrix (credential format, signing algorithm) are given and are based on the implementation support for that technology.

> [Check whether there are more criteria to determine the TRL:](/eCQxIbz4SsmIybwkDtOKCQ) 



### Properties of Credential Format
Apart form the common properties, the matrix provides information for the credential format on selective disclosure, predicates and crypto-agility. These properties will be described in the following sections.

#### Selective Disclosure
Selective disclosure allows a holder to present a subset of the attributes of the credential issued by the issuer. This minimizes the amount of the holder's information that is shared with the issuer. For example, the government issues a passport credential to Alice. The passport includes a variety of attributes, such as Alice's first name, last name, birthdate, social security number, et cetera. When Alice want to buy alcohol at the supermarket, she has to prove to the supermarket that she is of legal drinking age ($18+$) to buy alcohol. In the classical setting where Alice shows her passport to the supermarket, the supermarket sees all the attributes on her passport, even though they just need her birthdate. Using SSI with selective disclosure, she can simply present her birthdate with which the supermarket can verify that she is over $18$.

Selective disclosure can be achieved through the use of a signature algorithm that supports selective disclosure, such as BBS+ and CL signatures. Selective disclosure can also be achieved through governance, namely a community can agree on signing each attribute seperately, such that each attribute can also be presented seperately. As mentioned before, in our matrix we only look at choices on credential profile level, hence we only look at whether selective disclosure is achieved through the signature algorithm.

#### Predicates

Predicates allow the holder to further decrease the amount of information shared with the holder. Predicates check a value against a certain condition, resulting in true or false. Recall the example of Alice wanting to buy alcohol in the supermarket. Alice can prove that she is older than 18 using the predicate _age_ $\geq 18$. As Alice's age is $20$, the predicate $20 \geq 20$ is true. This way Alice can prove that she is allowed to buy alcohol without revealing her birthdate or even her age. 

Just like selective disclosure, predicates can be created on various levels. On a governance level, the issuer could issue common predicates to holders, such as $18+$ and $65+$. In the matrix, we only consider predicates through the capability of performing Zero-Knowledge Proofs in the credential profile. 

More information about predicates and zero-Knowledge-Proofs can be found [here](https://medium.com/51nodes/selectively-disclosed-verifiable-credentials-79a236b81ee2).

#### Crypto Agility
To support long term security the cryptographic algorithms that are used for encrypting, signing and hashing should be updatable without lossing features. Crypto agility could mean
- to increase the amount of bits for the keys
- to replace the algorithm with a new one 
It is difficult to predict the time when the algorithms have to updated. Typical scenarios are:
- the algorithm is broken and the security is suddenly lost
- the amount of computation power is high enough to perform a brute force attack in an acceptable amount of time
- there are faster algorithms that make the process more efficient without loosing features or lowering the security level

A relevant source is the recommendation of the German BSI(Federal Office for Information Security). They have published a [technical guideline for recommendations and key lengths](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/TechGuidelines/TG02102/BSI-TR-02102-1.pdf?__blob=publicationFile&v=4) listing the algorithms and parameters to use. It has to be mentioned that this is only a recommendation and not a direct law.

#### Encoding Scheme
There are various ways to encode the information within the credential, such as JSON, CBOR, Go Structs, etc.

#### Rich Schemas / Semantics
Rich schemas are hierarchically composable graph-based representations of complex data.

##### Security Considerations
When referencing to an external semantics like a json schema there is a risk of monitoring the usage of a credential:

The host provider is able to analyse the requests for the resource and find similarities (with information like the user agent and IP addresse they can find out which type of credentials are from one holder since verifier and issuer are normally using cloud systems)

When the issuer is also hosting the schema for its' credentials it is able to add a unique identifier to each new credential. This added tracking information allows the issuer to track the usage of a unique credential like
```
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://www.example.com/credentials/examples/v1.NSxma92am2s8wnnxz8"
  ],
```
where `NSxma92am2s8wnnxz8` is the unique identifier for a credential that is used for tracking.

### Properties of Signature Algorithm
Apart form the common properties, the matrix provides information for the signature algorithm on hardware support and unlinkability. These properties will be described in the following sections.

#### Recognition by Government Organizations

For regulated usecases, the national regulation agencies provide a list of recommended and accepted cryptographic algorithms, e.g. BSI TR-2102, NIST-xxx? This property describes whether the designated signature algorithm is recommended by national government agencies.

#### Hardware Support

Hardware support is required for regulated and highsecurity usecases to prevent credential/key duplication and theft. Existing hardware stores to sign inside the smartphones are Trusted Execution Environments, SecureEncalves, SecureElements and eUICCs, external authenticators and more. In the backend HSMs or TPMs can be used by issuers or Cloud-Wallets to secure the keys. The hardware-backed crypto processors often support only a limited set of established signature algorithms, therefore the use of modern cyrptography algorithms is limited for these use cases.

#### Unlinkability

Unlinkability is the property that an attacker cannot distinguish whether two or more items withinin a system (comprising these and possibly other items) are related or not. Within an identity ecosystem this applies for example that one verifier can link two credentials of an holder, two selective disclosures of the same credential or whether two colluding verifiers can link two seperate presentations of the same credential. This excludes the fact that linkability can also happen by the reavealed attributes themselves or unlinkability achieved by the infrastructure, e.g. just-in-time issuance.

#### Post-Quantum Security
With the computing power of quantum computers advancing, we need to think about post-quantum security with regard to SSI. Using our current signature algorithms, it allows attackers in the future after quantum computers have become computationally efficient enough to issue themselves credentials like they are issued right now. So Eve can issuer herself a university degree years from now, making it look like the credential was issued in 2022 by her university, as she can easily create the signature using a quantum computer.

In the comparison matrix, with regard to cryptography, we discuss signatures and their properties: selective disclosure and predicates. Currently, there are no common credential profiles that use signature algorithms that are post-quantum safe. NIST has recently announced their choice in [post-quantum safe signature algorithms](https://csrc.nist.gov/projects/pqc-dig-sig). The question is whether with these algorithms selective disclosure and predicates can still be provided. Predicates can still be achieved through post-quantum safe zero-knowledge proofs, such as zk-STARK and Aurora. For selective disclosure, it is not clear yet whether it can still be achieved through the post-quantum safe signature algorithm.


#### Performance

## Discussion
### notes, outcomes
The matrix sparked a deep discussion on existing revocation mechanisms and their limitations, potential attacks, and ways to resolve these issues.

Future work --> For technical decision makers and explorers, it would be good to be able to also find out whether certain combinations are not possible (and why). In the future it is possible to write a programm that allows to generate all possibilities.

### Objectivity and Subjectivity

Objective and subjective aspects are in the matrix --> try to be as objective as possible, where it becomes more subjective e.g. how complex the implementation is, we will give examples.


## Notes
### To Dos

TODO: need to streamline the use of *credentials* versus *verifiable credentials* across the paper and the matrix

TODO: add a definition/overview of the different properties of the profiles in the [scope](##Scope) section: credential format, signing algorthim, revocation mechanisms, key management systems.

TODO: revisit the **key management** property. There are now categories included that are not on the same level. E.g. a X.509 certificate and did:ion may both say something *about* key management, but not at the same level. A X.509 certificate is used to bind a public key to other attributes of the certificate holder. That is typically used establish trust in the certificate holder. 
Proposal: add another category for trust management. Examples include X.509, ETSi Trusted Lists, TRAIN.

TODO: Need to include information on existing libraries, SDKs for different programming languages and frameworks. Maybe at the top level, when selecting a credential profile to see whether there are existing libraries/SDKs -> Torsten

TODO: Just because the credential format supports crypto agility, it does not mean that all functions are still supported (JSON-LD with BBS+ signatures supports selective disclosure, but JSON-LD and JWT-VC do not. It would when selective disclosure is done via. hash-trees that are independant from the signature algorithm, etc) 

TODO: credential format: supporting of multi-signature (adding a list of signatures to a claim. maybe used as issuer where multiple entitites have to sign)

TODO: mixing up in the revocation list, add the recovation type (accumulator based, bitstring based). Describe how the expires date can be used to make it more secure

TODO: traceability when using json ld when hosting the json schema including a unique identitifier in each credential.

TODO: add solution strategies for some of the credential format limitations (e.g. hardware binding and AC, unlinkability and SD-JWTs, selective disclosure and JWTs)

TODO: add IRMA to credential profiles

TODO: add source of credential profile: where is this profile used? (e.g. wallet)
 

### Done

TODO: Should we add a new column for encoding at I15? Relevant since json, json-ld or cbor (https://www.w3.org/TR/vc-tdata-model/#syntaxes)

## Archive

<!-- ## Purpose: The reason for this artifact.
The work result is important because it allows a fact-based, more objective discussion of different credential profiles. There are multiple specifications of credentials out there with their strengths and disadvantages. Depending on the use case there are different demands and the comparison matrix can help to make the right credential profile decision.<!-- ## Audience & Impact: Beneficiaries of the work.  It supplies an assessment tool to help innovators, industry, developers, security researchers, and in general people that want to use credentials in their use cases:
1. Explore and understand the technical landscape;
2. Explore technical opportunities and challenges;
3. Make informed and explicit technical and use case design choices. -->



<!--## Creative Brief
Questions:
* Who's your audience?
* What change in their behavior do you want to induce? (Call to Action)
* What are the key points you're going to include?
The artifact's features make it interesting for various stakeholder groups. The specific target groups that have been considered when the artifact was created and what benefit they will be able to draw from it are discussed in the following: 
* Community experts. Thought leaders of the identity and trust services community get together to share their expert knowledge, collect and preserve it in a joint repository and entertain a discussion around it.
* Technology innovators. Those who are able and willing to follow the leading edge of the verifiable credential space can take more than a gut-based decision which technology to deploy in their innovation.
* Industry leaders. Decision takers on executive level who have a technical background and interested in the verifiable credential space can judge the relevance for their industry or business domain.
* Policymakers and regulators. Decisionmakers and their technically capable advisors can evaluate possible technologies and the implications of their implementation for their governmental use cases and mandates.
* Software developers. Highly technical audiences can dive deep into particular aspects of verifiable credentials and understand which properties they need to include in the application software they are creating.
* Security researchers. Security-oriented audiences can find out details of security mechanisms and cryptographic procedures in a credential profile, which is relevant for independent vetting of verifiable credentials.
* Others! Anyone considering deploying verifiable credentials in their use cases will gain rich insights into the matter and benefit from the expertise brought in by the content contributors and expert discussion outcomes.


As a summary, the artifact has
* an *education function*, i.e. it is a means for getting a better understanding of credentials and a wide variety of inherent aspects, some of them highly technical, others business and application related, and
* a *discussion facilitation function*, i.e. a concise and comprehensive repository of facts about credentials allowing and facilitating an objective comparison and discussion, and 
* a *decision support function*, i.e. a tool for comparing properties and finding the right approach for a specific use case in question.-->
 
<!--## Links
Google table with comparison matrix: https://docs.google.com/spreadsheets/d/1Z4cYfjbbE-rABcfC-xab8miocKLomivYMUFibOh9BVo-->
