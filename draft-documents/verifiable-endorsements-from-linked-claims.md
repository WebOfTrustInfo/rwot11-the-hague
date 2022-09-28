# Composable Credentials Paper

[![hackmd-github-sync-badge](https://hackmd.io/r8CsaGShSIu2z1K6iTHi6A/badge)](https://hackmd.io/r8CsaGShSIu2z1K6iTHi6A)

## Co-Authors

* Dmitri Zagidulin - @dmitrizagidulin
* Golda Velez - @gvelez17
* Philip D. Long - @longpd
* Oliver Klingefjord - @Klingefjord

## Abstract

The Verifiable Credential ecosystem has encountered several use cases that require a third-party assertion, or an endorsement of an existing object (another VC, a PDF, a webpage, etc). Whether it is product reviews, endorsements of self-created credentials, academic paper reviews, or some other general purpose third party assertion, these use cases have several requirements in common.  Each use case may also require a domain-specific set of fields.

We propose a minimal format for Linked Claims that will allow each use case of 3rd party assertions to be represented as a set of LinkedClaims.

Further, we propose to demonstrate the ability to compose several LinkedClaims into a single domain-specific credential, specifically a Verifiable Endorsement, that will satisfy the domain requirements of the likely users.

This approach will enable rich shared datasets to inform trust decisions, while satisfying the requirements of domain-specific end users.  If time permits a sample score can be built over the linked claim dataset.

## Requirements and Nice-to-haves

1. They must use the W3C Verifiable Credentials (v2) envelope data model.
2. They must be able to refer to (make a statement about) an external object, such as:
	* Another VC
	* A URL (web page, PDF, image, etc)
	* A subsection of another VC (for example, an individual achievement or course in a transcript VC that contains multiple courses).
3. They must provide an (optional) mechanism for cryptographic binding between VCs or between a VC and another URL. (Hashlink mechanism.)
4. They should define properties that describe the endorsement or assertion:
	* a property describing that is an extension of the VC issuer, describing who is making the endorsement, what their expertise/bonafides is, what their relationship to the subject, etc.
	* a property containing evidence of the assertion (images, URLs, published papers, Github repos, etc.)
	* human-readable description of the assertion
	* an optional rating (such as for ecommerce product reviews)

Nice to haves include:

1. Ability to create "local names" from the perspective of the issuer to generate URIs for things that do not have authoritative URIs
2. Ability to compose one or more minimal endorsement VCs into a composite for a specific use case
### Composed vs Atomic Credentials

explain, add picture -- the VC model in general, and the hash linking mechanism, enables a set of claims to be expressed either as standalone credentials, or as a single composed credential.

## Use Cases
 * Endorsements of self-asserted skill credentials
 * A review of a paper submitted to an academic conference
 * An ecommerce product review (5-star type)
 * Assertion that an image/video was taken by a particular camera at a particular datetime (for https://proofmode.org/ )
 * A person was harmed by an entity (may be known or unknown)
 * Task completed and reviewed in a task tracking system (adds signal to worker reputation)
 * An endorsement that attests to authenticity of an article posted in a published news service
 * Reputation systems for social media platforms
 * Social impact - philanthropic grant helped attesting individual (or witnessed)
 * Academic class completed or exam score achieved

## Formats

Format in development see [composable claims examples](https://github.com/WebOfTrustInfo/rwot11-the-hague/tree/master/draft-documents/vc-le/composable-sample1/)

### Model

The endorsement could be rolled up with 

Replabs DAO: https://replabs.web.app/dao/tec
Replabs Twitter: https://replabs.web.app/twitter/1548015533710123010


## References

### Relates to Advanced Readings

https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/advance-readings/endorsements.md

https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/advance-readings/a-minimal-approach-to-linked-trust-with-uncertainty.md

https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/advance-readings/Multi-dimensional%20reputation%20systems%20using%20webs-of-trust.md

### Standards

https://www.w3.org/TR/vc-data-model-2.0/#dfn-verifiable-credentials

---
Syncs to -> https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/draft-documents/verifiable-endorsements-from-linked-claims.md

Original draft at https://docs.google.com/document/d/1mgIKC3U3OaYtq2koht9aQwAgJIrAEFCHq3XJvUOie5o/edit#

Contact @BRiIYS-0T9GKZAz7VgyEQg / @gvelez17 if you want to push a change from HackMD

