# Advance Readings

In advance of the design workshop, all participants produced a one-or-two page advance reading to be shared with the other attendees on either:

* A specific problem that they wanted to solve with a web-of-trust solution, and why current solutions (PGP or CA-based PKI) can't address the problem?
* A specific solution related to the web-of-trust that you'd like others to use or contribute to?

If you will be attending Rebooting the Web of Trust Fall 2022 in The Hague, Netherlands, please upload your advance readings to this directory with a pull request.

## Pull Request Submission

To add a paper, create a pull request to this repo with your contribution (preferably as an .md file, but if you can't, as a PDF), along with updates to the README.md in this folder. Please also include a byline with contact information in the paper itself.

Please also enter your paper _twice_ in this README file, once in the topical listing (adding a new category describing your topic, if necessary) and one in the alphabetical listing. Please be sure to include the full URL for your paper in the README, so that we can copy it to the main page URL and have it still correctly link.

If you don't know how to submit a pull request, please instead submit an issue.

## Request RWOT11 discount code

To those who have submitted an Advance Readings paper, RWOT11 offers a steep discount on the ticket price for participation to the event. Please obtain your discount code as follows.
* Copy the link to your Pull Request (see previous section)
* Email to [questions@weboftrust.info](mailto:questions@weboftrust.info), paste the link to the Pull Request and ask for the discount code

Please make sure to make your Pull Request Submission BEFORE you buy the tickets for RWOT11, in order to apply your discount code.

## Primer Listing

These primers overview major topics which are likely to be discussed
at the design workshop. If you read nothing else, read these. (But
really, read as much as you can!)

* [Advance Reading Primer](./advance-reading-primer.md) — About the advance reading papers
* [RWOT Primer](./rwot-primer.md) — How the design workshop works
* [DID Primer](./did-primer.md) — Decentralized Identifiers ([extended version](./did-primer-extended.md) also available)
* [Functional Identity Primer](./functional-identity-primer.md) — A different way to look at identity
* [Verifiable Credentials Primer](./verifiable-credentials-primer.md) — the project formerly known as Verifiable Claims
* [Glossary of Terms](./glossary-primer.md) — a brief dictionary of technical terms used at RWOT
* [Data Generator](./data-generator.md) — a data-generator for SSI

## Topical Listing

_Please add a level three header (`###`) for your paper's topic if it's not there already, then link it in the form:_

```
[name](link)
   * by [author](mailto:if desired)
   * One to two sentence synopsis or quote
   * #hashtags for topics
```


### [CESR adapter for sophisticated multisig](https://hackmd.io/GbQO3p6QTge-8eQMGuMaeQ)
   * by [Henk van Cann](mailto:h.vancann@blockchainbird.org), Blockchainbird.org, The Netherlands
   * Bridge Keep wallet of KERI / ACDC and the more sophisticated solutions at BCC for keeping secrets secret. At the same time: study and work towards KERI, CESR and ACDC supporting sophisticated multisignature schemes.
   * #SeedTool #KERI #CESR #ACDC #KEEP #ToIP #BCC

### [DID Connect, connecting people, devices and applications via DID and Verifiable Credentials](./did-connect.md)
  * by [Robert Mao](mailto:rob@arcblock.io), ArcBlock, United States
  * DID Connect is a suite of RESTful APIs, UX components and SDK that provide a framework for DID interactions, connecting people, devices and applications via DID and Verifiable Credentials.
  * #connect #application #framework #VerifiableCredentials #UX

### [Did Resources for SSI - address ALL requirements via DIDs](./did-resources.md)
   * by [Mirko Mollik](mailto:mollik@trustcerts.de)
   * DIDs allow us today to request the public keys to validate signature from a distributed verifiable data registry. Why not addressing all required resources like that, but independent from one specific vdr?
   * #did #vdr #resources
### [eSSIF-Lab: Towards a European SSI ecosystem](./eSSIF-Lab%20-%20Towards%20a%20European%20SSI%20ecosystem.md)
   * by [Oskar van Deventer](mailto:oskar.vandeventer@tno.nl), TNO, Netherlands
   * Overview of the eSSIF-Lab SSI ecosystem. "eSSIF-Lab is a 7 M€, three-year (2019-2022), European-Commission-funded program that has been sponsoring start-ups, SMEs and innovators to develop open-source SSI components, SSI products and SSI services."
   * #eSSIF-Lab #SSI-ecosystem #Europe

### [Multi-dimensional reputation systems using Webs of Trust](./Multi-dimensional%20reputation%20systems%20using%20webs-of-trust.md)
   * by [Oliver Klingefjord](mailto:hello@replabs.xyz), Replabs, Berlin.
   * A proposal for a novel multi-dimensional reputation system framework for social media using language models and webs of trust.
   * #Reputation #Webs-of-trust #Trust-networks

### [Rendering Verifiable Credentials](./rendering-verifiable-credentials.md)
  * by [Manu Sporny](mailto:msporny@digitalbazaar.com), Digital Bazaar, USA
  * A Verifiable Credential extension to support rendering using graphics, audio, or braille.
  * #VerifiableCredentials #w3c #a11y
  
### [SSI data Generator](./data-generator.md)
   * by [Moritz Schlichting](mailto:moritz@animo.id), Animo Solutions, Utrecht, The Netherlands
   * A data generator for SSI interactions and mocking
   * #eSSIF-Lab #SSI-ecosystem #Europe #Data #Generator #tools

### [Validation - The Missing Link](./validation-the-missing-link.md)
  * by [Rieks Joosten](mailto:rieks.joosten@tno.nl), TNO, Netherlands
  * In order to adopt VCs (or SSI technology), we need to explore what individual parties need *apart* from what's already part of VCs (e.g.: proofs), and how such needs can (also) be accommodated.
  * #validation #verification #sovereignty

### [Verifiable Credentials Holder Binding](./verifiable-credentials-holder-binding.md)
   * by [Oliver Terbu](mailto:oliver.terbu@spruceid.com), Spruce Systems, Inc., Berlin/New York
   * A proposal how to define a flexible and deterministic approach to verify the binding between the holder and the credential subject of the verifiable credential which is a blindspot of the W3C Verifiable Credentials Data Model 1.0 standard today.
   * #VerifiableCredentials #HolderBinding #2FA #Biometrics #Delegation

### ... more ...

## Alphabetical Listing

_Please also enter your paper alphabetically in the form:_

```
* [Paper Name](link)
```

* [CESR adapter for sophisticated multisig](./CESR-adapter-for-sophisticated-multisig.md)
* [DID Connect, connecting people, devices and applications via DID and Verifiable Credentials](./did-connect.md)
* [Did Resources for SSI - address ALL requirements via DIDs](./did-resources.md)
* [eSSIF-Lab: Towards a European SSI ecosystem](./eSSIF-Lab%20-%20Towards%20a%20European%20SSI%20ecosystem.md)
* [Multi-dimensional reputation systems using Webs of Trust](./Multi-dimensional%20reputation%20systems%20using%20webs-of-trust.md)
* [Rendering Verifiable Credentials](./rendering-verifiable-credentials.md)
* [SSI data generator](./data-generator.md)
* [Validation - The Missing Link](./validation-the-missing-link.md)
* [Verifiable Credentials Holder Binding](./verifiable-credentials-holder-binding.md)
* ... more ...

## RWOT10 Papers

You may also want to consult the papers from [RWOT10](https://github.com/WebOfTrustInfo/rwot10-buenosaires/blob/master/topics-and-advance-readings/README.md), as that design workshop was cancelled due to COVID.


