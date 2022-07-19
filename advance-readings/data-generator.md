### Data Generator for SSI interactions

- Moritz Schlichting, [moritz@animo.id](mailto:moritz@animo.id)
- Software Developer [@animosolutions](ww.animo.id)

#### Background and Problem

Common use-cases of Self-Sovereign Identity (SSI) implementations involve interacting with `Schema`, `Credential Definition` and `Proof Request` data representations. Reading these is one thing, writing another. Writing a full proof request is relatively cumbersome, repetetive, and error-prone as they are often nested JSON objects or some data structure representation corallary. For general-purpose data there exist such libraries such as [faker](https://fakerjs.dev/). Regularly, especially in a development context, a developer simply wants to create a mock or arbitrary proof request for testing purposes. This also implies creating mock schemas and credential definitions.

#### Proposed Solution

In order to address the problem at hand one can create a data-generator that:

1. Can generate proofs/proof requests filled with 'random' but valid data
2. Can generate credentials and credential requests with 'random' but valid data

This can also be extended to be a general-purpose data-generator for Hyperledger Aries that is able produce mock data for any datatype used in interactions.

#### Research questions

1. How can such generator best be implemented?
2. What is the scope of such a generator?
3. How would the generator deal with [JSON-LD](https://json-ld.org/) data?
   1. For instance, should there be a common resource/server to provide such mock data? See also [schema.org](https://schema.org/AdministrativeArea)
4. What are the limitations of such generator?
   1. For instance, providing sensible values and comparators for attributes and predicates

#### Relevant Sources

1. [JSON-LD](https://json-ld.org/)
2. [schema.org](https://schema.org/AdministrativeArea)
3. [faker](https://fakerjs.dev/)
4. [Hyperledger Aries Present Proof v2](https://github.com/hyperledger/aries-rfcs/blob/main/features/0454-present-proof-v2/README.md)
