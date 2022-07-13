[eSSIF-Lab: Towards a European SSI ecosystem](./eSSIF-Lab - Towards a European SSI ecosystem.md)

   * by [Oskar van Deventer](mailto:oskar.vandeventer@tno.nl), TNO, Netherlands
   * Overview of the eSSIF-Lab SSI ecosystem
   * #eSSIF-Lab #SSI-ecosystem #Europe



This is a proposed collaborative paper to be completed at [RWOT 2022](https://rwot11.eventbrite.com/), Den Haag, Netherlands, 26-30 September. Advance reading: see [here](https://github.com/WebOfTrustInfo/rwot11-the-hague/tree/master/advance-readings).



# eSSIF-Lab: Towards a European SSI ecosystem

Oskar van Deventer (TNO), eSSIF-Lab subgrantees (to be invited)

## Summary

eSSIF-Lab is a 7 M€, three-year (2019-2022), European-Commission-funded program that has been sponsoring start-ups, SMEs and innovators to develop open-source SSI components, SSI products and SSI services. A total of 54 eSSIF-Lab subgrantees has developed a wide variety of SSI solutions, which have been  interop-tested with other eSSIF-Lab subgrantees and innovators outside the program, which have been contributed to standardisation in W3C, Aries, DIF, OIDC and other, and which have been commercially deployed in the European market. Many eSSIF-Lab subgrantees have managed to secure external investments, and a few have even been involved in mergers & acquisitions. Many of the eSSIF-Lab outputs are available in the form of well-documented open-source code, ready for deployment. This includes SSI wallet infrastructure, SDKs for SSI wallets, SSI-standards-compliant API libraries, tooling for SSI trust infrastructure, tooling for SSI-based mandating/delegation and several other. Other eSSIF-Lab outputs are commercial propositions including SSI applications for educational credentials, for the health sector, for e-government and other.

This RWOT paper provides a selection of impactful eSSIF-Lab subgrantee projects, and provides pointers how to download or use these results for your own SSI projects.

## 1. Introduction: SSI and eSSIF-Lab

Self-Sovereign Identity (SSI) does not need any introduction in the context of RWOT [1]. People are encouraged to read primers on SSI e.g. here: [2], [3], [4], [5].

eSSIF-Lab [6] (European Self-Sovereign-Identity-Framework Laboratory) is part of of the Next Generation Internet (NGI) programme, organised by the European Commission in the context of the Horizon 2020 Research and Innovation Actions [7] funding. eSSIF-Lab was partly modeled after the Silicon Valley Innovation Programme [8] (SVIP) of the American Deparment of Homeland Services. **<u>*< ... more about eSSIF-Lab, its consortium, its goverance, budgets, numbers, etcetera ... >*</u>** 

eSSIF-Lab booklet [9]

Relation with EBSI-ESSIF [10]

## 2. eSSIF-Lab subgrantee project results

**<u>*< ... To be discussed whether a further structuring is useful, e.g. one subsection for library projects, another for SSI wallets, etcetera ... >*</u>**

### 2.1 Automated data agreements by iGrant.io (Sweden)

The ADA project [11] builds a fully auditable digital infrastructure that enables sustainable use, reuse and exchange of personal data to enable advanced digitalisation enforced via Data Agreements. A Data Agreement records the conditions for an organisation to process personal data following privacy regulations (e.g. GDPR) captured as a signed receipt given to an individual and to organisations wishing to record their personal data processing. The receipt acts as evidence, demonstrates a higher level of accountability, and is based on standard schemas. The accountability is further enhanced by directly integrating the Data Agreement with the input from a risk assessment, e.g. Data Protection Impact Assessment.

Once created, the Data Agreement is integrated into SSI-based workflows, resulting in an easy-to-adopt and automated solution for data exchange, making every transaction trustworthy, auditable and immutable.

The Data Agreement specification is openly available [12] and implemented over DIDComm protocol, integrated into Aries and EBSI (European Blockchain Service Infrastructure) presentation exchanges. 

### 2.2 eSSIF-Lab subgrantee project BBB

### 2.3 eSSIF-Lab subgrantee project CCC

## 3. SSI standardisation and interop testing

< ... Further structuring to be discussed ... >

### 3.1 Data Agreement standards and Interop

The Data Agreement schema is standardised as part of ISO 27560 and driven via DIF (Decentralized Identity Foundation) Data Agreement WG [13]. The DIF workgroup will further investigate standardising the DID:mydata introduced as part of the Automated Data Agreement project by iGrant.io (Sweden).

### 3.2 Standard/interop YYY

### 3.3 Standard/interop ZZZ

## 4. Conclusions

## 5. References

[1] https://rwot11.eventbrite.com/ 

[2] [The Path to Self-Sovereign Identity (lifewithalacrity.com)](http://www.lifewithalacrity.com/2016/04/the-path-to-self-soverereign-identity.html)

[3] [Self-Sovereign Identity - the good, the bad and the ugly; May 2019 | TNO](https://blockchain.tno.nl/blog/self-sovereign-identity-the-good-the-bad-and-the-ugly/)

[4] [rwot11-the-hague/advance-readings at master · WebOfTrustInfo/rwot11-the-hague (github.com)](https://github.com/WebOfTrustInfo/rwot11-the-hague/tree/master/advance-readings)

[5] **<u>*< ... more SSI references ... >*</u>**

[6] [eSSIF-Lab | eSSIF-Lab: Help Shape a Safe and Secure Next Generation InternetT GENERATION INTERNET](https://essif-lab.eu/)

[7] [h2020-wp1820-annex-d-ria_en.pdf (europa.eu)](https://ec.europa.eu/research/participants/data/ref/h2020/other/wp/2018-2020/annexes/h2020-wp1820-annex-d-ria_en.pdf)

[8] [SVIP | Homeland Security (dhs.gov)](https://www.dhs.gov/science-and-technology/svip)

[9] [essif booklet 22 (essif-lab.eu)](https://essif-lab.eu/wp-content/uploads/2022/03/essif-booklet-22-1.pdf)

[10] [High-level scope (ESSIF) - EBSI Documentation - (europa.eu)](https://ec.europa.eu/digital-building-blocks/wikis/pages/viewpage.action?pageId=379913698)

[11] Automated Data Agreement by iGrant.io, avaialble at: https://essif-lab.eu/automated-data-agreements-to-simplify-ssi-work-flows-by-igrant-io/

[12] Automated Data Agreement specification, available at: https://github.com/decentralised-dataexchange/automated-data-agreements/blob/main/docs/data-agreement-specification.md

[13] DID Data Agreement WG: https://github.com/decentralized-identity/data-agreement
