# Excerpting Known Issuer/Verifier Registers

## Enabling anyone to share information about the issuers and verifiers for whom they assure trust

Authors: Manu Sporny (Digital Bazaar), Oskar van Deventer (TNO), Isaac Henderson Johnson Jeyakumar (Uni-Stuttgart, Fraunhofer IAO), Shigeya Suzuki (Keio University), Konstantin Tsabolov (Spherity GmbH), Line Kofoed (Bloqzone)

Date: 27 September 2022

Venue: RWOT Den Haag


# Abstract

This work will focus on how a party or its agent can decide whether or not to engage with a counterparty in a transaction. This document first does a survey of prior art related to trust frameworks and technologies to collect the current state of the art. It then extracts requirements from each of these works. It discusses the work at two levels, technical solutions and governance. It then attempts to summarize a data model that can support the requirements. The paper then proposes multiple serializations of the data model, including but not limited to Verifiable Credentials, DNSSEC, and blockchain-based serializations, that could then be incubated and sent onto the standards track at global standards setting organizations.

Keywords: self-sovereign identity, known issuers register, known verifiers register, trusted issuer, trusted verifier, trust list, known authority catalog


# 1. Introduction

Known Issuers Registers are a well-known concept also from the pre-internet age. Whenever there is a diploma signed by a university, there are people and organizations that keep track of what universities exist and what methods there are to confirm the authenticity of that diploma. A register (“list”) could be maintained by HR staff for the purpose of hiring personnel, and the governance of that register would be minimal. Another register could be maintained by a government, associated with well-governed accreditation procedures, for the purpose of assuring that a diploma represents a proper education. Known Issuers Registers support verifiers in their decision to trust the issuer of a verifiable credential that is presented by a holder.

Known Verifiers Registers are a relatively new concept[^1], arising in the digital age. Examples are the European register of parties that are allowed to use the digital fingerprint information on the chip of European passports. This is cryptographically enforced: “chips-says-no” when an unauthorized party attempts to access this information on the chip. Also eIDAS v2 will have a Known Verifiers Register that limits the access of verifiers to credentials in an EUDI (EUropean Digital Identity) wallet. Known Verifiers Registers support holders in their decision to trust a verifier to share a verifiable presentation to that verifier.

Both digital Known Issuer Registers and Known Verifier Registers help automating the decision process and making it more auditable.

Note that “trusted” or “authorized” are sometimes used as synonyms for “known”, as the purpose of many of those registers is to assure trust or authority. We are using “known” as we do not want to make any presumptions about the application of the registers, or the trust/authority that they assure. Similarly, the word “list” could be considered synonymous to “register”, depending on the amount of governance, assurances and authority associated with it. We are using “register” as there would always be some form of governance, if only the establishment of its purpose and the format of its entries.

Section 2 presents a set of digital-age use cases that explain use of Known Issuers Registers and Known Verifier Registers.

Section 3 analyses prior art, i.e. examples Known Issuers Registers and Known Verifier Registers that have already been deployed, or that are being developed, as well as a gap analysis

Section 4 presents a simple model of a Known Issuers/Verifiers Register, its entries and associated roles, followed by an initial list of requirements.

Section 5 provides a data model and possible serializations, which could serve as a starting point for future standardization.

Section 6 discusses possible next steps towards such future standardization

Section 7 makes conclusions and proposes future work

The target audience of this paper are people that know the basics of SSI, e.g. the concepts of issuer, holder, verifier and verifiable credential. SSI developers may use this document as input and inspiration for their code and other products. Deployers of SSI use cases may use this document in the specification process of their deployment.


# 2 Use Cases

ACTION: Everyone that created use cases should detail them and make sure they contain the information they wanted to include in the paper.


## 2.1 General

The studied use cases are in two categories.



* Known-Issuer-register use cases
* Known-Verifier-register use cases

The final subsection checks for commonalities and differences between the two categories.

&lt;Acknowledge that there exist many more use cases, with links to them>


## 2.2 Known-Issuer-Register Use Cases



* Acme Inc. is a producer of medical equipment. Twin Mountains Hospital decided to buy equipment from Acme Inc. The law says that medical equipment should be certified by a 3rd party certification body. Twin Mountains Hospital requests a certification from Acme, Inc., which then delivers that certification to Twin Mountains Hospital. The hospital then checks if Acme Inc. is in the register of licensed 3rd party certification bodies to see if the issuer of Acme Inc.'s certification is an approved certification body.
    * Note: The solution might need to convey a single item in a register vs. the entire register.
    * Note: Many similar certification/license use cases are out there.
* Rolf is a permanent resident of Utopia and is given the option of receiving a digital permanent resident card. When Z
* Alice is traveling from country B  to country A  during covid Pandemic and she needs to provide her covid certificate on country A upon Arrival. How does the verifier in country A knows that Alice was issued covid certificate from an authorized Health provider in country B and also what data has to be transferred to verify the information.
* Yuri has a digital driver's license and is attempting to rent a car from CarMart. CarMart requests to see Yuri's age, motor vehicle class, and driver's license number. Yuri's software checks against a register to make sure that CarMart is a known authority when asking for that information so it can warn Yuri if CarMart isn't trusted to request that information from Yuri.
* Yukari is trying to find a job. She would first make a register of companies seeking employers and contact each one. In contacting the contact person at those companies, she needs to make sure that the contact person is the correct contact who represents the company. In addition, the company will ask for as much information about her as they need. Each party will need a way to confirm the existence of the other party and will need a trusted third party to do so.
* Walmay, Inc. is a wholesaler of drugs. John & Jane is a manufacturer of drugs. Now, Walmay, Inc. finds out that a party of drugs has broken packaging and decides to return the party to the manufacturer. After the law it’s required that all interactions in the drug market must be done only between authorized trading partners. John & Jane requests an authorized trading partner certificate from Walmay Inc. The certificate credential contains a link to the issuer. John & Jane then verifies that the issuer is a member of the register of Authorized Issuers of ATP credentials.


## 2.3 Known-Verifier-register Use Cases



* See also [Verify the Verifier - Anti-coercion by Design; October 2020 | TNO](https://blockchain.tno.nl/blog/verify-the-verifier-anti-coercion-by-design/)
* Oskar joins a tennis club. The tennis club requests a government-issued proof of birth date. However, the tennis club does not have authorization for asking for this personal information. As a consequence, Oskar’s certified EUDI wallet refuses to present this information. The tennis club realizes that they cannot obtain this high-LoA information from the EUDI wallet, and instead accepts a fake self-assured date-of-birth by Oskar.
* Oskar was invited by the European Commission to become an evaluator. Even though Oskar would be paid only the equivalent of a book voucher, the EC requires a full contracting process, which includes an eIDAS LoA high identification and a recent authentic bank statement. And even though Oskar considers these requirements unreasonable, Oskar’s certified EUDI wallet accepts the request. This way, Oskar knows at least that the request is genuine, and that there exists a sufficiently-well-governed policy associated with the request. .
* Oskar crosses the border with Dystopia. Immigration requests Oskar to surrender all verifiable credentials in his SSI wallet, including identification, driving, diplomas, certifications and other. Immigration of this country is not authorized to such a wide request.  As a consequence, Oskar’s certified EUDI wallet refuses to present this information. Even the threat of denial-of-entry or worse cannot change the situation, as neither immigration nor Oskar himself is physically able to compromise Oskar’s EUDI wallet to surrender the information.
* Use case with picture from [https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/advance-readings/posters/eSSIF-TRAIN%20Trust%20Registry%20Poster.pdf](https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/advance-readings/posters/eSSIF-TRAIN%20Trust%20Registry%20Poster.pdf)


## 2.4 Commonalities and differences

Conceptually and technically, the two types of registers (known issuer, known verifier) are fairly similar. Each type is a governed list of parties with a role in SSI exchanges. Each type needs to provide some form of publication or access, so the registers can be used. This paper will presume that the types of registers themselves, as well as their publication and access methods can be technically identical. The only distinction is that a register could contain only known issuers, only known verifiers or a mixture[^2] of those, so the data model should accommodate this.

Major differences arise in the applications surrounding the registers. Known Issuer Registers target verifier implementations, whereas Known Verifier Registers target holder implementations. Also there may be major differences in the governance between the two types of registers, or whether/how the consulting of registers is implemented and enforced. All of these differences are out of the scope of this paper


# 3. Analysis of Prior Art


## 3.1 General


## 3.1.2 Historic Perspective of Known Issuer/Verifier Registers

~~ACTION: Oskar and~~ ~~Line to provide general historic perspective~~

~~ACTION: Shigeya to provide background on IANA~~.

~~ACTION: Line to provide some background on Dutch perspective~~

Issuer registers pre-date the digital age. Governments have always maintained lists of organizations with accreditation. This includes educational accreditation (schools, universities), bank accreditations, telecom-operator licenses, etcetera. A chamber-of-commerce typically maintains a queryable register of companies. Many of those registers have become queryable via an electronic API.



* ~~Dutch Government~~
    * ~~Given authorities mandate for certain tasks - have sole right and obligation to register companies. Top-down from Dutch Government~~
    * ~~State department, issuer issuing the mandate the authority to carry out some task~~
    * ~~Chamber of Commerce in Netherlands - micromandates, one registration as company owner but can't register delegated tasks in organization ~~
    * ~~Service that takes care of driver's license – issued or revoked, sole task, delegated to postal office (certain tasks). Need for a chain of delegation of tasks rooted in the Dutch government.~~
* Network Resource Allocation and IANA

The beginning of network resource allocation management was initiated by Jon Postel in 1982 as part of ARPANET activity. John Postel was a graduate school student at that time. ARPANET is a research network established by the US Department of Defense’s Advanced Research Project Agency (DARPA). Later, ARPANET became the basis of the Internet. Later, Postel proposed to have a “numbering czar” be appointed to manage various numbers in emerging ARPANET. This event began the Internet’s number authority, later known as Internet Assigned Numbers Authority — IANA.

IANA allocates and maintains unique codes and numbering systems used in the technical standards (“protocols”) that drive the Internet. It currently manages Domain Names, Number Resources, and Protocol Assignments.  Table X shows items currently managed by IANA.

(To be written: TABLE X )

Each of the resources is maintained under policies defined for each of the resources.

The policies for each of the resources and also related documents are published as IETF RFC. All of the policies are available at its website `https://iana.org`.


## 3.2 EBSI Trusted Issuer Registry

EBSI, the European Blockchain Service Infrastructure, is a joint initiative from the European Commission and the European Blockchain Partnership, see also

[https://api.preprod.ebsi.eu/docs/apis/trusted-apps-registry/latest#/](https://api.preprod.ebsi.eu/docs/apis/trusted-apps-registry/latest#/)

One of the services offered by EBSI is a Trusted Issuers Registry (TIR). The TIR is a generic decentralized registry holding information about trusted issuers, like public information, accreditations and other. The TIR enables a verifier to validate the identity and accreditations of Trusted Issuers. The TIR is deployed as an Ethereum smart contract deployed on the permissioned EBSI ledger for the purpose of being public while at the same time ensuring a high level of trust and transparency. The public smart contract methods are exposed via APIs: JSON-RPC for write and REST for the read operations. The API of the EBSI TIR is published at [https://api.preprod.ebsi.eu/docs/apis/trusted-issuers-registry/latest#/](https://api.preprod.ebsi.eu/docs/apis/trusted-issuers-registry/latest#/). The authors could not find any public information about the governance of the TIR, e.g. how an organization could get itself registered on the EBSI TIR. The EBSI documentation states: “Accreditation of trusted issuers domain-specific and is outside the EBSI scope”.

The authors asked EBSI about Trusted Verifier Registry, and got the following response: “At this moment, EBSI does not have a Verifier Register as the Use Cases we are currently working on don't require one. This means that Verifiers are not onboarded and they are not accredited either – in the sense of the accreditation given to Issuers. If needed be, we could replicate the Issuers’ trust model and apply it to Verifiers. However, before doing this, we would need to have a requirement from a Use Case”[^3].


## 3.3 European biometric passport chip

European passports have a chip that stores among others biometrics (facial image and fingerprints), see [https://home-affairs.ec.europa.eu/policies/schengen-borders-and-visa/document-security_en](https://home-affairs.ec.europa.eu/policies/schengen-borders-and-visa/document-security_en)

The chip is cryptographically secured. Only authorized chip readers can read and verify the fingerprint information. This is enforced through technology and governance processes that include a Known Verifier Register &lt;reference needed, OSKAR is checking>.


## 3.4 eSSIF-Lab TRAIN (Isaac will expand)


### 3.4.1 TRAIN (TRust mAnagement INfrastructure)

TRAIN &lt;reference> provides a trust management infrastructure that allows to verify the trustworthiness of involved parties in an SSI Ecosystem. An example would be if a certain issuer is trustworthy (e.g. is it a real bank or just a fake bank).

TRAIN aims to add a trust-component to an SSI ecosystem. This component enables the discovery and verification of lists of trustable parties in the ecosystems (Trust Registries), as well as the definition, consideration, and verification of eIDAS compliance (including LoAs) of involved parties. TRAIN provides a decentralized framework for the publication and querying of trust information. It makes use of the Internet Domain Name System (DNS, DNSSEC) with its existing global infrastructure, organization, governance and security standards to establish the trust discovery process.


### 3.4.2 Interoperability using ETSI Trust List

TRAIN leverages the ETSI standard TS 119 612 [1] for Trust Lists to facilitate interoperability and adoption. This standard is already in productive use for eIDAS Trust Lists for the identification and verification of Qualified Trust Service Providers (QTSP). eIDAS Trust List compile different accredited Trust Service Providers along with their services in a machine-readable form. For the SSI ecosystem the Trust Service Providers’ equivalent will be trustable (according to the rules and accreditation processes of the respective Trust Scheme/Trust Framework) entities who operate as Issuers, Holders and Verifiers. Entities and services can vary according to the respective requirements and application domains of a certain Trust Scheme. For example: A State authority can be a Trust Service Provider who offers different service like National identity credential issuance, social security number issuance etc. These details are made available through TRAIN Trust Lists in a machine-readable form. Thereby other entities are able to verify the trustworthiness of these entities.


### 3.4.3 TRAIN Outcomes

An illustrative interoperability use case for the European Health Insurance Card (EHIC) has been realized and demonstrated with SICPA SA and Validated ID [3]. The latest draft of OpenID Connect for Verifiable Presentations (OIDC4VC) [4]contains informative implementation guidelines describing how issuers, holders and verifiers can utilise the TRAIN trust scheme approach. TRAIN approach was also used to develop a Proof of Concept (PoC) for Global Covid Certificate Network (GCCN) an initiative by Linux Foundation for Public Health (LPFH) to identify the trustworthiness of Covid Credentials on a global scale[5].



* ACTION: Isaac to expand section on TRAIN.
* Fraunhofer TRAIN
* [https://train.trust-scheme.de/info/](https://train.trust-scheme.de/info/)
* [https://github.com/WorldHealthOrganization/ddcc-trust/blob/main/TrustListSpecification.md](https://github.com/WorldHealthOrganization/ddcc-trust/blob/main/TrustListSpecification.md)
* [https://openid.net/specs/openid-4-verifiable-presentations-1_0.html](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html)
* [https://dl.gi.de/handle/20.500.12116/38702](https://dl.gi.de/handle/20.500.12116/38702)
* [https://tspa.trust-scheme.de/tspa_train_domain/api/v1/scheme/gccn-registry-test.train.trust-scheme.de](https://tspa.trust-scheme.de/tspa_train_domain/api/v1/scheme/gccn-registry-test.train.trust-scheme.de)
* [https://verifier-api.coronacheck.nl/v4/verifier/public_keys](https://verifier-api.coronacheck.nl/v4/verifier/public_keys)
* Uses DNS name to locate trust list - pointer to trust list is in DNS Record. Every zone is managed by zone manager, can access record
    * Two records
    * PTR records
        * Used to point to scheme
    * URL records
        * Points to trust list URL
        * List can be hosted on IPFS or own server (have freedom to choose)
        * Main advantage - WHO - countries issuing different covid certificates, can provide different trust lists - can be decoded automatically at verifier, trusted authority or not
    * Limited to X509, but can be used in other formats - different authorized issuers can be in trust issuer list – entity identifier list, qualifier details, address, notaries in agent list can have authorized agents, they can offer different services
        * Corona verification, different services, single entity can have different services, issuer/verifier can be in the same list or different lists.
        * List can be digitally signed using X509 certificate
        * In TRAIN, the hash of the signature is in DNS, and can verify chain of trust via hash in DNS.


## 3.5 Ethereum-based

Spherity GmbH ([https://www.spherity.com/](https://www.spherity.com/)), a German company is working on a solution named CARO ([https://www.caro.vc/](https://www.caro.vc/)) which enables trading partners in the US pharmaceutical industry to verify the Authorized Trading Partner status of their business partners. During the verification process an ATP should check if the issuer of the counterparty Verifiable Credential was issued by a trusted Issuer.

The implementation ([https://github.com/Open-Credentialing-Initiative/trusted-issuer-registry](https://github.com/Open-Credentialing-Initiative/trusted-issuer-registry)) implies the storage of the DIDs of trusted issuers in a smart contract on the Ethereum blockchain. The application then makes a request to Ethereum in order to get the list of trusted issuers and check if that of the interest is in the list.

The governance of the list of trusted issuers if done by Open Credentialing Initiative ([https://www.oc-i.org/](https://www.oc-i.org/)). Each member of the board of OCI is registered as a gatekeeper on the smart contract. Each of the statekeepers can add new trusted issuers (or, more precisely, their DIDs) into the list. The process of adding new statekeepers into the smart contract is a subject for voting, where at least 80% of already existing statekeepers should give their vote for the proposal.

The solution is going to go into production late 2022.

The approach aims to enforce the following policies:



* Always available
    * Calling the known authorities list is an integral part while verifying a counterparty identity or/and credentials, so it should be always available.
* Trustless
    * The architecture and the execution of the known authorities list should not be owned and controlled by a single entity.
* Transparent
    * The code, state, and executions of the known authorities list should be transparent to all parties in the ecosystem.
* Auditability
    * It should be possible to retrieve a previous state of the known authorities list.
* Security
    * Changes to the known authorities list should only be made by trusted entities. For this, a governance protocol is defined which relies on strong cryptography enforced by the Ethereum network.
* Privacy
    * Only the changes to the known authorities list are visible (as events in the Ethereum network). Read operations are not recorded in the Ethereum network, so no one can trace if the list was retrieved or the frequency of such operations.


### Architecture

The smart contract containing the trusted issuer registry is deployed to the Ethereum blockchain and acts as a backend. Its state and methods can be accessed via an Ethereum node, e.g., an OCI-owned one, that exposes all needed RPC methods or a service like Infura.


![alt_text](images/image1.png "image_tooltip")



### ~~Existing applications~~

~~The proposed solution will be used in production starting 2022 to enable trusted digital interactions between acting parties.~~



* ~~ACTION: Kostantin to expand section on Ethereum~~
* ~~Not VC specific, list of DIDs which could be trusted~~
* ~~Governed by a group of Ethereum wallets~~
* ~~[https://github.com/Open-Credentialing-Initiative/trusted-issuer-registry](https://github.com/Open-Credentialing-Initiative/trusted-issuer-registry) ~~
* ~~[https://trusted-issuers.netlify.app/](https://trusted-issuers.netlify.app/)~~
* ~~Spherity working on US Market product in healthcare - pharmaceutical industry~~
    * ~~Open Credentialing Initiative~~
        * ~~Give the body to decide which issuers to trust~~
        * ~~Solidity contract in testnet of Ethereum~~
            * ~~Contract manages two lists~~
                * ~~List of state keepers (make proposals to add entries to trusted issuers list)~~
                * ~~Quorum is required to add things to state keepers or to trusted issuers list~~
                * ~~There can be multiple lists (for different VCs)~~
                * ~~Auditability - you can see all events that have happened, check to see if issuer was trusted at past point in time, every transaction is an event you can see for the purposes of auditing.~~
                * ~~Both the source code and the list are auditable~~


## 3.6 Trust-over-IP Trust Registry Task Force (Isaac)

The Trust Registry Task force of Trust Over IP Foundation (ToIP) &lt;reference needed> attempts to address the requirement of enabling interoperability inorder to support transitive trust within and between different trust communities implementing the ToIP stack. In this case, the desired interoperability outcome is a common protocol that works between any number of decentralized peer trust registries operated by independent governing authorities representing multiple legal and business jurisdictions.

In the v1 specification of Trust Registry Protocol the trust registry was planned to include the authorized issuers/verifiers. The scope of the specification was restricted to query the current status of the entry in the trust registry. But the definition of other meta data types has been planned for the second version of the specification. And in current specification the query works based on the REST APIs but it seems to be moved to DIDComm. And there is also a swagger API available how the query response looks like.

The specification also contains the details to include **TrustService <code><em>type </em></code></strong>Property in the DID Document there by allowing authorities to configure their trust registries in <code>serviceEndpoint </code>as HTTPS URI<code>. </code>Based on the current specification it seems like the trust registry supports DID serializations but there is not much clarity to accommodate different serializations like x.509, VC etc.

ACTION: Isaac to write section on Trust over IP



* [https://github.com/trustoverip/tswg-trust-registry-tf/blob/main/api/toip.trustregistry.api.yaml](https://github.com/trustoverip/tswg-trust-registry-tf/blob/main/api/toip.trustregistry.api.yaml)
* [https://github.com/trustoverip/tswg-trust-registry-tf/blob/main/docs/ToIP%20Trust%20Registry%20V1%20Specification.md](https://github.com/trustoverip/tswg-trust-registry-tf/blob/main/docs/ToIP%20Trust%20Registry%20V1%20Specification.md)
* [https://wiki.trustoverip.org/display/HOME/Trust+Registry+Task+Force](https://wiki.trustoverip.org/display/HOME/Trust+Registry+Task+Force)
* [https://wiki.trustoverip.org/display/HOME/ToIP+Trust+Registry+Protocol+Specification](https://wiki.trustoverip.org/display/HOME/ToIP+Trust+Registry+Protocol+Specification)
    * Not much work happening over Trust over IP work
    * It should always be in the credential
    * Work discontinued - architecture diagram, governing authority, trust registry, there is an API example document
    * Interoperating with good health pass, which was discontinued last April.
    * Interop w/ x509 certificates was desired, no concrete implementations of the group so far


## 3.7 Expression as Verifiable Credential (Manu)



* ACTION: Manu to write this section
* [https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/advance-readings/authorized-issuer-lists.md#the-authorizedissuerlist-verifiable-credential](https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/advance-readings/authorized-issuer-lists.md#the-authorizedissuerlist-verifiable-credential)


## 3.8 Governance of the Elements of Trust (Shigeya)



* ACTION: Shigeya to write this section.
* The following two documents discussed a highly abstract model of governance of “small data” (i.e., Trust List). Shigeya is the author of the two documents and thinks it is okay to borrow some of the discussion from there.
* SUZUKI, Shigeya. Multistakeholder Governance for the Internet. In: International Conference on Financial Cryptography and Data Security. Springer, Cham, 2020. p. 230-241.
* Shigeya Suzuki, Tatsuya Kurosaka, Jun Murai, Keio University, “Dependency among Data, Code, Governance, and Operation in Trust, Symposium on Designing the New Cyber Civilization”, Cyber Civilization Research Center, Keio University, January 2022.

    [https://www.ccrc.keio.ac.jp/wp-content/uploads/2022/02/Suzuki-Kurosaka-Murai-Dependency-among-Data-Code-Governance-and-Operation-in-Trust.pdf](https://www.ccrc.keio.ac.jp/wp-content/uploads/2022/02/Suzuki-Kurosaka-Murai-Dependency-among-Data-Code-Governance-and-Operation-in-Trust.pdf)

* “A Study on Governance for Decentralized Finance Systems Using Blockchain Technologies”, Joint Research of Keio University and Japan Financial Services Agency, May 2020, \
[https://www.fsa.go.jp/en/policy/bgin/information.html](https://www.fsa.go.jp/en/policy/bgin/information.html) (at the very end of the page)


## 3.9 Governance + DNSSec (Shigeya)



* ACTION: Shigeya to write this section.
* Revisiting Usefulness of Centralized System for Establishing Trust \
[https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/advance-readings/revisiting-usefulness-of-centrailzed-system.md](https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/advance-readings/revisiting-usefulness-of-centrailzed-system.md)
* Proposal on the Design and Implementation of a DID method over DNSSEC (did:dnssec) \
[https://shigeya.github.io/did-dnssec-proposal/main/draft-suzuki-did-dnssec-proposal.html](https://shigeya.github.io/did-dnssec-proposal/main/draft-suzuki-did-dnssec-proposal.html)


## 3.10 Miscellaneous

The following are other examples of work on trusted issuer registries.



* ~~OpenID Connect Federation ([https://openid.net/specs/openid-connect-federation-1_0.html](https://openid.net/specs/openid-connect-federation-1_0.html)): An Entity in the federation must be able to trust that other entities it is interacting with belong to the same federation.~~
* ~~[https://danubetech.github.io/did-method-dns/#:~:text=The%20target%20system%20of%20the,specific%20identifier%20in%20the%20DID](https://danubetech.github.io/did-method-dns/#:~:text=The%20target%20system%20of%20the,specific%20identifier%20in%20the%20DID).~~
* Trinsic trust registry: [https://gitlab.grnet.gr/essif-lab/infrastructure_3/trinsic](https://gitlab.grnet.gr/essif-lab/infrastructure_3/trinsic)


## 3.11 Gap analysis: missing standards and VCs

The discussed prior art shows that, although there exist quite a few implementations of Known Issuers Registers, and fewer Known Verifiers Registers, all of them use proprietary APIs to access entries to those registers. This is limiting, as APIs require a “phone-home” API call for every verification, which is inefficient, time-consuming, a potential privacy risk, and impractical in off-line scenarios. Moreover, the proprietary nature of the APIs imply significant integration cost for implementations that aim to support multiple registers, and that give users and stakeholders viable choice and switching possibility between registers.

The proprietary nature of the APIs can be resolved through harmonization and standardization of both the data model and the serialization of Known Issuers/Verifiers Registers.

The time/efficiency, offline and privacy issues with the API approach can be resolved by including a standardisable serialization based on verifiable credentials and/or anonymous credentials (anoncreds).

&lt;@Manu: should we invite Stephen Curran to develop a serialization for anoncreds?>


# 4. Requirements


## 4.1 Model

Figure 4.1.1 provides a simple model of a Known Issuers/Verifiers Register.



* A Known Issuers/Verifiers Register contains entries with information about the issuers and/or verifiers that it knows.This information can be as minimal as a single DID or public key per known issuer or verifier, or it can also include lots of other metadata about those.
* An Assurance Community is what governs the Known Issuers/Verifiers Register. This can be a single person, a group of persons, an organization, a group of organizations or other. The governing can be purely manual, or partially/fully automated (e.g. smart contract).
* A Subscriber is what/who uses entries from a Known Issuers/Verifiers Registry. A Subscriber is typically an issuer-, holder- and/or verifier agent.


![alt_text](images/image2.png "image_tooltip")


Figure 4.1.1: Model of a Known Issuer/Verifier Register


## 4.2 Requirements

ACTION: Oskar to refine requirements.

ACTION: Everyone to review requirements.

The following requirements have been specified by the authors, both requirements on a Known Issuers/Verifiers Register (“a register” in short) as a whole and its individual entries. These requirements may be updated in the future.



* A register may be created and governed by any individual, group of individuals, organization, group of organizations or other
* A register and/or its entries shall be made available to subscribers
* A register and/or its individual entries shall be serializable in one or more formats
    * Verifiable Credential (mandatory)
    * Other formats?
* Entries may be made available via a Wallet, a Website, a URI, a QR code, a DNS Resource Records, DNSSEC, onchain Ethereum, and other methods
* A register and its entries shall be cryptographically verifiable
    * Accommodate Different cryptographic mechanisms (X.509, JWK etc..)
    * Ability to authenticate the register or an individual entry
* A register and its entries shall have associated Governance Metadata Format
    * Policies
    * Qualifier details
    * … more
* A register and its entries shall be able to be publicly resolvable
* A register and its entries shall be able to be privately transmittable/retrievable
* A register may have metadata associated with it, e.g. metadata that is applicable to all of its entries
* A register may have different levels of privacy/confidentiality, ranging from fully public to for-authorized-yes-only
* Entries shall be able to be created, read, deleted.
* Entries may be updated, suspended and/or revoked
* Entries may have have an individual level of assurance associated with it
* Entries may have an associated level of assurance


# 5. Implementations


## 5.1 General

The following subsections provide a data model for entries to the Known Issuers/Verifiers Register, their serialization and a view on its governance model.


## 5.2. Data Model(s)

The data model described in this section has been built using input from a variety of the prior art evaluated for this paper including input from the EBSI Trusted Issuer Registry, ETSI TS 119 612, eSSIF-Lab TRAIN, the Trust over IP Foundation Trust Registry Protocol, and Rebooting the Web of Trust input documents. The data model described in this section is capable

ACTION: Manu to clean up data model section



* The data model is a list/register/catalog/directory that contains entries
    * Each entry contains an identifier
    * Each entry contains a type
    * Each entry might contain:
        * The common name of the individual or organization
        * The legal name of the individual or organization
        * The name of the scheme (e.g. "eIDAS Trust Scheme")
        * Alternative identifiers for the individual or organization
            * Type
            * Value,
            * URI
        * The set of addresses associated with the entry
        * A set of email addresses associated with the entry
        * The website address of the entry
        * ~~A set of agents that can act on behalf of the entry~~
            * ~~Note: It's not clear if these organizations can digitally sign for the entry~~
                * If you want to assign/use an agent, just add it to the list
        * A set of certifications that qualify the organization to provide the services listed
        * One or more services offered by the entry which might contain
            * Identifier
            * Name
            * Type of service
            * Types of identifiers provided by service (X509, DID Document) - schema used to verify that the serialization matches the service
            * Status of service
                * When service started operation
                * When service stopped operating
            * Policies associated with the service
            * Additional service information (URI)
            * Different supported key types (Eddsa, JWS, etc.)


## 5.3 Serialization(s)


### 5.3.1

ACTION: Konstantin to express data model in a way that works with DLT-based approach.


### 5.3.2 Serialization for x.509 using DNS

ACTION: Isaac to detail approach that works with DNS and X509.

In this approach qualified Domain Name will be used as Identifier of the entity and this will be included in the <code><em>SubjectAltName</em></code> attribute of the x.509 certificate. At the verifier side the <code><em>SubjectAltName</em></code> is extracted from the x.509 certificate. And the issuer details can be a HTTPS URI or DID depends on the issuer. The TRAIN infrastructure offers a API which acts as a proxy service for trust list discovery and provider verification.  The query of the TRAIN API looks as follows.


```
{
   "Issuer": "https://universityx.com/2142",
   "Trust_Scheme_Pointer": exams.universityx.com
}

```



```

```



### 5.3.3 Serialization with DNSSEC and Web

ACTION: Shigeya to detail approach that works with DNSSEC.

Maintain a list of entities as a labels in a DNS Zone.

Each of fully qualified domain name of the label treated as the identifier of the entity.

Each of the label (or typed sub label) bounds to pubic keys for the entity.

Each of the label (or typed sub label) may refer external resources which contain additional information (other than the identifier and the public keys) of the entity.

(Followings are list of things need to be done for the each of process. Will rewrite to match with other sections)



1. Select a zone act as location of the list. The list is shared among the entities which use the list. ( ‘example.net’ )
2. **Adding an entry**
    1. Select a unique label for the organization,. Use the FQDN with the label. (if label is  ‘entity1’, FQDN will be ‘entity1.example.net’ ).
    2. Either generate key pair or recieve a public key for register
    3. Register the key into the zone as a Resource Record (RR) type XX.
    4. As needed, register additional information as external data, place in a URL (possibly with Hashlink) and add the URL to the zone as RR type XX with sublabel.
3. **Removing (Revoking?) an entry**
4. **(To be written)**


### 5.3.4 Verifiable Credentials Serialization

ACTION: Manu to detail approach that works with Verifiable Credentials.


```json
{
  "@context": [
    "https://www.w3.org/2018/credentials/v2",
    "https://w3id.org/vc/???/v1"
  ],
  "issuer": {
    "id": "did:web:authority.example",
    "name": "National Education Accreditation Authority of Utopia"
  },
  "issuanceDate": "2023-02-13T00:18:30.053Z",
  "type": ["VerifiableCredential", "Known???Credential"],
  "credentialSubject": [{
    "id": "did:web:registrar.utopia.edu.example",
    "type": "KnownIssuer",
    "name": "Utopia University Registrar",
    "legalName": "The Polytechnic University of Utopia Registrar",
    "website": "https://utopia.edu.example/",
    "email": "accreditation@neaau.org.example",
    "identifier": [{
      "type": "PropertyValue",
      "propertId": "Utopia Educational Institution ID",
      "value": "123456789"
    }],
    "usesOperationalScheme": [{
      "id": "http://oid-info.com/get/1.2.3.4.5",
      "name": "Utopian Trust Scheme 819-4"
    }],
    "accreditation": [{
      "id": "https://utopia.gov.example/accreditations/123"
    }],
    "authorizedToIssue": [{
      "type": "UniversityDegreeCredential",
      "credentialSchema": {
        "id": "https://issuer.example/degree.json",
        "type": "AuthorizedIssuerJsonSchema2022",
        "schema": "{\"properties\":\{\"credentialSubject.state\":\"UA\"}}"
      }
    }]
  },
  "proof": { ... }
}

```



### 5.3.2 Serialization for Smart Contract-enabled environments

The example here is one of many possible ways of maintaining a list on DLTs. This implementation was done for Ethereum blockchain and smart contracts. The example implies that only a portion of the data is actually stored on the ledger.

The minimally reasonable part of data would be a list of identifiers of the trusted/known entities. The rest of the data to be resolved by a service whose duty is to dereference/resolve data and enrich it with data from external data sources including but not limited to databases, distributed ledgers, and 3rd-party APIs.

The following diagram illustrates the high-level architecture of the proposed methodology:


![alt_text](images/image3.png "image_tooltip")


EXAMPLE: Response from the smart contract


```
[
  "did:web:weboftrust.info",
  "did:ethr:0x0..."
]
```


EXAMPLE: Minimal response from the Register Access Point


```
[
  {
    "id": "did:web:weboftrust.info",
    "type": "KnownIssuer"
  },
  {
    "id": "did:ethr:0x0...",
    "type": "KnownIssuer"
  }
]
```


EXAMPLE: Rich response from Register Access Point


```json
[
  {
    "id": "did:web:weboftrust.info",
    "type": "KnownIssuer",
    "name": "Utopia University",
    "legalName": "The Polytechnic University of Utopia",
    "website": "https://utopia.edu.example/",
    "email": "accreditation@neaau.org.example",
    "identifier": [
      {
        "type": "PropertyValue",
        "propertId": "Utopia Educational Institution ID",
        "value": "123456789"
      }
    ],
    "usesOperationalScheme": [
      {
        "id": "http://oid-info.com/get/1.2.3.4.5",
        "name": "Utopian Trust Scheme 819-4"
      }
    ],
    "accreditation": [
      {
        "id": "https://utopia.gov.example/accreditations/123"
      }
    ],
    "service": [
      {
        "id": "did:example:123456789",
        "name": "University Diploma Service",
        "authorizedToIssue": [
          {
            "type": "UniversityDegreeCredential",
            "credentialSchema": {
              "id": "https://issuer.example/degree.json",
              "type": "AuthorizedIssuerJsonSchema2022"
            }
          }
        ]
      },
      {
        "id": "did:example:abcdefghij",
        "name": "University Student Identity Services",
        "authorizedToIssue": [
          {
            "type": "StudentIdCredential",
            "credentialSchema": {
              "type": "AuthorizedIssuerJsonSchema2022",
              "schema": "{\"properties\":\{\"credentialSubject.state\":\"UA\"}}"
            }
          }
        ]
      }
    ]
  }
]
```



## 5.4. Governance Models

Governance of a Known Issuers/Verifiers Register may include the following.



* Policies that determine what requirements issuers and/or verifiers need to satisfy and comply with, in order to be registered on a Known Issuers/Verifiers Register
* Policies that determine how one can become a subscriber, and how they may access the register
* Policies about the business model of the registry
* Enforcement of these policies, e.g. what happens if an issuer or verifier starts violating the policies. Governance is about policies related to subscribers and whether/how they may access the register.
* Policies about how the policies are maintained, and who decides about those policies.
* Policies about the assurance community that governs the register, e.g. how to join or leave the assurance community

A Known Issuers/Verifiers Register also needs technical policies, which includes decisions about the data model of the register and its serialization. The present document provides a possible approach for this.


# 6. Actionable Next Steps Towards Standardization



* Analysis what aspects would lend to standardization
* Analysis what (combination of?) standards bodies would be most appropriate for the work


# 7. Conclusions and future work


## 7.1 Conclusions


## 7.2 Future work

&lt;Speculation about future Known SSI-Wallets-Supplier Registers and potential reuse of the present work on Known Issuers/Verifiers Registers.>

---


#


# Coordination stuff


# Purpose

Encourage assurance communities to implement known issuer/verifier registers to support their subscribers with a decision to trust specific issuers and/or verifiers with the issuing and/or verifying of verifiable credentials.

Encourage the development of open-source technologies and standards that enable easy, non-vendor-lock-in sharing of this information.


### Alternate Paper Titles



* Known Authority List
* As-far-as-I-know issuer/verifier list
* Sharing metadata about issuers and verifiers that you know/trust \
(too abstract?)
* Making available decentralizing issuer and verifier lists
* Sharing Issuers/Verifiers Lists
* Sharing your known Issuers/Verifiers Lists
* Decentralized Management of  Known Issuers and Verifiers
* Known Issuer and Verifier Lists
* Known Authority Lists
* AFAIK Authority Lists
* AFAIK Lists
* Known Service Provider List


### External Paper Resources

Editable pictures at [https://docs.google.com/presentation/d/1mS2pJ-x-K6E7Iv3o8NvlC5UKuS3_EwB5FlXQ6mMLwOg](https://docs.google.com/presentation/d/1mS2pJ-x-K6E7Iv3o8NvlC5UKuS3_EwB5FlXQ6mMLwOg/edit?usp=sharing)


# Creative Brief (Audience & Impact)



* Audience
    * Introduction→ general (business) audience, understandable by anyone above 5th grade level education
    * Use Cases / Requirements / Governance Models → Business / Assurance Communities
    * Data Model / Serializations → Developer Audience
* Change in behavior
    * Awareness→- make sure business-side understands the concepts (ideally, individuals understand and/or are impacted by the concepts)
    * Wallet and Verifier infrastructures to use the capabilities outlined in this document
* Key points
    * Key points are expressed in the outline of the document.
* Impact: creation and usage of the technologies and associated standards


# Concrete Personal Outcome



* Konstantin
    * Would be cool to have a standard
    * Analysis of what's going on, perhaps with a recommendation at the end
* Oskar
    * Ultimately, "Gorilla[^4] protection" – big/powerful parties (governments, businesses, service providers, guy-with-gun) that ask for more information than they strictly need for the purpose of the transaction at hand. How to prevent them from asking/obtaining that data. We need counter-balances - trusted issuer/verifier list, what solutions exist, what is still missing? Most wallets don't verify the verifier - no SSI solution says "No" to a gorilla – "blame the wallet" when a gorilla asks for your credentials.


* Isaac
    * Would like to create a specification/standard for trust lists, how to include attributes, have trust lists as reference – see what's missing, add data protections. Propose as spec/standard.
    * Technology has to be tech agnostic, not just for Blockchain, the tech should fit into different platforms.
* Shigeya
    * Want to separate discussion between governance and technical.
    * Would like to see a technology-agnostic approach. Original purpose of the paper is to use DNSSEC to deliver data.
    * Thinking about consortium issuing a sublevel of DNS and keys, DNS Zone controlled by consortium, each member agrees to join consortium, DNS Zone is part of issuer list, where members are included in the list.
    * Want to see separation between governance and technology. Eventually, good to see the standard, but don't know how that will happen, will have to wait to see about output.
* Manu
    * Interested in creating a standard, would like to see concrete output that can be put standards-track at W3C.


## Open questions



* Should a register be an entity on itself? E.g. one could claim that a credential was issued by a member of a trusted register, but without specifying exactly who was that.
* What is the thing that the register contains?
    * Bunch of public crypto keys?
    * Unqualified DIDs?
    * Credentials about the nature of the known issuers/verifiers?
    * Name and contact details of the known issuers/verifiers?
    * Purpose for which an issuer is known (e.g. a university is known for issuing diplomas)
    * Purpose for which a verifier is known (e.g. a police officer is known for verifying driver’s licenses)
* Is the word “list” appropriate? A list sounds like something that someone could print out? Better use “register”
* What types of mechanisms are we considering?
    * Centrally managed register
    * Issuer/Verifier-specific verifiable credential
    * Single VC for whole register
    * Other?
* How about the CRUD of register entries?
    * Revocation
    * Speed of updating
* How much would we discuss how implementation could enforce a register? In particular, how can issuers assure that they only issue VCs to an SSI wallet that actually enforces a specific trusted-issuer register?
*

<!-- Footnotes themselves at the bottom. -->
## Notes

[^1]:
     A pre-digital-age example is a police uniform, which enables a citizen to distinguish a police officer from a mugger for the purpose of reducing misunderstandings that could lead to violence.

[^2]:
     For forward compatibility, it should be assumed that other “known roles” could arise.

[^3]:
     Joao Rodrigues Frade (EC DG DIGIT), personal communication

[^4]:

     American expression: “What do you give to an [800-pound gorilla](https://en.wikipedia.org/wiki/800-pound_gorilla)? Anything that it asks for!”.
