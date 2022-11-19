# Linking verifiable credentials with the right to use data in a secure, inclusive user interaction

**Revisiting the issue of patient data exchange in a cross-border, multi-jurisdiction and inclusive setting.**

*This short paper is the outcome of a collaborative project at the 11th Rebooting Web of Trust (RWOT) workshop from September 26 to 30 2022 in Den Hague, Netherlands*. 

Keywords:
---
Data Exchange Agreements (DEXA), Data Disclosure Agreements (DDA), Data Agreements (DA), Credential presentation, Accessibility features, Overlays Capture Architecture (OCA), multi-jurisdiction use cases

[![hackmd-github-sync-badge](https://hackmd.io/1wxXNi2vSIeEv2-Ua6f1vA/badge)](https://hackmd.io/1wxXNi2vSIeEv2-Ua6f1vA)

## Authors
* Lal Chandran [LC]([iGrant.io](https://igrant.io), Sweden)
* Fredrik Lindén [FL] ([MyData](https://www.mydata.org), Sweden)
* Philippe Page [PP]([Human Colossus Foundation](https://humancolossus.foundation), Switzerland)
* Víctor Martínez Jurado [VM] ([SICPA](https://www.sicpa.com), Switzerland)
* Andrew Slack [AS] ([SICPA](https://www.sicpa.com), Switzerland)

## Contributors

The authors want to extend special thanks to the following persons that made significant contributions in developing the concepts presented in the publication.  

* Mr. Jan Linquist (Linaltec, Sweden)
* Ms. Lotta Lundin (iGrant.io, Sweden)
* Mr. Max Carlson (Govstack Initiative)
* Mr. Paul Knowles (Human Colossus Foundation, Switzerland)
* Mr. George Padayatti (iGrant.io, Sweden)
* Dr. David Goodman (iGrant.io, Sweden)
    
## Abstract

In this collaborative work from RWOT11, we revisit the issue of patient data exchange in a cross-border, multi-jurisdiction and inclusive setting. Here, we combine accessibility and the right-to-use features into data exchange scenarios using Overlays Capture Architecture (OCA) and Data Exchange Agreements (DEXA).

We elaborate on a cross-border health data exchange ecosystem where organisations and individuals across geographical borders can digitally interact, addressing key issues concerning regulatory compliance, transparency, auditability and inclusiveness of any data exchange transaction. 

First, the paper reflects on accessibility requirements and security. This is an example of a human-centric feature that must meet regulatory requirements and end-user convenience. Then we introduce the DEXA protocol. It enables human-centric automated agreement handling for data exchange between a Data Source (DS) and a Data Using Service (DUS). 

Finally, the solution is adopted in a use case for medical prescriptions delivered to a patient in a cross-border setting. The use case highlights:

1. How Data Exchange Agreements address the key requirements of GDPR in a scalable, auditable and convenient manner for all parties involved in a data exchange transaction. 
3. How language and accessibility challenges can be bridged through semantic overlays.
    
## 1. Introduction

Verifiable credentials (VC) are positioned to be critical components for the digital transformation of real-world processes. However, in doing so, VC will have to be integrated into digital processes that deliver at least the same level of security and ease of use as their physical world counterpart. Therefore, to achieve this, VC faces a few steep challenges to ensure broad adoption. In this paper, we illustrate three challenges:

- VC presentation and wallet design
- VC and multi-jurisdictional data exchange agreements
- VC and context preservation
    
The collaborative work done during the RWOT11 conference, brought together the authors from three organisations to address theses challenges: 

- [VM,AS] *Accessability* requirement for VC presentation;
- [LC,FL] *Data exchange agreements*. DEXA protocol for data exchange
- [PP,PK] *Context preservation & governance*. Overlays Capture Architecture for data presentation

To provide a clear context and link this publication to further ongoing work, we use a multi-jurisdiction version of the medical prescription use case as a reference.
    
## 2. Credential representations

The experience and security of any system operated by people depend on the information conveyed through user interfaces, the response of the users, and the interpretation of their actions. Unfortunately, existing interaction patterns in verifiable credential wallets tend towards visual-centric models that may not be accessible and rely on inconsistent data representations. 
Unlike with physical credentials, issuers of verifiable data rely on software or hardware wallets to interpret and convey information to users in a meaningful way. They also define the representation of data and user experience in critical moments of interaction, moments in which users have to make choices about sharing, accepting and verifying that data.

While there are common patterns applied today to data representation, the implementation details remain at the sole discretion of wallet providers resulting in wildly different characteristics across software, platforms and devices. UX-informing material embedded or securely referenced within verifiable data can help issuers ensure consistent, recognisable and accessible representations of the data they sign. However, consistency in representation can mean something other than uniformity. Wallets should provide cohesive, culturally and contextually relevant experiences that cater to individual preferences and needs. In addition, an individual may interact with digital artefacts from multiple issuers within a single wallet. Therefore, a balance must be struck between consistent representations of issuer data and contextually relevant appropriations.

#### Current state of the art
*<TODO> Andrew List and critique existing proposals*

Within the verifiable credential space, there are proposals for defining how a credential should be 'rendered'. For example, they propose embedding document-centric visualisations, or UI markup, in the credential schema. While this gives issuers control over the consistent representation of their data, it does not allow for contextually relevant appropriation by the wallet or consumer preference. Additionally, such approaches risk adding significant bulk to the credential size. As a result, a considerable amount of additional information must be added to the credential.

A pattern already seen in popular OS wallets is for the wallet provider to define a set number of layout types depending on data object typology; for example, Apple Wallet has 5 Pass styles: Boarding pass, Coupon, Event ticket, Store card and Generic. The data provider can then populate these layouts with attributes and attribute characteristics. This pattern provides a consistent in-wallet experience while still allowing the data provider to define specific characteristics about how the attributes are represented in different media. This mechanism helps to create distinctive representations, allowing for easier recognition and lower cognitive burdens for data consumers.

### Decoupling verification and presentation

Such an approach also decouples the verifiable data from the presentation layer, moving away from a document-centric approach to representation and instead reflecting a principle of providing verifiable data that is 'designed for appropriation'. The benefits of this are 2-fold.

* It discourages skeuomorphic representations of data objects, for example, a passport that looks like a physical passport document. This pattern is potentially dangerous since verifiable data made to look like existing physical artefacts can introduce confusion into verification flows, whereby uninformed verifiers may revert to visual checks of information, trusting visual inspections rather than cryptographically verifying the data presented.
* It allows verifiable presentations to draw on UX-informing material for attributes sourced from multiple credentials.
* It allows verifiable presentations to draw on UX-informing material for attributes sourced from multiple credentials.
*<TODO>

Andrew will add on 14/11

Describe inclusivity concerns, defining accessibility, usability and inclusivity definitions.
Describe the need for contextually relevant presentations with specific metadata available to support comprehension by assistive devices and tooling.*
Relate to the scenario

## 3 Data Exchange Agreements (DEXA) protocol

#### Background: The data exchange landscape

New data regulations are emerging worldwide, mandating organisations to implement controls and safeguards when processing, consuming and exposing personal data. Typically, this is ensured via a Data Protection Impact Assessment (DPIA) or similar detailing the purpose of data usage, the lawful basis etc.

In the DEXA framework, the DPIA results are converted to a machine-readable format and constitute the basis for any agreement between the stakeholders in the data exchange ecosystem, as illustrated in Figure 1 below.
    
![](https://i.imgur.com/0uCLE9k.png)

*Figure 1: Data Exchange Agreement Landspace [4]*

The Data Exchange Agreement (DEXA) [4] protocol suite enables automated agreement handling for data exchange between a Data Source (DS) and a Data Using Service (DUS). By creating a cryptographically signed data agreement between the individual and the organisation(s) involved, DEXA provides a human-centric and auditable approach to the data transaction. For organisations, it helps to be transparent and legitimate in their data usage while leveraging data in a scalable manner as part of a data ecosystem. Furthermore, the DEXA protocol brings in the requisite trust and governance to establish a ubiquitous data exchange space while empowering individuals to control their data.

#### The rationale for a multi-jurisdictions approach

Today, the governance of data exchanges is dependent on centralised platforms. This limits the impact of the Self-Sovereign approach for the end-user as the transaction's regulatory compliance remains under the platform's control. Despite receiving a decentralised capacity of authenticating itself, the end-user remains trapped in a "cookie" style agreement over the overall relationship instead of receiving proof of compliance specific to a transaction.

To illustrate the limitation of the platform governance approach, we revisit a classic use case of a patient receiving a medical prescription and using it to receive the medication. The thorny problem lurking behind this use case differs from the authentication of the prescription holder. Instead, it is the *double-spend* problem. How the system ensures the medication is requested only sometimes.

The "*platform approach*" might be tempting within a single jurisdiction. But when real-world constraints are applied, it quickly becomes apparent that the mesh of agreements to be satisfied by a given transaction requires either a re-centralisation of the whole process or simplification that strongly limits the applicability (and thus adoption) of the system. At a time when the concept of European-wide health data space is pushed forward, this problem needs to be addressed urgently to prevent wrong core architectures from being developed.

#### The base scenario

In our scenario, a healthcare provider in Sweden leverages the DEXA protocol to publish the availability of their prescriptions, in Swedish, in a cross-border healthcare data space. Subsequently, a Pharmacy in Zurich signs up to process the prescription in German and issues a generic medicine to the patient, Fredrik. To integrate the other challenges addressed by this paper, we also include the following constraints to illustrate the difficulties of preserving context in an inclusive digital health system:
Frederik does not understand the local language;
Frederik is visually impaired.

Section **PP: add link** introduce the Overlays Capture Architecture (OCA) to enable language localisation and to secure accessibility requirements for the credential presentation.

Our scenario requires that all transactions are auditable, and Fredrik is issued a receipt with a warning in Swedish for the possible adverse effects of taking medicine. 
The above scenario illustrates that many agreements govern the transaction in a data exchange ecosystem. The *"one-size-fits-all"* approaches will not work at scale. Integrating many contracts into a single legally binding data exchange is beyond the reach of international agreements. 

The proposed data exchange agreements attached to the transaction integrate better into the context of the relationships between organisations and individuals, depending on their roles in different usage scenarios involving personal data. The agreements can be classified into four broad categories as shown in figure below. These are agreements between:

* An individual and an organisation (data agreement)
* Two organisations, a data source and a data-using service (data disclosure agreement)
* An organisation and its supplier (data processing agreement)
* Two individuals (delegation agreement)
    
#### Data Agreements

A *Data Agreement* (DA) also referred to as a personal data agreement, exists between an organisation and an individual regarding the use and processing of personal data. A data agreement can have
any legal basis outlined by the relevant data protection regulation. The agreement can be with a data source (issuer) or a data-using service (verifier) and can also be used for personal data exchange with third parties.

A W3C-specified decentralised identifier (DID) implements the data agreement within DEXA. It records the conditions for an organisation to process personal data following the relevant data protection regulations, which could be data laws or norms such as the MyData principles.

Example of a Data Agreement as part of a credential presentation: 

![](https://i.imgur.com/jnF7zF5.jpg)

#### Data Disclosure Agreements

A *Data Disclosure Agreement* (DDA) enables automated agreement handling for data exchange between a Data Source (DS) and Data Using Service (DUS). It helps organisations to continue leveraging their data assets while being transparent and legitimate in their data usage. Automated agreement handling is a requisite for a scalable and regulatory-compliant data space. It also provides individuals control over how their data is used and exchanged.

Example of a Data Disclosure Agreement: 
**LC to add an image**

#### Data Processing Agreements
[LC] to finalise
Example of a Data Processing Agreement: 
**LC to add an image**

#### Delegation Agreements
[LC] to finalise
Example of a Delegation Agreement: 
**LC to add an image**

    
## 4 Context preservation - a Decentralised Semantic approach
*See reference [7,8]*

There is a common requirements to address the challenges presented in sections 3 (VC presentation) and section 4 (VC links to agreements): context preservation.
    In each 
Overlays Capture Architecture (OCA) is an explicit representation of task-specific objects that have deterministic relationships with other objects. These “Overlays” define individual semantic tasks, which, when combined, provide additional context to the object. An OCA bundle consists of a “Capture Base” and “Overlays”. The sum of its parts represents a contextually-rich schema.

The segregation of overlays by task enables interoperability in the construction process of any digital object without compromising the integrity of the semantic structure, modular components, or the relationship between those objects.

**4 OCA BEING REWORKED**
### Health domain regulations

Being a highly regulated domain we choose not to reference all these, but rather state that to act in the European Health Data Spaces you have a requirement on conformity testing which references several important bodies of standards. This drives the need for compliance and provenance of data. OCA has a bridge functionality to make a FHIR-profile an OCA resource.


OCA is ontology-agnostic, offering a harmonisation solution between data models and data representation formats while providing a roadmap to resolve privacy-compliant data sharing between servers, networks, and across sectoral or jurisdictional boundaries.

The deterministic interplay between overlays combined with the unicity of the composite bundle is proving to be an exciting field of research.

    OCA for inclusive representations of credentials
    
**Overlays Definitions**
In this paper, we will be primarily concerned with the following overlays:
- Capture base
- Meta overlay
- Character Encoding overlay
- Format overlay
- Label overlay
- Information overlay
    
Other overlays and OCA objects are defined in the OCA specification ([here](https://oca.colossi.network/v1.1.0-rc.html))[add reference]
    
#### The Benefits of OCA
The list of OCA benefits is maintained on the official OCA wwbsite.
    
In this work, the following OCA fatures are relevant for DEXA:

<TODO>
    
In this work, the following OCA features are relevant for accessibility:

<TODO>
        
### 3.3 Governance model
**Work iN PROGRESS**
    
### 1.4 New contribution of this paper.

<each item: write what is new>
    
1. Verified and trusted issuers

2. Trusted verifiers

3. Auditable and transparent data exchange

4. Lawful and linked to DPIA (Data Protection Impact Assessment)

5. Cross border, multi-lingual and accessible data exchange agreement
    
## 5. Conclusions  
The challenges of VCs addressed in this paper have a primary interest for any organisation currently invloved in the digital transformation of citizen centric process. This is particularly the case for the healthcare sector with large scale initiatives like the EU Health Data Space or the US-HIE (Health Information Exchange). 

The novelty of the approach we bring here is the combination of the concept of considering the user as the carrier of trust across ecosystems **[PP add references to NGI projects]** Organisations wanting a cross border exchange of data in a scalable, data regulatory compliant manner should find interest in implementing this approach through user centric data agreements. And maybe the most imortant call to action is to consider up-front the accessibility requirements, not as a secondary process done to meet inclusivity compliance requirements. 

The challenges presented here also indicates that the concept of Self-Sovereign Identity as developed until now must absolutely consider the societal landscape in which systems are being deployed. The risks of not doing so have been pointed out at ROWT11 **[PP] add links to conference of XXX and YYY**
     
## 6. Acknowledgements
   
We thank the following personnel who supported us during the course of writing this paper


## 7. References

[1] European Union e-Health network, e-prescriptions and eIDAS integrated vision: https://health.ec.europa.eu/latest-updates/eprescription-eidas-integrated-vision-2022-08-01_en (Last accessed: 08-Oct-2022)

[2] Automated Data Agreement specification, available at: https://github.com/decentralised-dataexchange/automated-data-agreements/blob/main/docs/data-agreement-specification.md (Last accessed: 08-Oct-2022)

[3] DID Data Agreement WG: https://github.com/decentralized-identity/data-agreement (Last accessed: 08-Oct-2022)

[4] iGrant.io whitepaper: Data Exchange Agreements - Removing the barriers to consent-based, auditable and immutable data transactions: https://igrant.io/papers/iGrant.io_DataExchangeAgreements_v2.0.pdf (Last accessed: 18-Nov-2022)
    
[5] Reference relevant technical standards e.g. [WCAG](https://www.w3.org/WAI/standards-guidelines/wcag) for HTML and javascript content (Last accessed: 12-Oct-2022)

[6] European digital accessibility standard for public sector organisations (EN 301 549), US Section 508 requirements for Federal Agencies
    
[7] Overlays Capture Architectures (OCA) specifications, https://oca.colossi.network/v1.1.0-rc.html (Last accessed: 11-Nov-2022)

[8] OCA transformation layer (add link:Philippe)

[9] Accessibility Specification
    
[10] An AnonCreds OCA Architecture, https://docs.google.com/presentation/d/1Ps7OPrcQBSem6ygSLSYoYq3HfpNevNYYy5e2ziGjsqU/edit#slide=id.p (Last accessed: 11-Nov-2022)

---

## Appendix 1 Use case: Using a medical prescription in a different country
 ** ADD FIGURES AND SEQUENCE DIAGRAMS**
    
A typical cross border data exchange scenario is well laid out in the European Union e-Health network, e-prescriptions and eIDAS integrated vision [1] and is as given below: 

1. A patient receives a prescription from an authorised prescriber in Country A. The wallet of the patient or their authorised representative is made aware of the prescription.

   Connection to the ePrescription service in Country A, display of ePrescriptions (as per pre- requisites)

2. A patient or their representative from Country A visits a pharmacy in Country B to get the medicine(s) prescribed in Country A.	

3. (optional) The patient or their representative identifies himself/herself in the pharmacy. 

   The case of representation (by an authorised third party, e.g. by Next of Kin) needs to be covered.	

   User identification (also: representation)

4. The health professional (pharmacist) informs the patient or their representative about their data protection rights and asks for the patient's consent (where applicable).	

    **Option A** Prescription list	The patient or their representative presents a QR code containing

    * Member State code1
    * Set of prescription holder's identifiers. 
    * Set of the wallet holder identifiers (if different from prescription holder). 
    * Timestamp and digital signature	Wallet generates QR code containing identifiers and instructions on how to fetch the prescription list1. 

    Wallet could show a prescription list to the patient

    **Option B** Specific prescription	The patient or their representative presents a QR code containing

   •	Member State code
   •	Set of prescription holder's identifiers
   •	Set of the wallet holder identifiers (if different from prescription holder)
   •	Prescription ID, dispensation PIN or other similar details

    Wallet generates QR code containing identifiers and instructions on how to fetch a specific prescription, and including limited prescription details (for offline use in exceptional situations)

  * ATC code of the prescription, IDMP attributes (such as EDQM dose form), prescribed amount or other critical data
  * Timestamp and digital signature	


5.	The dispensation provider (pharmacy) scans the QR code, verifies the digital signature and generates a request to be sent to country A based on the information included.	
 
6. A Default option	[Typical steps following the MyHealth@EU workflow leading to a possible dispensation]		

   Option B Exceptional situations (internet disruption or other similar case)	(If supported by both Country A and Country B)

   In case of disruption or other exceptional situation preventing communication via MyHealth@EU, the dispenser evaluates the possibility of dispensing medicine based on the information included in the QR code.

   If dispensation can be performed, its details will be stored in the pharmacy system. Steps under 6A Default option will need to be
performed once connectivity is restored.		

7. The pharmacist system reads the electronic Product Information and (ePI) correlates it to the patients IPS https://international-patient-summary.net/ and since the pharmacy does not have the Brand Medicine prescribed but they do have two different other brands available the system notifies based on the ePI (Electronic Product Information http://build.fhir.org/ig/HL7/vulcan-eproduct-info/toc.html). The Pharmacist gets notified visually and the Patient verbally due to the patients having enabled accessibility features in their phone, that one of the two drugs have a different chemical substance added to it that the patient is allergic/sensitive to so they need to agree on which medicine to dispense.

8.	The dispenser provides the medicine to the patient.

    In case of 6B, the dispenser manually invalidates the prescription in the Wallet app.

9.	Wallet receives updated prescription status from country A with the invalidated or updated (in case dispensed partially) dispensed prescription		

    Updated prescription status in Wallet, possibly received through a push notification.
			
10.	The workflow is terminated. No more access
to patient data from Country A is possible.		

---


### Appendix 2 Overview of OCA Overlays
For sake of completness we present here additional information on OCA valid at the time RWOT11 took place.

The OCA specification is maintained at the Human Colossus Foundation and can be accessed here **[PP] add link**. More information OCA can be found on the official [OCA website](https://oca.colossi.network).
    
    
The following OCA features to support the inclusive representation of credentials:

#### The Capture Base 
A list of attributes in the schema for credential type. The attribute is based on types defined in the OCA specification. The list of Flagged Attributes that contain identifying information. At application level the flagged attribute list is used to inform elements that should be protect against unwarranted disclosure. Such that wallets can be guided on which sensitive information should not be immediately rendered without holder intervention.
    
#### The Meta Overlay 
Defines localised meta information about the credential in a given language.

#### The Character Encoding Overlay 
Defines the encoding used for each attribute for correct display at application level.

#### Format overlay
Defines localised format the data is displayed on in a given language or preference setting. For example date-time formatting in a given calendar

#### Label Overlay
Defines the label to be used for each attribute in a given language. This label is used by Assistive Technologies (AT) to consistently describe data.

#### Information Overlay
Defines the description to be used for each attribute in a given language. This label is used by Assistive Technologies (AT) to consistently describe data.

We also propose additions to the OCA architecture to support improved usability and accessibility of data represented at the application layer.
    
#### Asset Overlay
Defines assets to be used to visually describe attributes. For example logos and icons. Within the health domain visually describing data with icons can support health professionals in parsing data, reducing cognitive burden.

```JSON
{
  "capture_base": "EPMaG1h2hVxKCZ5_3KoNNwgAyd4Eq8zrxK3xgaaRsz2M",
  "type": "spec/overlays/assets/1.0",
  "issuedBy": "../IssuerLogo.svg",
  "dateOfBirth": "../vectorIcons/calendar.svg"
}
```

#### Presentation Overlay

Defines representation of the data object at application layer, supporting accessibility concerns and providing issuer defined asthetic attributes. We propose a change to the existing 'Layout Overlay' so that representation definitions can be expressed as key, value pairs that may be interpreted by any application layer codebase.

```JSON
{
  "capture_base": "EPMaG1h2hVxKCZ5_3KoNNwgAyd4Eq8zrxK3xgaaRsz2M",
  "type": "spec/overlays/credential_representation/1.0",
    "primary_colour": "rgba(0,0,0,1)",
    "secondary_colour": "rgba(255,255,255,1)",
    "background-image": "../backgroundImage.svg",
    "minimum-contrast-ratio": "4.5:1",
    "voice": "en-US-JennyNeural", //SSML voice support
    "maximum-line-length": "70", //characters for readability
    "hyphenation": "none", //supports readability
    "primary_attribute": "fullName", //defines ordering of attributes, could alternatively be an ordered array
    "secondary_attribute": "dateofBirth",
}
```

#### Data-Representation Overlay

Defines representation of individual attributes at application layer. This may be used by data providers that need to define attribute specific representation behaviours. These definitions can be used in verifiable presentations that draw on attributes from multiple credentials.

```JSON
{
  "capture_base": "EPMaG1h2hVxKCZ5_3KoNNwgAyd4Eq8zrxK3xgaaRsz2M",
  "type": "spec/overlays/data_representations/1.0",
  "photoImage": {
        "aspect_ratio": "3:4",
        "color_space": "RGB"
        },
    "dateofBirth": {
        "color": "rgba(255,0,0,1)"
        }
    "documentType": {
        "backgroundImage": "./animatedGenerativePattern.svg"
    }
}
```
