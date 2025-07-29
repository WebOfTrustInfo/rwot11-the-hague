# Analysis of hybrid wallet solutions - Implementation options for combining x509 certificates with DIDs and VCs 

**Authors:** Carsten Stöcker (Spherity), Christiane Wirrig (Spherity), Paul Bastian (Bundesdruckerei, IDunion) and Steffen Schwalm (msg Group, IDunion)

**Abstract:** The EU Commission&#39;s proposal for review of the eIDAS Regulation from 2021 has opened strong expectations for a deep change in traditional identity models. The user-centric identity model proposed starts with the creation of European Digital Identity Wallets that will enable citizens&#39; (and legal entities&#39;) control over their data in identification and authentication processes without control by entities providing the identification services. Likewise digital identities and digital signatures are in place and interoperability between existing hybrid solutions mainly based on x509 certificates and decentralized PKI using DID/VC are foreseeable. This RWOT draft topic paper provides various options to address different implementation alternatives in combining x509 and DID/VC approaches.

**Keywords:** DID, eIDAS, EU Digital Wallet, hybrid model, legal trust, self-sovereign identity, SSI, x509 

## 1. Introduction

Unique identification of legal or natural entities as well as their objects – the basement for a digital identity – allows the verification of citizens or companies (Do they really exist?), persons acting for the company (Do they really exist?) and their authorization (Does Alice have a driver&#39;s license or diploma? Is Alice authorized to act for company A?).

Today, digital identities and digital signatures are typically issued by a centralized authority using [x509] certificates as well as [OIDC] and [OAuth2]-protocols. There are working well established PKI and OIDC infrastructures in place that are compliant with eIDAS 1.0 trust frameworks.

Recently, a new technology ecosystem has emerged with the intention of establishing a universal decentralised identity system based on open standards, such as W3C decentralised identities (DID) and verifiable credentials (VC), or self-sovereign identity (SSI).

Behind the development of SSI is the goal of creating a more flexible identity and trust infrastructure for the broader digitalisation of personal, government and commercial identity &amp; trust use cases. This infrastructure should enable any combination of actors along any given value or trust chain to verify provenance or authorisation properties of identity subjects.

Such an infrastructure is needed to establish authentication, authorisation and compliance applications in any digital value chain or supply chain and to secure critical infrastructures. Privacy or business confidentiality shall be enabled by the way the technology is implemented. Such an implementation paves the way for secure transactions between people, organisations and machines in the digital everyday life of a Social Network, Digital Economy, Digital State or Smart City.

The advantage of X.509 certificates is that the technology and processes, as well as their compliance verification, are known and implemented in productive applications. This advantage should not be underestimated. The X.509 infrastructure is proven and has a long tradition in the secure transmission of trusted public keys.

On the other hand, SSI built upon DIDs and Verifiable Credentials are relatively new and offer a variety of important new features for the European digitisation agenda.

SSI promises the identity owner full control over its identity and attributes [Allen]. All identity information is stored decentralized and only the holder should decide whom he will give access or transmit identification information to. Currently SSI lacks the legal trust because current [eIDAS] mainly focused on government eID not integrating the new SSI-paradigm.

Accelerated by success of DLT and developments like EBSI but also the limited utilization of existing (centralized) eID, the EU-Commission just revised eIDAS and proposed a re-engineered regulation in June 2021 – recognizing decentralization on one hand and requirement of legal trust on the other one.

An excellent property of x509 is its technology neutrality. [x509] is widely used for digital identities as well as encryption, digital signatures, or secure communication. It is internationally standardized in ISO/IEC 9594-8 [IS20] and adopted for standards of mentioned use cases e.g. ETSI ESI, [TR-02102] etc. Furthermore, it must be mentioned that x509 is also included in legal frameworks such as EU Green Certificate Regulation [COVID] or [eIDAS] [2015/1506]. So x509 contains a long successful tradition in secure digital identities, secure communication and centralized public key infrastructures including interoperability and trust.

In SSI the utilization of Decentralized Identities (DIDs) and verifiable credentials (VCs) using a Verifiable Data Registry (VDR) (mainly DID:web, DID:key, Hyperledger Indy or Ethereum) as decentralized PKI is an option used by different consortium projects in Europe e.g., ID Union, Alastria, Gaia-X, and the US e.g. Department of Homeland Security, etc.

The success of SSI depends on its interoperability with existing digital identity frameworks and public key infrastructures, for example how SSI may be leveraged by relying parties using existing identity providers or identity and access management solutions. This requires the interoperability between x509 and DID/VC. The combination of x509 and DID/VC is especially necessary if centralized PKI is established and usable for verified identity attributes in an SSI-environment based on DID/VC. With such a hybrid approach it might be possible to link DID/VC with x509 certificates to achieve legal trust. The main precondition is the recognition of relevant security, compliance, and business requirements in the given use cases.

Therefore, we expect the adoption of a hybrid approach for Digital Identity Wallet implementations in the EU and elsewhere. A proposed hybrid approach combines the following capabilities:

- existing, proven PKI infrastructures,
- proven cryptographic algorithms, primitives and protocols that are &quot;mainstream&quot; in the security community today, and
- credential formats based on logically grouped hash digests similar to the mDL (mobile driving licence) proof format and protocol already implemented in some states of the US with
- pen SSI architectures that enable self-managed, self-certifying identifiers and multi-proof formats.

There are multiple approaches to &quot;bridge&quot; trust chains in both worlds, PKI and SSI-world. Typically trust chains are bridged via a form of &quot;nested&quot; signatures. One example is the ESSIF eIDAS bridge.

This paper specifically describes and discusses possible approaches on how to technically combine x509 and DID/VC as well as the interaction with the [eIDASBridge]. The main goal is to initiate a discussion on interoperability of centralized and decentralized digital identities. The proposed approaches are a result of research projects from _GAIA-X Federation Services_ and _IDunion_ where the authors take part in.

## 2. Area of application of x509 and introduction of hybrid approaches

### 2.1 Area of application x509

Some main areas of application of x509 are:

- eID infrastructure of notified eID
- digital signatures
- digital identities in special industries e.g., energy industry, life sciences, etc.
- PKI for IoT
- SSL-certificates for internet domains and servers
- Extended SSL-certificates for verification company identities

If in any use case x509 is already in place a hybrid approach with DID/VC might be helpful for the utilization of SSI based on DID/VC.

### 2.2 Hybrid-Approaches x509 and DID/VC

Conceivable hybrid approaches for combination of x509 and DID/VC are mentioned below:

- Embedding DID in x509 certificate
- Derivation DID from x509 key pair
- Encapsulated credential during onboarding in use case domain including issuance of identity credential
- x509 based wallet infratstructure
- Signed x509 in DID-Document
- Using [eIDASBridge]

This list is not comprehensible so there are more approaches possible.

## 3. Discussion of hybrid approaches

### 3.1 Option 1: Embedding DID in x509 certificate

During issuance of a x509 certificate a signed DID will be embedded in the x509 certificate. It&#39;s necessary to ensure that a (qualified) trust service provider acc. [eIDAS] is needed to ensure that the DID is really linked to the identified natural or legal entity.

![](https://i.imgur.com/G0dcMLH.png)


Figure 1: Embedding DIDs in x509 certificates

This means that the onboarding process for x509 certificates must be changed such that the QTSP as an issuer of x509 certificates validates the signed DID of the identified natural or legal entities using a secure communication channel e.g., TLS acc. [TR02102].

Afterwards the DID will be integrated into the certificate as an x509 extension and a trusted resolver survive might be referenced in the extension as well so that the verifier gets the information how to resolve the DID from the DID document.

This means that in the results the x509 includes a DID which can be resolved by a trusted 3rd party to ensure verifiability and useability of VC of wallet service endpoint of the given holder. Any other identity x509 attributes including the Root-CA can be used as usual without any change needed.

Optionally it it possible to add more attributes in the extension of x509 certificate e.g., a link to a verifiable credential which is stored in a registry i.e., trusted registry acc. [eIDAS2]. With this VC the verifier may validate those attributes. This mechanism would be meaningful for registry modernization and automatization as required in Germany. Alternatively, the verifier may send a request to the holder to share VC as verifiable presentation.

| **Option** | **Advantages** | **Disadvantages** |
| --- | --- | --- |
| Embedding DID in x509 certificate
 | Method for combination of x509 certificates with DID for inheritance of properties/credentials of verified entities | Change in x509 issuance process including a protocol to prove that the identity subject controls a DID provided by a secure wallet infrastructure |

Table 1: Summary Option 1

### 3.2 Option 2: Derivation DID from x509 key pair

For the special use case that x509 certificates and DID use the same cryptographic primitives the key material of x509 may be used for evidence of control of the x509 certificate itself as well as the given DID document.

![](https://i.imgur.com/muIWNAh.png)


Figure 2: Derivation of a DID from x509 key pair

Public and private key pair of the x509 certificate will be used for the creation of a new DID and DID document.

This approach can be beneficial if dedicated crypto primitives are mandatorily required due to compliance, business or legal needs. In this case DID:web and DID:Key may be defined and implemented in a manner that recognizes those requirements. Additionally a service endpoint may be configured in a DID document so that the verifier can request a valid x509 certificate – a similar approach to Option 1.

Optionally a self created or delivered by QTSP credential including the x509 certificate can be used to validate the authenticity of DID for the contained x509. This requires a dedicated validation method which has to be developed and standardized.

| **Option** | **Advantages** | **Disadvantages** |
| --- | --- | --- |
| Derivation DID from x509 key pair
 | Method for combination of x509 certificates with DID for inheritance of properties/credentials of verified entities | Requires utilisation of same crypto primitives for x509 and DID as well as authoritative control for signatures in DID Document and /or the VDR |

Table 2: Summary Option 2

### 3.3 Option 3: Encapsulated credential during onboarding

The idea of option 3 is that a verification services validates if the holder really owns two private keys:

- Private key for x509 certificate
- Private key of self created (or created by TSP) DID

In this case the holder creates and signs the credential with his private keys to achieve an encapsulated data structure which contains both signatures. The aim is that the verifier is enabled to validate if the holder controls both private keys

- X509 🡪 identity proof, e.g. EV or QWAC certificate
- DID 🡪 control of DID private key

Sequence of encapsulation does not matter and may be designed according to the communication protocols in use. Alternatively, the encapsulation can also be reached with an authenticated communication channel.

![](https://i.imgur.com/Hgwq2ar.png)

Figure 3: Nested credential during onboarding

If the verifier is an onboarding or verification service, the signature can be verified directly in the encapsulated credential itself. Additionally, the x509 verification service verifies the validity and trust chain of the x509 certificate. In the next step the service (e.g., qualified attestation service as trusted issuer) can create verifiable credential for the holder where the trust is given by e.g., at the trusted issuer. One example for this approach is the experimental [BaseID] in combination with the German eID.

As an option the verification service can create an additional x509 certificate like option 1.

| **Option** | **Advantages** | **Disadvantages** |
| --- | --- | --- |
| Encapsulated credential during onboarding | Method for combination of x509 certificates with DID for inheritance of properties/credentials of verified entities Encapsulated credentials are established approachNo change in x509 specification | Additional verification service (trusted third party) for issuance of VC |

Table 3: Summary Option 3

### 3.4 Option 4: x509 based wallet infrastructure

X509 certificates may also be used to validate if the holder communicates with the infrastructure domain of a verified issuer or verifier. Under the assumption that those systems running in the same infrastructure domain the verifier may assume that the DID-based Wallet hosted in this domain is owned by the given holder.

![](https://i.imgur.com/PugGGvg.png)

Figure 4: x509 based wallet and trusted verifier who runs the wallet application on an infrastructure secured with an EV certificate

This implies that an SSI agent will create a channel to a service endpoint e.g., using an Aries DIDComm-Channel running over HTTPS. The communication is operated encapsulated with the assumption that if the user the x509 certificate of the outer channel is trustworthy (if it is e.g., a qualified website certificate acc. to Art 45 [eIDAS]) that the endpoint of HTTPS is the mentioned DID subject and consequently the verifier is trustworthy too.

The X.509 certificate can be an Extended Validation Certificate (EV) or a Qualified Website Authentication Certificate (QVAC). EV certificates are certificates conforming to X.509 that prove the legal entity of the owner and are signed by a certificate authority key that is qualified to issue EV certificates (e.g. QTSPs).

| **Option** | **Advantages** | **Disadvantages** |
| --- | --- | --- |
| Wallet infrastructure with an X.509 Certificate (e.g. Extended Validation Certificate) | Easy to implementMay solve issuer of trusted verifier | No solution for interoperability between x509 and DID/VC Only works for HTTPS-related communication while DIDComm also supports other channels like Bluetooth or NFC |

Table 4: Summary Option 4

### 3.5 Option 5: Signed x509 in DID-Document

Another option is to add a signed x509 certificate (e.g., signed by a qualified trust service provider) in the DID-document of the holder and the certificate end point in the DID-document itself. The result is an encapsulated credential like option 2. During the addition of signed x509 in DID-document this must also be signed with its private key to update the DID-document including the x509 certificate.

![](https://i.imgur.com/jJ2DrP7.png)

Figure 5: Signed x509 in DID-Document

| **Option** | **Advantages** | **Disadvantages** |
| --- | --- | --- |
| Signed x509 in DID-Document | Method for combination of x509 certificates with DID for inheritance of properties/credentials of verified entities | Addition of signed x509 in DID-document is not defined in W3C-DID-Specification, extension allowed


 Update of DID-document implies no secured link. In an improved implementation the DID will be part of the x509 certificate. |

Table 5: Summary Option 5

### 3.6 Option 6: eIDAS Bridge

Further option is the utilization of [eIDASBridge]. The [eIDASBridge]. was developed by the European Commission to establish a legal complaint link between SSI based on DID/VC and existing digital identities based on x509. It contains legal reports and technical specifications and ensures legal trust in SSI if [eIDAS2] is not fully applicable. The [eIDASBridge] implies that verifiable credentials are signed with an additional (qualified) electronic signature or seal of the issuer from a qualified trust service provider acc. to [eIDAS]. In result existing validation mechanism acc. [ETSIEN319102] can be used to make the authenticity and integrity of the VC evident against 3rd parties to fulfil the burden of proof and documentation requirements. The [eIDASBridge] mainly focus on legal trust, not primarily the interoperability between DID/VC environments and x509 identities but delivers a feasible solution for high regulated industries with its requirements on records management and archiving [Ko20], [Ko21], [We18].

![](https://i.imgur.com/ctXfKPw.png)


Figure 6: Option 6

| **Option** | **Advantages** | **Disadvantages** |
| --- | --- | --- |
| eIDAS Bridge
 | Ensures legal trust of VCVerifiability of VC by any validation service acc. eIDAS | Less feasible for interoperable attribute exchange between x509- and DID/VC-based environments |

Table 6: Summary Option 6

## 4. Outlook

The interoperability between x509 and DID/VC based digital identities as well as digital signatures can be mentioned as one of the most important success factors for SSI. If natural or legal entities are not able to use their centralized or decentralized digital identities in all environments only depending on necessary Level of Assurance acc. [eIDAS], SSI will remain academic or limited utilisation as current identities like criticized in [eIDAS2] The presented option address different aspects of this necessary interoperability between x509 and DID/VC. Further research should be targeted on these aspects. The [eIDASBridge] promises a fast adoption due to the direct combination of eIDAS-Trust services and SSI with DID/VC. The interoperability of x509 and DID/VC in the sense of data exchange and utilization between existing identity providers or IAM or digital signatures using x509 (and OIDC/OAuth2 which were hide due to limited focus) and DID/VC need further standardization in ETSI ESI and CEN. The authors will bring the research results in the European standardization acc. [eIDAS2] to solve this challenge.

## References

[2015/1506] COMMISSION IMPLEMENTING DECISION (EU) 2015/1506 of 8 September 2015 laying down specifications relating to formats of advanced electronic signatures and advanced seals to be recognised by public sector bodies pursuant to Articles 27(5) and 37(5) of Regulation (EU) No 910/2014 of the European Parliament and of the Council on electronic identification and trust services for electronic transactions in the internal market

[Al20] Alamillo Dr. I-: SSI eIDAS Legal Report. How eIDAS can legally support digital identity and trustworthy DLT-based transactions in the Digital Single Market. Brussels 2020.

[Allen] Allen, C.: [https://github.com/WebOfTrustInfo/self-sovereign-identity/blob/master/self-sovereign-identity-principles.md](https://github.com/WebOfTrustInfo/self-sovereign-identity/blob/master/self-sovereign-identity-principles.md)

[BaseID] https://www.personalausweisportal.de/Webs/PA/EN/business/the-digital-identities-project/the-digital-identities-project-node.html;jsessionid=2FAEAAFA0A8619C9A022FBFF845029A8.2\_cid373

[Co21] Corici A. et. al: Towards Interoperable Vaccination Certificate Services. 17th International Conference on Availability, Reliability and Security (ARES 2021) mGov4EU - Mobile Cross-Border Government Services for Europe 08 2021

[COVID] Regulation of the European Parliament and of the Council on a framework for the issuance, verification and acceptance of interoperable certificates on vaccination, testing and recovery to facilitate free movement during the COVID-19 pandemic (Digital Green Certificate)

[eIDAS1] Regulation (EU) No 910/2014 of the European Parliament and of the Council - of 23 July 2014 on electronic identification and trust services for electronic transactions in the internal market and repealing Directive 1999/93/EC. eIDAS, 2014.

[eIDAS2] Proposal for a REGULATION OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL amending Regulation (EU) No 910/2014 as regards establishing a framework for a European Digital Identity {SEC(2021) 228 final} - {SWD(2021) 124 final} - {SWD(2021) 125 final}

[eIDASBridge] Burgos, O. et al: SSI eIDAS Bridge - Use cases and Technical Specifications. Brusssels 2020: https://joinup.ec.europa.eu/collection/ssi-eidas-bridge/document/ssi-eidas-bridge-use-cases-and-technical-specifications

[ETSIEN319102] ETSI EN 319 102-1 Electronic Signatures and Infrastructures (ESI). Procedures for Creation and Validation of AdES Digital Signatures; Part 1: Creation and Validation

[IS20] ISO/IEC 9594-8:2020 Information technology - Open systems interconnection - Part 8: The Directory: Public-key and attribute certificate frameworks

[Ko20] Korte, U. et. al.: Criteria for trustworthy digital transactions – Blockchain/ DLT between eIDAS, GDPR, Data and Evidence Preservation. OpenIdentity Summit 2020. Lecture Notes in Informatics (LNI). Proceedings. Bonn 2020 S. 49-60

[Ko21] Korte, U. et. Al.: Records Management and Long-Term Preservation of Evidence in DLT. In: Roßnagel, H., Schunck, C. H. &amp; Mödersheim, S. (Hrsg.), Open Identity Summit 2021. Bonn: Gesellschaft für Informatik e.V.. (131-142)

[Ku20] Kubach M. et. al.: Self-sovereign and Decentralized identity as the future of identity Management?. In: Roßnagel, H., Schunck, C. H., Mödersheim, S. &amp; Hühnlein, D. (Hrsg.), Open Identity Summit 2020. Bonn: Gesellschaft für Informatik e.V.. (S. 35-47). DOI: 10.18420/ois2020\_03

[OIC] Hendrix, P et. Al.: Credential Issuer Conformance Criteria v2.0.0. W3C. 2020

[OIDC] OpenID Connect protocol: https://openid.net/connect/

[OAuth2] OAuth2 protocol: https://oauth.net/2/

[RFC5280] Cooper, D. et. Al.: Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile. 2008

[TR02102] Technical Guideline TR-020159. BSI TR-02102 Cryptographic Mechanisms. Federal Office for Information Security. https://www.bsi.bund.de/EN/Service-Navi/Publications/TechnicalGuidelines/tr02102/tr02102\_node.html

[W320] W3C: Decentralized Identifiers (DIDs) v1.0. 2020.

[We18] Weber, M. et al.: Records Management nach ISO 15489. Einführung und Anleitung. Beuth Verlag, Berlin, 2018.

[x509] https://www.itu.int/rec/T-REC-X.509/en

[Zac20] Zaccharia et. al.: EU eIDAS-Regulation: Article-by-Article Commentary. Brussels 2020
