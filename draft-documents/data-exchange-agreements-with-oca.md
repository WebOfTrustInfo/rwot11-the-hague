# A semantic approach to auditability and inclusivity for cross border, multi-jurisdiction personal data exchange (Work in progrss. Draft version)

Keywords: Data Exchange Agreements (DEXA), Data Disclosure Agreements (DDA), Data Agreements (DA), Credential presentation, Accessibility features, Overlays Capture Architecture (OCA) for multi-jurisdiction use cases

[![hackmd-github-sync-badge](https://hackmd.io/1wxXNi2vSIeEv2-Ua6f1vA/badge)](https://hackmd.io/1wxXNi2vSIeEv2-Ua6f1vA)

## Authors
* Lal Chandran (iGrant.io, Sweden)
* Fredrik Lindén (MyData.org, Sweden)
* Philippe Page (Human Colossus Foundation, Switzerland)
* Víctor Martínez Jurado (SICPA, Switzerland)
* Andrew Slack (SICPA, Switzerland)

<Please add>

## Contributors
    
* Mr. Jan Linquist (Linaltec, Sweden)
* Ms. Lotta Lundin (iGrant.io, Sweden)
* Mr. Max Carlson (Govstack Initiative)
* Mr. Paul Knowles (Human Colossus Foundation, Switzerland)
* Mr. George Padayatti (iGrant.io, Sweden)
* Dr. David Goodman (iGrant.io, Sweden)
    
<Please add>

## Abstract

***WORK IN PROGRESS***

This paper is a collaborative project at the 11th Rebooting of Web of Trust (RWOT) workshop in The Hague in September 2022.  It brings together DEXA (Data exchange agreements) [4] and OCA (Overlays Capture Architecture) a decentralised semantic architecture [add reference].

We address the question of regulated data exchange across jurisdictions. It elaborates on a cross-border data exchange ecosystem where organisations and individuals across geographical borders can digitally interact addressing key issues concerning compliance, transparency, auditability and inclusiveness of any data transaction.

We start by introducing Data Exchange Agreement (DEXA) protocol suite that enables human-centric automated agreement handling for data exchange between a Data Source (DS) and a Data Using Service (DUS). Then accessibility features are introduced as an example of human centric feature that needs to meet regulatory requirements. The introduction ends with an explanation on how semantic is introduced to maintain context and purpose through out the process.

Using OCA (Overlay Capture Architecture) in DEXA ensures cross-border data exchange across multiple jurisdictions while addressing accessibility concerns. The solution is described through a use case of a prescription delivered to a patient. The prescription issued to the patient by a healthcare entity is used to receive medicines from a pharmacy while catering to the following:

1. An auditable signed and counter signed agreement compliant to gdpr describing the prescription usage is generated during the data exchange transaction. 

2. Localisation and accessability features, for e.g. vision impared patients are taken care using semantic overlays.

**Table of Contents** 
> [TOC]

## 1. Introduction
*WHERE WE INTRODUCE THE 3 MAIN SUBJECTS, AUDITABILITY, ACCESSABILITY FEATURES, SEMANTIC*

### 1.1 Credential representations

The experience and security of any system operated by people depends on the information conveyed through user interfaces, the response of the users, and the interpretation of their actions. Existing interaction patterns in verifiable credential wallets tend towards visual-centric models that may not be accessible and rely on inconsistent representations of data. Unlike with physical credentials, issuers of verifiable data rely on software or hardware wallets to interpret and convey information to users in a meaningful way, defining the representation of data and user experience in key moments of interaction; moments in which users have to make choices about sharing, accepting and verifying that data.

While there are common patterns applied today to the representation of data, the implementation details remain at the sole discretion of wallet providers resulting in wildly different characteristics across various software, platforms and devices. UX-informing material embedded or securely referenced within verifiable data can help issuers ensure consistent, recognisable and accessible representaions of the data they sign. However, there are equally benefits that arise from variations in representation across wallets such as providing options for users to choose culturally relevant experiences that cater to individual preferences and needs. Wallet-driven conformity of representations can also help to provide cohesive, crafted, contextual and environment specific experiences for users that may interact with these digital artefacts across multi-modal endpoints.
    
There are existing proposals for defining how credentials should be 'rendered':

<TODO>
List and critique existing proposals

A pattern already seen in popular OS wallets is for wallets to define a set number of layout types depending on data object typology, for example Apple Wallet has 5 Pass styles: Boarding pass, Coupon, Event ticket, Store card and Generic. These layouts can then be populated with attributes and attribute characteristics by the data provider. This pattern provides a consistent in-wallet experience while still allowing the data provider to define certain characteristics about how the attributes are represented in different media. This helps to create distinctive representations, allowing for easier recognition and lower cognitive-burdens for users.

Such an approach also decouples the verifiable data from the presentation layer, in doing so moving a way from a document-centric approach to representation and instead reflecting a principle of providing verifiable data that is 'designed for appropriation'. The benefits with this are 2-fold.

* It discourages skeuomorphic representations of data objects, for example a passport that looks like a physical passport document. This is a potentially dangerous pattern since verifiable data that is made to look like existing physical artefacts can introduce confusion into verification flows, whereby uninformed verifiers may revert to visual checks of information, trusting visual checks rather than cryptographically verifying the information presented.
* It allows verifiable presentations to draw on UX-informing material for attributes sourced from multiple credentials.

<TODO>
Describe inclusivity concerns, defining accessibility, usability and inclusivity definitions.
Reference supplementary paper on the topic.
Describe the need for contextually relevant presentations with specific metadata available to support comprehension by assistive devices and tooling.

### 1.2 Data exchange Auditability - The DEXA Protocol

***WORK IN PROGRESS***

#### Background
**The Data Exchange Landscape**
The Data Exchange Agreement (DEXA) protocol suite enables human-centric automated agreement handling for data exchange between a Data Source (DS) and a Data Using Service (DUS). It helps organisations to be transparent and legitimate in their data usage while leveraging data in a scalable manner as part of a data ecosystem. Furthermore, the DEXA protocol brings in the requisite trust and governance to establish a ubiquitous data exchange space while empowering individuals to be in control of their data. All organisations need to ensure that they are on the right side of the law (e.g. the GDPR) when consuming personal data (risk management) and to establish the digital trust needed for individuals to say yes to sharing their data.

Using OCA (Overlay Capture Architecture) in DEXA ensures cross-border data exchange across multiple jurisdictions while addressing accessibility concerns.

In our scenario, a healthcare provider in Sweden could leverage the protocol to publish the availability of their prescriptions, in Swedish, in a cross-border healthcare data space. A Pharmacy in Zurich could sign up to read the prescription in German and issue a generic medicine to Fredrik. The use of OCA enables language localisation and ensures Fredrik, who is visually impaired, can understand the Data Agreement presented by the Pharmacy during the transaction. All transactions are auditable, and Fredrik is issued a receipt with a warning in Swedish for the possible adverse effects of taking the medicine. 
In a data exchange ecosystem, there are a number of agreements that are required to legally validate data exchanges. The various data exchange agreements contextualise the relationships that exist between organisations and individuals, depending on their roles in different usage scenarios involving personal data. The various agreements involved can be classified into four broad categories as shown in figure below. These are agreements between:

* An individual and an organisation (data agreement)
* Two organisations (a data source and a data using service (data disclosure agreement)
* An organisation and its supplier (data processing agreement)
* Two individuals (delegation agreement)

<data exchange landscape picture>
    
#### Data Agreements
A data agreement, also referred to as a personal data agreement, exists between an organisation and an individual regarding the use and processing of personal data. A data agreement can have
any legal basis as outlined by the relevant data protection regulation. The agreement can be with a data source (issuer) or a data using service (verifier) and can also be used for personal data exchange with third parties.

Today, a data agreement is implemented via a W3C-specified decentralised identifier (DID). It records the conditions for an organisation to process personal data in accordance with the relevant data protection regulations which could be data laws or norms such as the MyData principles.

Example of a Data Agreement: 

![](https://i.imgur.com/HP5a6Du.jpg)

    
#### Data Disclosure Agreements
A Data Disclosure Agreement (DDA) enables automated agreement handling for data exchange between a Data Source (DS) and Data Using Service (DUS). It helps organisations to continue leveraging their data assets while being transparent and legitimate in their data usage. Automated agreement handling is a requisite for a scalable and regulatory-compliant data space. It also provides individuals control over how their data is used and exchanged.

*EXAMPLE OF A DATA DISCLOSURE AGREEMENT*

    
### 1.3 Context preservation - Semantic approach - the Overlays Capture Architecture (OCA)
*See reference [7,8]*
    
Overlays Capture Architecture (OCA) is an explicit representation of task-specific objects that have deterministic relationships with other objects. These “Overlays” define individual semantic tasks, which, when combined, provide additional context to the object. An OCA bundle consists of a “Capture Base” and “Overlays”. The sum of its parts represents a contextually-rich schema.

The segregation of overlays by task enables interoperability in the construction process of any digital object without compromising the integrity of the semantic structure, modular components, or the relationship between those objects.
    
OCA is ontology-agnostic, offering a harmonisation solution between data models and data representation formats while providing a roadmap to resolve privacy-compliant data sharing between servers, networks, and across sectoral or jurisdictional boundaries.

The deterministic interplay between overlays combined with the unicity of the composite bundle is proving to be an exciting field of research.

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
    
### 1.4 New contribution of this paper.

<each item: write what is new>
    
1. Verified and trusted issuers

2. Trusted verifiers

3. Auditable and transparent data exchange

4. Lawful and linked to DPIA (Data Protection Impact Assessment)

5. Cross border, multi-lingual and accessible data exchange agreement
    
## 2. Use case: Using a medical prescription in a different country

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
* Overlay Capture Architecture (OCA): 

#### Usecases using DEXA with OCA
    
**Example uses within the scenario**
    
**Representing a credential in a web-wallet**

**Representing a credential in a native wallet**

**Representing a credential in a paper based format**


## 3. Analysis & Proposals
***WORK IN PROGRESS***
### 3.1 Health domain regulations

Being a highly regulated domain we choose not to reference all these, but rather state that to act in the European Health Data Spaces you have a requirement on conformity testing which references several important bodies of standards. This drives the need for compliance and provenance of data. OCA has a bridge functionality to make a FHIR-profile an OCA resource.


### 3.2 OCA for inclusive representations of credentials
    
We propose the use of the following OCA features to support inclusive representation of credentials:

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
Defines assets to be used to visually describe attributes. For example logos and icons. Within the health domain context visually describing data with icons can support health professionals in visually parsing data, reducing cognitive burden.
    
<to add NHS icon example>

```JSON
{
  "capture_base": "EPMaG1h2hVxKCZ5_3KoNNwgAyd4Eq8zrxK3xgaaRsz2M",
  "type": "spec/overlays/assets/1.0",
  "issuedBy": "../IssuerLogo.svg",
  "dateOfBirth": "../vectorIcons/calendar.svg"
}
```

#### Presentation Overlay

Defines representation of the data object at application layer, supporting accessibility concerns and providing issuer defined asthetic attributes. We propose a change to the existing Layout Overlay so that representation definitions can be expressed as key, value pairs that may be interpreted by any application layer codebase.

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

Defines representation of individual attributes at application layer. This may be used by data providers that need to define attribute specific representation behaviours. These definitions can be drawn on in verifiable presentations that draw on attributes from multiple credentials.

```JSON
{
  "capture_base": "EPMaG1h2hVxKCZ5_3KoNNwgAyd4Eq8zrxK3xgaaRsz2M",
  "type": "spec/overlays/data_representations/1.0",
  "photoImage": {
        "aspect_ratio": "3:4",
        "colour_space": "RGB"
        },
    "dateofBirth": {
        "color": "rgba(255,0,0,1)"
        }
    "documentType": {
        "backgroundImage": "./animatedGenerativePattern.svg"
    }
}
```

    
### 3.3 Governance model
**Work iN PROGRESS**

## 4. Further research

## 5. Acknowledgements
    
## 6. References

[1] European Union e-Health network, e-prescriptions and eIDAS integrated vision: https://health.ec.europa.eu/latest-updates/eprescription-eidas-integrated-vision-2022-08-01_en

[2] Automated Data Agreement specification, available at: https://github.com/decentralised-dataexchange/automated-data-agreements/blob/main/docs/data-agreement-specification.md

[3] DID Data Agreement WG: https://github.com/decentralized-identity/data-agreement

[4] Data Exchange Agreements:  
    
[5] Reference relevant technical standards e.g. [WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/) for HTML and javascript content.

[6] European digital accessibility standard for public sector organisations (EN 301 549), US Section 508 requirements for Federal Agencies
    
[7] Overlays Capture Architectures (OCA) specifications, https://oca.colossi.network/v1.1.0-rc.html

[8] OCA transformation layer (add link:Philippe)

[9] Accessibility Specification
    
[10] An AnonCreds OCA Architecture, https://docs.google.com/presentation/d/1Ps7OPrcQBSem6ygSLSYoYq3HfpNevNYYy5e2ziGjsqU/edit#slide=id.p
  
## SCRAP PAD
    
**Who's your audience?**

    
    Organisations wanting a cross border exchange of data in a scalable, data regulatory compliant manner.
    e.g. EU e-health network and US-HIE:s (Health Information Exchanges)
    
**What change in their behavior do you want to induce? (Call to Action)**
    
    * Adopt the values offered by self-sovereign technologies
    * Any organisations can be part of a cross border data exchange ecosystem 
    
**What are the key points you're going to include?**

    * Introduction
      * Data Exchange Landscape
      * Introduce Data Exchange Agreements 
      * Introduce OCA and its capabilities
      * Combine DEXA with OCA
    * Benefits
    * Usecase scenario
    
    
XXXXXXXXXX
In our scenario, a healthcare provider in Sweden could leverage the protocol to publish the availability of their prescriptions, in Swedish, in a cross-border healthcare data space. A Pharmacy in Zurich could sign up to read the prescription in German and issue a generic medicine to Fredrik. The use of OCA enables language localisation and ensures Fredrik, who is visually impaired, can understand the Data Agreement presented by the Pharmacy during the transaction. All transactions are auditable, and Fredrik is issued a receipt with a warning in Swedish for the possible adverse effects of taking the medicine. 