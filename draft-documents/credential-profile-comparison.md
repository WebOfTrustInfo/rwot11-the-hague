# RWOT11 Credential Profile Comparison

<!-- Task: Create an abstract
* A self-contained text, not an exceprt from the paper
* Be fully understandable on its own
* Reflect the structure of your larger work -->

<!-- ## Artifact: The targeted outcome.  -->
## Abstract
The artifact created is a *comparison matrix* for the wide variety of credential formats and their related signing algorithms, revocation mechanisms, and key management systems (collectively referred to as **credential profiles**), and an *application guideline* for using the matrix to conduct own assessments of such profiles. The RWOT11 session continues the work kicked off in an IIWXXIV session in April 2022 and worked on offline afterwards. It is a second iteration of the overview of credentials, with validated attributes and categories and further content added. A discussion of the different credential profiles will follow later and is not subject of the work at RWOT11.

The list contains commonly discussed profiles like [W3C Verifiable Credentials](https://w3c.github.io/vc-data-model/), [AnonCreds](https://anoncreds-wg.github.io/anoncreds-spec/), ISO-standard [Mobile Driving License (mDL)](https://www.iso.org/standard/69084.html) but also legacy technologies like X.509 for comparison.


<!-- ## Purpose: The reason for this artifact.
The work result is important because it allows a fact-based, more objective discussion of different credential profiles. There are multiple specifications of credentials out there with their strengths and disadvantages. Depending on the use case there are different demands and the comparison matrix can help to make the right credential profile decision.<!-- ## Audience & Impact: Beneficiaries of the work.  It supplies an assessment tool to help innovators, industry, developers, security researchers, and in general people that want to use credentials in their use cases:
1. Explore and understand the technical landscape;
2. Explore technical opportunities and challenges;
3. Make informed and explicit technical and use case design choices. -->



## Creative Brief
<!-- Creative Brief Questions:
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
* Others! Anyone considering deploying verifiable credentials in their use cases will gain rich insights into the matter and benefit from the expertise brought in by the content contributors and expert discussion outcomes. -->


As a summary, the artifact has
* an *education function*, i.e. it is a means for getting a better understanding of credentials and a wide variety of inherent aspects, some of them highly technical, others business and application related, and
* a *discussion facilitation function*, i.e. a concise and comprehensive repository of facts about credentials allowing and facilitating an objective comparison and discussion, and 
* a *decision support function*, i.e. a tool for comparing properties and finding the right approach for a specific use case in question.
 


## Keywords
Verifiable Credentials, Credential Format, Signing Algorithm, Revocation Mechanism, Key Management, SSI Components, ToIP Layer 3, Comparison Matrix, Anoncreds, mDl, Zero Knowledge Proofs

## Links
Google table with comparison matrix: https://docs.google.com/spreadsheets/d/1Z4cYfjbbE-rABcfC-xab8miocKLomivYMUFibOh9BVo



## To Dos

TODO: Need to include information on existing libraries, SDKs for different programming languages and frameworks. Maybe at the toplevel, when selecting a credential profile to see whether there are existing libraries/SDKs

TODO: Just because the credential format supports crypto agility, it does not mean that all functions are still supported (JSON-LD with BBS+ signatures supports selective disclosure, but JSON-LD and JWT-VC do not. It would when selective disclosure is done via. hash-trees that are independant from the signature algorithm, etc) 

TODO: credential format: supporting of multi-signature (adding a list of signatures to a claim. maybe used as issuer where multiple entitites have to sign)

TODO: mixing up in the revocation list, add the recovation type (accumulator based, bitstring based). Describe how the expires date can be used to make it more secure

TODO: traceability when using json ld when hosting the json schema including a unique identitifier in each credential.

TODO: add solution strategies for some of the credential format limitations (e.g. hardware binding and AC, unlinkability and SD-JWTs, selective disclosure and JWTs)

TODO: add IRMA to credential profiles

TODO: add source of credential profile: where is this profile used? (e.g. wallet)
 

## Done

TODO: Should we add a new column for encoding at I15? Relevant since json, json-ld or cbor (https://www.w3.org/TR/vc-tdata-model/#syntaxes)

# Introduction
## Background, problem setting
There is an increasing agreement among technical experts as well as industry leaders and governmental agencies and regulators that Verifiable Credentials (VCs) are needed and a most useful means to enable broad digitalization. VCs allow moving around data between parties under full control of data subjects. Hence they have arrived in the mainstream discussion and practical application.

Especially among technical experts, there appears to be a shared understanding of the advantages and disadvantages of various types of VCs. However, where technical specifications oftentimes refer to these VCs by a single common denomination, such as AnonCreds or W3C JSON-LD VC, a lot of technical and non-technical underpinnings, assumptions, and prerequisites remain inexplicit. So even among technicale experts, discussions and technical decision-making often take place without a shared understanding of the full technical feature set and requirements underpinning those technical decisions. Without making these underpinnings explicit, such discussions can remain restricted and unable to cross technological and philosophical paradigms. This is problematic also for less technical stakeholders, such as business innovators, industry leaders or governmental institutions and regulators interested in VCs, who rely on technical expert guidence for their own strategic decision making. 



## Objective
<!-- needs rewording-->
The work result is important because it allows a fact-based, more objective discussion of different credential profiles. There are multiple specifications of credentials out there with their strengths and disadvantages. Depending on the use case there are different demands and the comparison matrix can help to make the right credential profile decision.<!-- ## Audience & Impact: Beneficiaries of the work. --> It supplies an assessment tool to help innovators, industry, developers, security researchers, and in general people that want to use credentials in their use cases:
1. Explore and understand the technical landscape;
2. Explore technical opportunities and challenges;
3. Make informed and explicit technical and use case design choices.

As a summary, the artifact has
* an *education function*, i.e. it is a means for getting a better understanding of credentials and a wide variety of inherent aspects, some of them highly technical, others business and application related, and
* a *discussion facilitation function*, i.e. a concise and comprehensive repository of facts about credentials allowing and facilitating an objective comparison and discussion, and 
* a *decision support function*, i.e. a tool for comparing properties and finding the right approach for a specific use case in question.

This document is an application guideline on the
[comparison matrix](https://docs.google.com/spreadsheets/d/1Z4cYfjbbE-rABcfC-xab8miocKLomivYMUFibOh9BVo). 

## Structure of the Application Guideline
In the introduction, we have summarized the need for a deeper and more accessible analysis of the various credential types and their technological underpinnings, requirements and implementations. In the follow section, we will briefly outline the methodological choices that were made in defining the target audience, their needs, and the inclusion and exclusion of variables in the the comparison matrix. Here, we also summarise the included variables and their definitions. Finally, in the discussion we will highlight several preliminary lessons learned and outline a path to move this initiative forward.



# Methodology
The artifact's features make it interesting for various stakeholder groups. The specific target groups that have been considered when the artifact was created and what benefit they will be able to draw from it are discussed in the following: 
* Community experts. Thought leaders of the identity and trust services community get together to share their expert knowledge, collect and preserve it in a joint repository and entertain a discussion around it.
* Technology innovators. Those who are able and willing to follow the leading edge of the verifiable credential space can take more than a gut-based decision which technology to deploy in their innovation.
* Industry leaders. Decision takers on executive level who have a technical background and interested in the verifiable credential space can judge the relevance for their industry or business domain.
* Policymakers and regulators. Decisionmakers and their technically capable advisors can evaluate possible technologies and the implications of their implementation for their governmental use cases and mandates.
* Software developers. Highly technical audiences can dive deep into particular aspects of verifiable credentials and understand which properties they need to include in the application software they are creating.
* Security researchers. Security-oriented audiences can find out details of security mechanisms and cryptographic procedures in a credential profile, which is relevant for independent vetting of verifiable credentials.
* Others! Anyone considering deploying verifiable credentials in their use cases will gain rich insights into the matter and benefit from the expertise brought in by the content contributors and expert discussion outcomes.
What is credential profile? Combination of ...

We should mention that we only looking at open source algorithms/techniques etc. so everyone is able to use it.

Objective and subjective aspects are in the matrix.

The credential profile should only include the most used right now. For technical decision makers and explorers, it would be good to be able to also find out whether certain combinations are not possible (and why). In the future it is possible to write a programm that allows to generate all possibilities.

ongoing work, living document


## Scope
In the comparison matrix and this application guideline, with credential we mean digital credentials. Physical credentials are out of scope.

We only consider the properties of underlying technologies directly relevant to the credential profile and what those properties mean for the properties of the credential profile. Based on this criterium, we place exchange protocols out of scope, including the possibility for offline verification of credentials, as this is a property emerging from the exchange protocol. A properties can also manifest itself on different levels of the ToIP technology stack, or on a governance level. In the comparison matrix, only the property on the credential profile level are considered.

The credential format and the signature algorithm are in scope, as the choice in these technologies directly impact the properties of the credential profile.
> [To be discussed: is revocation and key management in scope?](/AqZvZR3rRcGg02oMrtFNaw)

# Credential Profile in Comparison Matrix
explain why some properties emerge from signature/revoation algo


### Common properties across tables
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



## Properties of Credential Format
Apart form the common properties, the matrix provides information for the credential format on selective disclosure, predicates and crypto-agility. These properties will be described in the following sections.

### Selective Disclosure
Selective disclosure allows a holder to present a subset of the attributes of the credential issued by the issuer. This minimizes the amount of the holder's information that is shared with the issuer. For example, the government issues a passport credential to Alice. The passport includes a variety of attributes, such as Alice's first name, last name, birthdate, social security number, et cetera. When Alice want to buy alcohol at the supermarket, she has to prove to the supermarket that she is of legal drinking age ($18+$) to buy alcohol. In the classical setting where Alice shows her passport to the supermarket, the supermarket sees all the attributes on her passport, even though they just need her birthdate. Using SSI with selective disclosure, she can simply present her birthdate with which the supermarket can verify that she is over $18$.

Selective disclosure can be achieved through the use of a signature algorithm that supports selective disclosure, such as BBS+ and CL signatures. Selective disclosure can also be achieved through governance, namely a community can agree on signing each attribute seperately, such that each attribute can also be presented seperately. As mentioned before, in our matrix we only look at choices on credential profile level, hence we only look at whether selective disclosure is achieved through the signature algorithm.

### Predicates

Predicates allow the holder to further decrease the amount of information shared with the holder. Predicates check a value against a certain condition, resulting in true or false. Recall the example of Alice wanting to buy alcohol in the supermarket. Alice can prove that she is older than 18 using the predicate _age_ $\geq 18$. As Alice's age is $20$, the predicate $20 \geq 20$ is true. This way Alice can prove that she is allowed to buy alcohol without revealing her birthdate or even her age. 

Just like selective disclosure, predicates can be created on various levels. On a governance level, the issuer could issue common predicates to holders, such as $18+$ and $65+$. In the matrix, we only consider predicates through the capability of performing Zero-Knowledge Proofs in the credential profile. 

More information about predicates and zero-Knowledge-Proofs can be found [here](https://medium.com/51nodes/selectively-disclosed-verifiable-credentials-79a236b81ee2).

### Crypto Agility
To support long term security the cryptographic algorithms that are used for encrypting, signing and hashing should be updatable without lossing features. Crypto agility could mean
- to increase the amount of bits for the keys
- to replace the algorithm with a new one 
It is difficult to predict the time when the algorithms have to updated. Typical scenarios are:
- the algorithm is broken and the security is suddenly lost
- the amount of computation power is high enougth to perform a brute force attack in an acceptable amount of time
- there are faster algorithms that make the process more efficient without loosing features or lowering the security level

A relevant source is the recommendation of the German BSI(Federal Office for Information Security). They have published a [technical guideline for recommendations and key lengths](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/TechGuidelines/TG02102/BSI-TR-02102-1.pdf?__blob=publicationFile&v=4) listing the algorithms and parameters to use. It has to be mentioned that this is only a recommendation and not a direct law.

## Properties of Signature Algorithm
Apart form the common properties, the matrix provides information for the signature algorithm on hardware support and unlinkability. These properties will be described in the following sections.


### Hardware Support

Hardware support is required for regulated and highsecurity usecases to prevent credential/key duplication and theft. Existing hardware stores to sign inside the smartphones are Trusted Execution Environments, SecureEncalves, SecureElements and eUICCs, external authenticators and more. In the backend HSMs or TPMs can be used by issuers or Cloud-Wallets to secure the keys. The hardware-backed crypto processors often support only a limited set of established signature algorithms, therefore the use of modern cyrptography algorithms is limited for these use cases.

### Unlinkability

Unlinkability is the property that an attacker cannot distinguish whether two or more items withinin a system (comprising these and possibly other items) are related or not. Within an identity ecosystem this applies for example that one verifier can link two credentials of an holder, two selective disclosures of the same credential or whether two colluding verifiers can link two seperate presentations of the same credential. This excludes the fact that linkability can also happen by the reavealed attributes themselves or unlinkability achieved by the infrastructure, e.g. just-in-time issuance.



## notes, outcomes
The matrix sparked a deep discussion on existing revocation mechanisms and their limitations, potential attacks, and ways to resolve these issues.
