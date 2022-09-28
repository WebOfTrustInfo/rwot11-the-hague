Link: [Verifiable Credentials Holder Binding](./verifiable-credentials-holder-binding.md)

This is a proposed collaborative paper to be completed at [RWOT 2022](https://rwot11.eventbrite.com/), Den Haag, Netherlands, 26-30 September. Advance reading: see [here](https://github.com/WebOfTrustInfo/rwot11-the-hague/tree/master/advance-readings).

# W3C Verifiable Credentials Holder Binding Specification

by [Oliver Terbu](mailto:oliver.terbu@tspruceid.com), Spruce Systems, Inc. (Berlin/New York), Paul Bastian, Snorre, Rieks, Antonio, Nikos, Zaida 

## Abstract

The W3C Verifiable Credentials Data Model does not define how to bind the W3C Verifiable Credential to the W3C Verifiable Presentation, so that the Verifier can verify that the holder of the verifiable presentation is the rightful or intended holder of the verifiable credential. Verifying a verifiable presentation does not include verifying the binding between the verifiable credential subject and the verifiable presentation holder. There is no normative reference for any existing approach.

For these reasons, this paper describes a mechanism and a data model that allows Holders and/or Issuers to indicate how the rightfulness of the presentment can be verified at the time of presentment. Binding multiple Verifiable Credentials to a Holder should be possible. The W3C Verifiable Credentials Data Model 1.1 specification which is essentially equivalent to no guidance on the Holder Binding is provided. This mechanism is fully backward compatible with existing verifiable credentials and verifiable presentations. This paper does not mandate a specific form of holder binding or W3C Verifiable Credential proof type or format. Instead it provides a framework for Issuers, Holders and Verifiers to provide guidance on how Holder Binding can be checked deterministically according to their intentions.