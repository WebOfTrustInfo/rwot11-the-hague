# Composable Credentials Paper

[![hackmd-github-sync-badge](https://hackmd.io/r8CsaGShSIu2z1K6iTHi6A/badge)](https://hackmd.io/r8CsaGShSIu2z1K6iTHi6A)

## Co-Authors

* Dmitri Zagidulin - @dmitrizagidulin
* Golda Velez - @gvelez17
* Philip D. Long - @longpd
* Oliver Klingefjord - @Klingefjord

## TODO
- Confirm that VC-DATA-MODEL v2.0 has the 'effectiveDate' field
- Decide on top-level credential type
- Decide on context url
- howKnown -> source_type
- best way to express controlled/suggested vocabs?


- Verifier for correctly composed and correctly linked credentials

   * composed means the subject is the uri of a claim 
   * linked means the subject is the issuer or source of a claim


## Abstract

The Verifiable Credential ecosystem has encountered several use cases that require a third-party assertion, or an endorsement of an existing object (another VC, a PDF, a webpage, etc). Whether it is product reviews, endorsements of self-created credentials, academic paper reviews, or some other general purpose third party assertion, these use cases have several requirements in common.  Each use case may also require a domain-specific set of fields.

We propose a minimal format for Linked Claims that will allow each use case of 3rd party assertions to be represented as a set of LinkedClaims.

Further, we propose to demonstrate the ability to compose several LinkedClaims into a single domain-specific credential, specifically a Verifiable Endorsement, that will satisfy the domain requirements of the likely users.

This approach will enable rich shared datasets to inform trust decisions, while satisfying the requirements of domain-specific end users.  If time permits a sample score can be built over the linked claim dataset.

## Requirements for Linked Claims and Endorsements

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

## Use Cases

### Endorsements of self-asserted skill credentials
  Alice has worked in warehouse distribution centers since she dropped out of high school to earn money to support her mother, and siblings, after her mother was forced to recuperate from injuries incurred in a vehicle accident.
Alice started as a custodian but over time and through observation and conversation with her co-workers she learned she could get trained to drive a warehouse forklift and significantly increase her earning potential. She enrolled in class 4 OSHA certified forklift driver training course while continuing her night custodian job. After receiving her certification she applied for a forklift driver opening at the company where she was employed but sought corroboration of her skills both from her instructors at ISETA (Bootcamp 1.0) and the forklift specialization course, along with an endorsement from her current supervisor attesting to her reliability, teamwork, and attention to detail she has expressed in her current job.
  
  Alice sends the self-asserted credential describing her skills relevant to the forklift driver position to Bob, her instructor ay ISETA of the OSHA forklift training course by email and points out the attributes she thinks he can attest to amongst her skill claims. 
  
  Alice does the same thing sending her self-assertion credential to Juanita,her current supervisor, pointing out those attribute she suggests Juanita has direct knowledge about her performance.
  
  Both Bob and Juanita construct a linked-claims Verifiable Credential endorsing Alice for those attributes they have expertise in and can address with professional credibility based on their own bona fides included in their relevance arrestations describing their own training and background.
  
  Juanita and Bob send their self-asserted skill endorsements to Alice after binding their attributions to those skills and competencies based on their knowledge of Alice's capabilities. Alice selects these credentials for inclusion in the set she prepares as a verifiable presentation to submit to the job application site.

### An endorsemet of an institution/busniess/gov issued credential to an individual by a third party.
Claudio recently complete a certificate program in cybersecurity. The technical college issued the certificate in both paper and VC formats. Through conversations with some of his instructors he's become aware of an opening in a local cybersecurity sourcing company who provides short (1 to 6 month consulting project contracts) and medium term placements for contract employees). Claudio asks one of his instructors, Laura,for a reference. Laura agrees to serve as a reference and suggests that she provide a verifable endorsement credential to Claudio's digital credential wallet.

Laura asks Claudio for (a copy of) his VC conferring his cybersecurity certifiate awarded to him for successfully completing his course of study that awarded him a Certificate in Cyber Threat Analytics and Prevention (CTAP).Laura composes a self asserted verifiable endorsement VC that establishes her credentials or bona fides as a credible judge of Claudios knowldge, skills and abilities in this domain. She provides verifiable documentation of her work in the field through links to papers she has published, reports to which she contributed on cyberthreat assessment, and grants she has received for her workmin this domain.

She describes the the work she has seen done by Claudio and her view of the level of performance he demonstrated. Laura also has offeres additional evidence of Claudios knowledge in this discipline from the help he provided as a contracted worker under a cyberassessment contract she oversaw for a local regional bank. These included statistical analyses of penetration tests, attack simulations and summary reports all in his Github account, all hashlinked into the evidence section of her endorsement VC for Claudio.

Laura signs her verifiable endorsement VC and sends it as a VP to Claidios credential wallet. He accepts the presentation which puts the endorsement VC in his wallet and generates a VP including his CTAP certificate VC, the endorsement VC and several others that document related credentials pertinent to the job requirements. This VP is then sent to the cybersecurity sourcing company as part of his Verifiable Resume (TM).

### A review of a paper submitted to an academic conference
  Layla Soliman registered to attend her disciplinary conference in molecular genetics. The conference organizers asked her to review a paper submitted for presentation at the meeting to which she agreed. The organizers send Layla a link to the paper in a Google docs directory.
  
  Layla follows the link to the paper, reads the reviewer guidelines and sets out reading and taking notes and preparing her review comments.On completion of the reading the submitted paper manuscript she prepares her final comments and creates a self-assertion credential of type equals "review". Essentially this is a narrative credential that is cryptographically signed and linked to hashlinked to the Google doc location of the manuscript.
  
  Layla creates a simple Verifiable Presentation to send her review to the conference organizer's digital wallet where reviews are collated. The linked data endorsement is of type: review and contains the narrative of her review comments

### An ecommerce product review (5-star type)

### Assertion that an image/video was taken by a camera crew is not been altered from the time the images were captured.  (for https://proofmode.org/)
Follow up with Joe Andrieu re: the issues of image capture and using multiBase hashlink signature methods.

### A person was harmed by an entity (may be known or unknown)

### Task completed and reviewed in a task tracking system (adds signal to worker reputation)

### An endorsement that attests to authenticity of an article posted in a published news service

Island News, the daily morning paper for the Signal Islands, has a reputation formin depth investigative reporting. Recently controversies has emerged when reporting on inappropriate use of provincial revenue collected from bond financing was published stating that government ministers involved in the oversite of the fund accounts associated with a new economic development, anchored by Wind Casinos, redirected hundreds of bitcoin to private ministerial accounts.

Representatives of these ministers countered these accusations were fabricated and published purported notes from the reporting journaistis corroborating their claims.The journalists contested these representations of their work, with the back and forth of accusations and countering claims devolving into a confusing and ultimately unresolvable incident that diverted public attention tomthe serious concerns initially raised.

Island News decided to hashlink future investigative reporting and associate them with a verifiable credential signed by the reporters involved. This was further subatantiated by an verifiable endorsement credential issued by The Internation Consortium of Investigative Journalism (the TICIJ), corroborating by a respected third party the claims of authenticity derived bybtheor review of the investigative journalism process and specufic transcripts of notes, photographic evidence and recordings the Island News submitted to them and they independently analyzed.

Future investigative journalism reports contain the links to these credentials, publicly accessible, and verifiable for all who wish to see them.

### Reputation systems for social media platforms
.l
### Social impact - philanthropic grant helped attesting individual (or witnessed)

### Academic class completed or exam score achieved

## Composing Credentials via Anchored Resources / Hashlinking

### Hashlink Prior Art

- [Cryptographic Hyperlinks IETF Draft](https://datatracker.ietf.org/doc/html/draft-sporny-hashlink-07)
- [ACDC - Authentic Chained Data Containers Draft](https://www.ietf.org/archive/id/draft-ssmith-acdc-02.html)

### Proposal
This paper introduces two new related properties: `anchoredResource` and `digestMultibase`.

#### Anchored Resource
An anchored resource points to one or more linked or bound resources. It can appear in the `credentialSubject` section (which implies that the resource is linked to the subject), or in the top level credential (same level as issuer, issuanceDate, etc), which implies that the resource is linked to the credential itself.

#### digestMultibase
A `digestMultibase` property provides a way to lock down a link using a hash of its content, by specifying the hash algorithm, and (optionally) the canonicalization mechanism to perform before hashing.

### Composed vs Atomic Credentials

explain, add picture -- the VC model in general, and the hash linking mechanism, enables a set of claims to be expressed either as standalone credentials, or as a single composed credential.

## Data Model

Format in development see [composable claims examples](https://github.com/WebOfTrustInfo/rwot11-the-hague/tree/master/draft-documents/vc-le/composable-sample1/)

## Mental Model

### Firsthand Observation

```
English: I witnessed an accident.
Subject: The accident
Claim: happened
Object: <something about the accident. For example, when & where it happened> -- this is a set of claims
Evidence: <I witnessed it firsthand>
```

```javascript
{
  issuer: "Me", // person who witnessed the accident
  credentialSubject: {
    "id": "https://accidents.example.com/reports/accident-1",
    "statement": "Some stuff happened at Elm St on Sunday.",
    "dateObserved": "Sunday",
    "location": "corner of Elm St"
  },
  evidence: [{
    "source": "firsthand witness"  
  }]
}
```

### Secondhand Observation

```
English: I heard Charles say that he witnessed the accident
Subject: The Accident
Claim: happened
Object: "(same as previous example - the accident happened)"
Evidence: <I heard Charles said that he witnessed accident>
```

```javascript
{
  issuer: "Golda", // person who heard Charles say he witnessed the accident
  credentialSubject: {
    "id": "https://accidents.example.com/reports/accident-1",
    "statement": "Some stuff happened at Elm St on Sunday.",
    "dateObserved": "Sunday",
    "location": "corner of Elm St"
  },
  evidence: [
    {
      "type": "secondhand",  // evidence type
      "witness": {
        "id": "<charless homepage>"
        "name": "Charles"
      },
      "statement": "I heard Charles say this"
    },
    {
      "type": "firsthand"
      "witness": "Golda",
      "statement": "I heard a noise at such & such time."
    }
  ]
}
```

## Examples

### Standalone Claim - Review

Example of a linked claim representing a product review.

- References an external product (no hashlink)
- No claimant expertise
- No evidence section

```javascript
{
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://www.w3.org/2018/credentials/examples/v1",
    "https://w3.id/vc/linked-claims" // <- TODO: decide on url
  ],
  "type": [ "VerifiableCredential", "LinkedClaim" ],
  "issuer": {
    "id": "spider",
    "name": "spider"
  },
  "issuanceDate": "2010-01-01T00:00:00Z",
  "expirationDate": "2020-01-01T00:00:00Z",
  "effectiveDate": "1970-01-01",  // core vc 2.0 see original
  "credentialSubject": {
    "id": "https://example.com/products/coffee-mug",

    "linkedClaim": {
      "type": "Review",
      "statement": "This is a great coffee mug, would buy again.",
      "review": {
        // "5-star" type review
        rating: 5,
        ratingMax: 5,
        ratingMin: 1
      } 
    }
  },
  "proof": { ... }
}
```

### Standalone Claim - Witnessing an Event
Example of a linked claim representing a witnessing of an event.

```javascript
{
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://www.w3.org/2018/credentials/examples/v1",
    "https://w3.id/vc/linked-claims" // <- TODO: decide on url
  ],
  "type": [ "VerifiableCredential", "LinkedClaim" ],
  "issuer": {
    "id": "did:web:bob.example.com",
    "name": "Bob"
  },
  "issuanceDate": "2010-01-01T00:00:00Z",
  "expirationDate": "2020-01-01T00:00:00Z",
  "effectiveDate": "1970-01-01",  // core vc 2.0 see original
  "credentialSubject": {
    // The subject id here is the id of the **report**
    "id": "https://reports.example.com/accidents/123",
    "linkedClaim": {
      "type": "EventWitnessClaim",
      "statement": "I have witnessed a bicycle accident on the corner of Elm and East 3rd St.",
      "source": "firsthand"
    }
  },
  "proof": { ... }
}
```

### Combined Linked Claim - A Verifiable Endorsement

This example is composed of two components -- an initial standalone VC, and then an _endorsement_ of that VC, with a one-way cryptographic binding to it.

**Initial (Self-issued) VC:**
```javascript
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

**Endorsement of above VC:**
```javascript
{
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://w3.id/vc/linked-claims" // <- TODO: decide on url
    "https://w3id.org/security/suites/ed25519-2020/v1"
  ],
  "type": [ "VerifiableCredential", "VerifiableEndorsement" ],
  "issuer": {
    "id": "did:web:bob.example.com",
    "name": "Bob"
  },
  "issuanceDate": "2010-01-01T00:00:00Z",
  "expirationDate": "2020-01-01T00:00:00Z",
  "credentialSubject": {
    // Note that the credentialSubject.id is the id of an individual Achievement in the target VC
    // It could just as readily be the id of the VC, but the authors wanted to highlight that a section of the VC could be targeted
    "id": "urn:uuid:e8096060-ce7c-47b3-a682-57098685d48d",
    "digestMultibase": "zb1B1M6Bve5JEaNqeJSmuE", // digest of the Achievement being endorsed
    "endorsement": {
       "type": "Endorsement",
       "statement": "This is an endorsement regarding Alice's 'UAV Control System for Drone Navigation' achievement. Alice has an exceptional skill set as an UAV guidance control engineer. See also the attached evidence.",
       "endorser": {
          "id": "did:web:bob.example.com",  // MUST be same as issuer
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
      "description": "The code used to control a UAV delivering packages to an address.",
      "digestMultibase": "..."
    },
    {
       "id": "https://control-systems-journal.example.com/12345.pdf",
       "digestMultibase": "zQmdfRKkx7Uf8Rpr079Uh",
        "name": "Geopositioning in Control Systems",
        "citation": "...",
        "description": "A particularly insightful implementation of geopositioning with precision; I was very impressed with Alice's approach."
    }
  ],
  "proof": {
    // Signature goes here
  }
}
```

### Decomposed Linked Claim - Verifiable Endorsement

This example is functionally identical to the previous (an initial standalone self-issued VC combined an _endorsement_ of that VC), except that it de-composes the parts of the endorsement into separate standalone VCs (that are still linked, cryptographically). These would typically be presented as a bundle, in a Verifiable Presentation:

1. A self-issued VC (a skill achievement badge) by Alice. Subject: Alice
2. An endorsement of the skill VC, issued by Bob. Subject: the ID of the VC #1.
3. A VC listing Bob's qualifications/bonafides (explaining why Bob is qualified to make the recommendation). Subject: The ID of the endorsement (#2)
4. A VC listing the _evidence_ behind Bob's endorsement. Subject: The ID of the endorsement (#2)

**#1 - Initial (Self-issued) VC:**
```javascript
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
    "id": "did:key:z6MkrHKzgsahxBLyNAbLQyB1pcWNYC9GmywiWPgkrvntAZcj",
    "name": "Alice Jones"
  },
  "id": "urn:uuid:f5a8b09a-424f-4aa1",
  "issuanceDate": "2022-05-01T00:00:00Z",
  "credentialSubject": {
    "type": "AchievementSubject",
    // Note that the subject of the VC is the issuer, hence self-issued
    "id": "did:key:z6MkrHKzgsahxBLyNAbLQyB1pcWNYC9GmywiWPgkrvntAZcj",
    "achievement": {
     "type": "Achievement",
     "name": "UAV Control System for Drone Navigation",
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

**#2 - Endorsement of VC #1:**
```javascript
{
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://w3.id/vc/linked-claims" // <- TODO: decide on url
    "https://w3id.org/security/suites/ed25519-2020/v1"
  ],
  "id": "urn:uuid:4b4d-8d0f-0ad47cf4e64c",
  "type": [ "VerifiableCredential", "VerifiableEndorsement" ],
  "issuer": {
    "id": "did:web:bob.example.com",
    "name": "Bob"
  },
  "issuanceDate": "2010-01-01T00:00:00Z",
  "expirationDate": "2020-01-01T00:00:00Z",
  "credentialSubject": {
    // Subject: the ID of VC #1
    "id": "urn:uuid:f5a8b09a-424f-4aa1",
    "digestMultibase": "zb1B1M6Bve5JEaNqeJSmuE", // digest of the VC being endorsed
    "linkedClaim": {
      "statement": "This is an endorsement regarding Alice's 'UAV Control System for Drone Navigation' achievement. Alice has an exceptional skill set as an UAV guidance control engineer. See also the attached evidence.",
    }
  },
  "proof": {
    // Signature goes here
  }
}
```

**#3 - Endorser Qualifications/Bonafides for Endorsement VC #2:**
```javascript
{
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://w3.id/vc/linked-claims" // <- TODO: decide on url
    "https://w3id.org/security/suites/ed25519-2020/v1"
  ],
  "type": [ "VerifiableCredential", "VerifiableEndorsement" ],
  "issuer": {
    "id": "did:web:bob.example.com",
    "name": "Bob"
  },
  "issuanceDate": "2010-01-01T00:00:00Z",
  "expirationDate": "2020-01-01T00:00:00Z",
  "credentialSubject": {
    // Subject: the ID of Endorsement VC #2
    "id": "urn:uuid:4b4d-8d0f-0ad47cf4e64c",
    "digestMultibase": "zb1B1M6Bve5JEaNqeJSmuE", // digest of the VC being referenced
    "endorsement": {
       "endorser": {
          "id": "did:web:bob.example.com",  // MUST be same as issuer
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
  "proof": {
    // Signature goes here
  }
}
```

**#4 - Evidence for Endorsement #2:**
```javascript
{
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://w3.id/vc/linked-claims" // <- TODO: decide on url
    "https://w3id.org/security/suites/ed25519-2020/v1"
  ],
  "id": "urn:uuid:4b4d-8d0f-0ad47cf4e64c",
  "type": [ "VerifiableCredential", "VerifiableEndorsement" ],
  "issuer": {
    "id": "did:web:bob.example.com",
    "name": "Bob"
  },
  "issuanceDate": "2010-01-01T00:00:00Z",
  "expirationDate": "2020-01-01T00:00:00Z",
  "credentialSubject": {
    // Subject: the ID of the endorsement #2
    "id": "urn:uuid:f5a8b09a-424f-4aa1",
    "digestMultibase": "zb1B1M6Bve5JEaNqeJSmuE", // digest of the VC being endorsed
        
    // OPTIONAL: Also hashlink to the original VC
    "anchoredResource": {
       "id": "<id of the original VC #1>",
       "digestMultibase": "<hash of the VC #1>"
    }
  },
  "evidence": [
    {
      "id": "https://github.com/example-org/control-test-suite",
      "type": ["EndorsementEvidence"],
      "name": "Control System Test Suite",
      "description": "The code used to control a UAV delivering packages to an address.",
      "digestMultibase": "..."
    },
    {
       "id": "https://control-systems-journal.example.com/12345.pdf",
       "digestMultibase": "zQmdfRKkx7Uf8Rpr079Uh",
        "name": "Geopositioning in Control Systems",
        "citation": "...",
        "description": "A particularly insightful implementation of geopositioning with precision; I was very impressed with Alice's approach."
    }
  ],
  "proof": {
    // Signature goes here
  }
}
```

### Verfier

to make this meaningful a verifier for a VP must validate that the composed documents are truly composed the way the business logic asserts; AND that linked documents are linked (by issuer/source) the way business logic asserts

So two new callbacks are needed 
    1) verify composition
    2) verify links

## References

Replabs DAO: https://replabs.web.app/dao/tec
Replabs Twitter: https://replabs.web.app/twitter/1548015533710123010

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

