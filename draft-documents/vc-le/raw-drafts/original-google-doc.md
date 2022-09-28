# Verifiable Endorsements from Linked Claims
see also: https://github.com/gvelez17/rwot11-the-hague/tree/master/draft-documents/endorsement-graph-team
https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/advance-readings/endorsements.md
https://www.w3.org/TR/vc-data-model-2.0/#dfn-verifiable-credentials  

*** FROM https://docs.google.com/document/d/1mgIKC3U3OaYtq2koht9aQwAgJIrAEFCHq3XJvUOie5o/edit# ***

## Abstract
The Verifiable Credential ecosystem has encountered several use cases that require a third-party assertion, or an endorsement of an existing object (another VC, a PDF, a webpage, etc). Whether it is product reviews, endorsements of self-created credentials, academic paper reviews, or some other general purpose third party assertion, these use cases have several requirements in common.  The specific requirements of individual use cases may be generated as a view from composed minimal assertions.

This proposal aims to gather example use cases, and to propose a minimal VC data model able to express those use cases.  A composed VC data model for specific use cases may be generated from linked minimal assertions.  Further, the intention is to have a working prototype capable of importing endorsements/assertions from external sources, publishing them to a shared data layer, and demonstrating a scoring model. 

Keywords: 
## Requirements and Nice-to-haves

1. They must use the W3C Verifiable Credentials (v2) envelope data model.
2. They must be able to refer to (make a statement about) an external object, such as:
	a. Another VC
	b. A URL (web page, PDF, image, etc)
	c. A subsection of another VC (for example, an individual achievement or course in a transcript VC that contains multiple courses).
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
Endorsements of self-asserted skill credentials
A review of a paper submitted to an academic conference
An ecommerce product review (5-star type)
Assertion that an image/video was taken by a particular camera at a particular datetime (for https://proofmode.org/ )
A person was harmed by an entity (may be known or unknown)
Task completed and reviewed in a task tracking system (adds signal to worker reputation)
An endorsement that attests to authenticity of an article posted in a published news service
Reputation systems for social media platforms
Social impact - philanthropic grant helped attesting individual (or witnessed)
Academic class completed or exam score achieved
## Formats

Linked Trust Example
Verifiable Endorsement Example

### Unified example with composition

{
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://www.w3.org/2018/credentials/examples/v1"
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
  "effectiveDate": "1970-01-01",  // core vc 2.0 see original
  "credentialSubject": {
    "id": "urn:uuid:e8096060-ce7c-47b3-a682-57098685d48d",
    "name": "skill endorsement of Alice for drone navigation"

    "linkedClaim": {
         "claim": "is_true",
         "type" : endorsement,  // or external_claim endorsement 
		"statement": "This is an endorsement regarding Alice's 'UAV Control System for Drone Navigation' achievement. Alice has an exceptional skill set as an UAV guidance control engineer. See also the attached evidence.",
        
         "aspect": "quality:skill",  // ?? optional maybe remove? 
         
         "howKnown": "first-hand",   // provenance? source? check journalism term

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
         
         "confidence": .8,
        
    }
  },
  "proof": { ... }
}
```

```
{
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://www.w3.org/2018/credentials/examples/v1"
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
  "effectiveDate": "1970-01-01",  // core vc 2.0 see original
  "credentialSubject": {
    "id": "did:web:bob.com",
    "name": "bob"

    "linkedClaim": {
         "claim": "is_true",
         "type" : expertise_claim,  // or external_claim endorsement 
		"statement": "This is a list of Bob's bona fides",
        
         "aspect": "quality:expertise",  // ?? optional maybe remove? 
         
         "howKnown": "first-hand",   // provenance? source? check journalism term

         "evidence": [
    	{
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
  	],
         
         "confidence": 1,
        
    }
  },
  "proof": { ... }
}


### Verifiable Endorsement Example
(may be generated from the decomposed claims above)

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
    // Note that the credentialSubject.id is the id of an individual Achievement in the target VC
    // It could just as readily be the id of the VC, but the authors wanted to highlight that a section of the VC could be targeted
    "id": "urn:uuid:e8096060-ce7c-47b3-a682-57098685d48d",
    "digestMultibase": "zb1B1M6Bve5JEaNqeJSmuE",
    "endorsement": {
       "statement": "This is an endorsement regarding Alice's 'UAV Control System for Drone Navigation' achievement. Alice has an exceptional skill set as an UAV guidance control engineer. See also the attached evidence.",
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

### Model

The endorsement could be rolled up with 

Replabs DAO: https://replabs.web.app/dao/tec
Replabs Twitter: https://replabs.web.app/twitter/1548015533710123010


### Linked Trust Datamodel Example

```
{
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://www.w3.org/2018/credentials/examples/v1"
  ],
  "id": "http://trustclaims.whatscookin.us/claim/1001",
  "type": ["VerifiableCredential", "LinkedCredential"],
  "issuer": "https://trustclaims.whatscookin.us/issuers/101",
  "issuanceDate": "2022-08-19T00:00:00Z",
  "credentialSubject": {
    "id": "https://en.wikipedia.org/wiki/Myanmar_Army",
    "name": "Myanmar Military",
    "linkedClaim": {
         "claim": "harmed",
         "object": {
             "id": "https://en.wikipedia.org/wiki/Salingyi_Township",
         }
         "aspect": "risk:safety",
         "effective_date": "2021-12-07",
         "how_known": "second-hand",
         "source": [ "direct conversation with local resident", "https://twitter.com/Shoon90644344/status/1468184590896435202"],
         "qualifier": "12 villagers were burned to death by Myanmar military, according to local sources",
         "confidence": .9,
         "reviewRating": {
             rating: -100,
             rating_max: 100,
             rating_min: -100
         } 
    }
  },
  "proof": { ... }
}
```

Related work:

OpenTrustClaims use cases
Trustclaims.whatscookin.us

https://github.com/Whats-Cookin/trust_claim_backend
https://github.com/Whats-Cookin/trust_claim

Models to roll up endorsements into reputation hierarchies:
https://github.com/Replabs
