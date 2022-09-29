# Data exchange agreements over OCA for an accessible, scalable and auditable data exchange ecosystem

[![hackmd-github-sync-badge](https://hackmd.io/1wxXNi2vSIeEv2-Ua6f1vA/badge)](https://hackmd.io/1wxXNi2vSIeEv2-Ua6f1vA)

## Authors
* Lal Chandran (iGrant.io, Sweden)
* Fredrik Linden (MyData.org, Sweden)
* Philippe Page (Human Colossus Foundation, Switzerland)
* Víctor Martínez Jurado (SICPA, Switzerland)
* Andrew Slack (SICPA, Switzerland)

<Please add>

## Contributors
    
* Mr. Jan Linquist (Linaltec, Sweden)
* Ms. Lotta Lundin (iGrant.io, Sweden)
* Mr. Max Carlson (Govstack Initiative)
* Paul Knowles (Human Collassus Foundation, Switzerland)
* Mr. George Padayatti (iGrant.io, Sweden)
* Dr. David Goodman (iGrant.io, Sweden)
    
<Please add>

## Abstract

This paper is a collaborative project at the 11th Rebooting of Web of Trust (RWOT) workshop in The Hague in September 2022. We present the Data Exchange Agreement (DEXA) protocol suite that enables human-centric automated agreement handling for data exchange between a Data Source (DS) and a Data Using Service (DUS). It helps organisations to be transparent and legitimate in their data usage while leveraging data in a scalable manner as part of a data ecosystem. Furthermore, the DEXA protocol brings in the requisite trust and governance to establish a ubiquitous data exchange space while empowering individuals to be in control of their data. All organisations need to ensure that they are on the right side of the law (e.g. the GDPR) when consuming personal data (risk management) and to establish the digital trust needed for individuals to say yes to sharing their data.

Using OCA (Overlay Capture Architecture) in DEXA ensures cross-border data exchange across multiple jurisdictions while addressing accessibility concerns.

In our scenario, a healthcare provider in Sweden could leverage the protocol to publish the availability of their prescriptions, in Swedish, in a cross-border healthcare data space. A Pharmacy in Zurich could sign up to read the prescription in German and issue a generic medicine to Fredrik. The use of OCA enables language localisation and ensures Fredrik, who is visually impaired, can understand the Data Agreement presented by the Pharmacy during the transaction. All transactions are auditable, and Fredrik is issued a receipt with a warning in Swedish for the possible adverse effects of taking the medicine. 

**Table of Contents** 
> [TOC]

## Introduction

### Data Exchange Landscape

In a data exchange ecosystem, there are a number of agreements that are required to legally validate data exchanges. The various data exchange agreements contextualise the relationships that exist between organisations and individuals, depending on their roles in different usage scenarios involving personal data. The various agreements involved can be classified into four broad categories as shown in figure below. These are agreements between:

* An individual and an organisation (data agreement)
* Two organisations (a data source and a data using service (data disclosure agreement)
* An organisation and its supplier (data processing agreement)
* Two individuals (delegation agreement)

<data exchange landscape picture>
    
### Data Exchange Agreements 

#### Data Agreement

A data agreement, also referred to as a personal data agreement, exists between an organisation and an individual regarding the use and processing of personal data. A data agreement can have
any legal basis as outlined by the relevant data protection regulation. The agreement can be with a data source (issuer) or a data using service (verifier) and can also be used for personal data exchange with third parties.

Today, a data agreement is implemented via a W3C-specified decentralised identifier (DID). It records the conditions for an organisation to process personal data in accordance with the relevant data protection regulations which could be data laws or norms such as the MyData principles.
    
#### Data Disclosure Agreements

A Data Disclosure Agreement (DDA) enables automated agreement handling for data exchange between a Data Source (DS) and Data Using Service (DUS). It helps organisations to continue leveraging their data assets while being transparent and legitimate in their data usage. Automated agreement handling is a requisite for a scalable and regulatory-compliant data space. It also provides individuals control over how their data is used and exchanged.

### Overlays Capture Architecture OCA
*See reference [7,8]*
    
Overlays Capture Architecture (OCA) is an explicit representation of task-specific objects that have deterministic relationships with other objects. These “Overlays” define individual semantic tasks, which, when combined, provide additional context to the object. An OCA bundle consists of a “Capture Base” and “Overlays”. The sum of its parts represents a contextually-rich schema.

The segregation of overlays by task enables interoperability in the construction process of any digital object without compromising the integrity of the semantic structure, modular components, or the relationship between those objects.
    
OCA is ontology-agnostic, offering a harmonisation solution between data models and data representation formats while providing a roadmap to resolve privacy-compliant data sharing between servers, networks, and across sectoral or jurisdictional boundaries.

The deterministic interplay between overlays combined with the unicity of the composite bundle is proving to be an exciting field of research.

### The Benefits of OCA
The list of OCA benefits is maintained on the official OCA wwbsite.
    In this work, the following OCA fatures are relevant for DEXA:
    ...
    ...
In this work, the following OCA fatures are relevant for accessibility features:
    ...
    ...
    
    
## Benefits of DEXA with OCA

1. Verified and trusted issuers

2. Trusted verifiers

3. Auditable and transparent data exchange

4. Lawful and linked to DPIA (Data Protection Impact Assessment)

5. Cross border, multi-lingual data exchange agreement
    
## Use cases

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

7. The pharmacist system reads the electronic Product Information and (ePI) correlates it to the patients IPS https://international-patient-summary.net/ and since the pharmacy does not have the Brand Medicine prescribed but they do have two different other brands available the system notifies (the Pharmacist (visually) and the Patient (verbally due to the patients having enabled accessibility features in their phone)that one of the two two drugs have a different chemical substance added to it that the patient is allergic/sensitive to so they need to agree on which medicine to dispense.

8.	The dispenser provides the medicine to the patient.

    In case of 6B, the dispenser manually invalidates the prescription in the Wallet app.

9.	Wallet receives updated prescription status from country A with the invalidated or updated (in case dispensed partially) dispensed prescription		

    Updated prescription status in Wallet, possibly received through a push notification.
			
10.	The workflow is terminated. No more access
to patient data from Country A is possible.		

### Health domain regulations

Being a higly regulated domain we choose not to reference all these, but rather state that to act in the European Health Data Spaces you have a requirement on conformity testing which references several important bodies of standards. This drives the need for compliance and provenance of data. OCA has a bridge functionality to make a FHIR-profile an OCA resource.

## OCA key functions

* Credentials (including data agreements) need to be accessible across multi-modal endpoints
* Accessibility concerns include common disability concerns but also incidental and environmental barriers to users that are context specific (technology access, lanuage..).
* To ensure inclusivity and support public wide adoption credentials need to be rendered as contextually relevant presentations with specific metadata available to support comprehension by assistive devices and tooling. e.g. this will be different across iOS, HTML, other
    
    
- Overlay Capture Architecture (OCA):

## Usecases using DEXA with OCA
    
### Example uses within the scenario
    
#### Representing a credential in a web-wallet


#### Representing a credential in a native wallet


## References

[1] European Union e-Health network, e-prescriptions and eIDAS integrated vision: https://health.ec.europa.eu/latest-updates/eprescription-eidas-integrated-vision-2022-08-01_en

[2] Automated Data Agreement specification, available at: https://github.com/decentralised-dataexchange/automated-data-agreements/blob/main/docs/data-agreement-specification.md

[3] DID Data Agreement WG: https://github.com/decentralized-identity/data-agreement

[4] Data Exchange Agreements:     
    
[5] Reference relevant technical standards e.g. [WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/) for HTML and javascript content.

[6] European digital accessibility standard for public sector organisations (EN 301 549), US Section 508 requirements for Federal Agencies
    
[7] Overlays Capture Architectures (OCA) specifications, https://oca.colossi.network/v1.1.0-rc.html

[8] OCA transformation layer (add link:Philippe)

[9] Accessibility Specification
  
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