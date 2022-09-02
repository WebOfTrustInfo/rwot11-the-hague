# Data Exchange Agreements - Making data transactions trustworthy, auditable and immutable

- Mr. Lal Chandran (iGrant.io, Sweden)
- Mr. Jan Linquist (Linaltec, Sweden)
- Ms. Lotta Lundin (iGrant.io, Sweden)
- Mr. Max Carlson (Govstack Initiative)
- Paul Knowles (Human Collassus Foundation, Switzerland)
- Dr. Philippe Page (Human Collassus Foundation, Switzerland)
- Mr. George Padayatti (iGrant.io, Sweden) 
- Dr. David Goodman (iGrant.io, Sweden)
- Mr. Fredrik Linden (MyData, Sweden)

## Abstract

The Data Exchange Agreement provides a suite of tools that enable automated agreement handling for data exchange between a Data Source (DS) and a Data Using Service (DUS). It helps organisations to be transparent and legitimate in their data usage while leveraging their data assets. Automated agreement handling is required for a scalable and regulatory-compliant data marketplace (data space). It also provides individuals control over how their data is used and exchanged.

This RWOT paper provides information on how any organisation can leverage data using SSI and non-SSI protocols while being lawful, scalable and trustworthy.

The project has been supported by multiple NGI-Trust initiatives. NGI-Trust eSSIF-Lab and NGI-Trust ONTOCHAIN. NGI eSSIF-Lab funded earlier work around Data Agreement [1], while NGI-ONTOCHAIN supported the key work involving Data Exchange Agreements and Data Provenance [4]. 

## Introduction

Data is the ​critical currency of an advanced digital economy, and trust is fundamental for continuous access to personal data. An adequate governance framework is essential to build the requisite trust and must involve, at the very least, the following actors:

- **Individuals**, who can manage their preferences and follow their data, should know who is consuming what, when and why.

- **Organisations**, which are either a DS or a DUS, should be able to leverage personal data and gain access to the right quality data, provided that:

   - they offer adequate transparency for individuals to trust them.
   - their data usage complies with the relevant data protection and privacy regulations which they can prove if requested.

- **Auditors**, who can independently prove fair data usage via independent audit mechanisms, can be used by organisations and individuals to ​verify the legitimacy of their claims in any legal dispute concerning the use or misuse of data.

Any organisation undergoing digital transformation needs to ensure that it can cater to the above, so individuals continue to say “yes” to sharing their data. Initiatives like **MyData Operator** and the proposed EU Data Governance Act point to the need for **data intermediaries** ​to enable the above for individuals and businesses.

The data exchange agreement suit aims to enhance data governance to ​increase transparency and authenticity as ​critical elements for digital trust. This paper describes how the key actors above can capture, view or disclose the provenance trail of a personal data exchange transaction​,​ starting with ​creating data disclosure agreements during any such data exchanges. It also specifies how a DS can define rules for data processing (to demonstrate regulatory compliance etc.) in a data exchange transaction.

## Proposal

This paper proposes a framework starting with a data exchange landscape and how to achieve lawful, auditable, immutable and trustworthy data exchange via a data exchange agreement suit. 

## Standardisation

The Data Agreement schema is standardised as part of ISO 27560 and driven via DIF (Decentralized Identity Foundation) Data Agreement WG [13]. The DIF workgroup will further investigate standardising the DID:mydata introduced as part of the Automated Data Agreement project by iGrant.io (Sweden).

## Near-term use cases

Following near-term use cases are identified to validate and roll out the DEXA protocols:

1) Govstack Inititiative (Consent building block)

2) NGI-Trust ONTOCHAIN and NGI eSSIF-Lab data exchange with decentralised digital wallets

3) Healthcare data sharing and system demonstrator projects (Swedish innovation agency, Vinnova)

4) Data4Diabetes use case from iGrant.io, MyData (Sweden) via Data Spaces

## References

[1] Automated Data Agreement by iGrant.io, available at: https://essif-lab.eu/automated-data-agreements-to-simplify-ssi-work-flows-by-igrant-io/ (NGI-Trust eSSIF-Lab)

[2] Automated Data Agreement specification, available at: https://github.com/decentralised-dataexchange/automated-data-agreements/blob/main/docs/data-agreement-specification.md

[3] DID Data Agreement WG: https://github.com/decentralized-identity/data-agreement

[4] Data Exchange Agreements: https://github.com/decentralised-dataexchange/data-exchange-agreements (NGI-Trust ONTOCHAIN)