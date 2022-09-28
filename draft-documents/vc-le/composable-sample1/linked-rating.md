{
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://www.w3.org/2018/credentials/examples/v1"
  ],
"type": [
    "VerifiableCredential",
    "LinkedClaim"
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
         "claim": "rated",
         "type" : expertise_claim,  // or external_claim endorsement 
		"statement": "Bob is an expert in the area of UAV systems",
        
         "aspect": "quality:skill",  // ?? optional maybe remove? 
         
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
