Authorized Issuer Lists
=======================

By Manu Sporny &lt;msporny@digitalbazaar.com&gt;

Trust can be more difficult to establish in decentralized systems than in
centralized ones. For example, how do you know whether to trust a Verifiable
Credential Issuer? As the Verifiable Credentials ecosystem grows, and the number
of Issuers increases, it will become increasingly difficult for Verifiers to vet
every Issuer of a Verifiable Credential. This paper explores mechanisms that
could be used by Verifiers to bootstrap which Issuers they should trust to issue
specific Verifiable Credentials.

The AuthorizedIssuerList Verifiable Credential
==============================================

This paper proposes a new Verifiable Credential called an
`AuthorizedIssuerList`, which could take the following form:

```javascript
{
  "@context": [
    "https://www.w3.org/2018/credentials/v2",
    "https://w3id.org/vc/ail/v1"
  ],
  "issuer": "did:web:authority.example",
  "issuanceDate": "2023-02-13T00:18:30.053Z",
  "type": [
    "VerifiableCredential",
    "AuthorizedIssuersCredential"
  ],
  "credentialSubject": [{
    "id": "did:web:issuer.example",
    "type": "AuthorizedIssuer",
    "authorizedToIssueCredential": [{
      "type": "UniversityDegreeCredential"
    }, {
      "type": "StudentIdCredential"
    }]
  },
  "proof": { ... }
}
```

The format above would enable Verifiers to injest a list of authorized issuers
for a particular set of credentials.

Collaboration at and Beyond RWoT 11
===================================

There are a number of open questions related to authorized issuer lists. These
questions include:

* Should the `AuthorizedIssuer` digitally sign their list of credentials they
  are authorized to issue to ensure that an publisher doesn't include an issuer
  against their will?
* Should there be an API to define how these lists are managed such that issuers
  can update their own information in the list?
* Should the `authorizedToIssueCredential` property contain something more than
  a QueryByExample mechanism? What about JSON Schema?
* Should Verifiers be able to add to the list in their own configurations?
* How is trust in the list provider established?

The author of this paper seeks individuals that are interested in publishing
lists of authorized issuers in a specific market vertical and would like to
collect answers to the questions above as well as other questions that ecosystem
participants have.
