### Using MultiBase Anchors within a Personally-Issued Endorsement Credential to Corroborate Attributes in an Existing Issued Credential

*Authors:* Phillip D. Long, Dmitri Zagidulin, Kerri Lemoie

A credential (either issued by an institution or self-issued) makes an assertion about the subject's knowledge, skills or abilities.  The subject wishes to have a third-party corroborate this credential to give it greater credibility. The subject asks a selected third-party to "endorse" their credential, confirming the claims in the credential, and add additional supporting information about it.

For the purposes of the VC-EDU a practical use case is in the context of an endorser creating an endorsement single assertion Verifiable Credential (VC) that is cryptographically linked to an independently issued VC held by a holder. Here a MultiBasehash-linked approach to connect the two independent VCs is necessary to link the two in a tamper evident way.

---
### Use Cases

1.  Personally-Issued Credential + Third-party Personal Endorsement
2.  Classic Organization-issued Credential + Third-party Personal Endorsement

The above use cases are actually equivalent, differing only in the original issuer. Note that the design intention, at least initially, is to enable third-party endorsements by individuals.
### Verifiable Endorsement

VCs by themselves are not sufficient to serve the endorsement use case - the Resource Anchoring and Hashlink mechanism is required.

A VerifiableEndorsement Credential is an application of the VC Data Model and a resource anchoring mechanism (via `digestMultibase`). It  describes the bona fides of the endorser and enables them to convey their affirmation of support for an assertion made by an independently issued  third-party credential (institutionally issued or self-issued) with sufficient granularity to endorse the entire credential or elements within it  about which their expertise and their knowledge of the subjects expertise  specifically pertains.
#### Distinguishing characteristics (of what makes a VerifiableEndorsement VC): <the spec>

* VC Data Model 1.1 credential, of type `EndorsementCredential` and using the context `https://w3id.org/endorsement/v1`
* (Required) Refers to any third party VC (such as an OBv3 achievement) or non-VC artifact, by setting the endorsement's `credentialSubject.id` property _to the id of the target achievement or artifact_.
* Defines an optional `issuer.endorserExpertise` property, describing:
    - the endorser's bona fides and expertise in the domain in which they're making the recommendation.
    - the relationship of the endorser to the endorsee
* Defines an optional (recommended) `endorsementEvidence` property (on the same level as the issuer and credentialSubject property) that lists various links, credentials and artifacts that support the endorsement, such as:
    - links to other relevant credentials
    - links to joint projects
    - listed from general domain to specific attributes associated with concrete endorsement
* Uses the Anchoring and Hashlinking mechanism to cryptographically bind the endorsement VC with any relevant evidence objects (Achievement credentials, non-VC objects such as PDFs, images, videos and so-on).
* Defines an optional `credentialSubject.endorsement` property (for example: "Alice has the skill to do X.Y. and Z.")

[So, the concept of endorsements involves a collection of Verifiable Credentials (and non-VC objects such as PDFs, images, videos and so on) linked together by `digestMultibase` style hashlinks.]

(See issue https://github.com/w3c/vc-data-model/issues/831 for more details on the anchoring and linking mechanism.)
### Related Work

This Verifiable Endorsement proposal adds to the space of general endorsements, by giving a granular, specific structure for making claims (by an endorser, of an endorsee).

The OpenBadges v2 specification (and the emerging OBv3 spec) has a concept of an Endorsement type, which focuses on single assertion achievements. It enables endorsements of Achievements/Badge Classes, Assertions, Profiles, and CLRCredentials.

For example (see the Endorsement Examples section of the OBv2 spec):

1. To indicate trust in an email address.
2. As a comment to express approval of a Badge Class (the abstract achievement type), indicating that it is a "good representation of the achievement it describes".
3. As support for a single OBv2 achievement earned by a unique individual  (by linking to an Assertion via claim.id).

### Verifiable Endorsement Semantics

In contrast, Verifiable Endorsements are intended to be a general purpose endorsement mechanism for the VC ecosystem. They are standalone Verifiable Credentials that can use the 'digestMultibase' anchor mechanism to endorse any other VC or non-VC artifact. In addition, Verifiable Endorsements have several supporting metadata sections that enhance the endorsement process, such as the `endorserExpertise` (providing the bona fides of the endorsing party), and a focus on the `endorsementEvidence` section (providing specific evidence artifacts that relate to the endorsement).
### Data Model Examples

We anticipate the wide adoption of OpenBadges v3 credentials as the format for skill or achievement assertions, either self-asserted or institutionally issued.

Example Self-issued OBv3 Credential:

```js
{
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://w3id.org/openbadges/v3"
  ],
  "type": [
    "VerifiableCredential",
    "OpenBadgeCredential"
  ],
  "issuer": {
    "type": "Profile",
    "id": "did:key:z6MkrHKzgsahxBLyNAbLQyB1pcWNYC9GmywiWPgkrvntAZcj",
    "name": "Alice Jones"
  },
  "issuanceDate": "2022-05-01T00:00:00Z",
  "credentialSubject": {
    "type": "AchievementSubject",
    // Note that the subject of the VC is the issuer, hence self-issued
    "id": "did:key:z6MkrHKzgsahxBLyNAbLQyB1pcWNYC9GmywiWPgkrvntAZcj",
    "achievement": {
      "id": "urn:uuid:e8096060-ce7c-47b3-a682-57098685d48d",
      "type": "Achievement",
      "name": "UAV Control System for Drone Navigation",

      // TBD: Link to Credential Engine competency framework here

      "description": "<description goes here>",
      "criteria": {
        "type": "Criteria",
        "narrative": "<narrative>"
      }
    }
  },
  "proof": {
    // Signature goes here
  }
}
```

Example VerifiableEndorsement of the above VC:

```js
{
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://w3id.org/endorsement/v1",
    "https://w3id.org/security/suites/ed25519-2020/v1"
  ],
  "type": [
    "VerifiableCredential",
    "VerifiableEndorsement"
  ],
  "issuer": {
    "id": "did:web:bob.com",
    "name": "Bob"
  },
  "issuanceDate": "2010-01-01T00:00:00Z",
  "expirationDate": "2020-01-01T00:00:00Z",
  "credentialSubject": {
    // Note that the credentialSubject.id is the id of the Achievement in the target VC
    "id": "urn:uuid:e8096060-ce7c-47b3-a682-57098685d48d",
    "endorsement": {
      "statement": "Alice has an exceptional skill set as an UAV guidance control engineer. See also the attached evidence.",
      "endorser": {
        "id": "did:web:endorser.example.com",
        // the endorsing entity's bona fides, tailored to the specific endorsement area or claims on a per-use basis
        "relevance": [
           // Generic expertise claims (such as CV / resume / degrees)
           {
             "id": "https://SmartResume.com",
             "type": "SmartResumeProfile"
           },
           {
             "id": "https://linkedin.com/Bob",
             "type": "LinkedInProfile"
           },
           {
             // link to a credential I received saying I have a degree to this subject
             "id": "https://example.edu/degrees/class-of-2021/bob",
             "name": "University Degree Credential"
           },
           {
             "id": "https://sigspatial.acm.org/members/12345",
             "description":
                      "https://www.acm.org/special-interest-groups/sigs/sigspatial",
             "name": "SigSpatial Membership Credential"
           },
           // Specific expertise item tailored to the endorsement
           {
             "id": "https://example-journal.com/my-article.pdf",
              // optional hashlink (note that 'multibase' is a part of the in-progress
              // IETF spec https://datatracker.ietf.org/doc/html/draft-multiformats-multibase
             "digestMultibase":"zQmdfTbBqBPQ7VNxZEYEj14VmRuZBkqFbiwReogJgS1zR1n",
             "name": "Control Systems in Unmanned Flight",
             "citation": "...",
             "description": "I have published an article in a peer-reviewed journal."
           },
           // TODO: Add a CID / Ceramic link as an example.
         ]
      }
    }
  },
  "evidence": [
    {
      "id": "https://github.com/example-org/control-test-suite",
      "type": ["EndorsementEvidence"],
      "name": "Control System Test Suite",
      "description": "The code used to control a UAV delivering packages to an address."
    }
  ],
  "proof": {
    // Signature goes here
  }
}
``` 
    
### Example Workflow / Protocol

TBA: Add a description + swimlane diagram for how Alice would request the endorser for the endorsement.
### Notes on Tooling

We expect that adding endorsements to VCs will be another feature offered by various wallets. A marketplace of authoring services we hope to see develop that offers options	 for endorsement credential authoring and connects to wallets via the Issuer API.

### Summary

This example of endorsement is intended to convey one of several potential use cases for the evidence-based corroboration of statements made in one credential by an endorser authoring a VC that allows the granular affirmation of elements within the endorsee’s issued credential using a proofing method that links the two credentials together, based on the affirmation of the endorser’s selection about which they are knowledgeable. It provides context for the endorser’s relevance or background to make those judgements and encourages the inclusion of evidence from the endorser’s own direct experience and artifacts relevant to the endorsee’’s claim.
