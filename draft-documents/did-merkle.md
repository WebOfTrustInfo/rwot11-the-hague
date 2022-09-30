# did:merkle

One Time Merkle Proofs for less correlatable credentials ?

One Time Revealable Credentials ?

Group credentials offer an opportunity for privacy preserving verification of group membership. We want to issue the exact same VC to all members of a group so that each VC reveals no information about who is a member of the group. We propose to do this by issuing a VC with subject id of the merkle root of cryptographic identifiers controlled by various group members. Upon presentation of that VC to a Verifier, group membership can be verified by testing that the cryptographic id that signs the VP is in the merkle tree. We create a did:merkle and merkleProof proof type so that the VC is issued to did:merkle and the VP includes TWO proofs. One is the traditional tamper-evident signature. The second is the merkleProof. For additional correlation protection, the issuer may include multiple cryptographic ids for each recipient, allowing recipients to use different proofs with different verifiers. This solution is cryptosuite agnostic and does not depend on novel cryptography such as group signatures.

NOTE: More about anti-correlation, or at least that its the two parts together (group membership and multiple proofs per member)

>Fred  
>NOTE: This kind of solution can be used with:  
>- Credentials with different values  
>- Different credentials attributes (see "Appendix")

## Creative Brief

### Audience
Technical: Developers, Standards advocates
Practical: Regulators, Product Managers, CEOs

### Change in behavior
We want readers to adopt this technology for appropriate use cases. Secondarily, we want them to contribute to a conversation about how to better support individuals in their group interactions.

### Key Points
1. Mathematically, anonymity can be expressed as the degree to which an partially identified party can be confused with other parties. 
2. Group membership is proven without revealing the members of the group
3. The same Verifiable Credential is issued to all members of the group, making the group membership aspects of the VC devoid of any personal data and personally identifiable information. Issuers must take care to not put other personal data in the shared VC.
4. Uses well-proven, tested cryptography
5. VC issuers embed multiple cryptographic identifiers for each member to enable different proofs for different verifiers. This is a flexible policy choice by the issuer.
6. Wallets need to track with proofs have been distributed to minimize re-use.
7. Issuers may support automated refresh properties
8. Issuers can selectively revoke the VC for particular members
9. ...
10. Implementation Guidance
    a. Wallets would benefit from using HDKeys for generating the ids used in the merkle tree. 
11. Opportunities for future evolution
    a.Use HDKeys in the merkle tree (so wallets give the issuer a master pubkey rather than individual keys)
    b. Additional claim content could be indexed in the merkletree
    c. A did:indirectMerkle could allow a decentralized registry to provide the "current" merkle root
    

### Output
1. DID Specification
2. Revocation Specification for Group VC: Member Revocation
3. White paper on using did:merkle to improve privacy for VCs related to group membership

## DID Method Name
A merkle DID is immutable and cannot be updated or deactivated.

The namestring that shall identify this DID `method-name` is: `merkle`.

A DID that uses this method MUST begin with the following prefix `did:merkle`. The prefix string MUST be in lowercase. The remainder of the DID after the prefix, is specified below:

### Method Specific Identifier
The DID merkle method-specific identifier (merkleroot-id) is made up of a root hash of a merkle-tree.


### merkle DID method syntax
```abnf
merkle-did         = "did:merkle:" merkleroot-id
merkleroot-id =    *( *idchar ":" ) 1*idchar
idchar             = ALPHA / DIGIT / "." / "-" / "_" / pct-encoded
pct-encoded        = "%" HEXDIG HEXDIG
```

### Examples of `did:merkle` identifiers

An example of a DID merkle:

```abnf
did:merkle:7Tqg6BwSSWapxgUDm9KKgg
```

An example of a DID merkle URL (used for verifying membership)
```
did:merkle:7Tqg6BwSSWapxgUDm9KKgg?leaf=did:example:abc&proof=hash1:hash2:hash3#key1

```

The fragment, if any, is applied to the resource at the leaf. 


## Multihash
https://github.com/multiformats/multihash
```
<varint hash function code><varint digest size in bytes><hash function output>
```
NOTE: TURN INTO ABNF
https://datatracker.ietf.org/doc/html/draft-snell-multihash-00
```abnf=
   varint-terminator = %x00-7f
   varint-continuation = %x80-ff
   unsigned-varint = *8varint-continuation varint-terminator
```

## Multibase
https://github.com/multiformats/multibase 
```abnf=
base-identifier = <ascii character>
multibase = base-identifier {base-encoded-data}
```


## DID Documents
A DID Document associated with a merkle DID is deterministically generated to enable DID-aware software to verify actions taken by a member of the group. The [representation of a when requested for production](https://www.w3.org/TR/did-core/#representations) MUST meet the DID Core specification.

### Deterministic DID Document
**Example 1**
```jsonld
{
  "@context": "https://www.w3.org/ns/did/v1",
  "id" : "did:merkle:zH3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV"
}
```

## Key Agreement
It's not clear we can do classic key agreement as a verification relationship because we are not able to perform encryption or decryption just because we have the did:merkle. In an interactive situation, a controller **could** give the did:merkle along with a merkle_path and their key to enable encryption... but if you are already in an interactive engagement, one can just first prove membership by authentication, then bootstrap a key for encryption/decryption.

## VC Issued to a did:merkle group
```jsonld
{
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://www.w3.org/2018/credentials/examples/v1",
    "https://hackmd.io/@JoeAndrieu/Hk_2NMmfi/download"
  ],
  "type": [
    "VerifiableCredential"
  ],
  "issuer": "did:ex:italy",
  "issuanceDate": "2010-01-01T19:23:24Z",
  "credentialSubject": {
    "@context": "https://hackmd.io/@JoeAndrieu/Hk_2NMmfi/download",
    "id": "did:merkle:zH3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV",
    "citizenship": "it"
  },
  "proof": {
    "type": "RsaSignature2018",
    "created": "2017-06-18T21:19:10Z",
    "proofPurpose": "assertionMethod",
    "verificationMethod": "did:ex:italy#key-1",
    "proof": "eyJhbGciOiJSUzI1NiIsImI2NCI6ZmFsc2UsImNyaXQiOlsiYjY0Il19..TCYt5XsITJX1CxPCT8yAV-TVkIEq_PbChOMqsLfRoPsnsgw5WEuts01mq-pQy7UJiN5mgRxD-WUcX16dUEMGlv50aqzpqh4Qktb3rk-BuQy72IFLOqV0G_zS245-kronKb78cPN25DGlcTwLtjPAYuNzVBAh4vGHSrQyHUdBBPM"
  }
}
```

## VP (with VC) presented by a member of a did:merkle group
```jsonld
{
  "@context" : ["https://www.w3.org/2018/credentials/v1"],
  "type" : "VerifiablePresentation",
  "verifiableCredential" : {
      "@context": [
        "https://www.w3.org/2018/credentials/v1",
        "https://www.w3.org/2018/credentials/examples/v1",
        "https://hackmd.io/@JoeAndrieu/Hk_2NMmfi/download"
      ],
      "type": [
        "VerifiableCredential"
      ],
      "issuer": "did:ex:italy",
      "issuanceDate": "2010-01-01T19:23:24Z",
      "credentialSubject": {
        "@context": "https://hackmd.io/@JoeAndrieu/Hk_2NMmfi/download",
        "id": "did:merkle:zH3C2AVvLMv6gmMNm3uVAjZpfkcJCwDwnZn6z3wXmqPV",
        "citizenship": "it"
      },
      "proof": {
        "type": "RsaSignature2018",
        "created": "2017-06-18T21:19:10Z",
        "proofPurpose": "assertionMethod",
        "verificationMethod": "did:ex:italy#key-1",
        "proof": "eyJhbGciOiJSUzI1NiIsImI2NCI6ZmFsc2UsImNyaXQiOlsiYjY0Il19..TCYt5XsITJX1CxPCT8yAV-TVkIEq_PbChOMqsLfRoPsnsgw5WEuts01mq-pQy7UJiN5mgRxD-WUcX16dUEMGlv50aqzpqh4Qktb3rk-BuQy72IFLOqV0G_zS245-kronKb78cPN25DGlcTwLtjPAYuNzVBAh4vGHSrQyHUdBBPM"
      }
  },
  "proof": {
    "type": "RsaSignature2018",
    "created": "2018-09-14T21:19:10Z",
    "proofPurpose": "authentication",
    "verificationMethod": "did:merkle:zH3C2AVvLMv6gmMNm3uVAjZpfkcJCwDwnZn6z3wXmqPV?leaf=did:key:abc&path=hash1:hash2:hash3", 
    "challenge": "1f44d55f-f161-4938-a659-f8026467f126",
    "domain": "4jt78h47fh47",
    "jws": "eyJhbGciOiJSUzI1NiIsImI2NCI6ZmFsc2UsImNyaXQiOlsiYjY0Il19..kTCYt5
      XsITJX1CxPCT8yAV-TVIw5WEuts01mq-pQy7UJiN5mgREEMGlv50aqzpqh4Qq_PbChOMqs
      LfRoPsnsgxD-WUcX16dUOqV0G_zS245-kronKb78cPktb3rk-BuQy72IFLN25DYuNzVBAh
      4vGHSrQyHUGlcTwLtjPAnKb78"
  }
}
```


## VC Issued by a member of a did:merkle group
(not quite complete)
```jsonld
{
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://www.w3.org/2018/credentials/examples/v1",
    "https://hackmd.io/@JoeAndrieu/Hk_2NMmfi/download"
  ],
  "type": [
    "VerifiableCredential"
  ],
  "issuer": "did:merkle:zH3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV?did=XYZ&proof=123",
  "issuanceDate": "2010-01-01T19:23:24Z",
  "credentialSubject": {
    "@context": "https://hackmd.io/@JoeAndrieu/r1ADDMQGs/download",
    "id": "did:merkle:zH3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV",
    "citizenship": "it"
  },
  "proof": [
    {
      "type": "merkleProof",
      "created": "2017-06-18T21:19:10Z",
      "proofPurpose": "assertionMethod",
      "verificationMethod": "did:merkle:abc?did=XYZ#proof-1",
      "signature": "eyJhbGciOiJSUzI1NiIsImI2NCI6ZmFsc2UsImNyaXQiOlsiYjY0Il19..TCYt5XsITJX1CxPCT8yAV-TVkIEq_PbChOMqsLfRoPsnsgw5WEuts01mq-pQy7UJiN5mgRxD-WUcX16dUEMGlv50aqzpqh4Qktb3rk-BuQy72IFLOqV0G_zS245-kronKb78cPN25DGlcTwLtjPAYuNzVBAh4vGHSrQyHUdBBPM"
    },
    {
      "type": "RsaSignature2018",
      "created": "2017-06-18T21:19:10Z",
      "proofPurpose": "assertionMethod",
      "verificationMethod": "did:merkle:abc?did=XYZ#key-1",
      "merkleProof": "eyJhbGciOiJSUzI1NiIsImI2NCI6ZmFsc2UsImNyaXQiOlsiYjY0Il19TCYt5XsITJX1CxPCT8yAV-TVkIEq_PbChOMqsLfRoPsnsgw5WEuts01mq-pQy7UJiN5mgRxD-WUcX16dUEMGlv50aqzpqh4Qktb3rk-BuQy72IFLOqV0G_zS245-kronKb78cPN25DGlcTwLtjPAYuNzVBAh4vGHSrQyHUdBBPM"
    }
  ]
}
```

## DID transaction operations

### Create DID
Steps to create a merkle DID:
```
                               ┌(Hash 0-0-0)─< did:key:JulietPubKey1
                    ┌(Hash 0─0)┤     
                    │          └(Hash 0─0-1)─< did:key:FedericoPubKey1
           ┌(Hash 0)┤  
           │        │          ┌(Hash 0─1-0)─< did:key:JulietPubKey2
           │        └(Hash 0-1)┤     
  (Merkle  │                   └(Hash 0─1-1)─< did:key:MarioPubKey1
─- Root  --┤  
   Hash)   │                   ┌(Hash 1-0-0)─< did:key:JulietPubKey3
           │        ┌(Hash 1-0)┤     
           │        │          └(Hash 1-0-1)─< did:key:MarioPubKey2
           └(Hash 1)┤  
                    │          ┌(Hash 1-1-0)─< did:key:MarioPubKey3
                    └(Hash 1-1)┤
                               └(Hash 1-1-1)─< did:key:FedericoPubKey2 
```
1. Holders share a set of `n` public keys or DIDs with the issuer
2. The issuer decide the batch size for issuance of the group credential
3. Once all holders `n` public keys or DIDs are collected the issuer generates a merkle-tree where each leave in the merkle-tree represents a hash of a single public key or DID
4. The issuer use the merkle-root hash as the DID identifier
5. The merkle DID can now be constructed by appending the merkle-root hash to `did:merkle`
6. Merkle DID example: `did:merkle:abc`

### Resolve DID

### Update DID
Merkle DIDs are immutable and cannot be updated.

### Deactivate DID
Merkle DIDs are immutable and cannot be deactivated.




## Security Considerations
1. Hash algorithm being used and security issues with MD5 as example
 
## Privacy Considerations
1.  Issuers must ensure that no PII is exposed via the verifiable credential issued to the group
2.  The quality of the Merkle tree has to be assured by the issuer (high number of different people and keys)  
 
## References
 
 ## TODO:
1.  How to update the merkle tree by removing or adding new users to the group


## Down the rabbit hole

### Claim value moved to leaves

Claim value can be moved from credential json to hashed contents of merkle tree leaves  

What would change from initial example :  

Updated credential content:  

"citizenship"~~: "it"~~  

New merkle would become:  

```
                               ┌(Hash 0-0-0)─< did:key:JulietPubKey1, IT
                    ┌(Hash 0─0)┤     
                    │          └(Hash 0─0-1)─< did:key:FedericoPubKey1, IT
           ┌(Hash 0)┤  
           │        │          ┌(Hash 0─1-0)─< did:key:JulietPubKey2, IT
           │        └(Hash 0-1)┤     
  (Merkle  │                   └(Hash 0─1-1)─< did:key:MarioPubKey1, IT
─- Root  --┤  
   Hash)   │                   ┌(Hash 1-0-0)─< did:key:JulietPubKey3, IT
           │        ┌(Hash 1-0)┤     
           │        │          └(Hash 1-0-1)─< did:key:MarioPubKey2, IT
           └(Hash 1)┤  
                    │          ┌(Hash 1-1-0)─< did:key:MarioPubKey3, IT
                    └(Hash 1-1)┤
                               └(Hash 1-1-1)─< did:key:FedericoPubKey2, IT
```

### Claim with differents value moved to leaves

Claim values can be moved from credential json to hashed contents of Merkle tree leaves 

Values can be different from one holder to another  

What would change from initial example:  

Removed from credential json:  

"citizenship"~~: "it"~~  

Introducing "Bjorn" from Sweden inside the initial tree, replacing Federico as an example

New merkle would become:  

```
                               ┌(Hash 0-0-0)─< did:key:JulietPubKey1, IT
                    ┌(Hash 0─0)┤     
                    │          └(Hash 0─0-1)─< did:key:BjornPubKey1, SU
           ┌(Hash 0)┤  
           │        │          ┌(Hash 0─1-0)─< did:key:JulietPubKey2, IT
           │        └(Hash 0-1)┤     
  (Merkle  │                   └(Hash 0─1-1)─< did:key:MarioPubKey1, IT
─- Root  --┤  
   Hash)   │                   ┌(Hash 1-0-0)─< did:key:JulietPubKey3, IT
           │        ┌(Hash 1-0)┤     
           │        │          └(Hash 1-0-1)─< did:key:MarioPubKey2, IT
           └(Hash 1)┤  
                    │          ┌(Hash 1-1-0)─< did:key:MarioPubKey3, IT
                    └(Hash 1-1)┤
                               └(Hash 1-1-1)─< did:key:BjornPubKey2, SU
```

### Claim attribute with different values moved to leaves

Claim attribute and values can be moved from credential json to the hashed content of merkle tree leaves  
Values can be different from one holder to another  

Claim attributes can be different from one holder to another

Introducing "Bjorn" from Sweden inside the initial tree, replacing Federico and Mario as an example

What would change from initial example:  

Removed from credential json:  

~~"citizenship": "it"~~  

New merkle would become:  

```
                               ┌(Hash 0-0-0)─< did:key:JulietPubKey1, citizenzip:IT
                    ┌(Hash 0─0)┤     
                    │          └(Hash 0─0-1)─< did:key:BjornPubKey1, citizenzip:SU
           ┌(Hash 0)┤  
           │        │          ┌(Hash 0─1-0)─< did:key:JulietPubKey2, citizenzip:IT
           │        └(Hash 0-1)┤     
  (Merkle  │                   └(Hash 0─1-1)─< did:key:JulietPubKey3, yearofbirth:2001
─- Root  --┤  
   Hash)   │                   ┌(Hash 1-0-0)─< did:key:BjornPubKey2, citizenzip:SU
           │        ┌(Hash 1-0)┤     
           │        │          └(Hash 1-0-1)─< did:key:JulietPubKey4, yearofbirth:2001
           └(Hash 1)┤  
                    │          ┌(Hash 1-1-0)─< did:key:BjornPubKey3, yearofbirth:1974
                    └(Hash 1-1)┤
                               └(Hash 1-1-1)─< did:key:BjornPubKey4, yearofbirth:1974
```

Note : attribute (e.g. here: "citizenship") should point to an associated context content

### Different Claim Attributes with different Values moved to leaves

Claim attributes and values can be moved from credential json to the hashed content of merkle tree leaves  

Values can be different from one holder to another  

Claim attributes can be different from one old to another

Introducing "Bjorn" from Sweden inside the initial tree, replacing Federico and Mario as an example


What would change from initial example:  

Removed from credential json:  

~~"citizenship": "it"~~  

New merkle would become:  

```
                               ┌(Hash 0-0-0)─< did:key:JulietPubKey1, citizenzip:IT
                    ┌(Hash 0─0)┤     
                    │          └(Hash 0─0-1)─< did:key:BjornPubKey1, citizenzip:SU
           ┌(Hash 0)┤  
           │        │          ┌(Hash 0─1-0)─< did:key:JulietPubKey2, citizenzip:IT
           │        └(Hash 0-1)┤     
  (Merkle  │                   └(Hash 0─1-1)─< did:key:MarioPubKey1, citizenzip:IT
─- Root  --┤  
   Hash)   │                   ┌(Hash 1-0-0)─< did:key:JulietPubKey3, citizenzip:IT
           │        ┌(Hash 1-0)┤     
           │        │          └(Hash 1-0-1)─< did:key:MarioPubKey2, citizenzip:IT
           └(Hash 1)┤  
                    │          ┌(Hash 1-1-0)─< did:key:MarioPubKey3, citizenzip:IT
                    └(Hash 1-1)┤
                               └(Hash 1-1-1)─< did:key:BjornPubKey2, citizenzip:SU
```

Note : attribute (e.g. here: "citizenship") should point to an associated context content