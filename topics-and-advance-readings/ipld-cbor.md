# Interplanetary Linked Data (IPLD) using CBOR and COSE-signed payloads 

By [jonnycrunch](https://github.com/jonnycrunch)

[Rebooting the Web of Trust 10, Spring Buenos Aires, Argentina 2020](https://github.com/WebOfTrustInfo/rwot10-buenosaires)

## Abstract

In my [last paper](https://github.com/WebOfTrustInfo/rwot7-toronto/blob/master/final-documents/ipld-did.md) I described leveraging Interplanetary Linked Data (IPLD) for Storage of DID documents and Verifiable Credentials [[1]](#1).  In this paper, I aim to discuss Concise Binary Object Representation (CBOR), which is the native data format used when storing IPLD objects and why it is a superior document syntax for representing DID documents.  In making my case, I will also explain how content addressing through hash-based linking is a better approach as compared to [JSON-LD]((https://www.w3.org/TR/json-ld/)) [[2]](#2), which is currently proposed as the default DID document syntax. I will also explore COSE signatures over CBOR serialized data using semanitcally interoperable self-decribing data that is store in IPLD syntax. And finally, I will address the drawbacks of using CBOR and COSE as a format for DID documents.     

## What is CBOR?

Like Javascript Object Notation ([JSON](https://tools.ietf.org/html/rfc7159)), Concise Binary Object Representation ([CBOR](https://tools.ietf.org/html/rfc7049#page-53)) defines a set of formatting rules for the portable representation of structured data. However, unlike JSON, which is a human-readable utf-8 text-based, language-independent data interchage format, CBOR aims to be a more concise machine-readible language-independent data interchange format that is self-describing and has built-in semantics for easy "batteries included" interoperability.  Natively, CBOR can support all JSON data types for conversion to and from JSON for human consumption. However, it is also extensible to allow for streaming media types and fallbacks to allow for consuption by earlier decoders.  

**Example 1: Show major tags and extensibility of indefinite length of string data**

Assume the following CBOR sequence:  
```
   0b010_11111 0b010_00100 0xaabbccdd 0b010_00011 0xeeff99 0b111_11111

   5F              -- Start indefinite-length byte string
      44           -- Byte string of length 4
         aabbccdd  -- Bytes content
      43           -- Byte string of length 3
         eeff99    -- Bytes content
      FF           -- "break"

   After decoding, this results in a single byte string with seven
   bytes: 0xaabbccddeeff99.
```

In CBOR, a data object can optionally be preceded by a tag to give it additional semantics while retaining its structure.  The tag  represents an integer number as indicated by the tag's integer value; the (sole) data item is carried as content data.  If a tag requires structured data, this structure is encoded into the nested data item.  The definition of a tag usually restricts what kinds of nested data item or items can be carried by a tag. A tag always applies to the item that is directly followed by it. Thus, if tag A is followed by tag B, which is followed by data item C, tag A applies to the result of applying tag B on data item C. That is, a tagged item is a data item consisting of a tag and a value. [5]

The [CBOR specification](https://tools.ietf.org/html/rfc7049) allows for CBOR encoders to only emit the resulting CBOR in a particular canonical form [[5]](#5).  In addition, such protocols might also have the decoders validate that their input is in 'canonical' form.  Those protocols are free to define what they mean by a 'canonical' format and what encoders and decoders are expected to do to achieve 'cononical' form. 


## Why IPLD?

<img src="https://cloudflare-ipfs.com/ipfs/Qmanm7XMi4M8jUScx7hApyMx8rwBh5CSwgRuszSLFsH5fo" alt="drawing" width="300"/>

***Image 1. Concept of IPLD linking data across ecosystems***


Content addressing through hashes has become a widely-used means of connecting data in distributed systems. [IPLD](https://ipld.io) is a way of representing hash-linked data to be used in content-addressed data retrieval systems such as [IPFS](https://ipfs.io). Other content that can be resolved using IPLD includes Git repositories and blockchains such as Bitcoin, Ethereum, and ZCash. IPLD enables creation of decentralized data-structures that are universally addressable, facilitating resolving content accross different protocols. It achieves this through an interoperable data model that represents various protocol formats. IPLD relies on [Content Identifiers (CIDs)](https://github.com/ipld/cid) for content addressing. CIDs are a self-describing, flexible, and interoperable way of expressing cryptographic hashes. It uses several multiformats to achieve flexible self-description, namely [multihash](https://github.com/multiformats/multihash) for hashes, [multicodec](https://github.com/multiformats/multicodec) for data content types, and [multibase](https://github.com/multiformats/multibase) to represent the base encoding of the CID itself. This interoperability makes IPLD a valuable structure for the DID document that can be used across a variety of DID methods or distributed ledgers and ensures cryptographic validity of the DID document.

![CID](https://cloudflare-ipfs.com/ipfs/QmX5cZLhrFoEp1vPotnmfma1pxouA9NzVC91tJ2swPS22v "Explaination of Content Identifiers")

***Image 2. Breakdown of a Content Identifier (CID)***

## How data is linked in IPLD?

IPLD uses an abstract model for linking data via cryptographic hashes, which enables the ability to traverse this link to the referenced data via path `"/"` notation.  This is accomplished by dereferencing this CID, resolving the downstream resource, cryptographically validating the hash of the returned resource and finally appending the retrieved data at the path as though it was one continuous payload. Since the referenced data is linked cryptographically, it represents an immutable Uniform Resource Identifier (URI) as compared to mutable URI if JSON-LD (more below).  This path notation has its roots in the Linux [Filesystem Hierarchy Standard](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard).  A link in IPLD is represented in JSON as a "link object" and uses the path syntax `"/"` as the key to the object that is followed by the CID of the link.    

For example:   
```
{ "/" : "zdpuAmoZixxJjvosviGeYcqduzDhSwGV2bL6ZTTXo1hbEJHfq" }
```

One additional point to emphasize is that the content loaded into IPLD is serialized and stored using Concise Binary Object Representation [(CBOR)](https://cbor.io) with associated algorithms for 'cononical' serialization, allowing for deterministic representation and retrieval. 

Moreover, content addressable linking of data using IPLD can be cryptographically resolved, dereferenced and retrieved using the HTTP protocol using various domain gateways.  The content can be retrieved via numerous http gateways including: [ipfs.io](https://ipfs.io), [ipfs.infura.io](https://ipfs.infura.io), [and cloudflare-ipfs.com](https://cloudflare-ipfs.com), as well as a locally hosted gateway or via the command-line [ipfs](https://ipfs.io) application. 

**Retrieval of IPLD content represented as dag-cbor from ipfs.io gateway and validating the content by reloading it into ipfs via command-line**   
```
> curl -s https://ipfs.io/api/v0/dag/get?arg=zdpuAmoZixxJjvosviGeYcqduzDhSwGV2bL6ZTTXo1hbEJHfq | ipfs dag put 
```
outputs: `zdpuAmoZixxJjvosviGeYcqduzDhSwGV2bL6ZTTXo1hbEJHfq`, thus validating the hash of the cid

**Retrieval of IPLD content represented as dag-cbor from ipfs command-line**
```
> ipfs dag get zdpuAmoZixxJjvosviGeYcqduzDhSwGV2bL6ZTTXo1hbEJHfq 
```
outputs the original JSON-LD schema [link](https://ipfs.io/api/v0/dag/get\?arg\=zdpuAmoZixxJjvosviGeYcqduzDhSwGV2bL6ZTTXo1hbEJHfq). 


## Semantic tag in CBOR for IPLD semantics 

As mentioned above, the CBOR specification allows for tags to enhance the semantic description of the data that follows.  IPLD CIDs are already built into the CBOR tags registry with the value '42'.  This tag describes the byte string representation of a CID linked object and is a building block for other methods found in the CBOR specification, such as COSE-signing (see below).  

```
Tag: 42 
  Data item: byte string
  Semantics: IPLD content identifier
  Created: 2019-08-20
```

## Dangers of JSON-LD

When using JSON-LD in a browser, it is impossible to discover the Base IRI after an http redirect ([see #316](https://github.com/json-ld/json-ld.org/issues/316)), and the content of the `@context` can potentially change over time [[3]](https://github.com/json-ld/json-ld.org/issues/547). Finally, since a URI depends upon the security of DNS, [DNS spoofing/DNS poisoning](https://en.wikipedia.org/wiki/DNS_spoofing) could offer a simple attack vector.  Essentially, without much effort, an attacker can adjust the cache of a DNS server and begin pointing traffic from 'schema.org' (or any other desired host) to anywhere else on the internet or local LAN. Given the critical nature of the JSON-LD `@context` resource, the attacker can make a fraudulent signature pass as being valid. 

Using IPLD, we can also use the entire JSON data model and we can layer any JSON-LD on top of IPLD [[4]](https://github.com/ipfs/ipfs/issues/36). This will enable cryptographic guarantees to the authenticity of the JSON-LD schema and mitigate such an attack.


## Benefits of using CBOR as the default Document Syntax for DID documents 

One large advantage of the CBOR and IPLD approach described here is that the data formats are unequivically well represented, so much so that it is machine-readble (by design).  Starting the data modeling with a binary representation and working upward to human-readibility allow for a solid foundation for data representation and decreases the possibility of mis-representation.  This is critical to the role of the DID and DID document that it be well represented using cryptographic methods and hash-based linking of data elements. 

Summary of the benefits of CBOR as default DID document syntax include: 

- CBOR has capabilities that are not present in JSON and are appropriate to use.  One example of this is the fact that CBOR has a method of encoding binary directly without first converting it into a base64-encoded string.
- CBOR has the ability to extend the data model by allowing for tagging to enhance the semantic representation at the Byte-level without the need for convoluted algorithmic exercises prone to misrepresentations.  
- Paired with COSE-signatures and CID tagging DID documents harden security 

## Drawbacks

- The CBOR specification does not define a deterministic encoding format and this is left to implementers to determine their own definition of what is deterministic.  Therefore at present while the format presented in IPLD is deterministic, it is not clear how this was generated such that other systems can replicate the results. 
- Not resolvable without hosting (This could be construed as a feature for linking private data).   
- `@context` is not a reserved word in the IPLD specificatioin.
- `{ "/" : "<CID>"` is not currently valid syntax for JSON-LD.  
- Not at all human-readable or intuative. 
- Lack of libraries to transform data from JSON-LD to IPLD.  


## COSE signatures of CBOR data in IPLD


**Example 2: CBOR siqnature syntax (tag 98) of pay as CID (tag 42)**

```
98(
  [
    / protected / h'a10300' / {
        \ content type \ 3:0
      } / , 
    / unprotected / {}, 
    / payload /  42: 'bafyreibtkfbzqiwdhd5bv53wrag43jbz4ytyixigde6wa5zuddxciq7s2m', 
    / signatures / [
      [
        / protected / h'a10126' / {
            \ alg \ 1:-7 \ ECDSA 256 \
          } / , 
        / unprotected / {
          / kid / 4:'did:ipid:12D3KooWDXDEZtLW5k16DjeHWkFZEeTKUF7PnzzY7m2UocmduhZV;/publicKey/0'
        }, 
        / signature / h'e2aeafd40d69d19dfe6e52077c5d7ff4e408282cbefb5d06cbf414af2e19d982ac45ac98b8544c908b4507de1e90b717c3d34816fe926a2b98f53afd2fa0f30a'
      ]
    ]
  ]
)
```

## Security considerations

Using the same key for two different algorithms can leak information about the key.  It is therefore recommended that keys be restricted to a single algorithm.


## Conclusion

TBD

## Discussion and Future Work

TBD 


## References 

[1] [WebOfTrustInfo/rebooting-the-web-of-trust-fall2016](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2016)

[2] [https://www.w3.org/TR/json-ld/](https://www.w3.org/TR/json-ld/)

[3] [https://github.com/json-ld/json-ld.org/issues/547](https://github.com/json-ld/json-ld.org/issues/547)

[4] [https://github.com/ipfs/ipfs/issues/36](https://github.com/ipfs/ipfs/issues/36)

[5] [https://tools.ietf.org/html/rfc7049](https://tools.ietf.org/html/rfc7049)