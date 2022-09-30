# A specification for ledger-agnostic AnonCreds

## Abstract

AnonCreds are a novel means of providing digitally verifiable data that is privacy-preserving and tamper-proof (for SSI). Currently, AnonCreds are coupled to Hyperledger Indy, however the underlying cryptographic logic is based on the Hyperledger Ursa library and henceforth uncoupled to any specific ledger. Many real-world use-cases for SSI implementations come with using multiple and different types of ledgers for the same user domain. For instance, a country could use verifiable credentials based on ledger A for issuing a driving license and certificate of citizenship, whilst using ledger B for banking-related matters. The ability to anchor AnonCreds related objects (schemas, credential definitions, etc..) on theoretically any ledger, is the goal of this proposal. The outcome is an AnonCreds specification describing how to use AnonCreds in a ledger agnostic way, based on the current Hyperledger Indy implementation, with modifications/shortcomings that describe possible extensions and updates to the current speicfication (such as removing the binding to CL signatures, or the revocation scheme).

## Work delivered during RWOT

During RWOT extensions were made to the AnonCreds specification. Specific focus was on making the current non-standardized AnonCreds specification ledger agnostic. Pull requests were made for the simpler objects (such as the schema, credential definition, and revocation registry). The revocation state data models, and the W3C Data Model were discussed and will be added to the final paper.

* Changes to Schema definition in the spec [PR](https://github.com/AnonCreds-WG/anoncreds-spec/pull/78)
    * Consistent human-readable spelling
    * Ledger Agnostic AnonCreds conformant data model
* Changes to Credential Definition data model in the spec [PR](https://github.com/AnonCreds-WG/anoncreds-spec/pull/80)
    * Consistent human-readable spelling
    * Ledger Agnostic AnonCreds conformant data model
* Changes to revocation registry definition [PR](https://github.com/AnonCreds-WG/anoncreds-spec/pull/82)
    * Consistent human-readable spelling
    * Ledger Agnostic AnonCreds conformant data model
* Remove indy specific things and increase concision [PR](https://github.com/AnonCreds-WG/anoncreds-spec/pull/76)
* Update tails file info [PR](https://github.com/AnonCreds-WG/anoncreds-spec/pull/79)
* Added how libursa currently manages the blinding of all hidden attributes (including link secret) [PR](https://github.com/AnonCreds-WG/anoncreds-spec/pull/81)

## Outstanding work

### Revocation Data Models

The revocation data models for AnonCreds are currently very specific to how the indy ledger works. During RWOT there have been discussions on the possiblities to store and query the revocation state. An idea was discussed to create a bit index revocation state data model that the AnonCreds object method should create. Under the hood this could be generated in various ways. The exact data model still needs to be worked out.

### New Revocation Scheme

A review of a [new revocation scheme](https://docs.google.com/presentation/d/10dGC-qKU7XT2WRd_wTxK82u0FmvjJrfdXwFEiWGauE4/edit#slide=id.p) designed by Andrew Whitehead needs to happen, with an approach to integrate this with both AnonCreds and other credentail types.

### W3C Data Model Representation for AnonCreds

A W3C Data Model representation for AnonCreds was discussed and reviewed. An initial version based on the learnings needs to be worked out and submitted as an `AnonCreds2022` proof type. The representation can build on the work done in this [PR](https://github.com/hyperledger/indy-sdk/pull/2223)

### Documentation on the Applied Cryptography 

The final specification should provide a concise picture to guide implmentors on the cryptographic primitives and constructs that AnonCreds support. 

However, much of the cryptographic material is included in the AnonCreds data model, 
therefore it is important to provide description and explanation on the underlying [CL signature scheme].
In addition, it will be helpful to document what the currently implementation does,
which will also provide the basis for evolution for next specification versions.

Remaining tasks include:

* Fill out terminologies describing cryptographic material
* Add description of underlying cryptographic schemes implemented in the [Ursa library]
* Create a new section to explain the elements in the cryptographic material and how they are used

[CL Signature scheme]: https://cs.brown.edu/people/alysyans/papers/cl04.pdf
[Ursa library]: https://github.com/hyperledger/ursa
