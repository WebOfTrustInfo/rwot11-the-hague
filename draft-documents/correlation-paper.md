# RWOT Correlation Paper 

[![hackmd-github-sync-badge](https://hackmd.io/1rGIb8kmSKWE7QYWfVR_rw/badge)](https://hackmd.io/1rGIb8kmSKWE7QYWfVR_rw)

Syncs to -> https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/draft-documents/correlation-paper.md

Contact @ChristopherA if you want push a change from HackMD.

## Co-Authors

* Christopher Allen - @ChristopherA (GitHub & Twitter), ChristopherA@LifeWithAlacrity.com - [Blockchain Commons](https://www.BlockchainCommons.com)
* Fabio Tagliaferro - @fabtagliaferro (GitHub), [University of Verona](https://www.di.univr.it/?ent=persona&id=39578&lang=en), [Commercio.Network](https://commercio.network/)
* Elena Chachkarova - @elenachachkarova (GitHub), [Nymlab](https://www.nymlab.it/#/)
* Markus Sabadello - @peacekeeper (GitHub), [Danube Tech](https://danubetech.com/)
* Brent Zundel - @brentzundel (GitHub), [Avast](https://www.avast.com/)

## Abstract

The goal of this paper is to enable decision makers, particularly non-technical ones, to gain a nuanced grasp of the privacy problems (and some advantages) caused by correlation. We will describe them in plain English, but with some rigor. This will enable readers of this paper to better understand anti-correlation best practices, to adopt the correct approaches for the appropriate use cases, and to assess techniques that enable those enhancements.

We begin with an exploration of data minimization as a principle, then discuss techniques that support data minimization such as selective disclosure and progressive trust. 

Data Minimization was previously a topic of an [RWoT paper](https://github.com/WebOfTrustInfo/rwot5-boston/blob/master/draft-documents/DataMinimization/Data%20Minimzation%20and%20Selective%20Disclosure.md), later published by W3C-CCG as a [Draft Community Group Report](https://w3c-ccg.github.io/data-minimization/).

This work is a re-boot of that paper. It expands and clarifies the topics of that paper, while removing examples and appendices that may no longer be as pertinant and replacing them with new ones. A significant addition is an update of the use cases provided as a means to explore the need for reducing correlation in different circumstances.

Once complete, this paper may serve as input to a Verifiable Credentials Working Group Note related to this topic.

## References

* Technologies:
    * BBS+ Signatures 2020: https://w3c-ccg.github.io/ldp-bbs2020/
    * BBS Signature Scheme: https://identity.foundation/bbs-signature/draft-looker-cfrg-bbs-signatures.html
    * AnonCreds: https://anoncreds-wg.github.io/anoncreds-spec/
    * SD-JWT: https://github.com/oauthstuff/draft-selective-disclosure-jwt
    * Merkle Disclosure Proof 2021: https://w3c-ccg.github.io/Merkle-Disclosure-2021/
    * Redaction Signature Suite 2016: https://w3c-ccg.github.io/lds-redaction2016/
    * Gordian Envelopes: https://github.com/BlockchainCommons/BCSwiftSecureComponents/blob/master/Docs/02-ENVELOPE.md

* Related RWOT Advance Readings & Topics
    * [Elision, Redaction, and Noncorrelation in Smart Documents](https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/advance-readings/elision-redaction-correlation-smart-documents.md)
    * [Reducing Correlation: To What Degree is it Necessary?](https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/advance-readings/reducing-correlation.md)
    * [Identity Crisis: Clearer Identity Through Correlation](https://github.com/WebOfTrustInfo/ID2020DesignWorkshop/blob/master/final-documents/identity-crisis.pdf)

### Unsorted Links

* [Engineering Privacy for Verified Credentials: In Which We Describe Data Minimization, Selective Disclosure, and Progressive Trust](https://github.com/w3c-ccg/data-minimization) (last updated Apr 12, 2022, released by W3C-CCG Apr 4, 2019)
* [Formalising Linked-Data based Verifiable Credentials for Selective Disclosure](https://ssr2022.com/slides/FormalisingLinkedDataBasedVerifiableCredentials.pdf)
* Recent PRs on [VC Data Integrity spec](https://w3c.github.io/vc-data-integrity/) in [W3C VC WG](https://www.w3.org/groups/wg/vc):
    * About unlinkability: https://github.com/w3c/vc-data-integrity/pull/52
    * About selective disclosure: https://github.com/w3c/vc-data-integrity/pull/53
