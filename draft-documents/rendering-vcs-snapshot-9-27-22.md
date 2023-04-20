# Rendering Verifiable Credentials  

Authors  

*   Dmitri Zagidulin @dmitrizagidulin  
*   Charles Lehner @cel  
*   Manu Sporny  
*   Ben Goering @bengo

## Ideas / TODO

*   propose a registry (or meta-type) of renderers as a work item in ccg  
*   ways of improving data model
*   Security Consideration of pre-baked rendered image vs templatehtml5 custom element renderer
*   and/or '3D renderer' (webgl, css 3d)
*   TODO: Check with Manu about adding the year to the render type. (We might not need it)  
*   appendix of test fixtures  
    
## Abstract  

In the Verifiable Credentials ecosystem, wallets and verifiers have expressed a strong preference for consistent rendering mechanisms because they will simplify the implementation of applications that are safe and easy to use. Several specifications have proposed credential rendering methods for a specific set of use-cases, but no interoperable scheme has emerged across use-cases. In this paper, the authors survey existing methods and propose a unified data model for rendering hints, renderer descriptions, and security considerations to keep in mind when using them.  

## Introduction

The Verifiable Credentials ecosystem is experiencing increasing adoption in a variety of markets such as education, supply chain, retail, banking and finance, workforce training, and corporate and government identification cards. Each of these markets have issued credentials for hundreds of years and have pre-conceived notions around what their credentials should look like. Similarly, it is important to understand that visually representing a Verifiable Credential could accidentally exclude those with accessibility needs. We need to consider people with sight needs such as larger font sizes, or the need to use colors that do not create challenges for those that are color blind. We also need to design for those that cannot see, how do they navigate digital wallets and use Verifiable Credentials?

This paper explores ways in which the Verifiable Credentials data model could be extended to support visual, audio, and physical renderings for Verifiable Credentials.  

## Use Cases  

### Presenting PDF Rendering at Border Crossing with no internet  

Alice is attending a cryptography conference 30 miles away in the next country, and will need to present proof of attendance at the border in order for border guards to authorize their entry. But the border crossing is known to have no cellular connectivity, so Alice is worried about how they will present their digital verifiable credential.  

Because Alice's conference attendance VC has a 'render' property of a PDF rendering, Alice's identity wallet can show a 'print' affordance on the credential, which will send the PDF representation of the credential to Alice's printer. This representation may have a QR code on it that the border crossing agents can scan in order to reconstruct a digital version of the Verifiable Credential and make an authorization decision.  

### Rendering Credentials while implementing an Open Source Identity Wallet  

An open source identity wallet may have credentials from an open world of issuers, but it wants to present them all in a consistent way without failing to render contextually relevant credential data for credential types that the wallet implementor didn't explicitly configure in their code. The wallet user interface can make use of VC render properties to determine an appropriate way of rendering the otherwise-unknown credential type.  

### Rendering Credentials on the web to initiate Issuance  

An end user uses a web application to solicit a credential. The Issuer creates a VC and presents it to the end-user via an HTML web page. The designer of the issuance web page wants to render the credential for the end-user so that the end-user can intuitively visualize the credential before deciding whether to initiate receiving the credential into their wallet.  

## Existing Specifications Overview  

### Open Badges (v1 - v3)  

The Open Badges family of specifications have traditionally embedded (or linked to) a pre-rendered static image, to present a credential visually. 

\[link to specs, name of field.\]  

[https://imsglobal.github.io/openbadges-specification/ob\_v3p0.html#achievementcredential](https://imsglobal.github.io/openbadges-specification/ob_v3p0.html#achievementcredential) (e.g. image property of AchievementCredential)  

Note that this is different from the "baking" mechanism ([https://imsglobal.github.io/openbadges-specification/ob\_v3p0.html#baked-badge](https://imsglobal.github.io/openbadges-specification/ob_v3p0.html#baked-badge)) which embeds the full credential data in the image (i.e. as a CDATA comment in an SVG image).

This paper allows this usecase  

### DIF Credential Manifest

The Credential Manifest spec [https://identity.foundation/credential-manifest/](https://identity.foundation/credential-manifest/) has several display-related properties in its \```output_descriptors` section:``  

*   \`styles\` - 
*   \`display\` - 

### DIF Wallet Rendering

The Wallet Rendering spec draft [https://identity.foundation/wallet-rendering/](https://identity.foundation/wallet-rendering/) grew out of Credential Manfest spec, and used in Presentation Exchange use cases.

### RWoT 11 Advanced Reading Paper

*   Manu's [advanced reading](https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/advance-readings/rendering-verifiable-credentials.md) for this RWoT [posted to CCG](https://lists.w3.org/Archives/Public/public-credentials/2022Jul/0054.html)  
    

## Use Cases

1.  University students presenting printed out PDF version of the credential at the border  
    
2.  Wallet implementer encountering a VC for which they don't have a hardcoded display comonent already  
    

## Data Model

\- Rendering is a hint from the issuer to wallet / verifier / anything else that displays the vc  
\- Needs to handle multi-modal rendering (visual, audio, tactile (braille-based), etc).  
\- Render hints can be linked (preferably hashlinked) or embedded  

### The `render` Property

This paper proposes a new property that can be associated with a Verifiable Credential called \``` render` ``. A rendering hint is a suggestion to a program that processes Verifiable Credentials that a rendering of some sort can be performed by combining the data in the Verifiable Credential with the rendering hint. An example of its usage is shown below:

```js  
{
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://www.w3.org/2018/credentials/examples/v1"
  ],
  "id": "http://example.edu/credentials/3732",
  "type": ["VerifiableCredential", "UniversityDegreeCredential"],
  "issuer": "https://example.edu/issuers/565049",
  "issuanceDate": "2010-01-01T00:00:00Z",
  "credentialSubject": {
    "id": "did:example:ebfeb1f712ebc6f1c276e12ec21",
    "name": "Jane Smith",
    "degree": {
      "type": "BachelorDegree",
      "name": "Bachelor of Science and Arts",
      "institution": "Example University"
    }
  },
  // The rendering hint
  "render": [{
    // An SVG file that can be used to render the credential
    "id": "https://svg.example/degree.svg",
    // The type of rendering hint
    "type": "SvgRenderingHint",  
    "mediaType": "image/svg+xml",
    // A multibase-encoded multi-hash of the SVG file
    "digestMultibase": "zQmAPdhyxzznFCwYxAp2dRerWC85Wg6wFl9G270iEu5h6JqW"
  }]
  "proof": { ... }
}  
```

### Visual Rendering

Visually rendering a Verifiable Credential could be done in a variety of ways. For example, a static bitmap image could be directly embedded or referenced. A templated-SVG file could be directly embedded or referenced. A list of properties that are important to display, along with their priorities for display could be included but without specific rendering instructions beyond that. A dynamic rendering of a subset of the data could be provided either statically or algorithmically (e.g., convert the entire VC to a CBOR-LD-encoded QR Code).

There are many types of visual rendering that issuers desire. Some of these visual representations are shown below:

[![University Degree](https://github.com/WebOfTrustInfo/rwot11-the-hague/raw/master/advance-readings/media/rvc-degree.jpg)](https://github.com/WebOfTrustInfo/rwot11-the-hague/raw/master/advance-readings/media/rvc-degree.jpg) [![Permanent Resident Card](https://github.com/WebOfTrustInfo/rwot11-the-hague/raw/master/advance-readings/media/rvc-prc.jpg)](https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/advance-readings/media/rvc-prc.jpg) [![Certificate of Origin](https://github.com/WebOfTrustInfo/rwot11-the-hague/raw/master/advance-readings/media/rvc-cog.jpg)](https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/advance-readings/media/rvc-cog.jpg)

It is also important to balance the variety of ways in which to visually render a Verifiable Credential with the implementation complexity of providing too many mechanisms.

For this reason, it is suggested that only one mechanism is provided that maximizes the number of use cases that can be achieved: A templated SVG format.

### Linking vs Embedding Render Hints

For each render hint item in the \`render\` property, you can:  

*   Embed the rendering hint contents directly (such a base64-encoded pre-rendered image or PDF, or a quote-escaped SVG or HTML resource)
*   Link to an externally hosted (on a website or a content-addressable store) rendering image or template
*   If you're linking, strongly consider using a hashlink (e.g. [Cryptographic Hyperlinks](https://datatracker.ietf.org/doc/html/draft-sporny-hashlink))  
    

### Pre-rendered Representation vs Template  

This paper deals solely with pre-rendered display hint, will tackle templates in Future Work section.

### Visual Rendering - Pre-Rendered Static PNG Example  

TODO: Add an example (from Open Badges v3) of a "baked" static image representation of the VC.

### Visual Rendering - Pre-Rendered Static PDF Example  

\[add PDF example from Snorre and from James at McMasters University\]  

### Visual Rendering - SVG Example  

Given the following example instantiation of the format:

```js  
  // The rendering hint
  "render": [{
    // An SVG file that can be used to render the credential
    "id": "https://svg.example/degree.svg",
    // The type of rendering hint
    "type": "SvgRenderingHint",  
    "mediaType": "image/svg+xml",
    // A multibase-encoded multi-hash of the SVG file
    "digestMultibase": "zQmAPdhyxzznFCwYxAp2dRerWC85Wg6wFl9G270iEu5h6JqW"
  }]  
``` 

A subset of the [Handlebars](https://handlebarsjs.com/guide/) format is suggested for use in the associated SVG file, due to its simplicity.  

Use of that format in an SVG file is provided as an example below:  

```svg  
<svg version="1.1" xmlns="http://www.w3.org/2000/svg">
  <rect width="300" height="100"
    style="fill:rgb(255,255,255);stroke-width:4;stroke:rgb(0,0,0)" />
  <text x="150" y="25" font-size="12" text-anchor="middle" fill="black">
    This {{credentialSubject.degree.name}} is conferred to
  </text>
  <text x="150" y="50" font-size="16" text-anchor="middle" fill="black">
    {{credentialSubject.name}}
  </text>
  <text x="150" y="75" font-size="12" text-anchor="middle" fill="black">
    by {{credentialSubject.degree.institution}}.
  </text>
</svg>  
``` 

When rendered, the following visual representation will be generated:  

[![A visual depiction of the SVG image above](https://github.com/WebOfTrustInfo/rwot11-the-hague/raw/master/advance-readings/media/rvc-svg-example.png)](https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/advance-readings/media/rvc-svg-example.png)  

Clearly, more elaborate renderings can be created by graphical illustrators. It is also important to note that bitmap images can be embedded in SVG files, thus there might not need to be a visual format other than SVG.

Items for further consideration at RWoT 11 include:

*   Is embedding an SVG document in a Verifiable Credential rendering a desired feature?
*   Are there other forms of visual rendering that are not accomplished via this approach?
*   Are there alternatives to the Handlebar template language? What subset is appropriate for us?
*   Should another graphical format other than SVG be considered?
*   Should [ARIA](https://a11y-guidelines.orange.com/en/articles/accessible-svg/) be included in the SVG file?
*   Should an "action label" be used to render buttons the individual can press such as "View Certificate" or "Present QR Code"?  
    
*   Consider use of JSONPath for templating?  
    

### Visual Rendering - HTML Example  

```
<div style="width:300px; height:100px; border: 2px solid black; text-align:center">
  <div>
    This {{credentialSubject.degree.name}} is conferred to
  </div>
  <strong style="font-size: 16px">
    {{credentialSubject.name}}
  </strong>
  <div>
    by {{credentialSubject.degree.institution}}.
  </div>
</div>
```

### Audio Rendering

Visual rendering might not always be suitable for all people or scenarios. At times, it might be useful to provide audio-based rendering. Consider the following rendering instruction:

```js  
  "render": [{
    // An rendering hint
    "type": "AudioRenderingHint",   
    "mediaType": "<TODO: what should this be?>",
    "description": "This Bachelor of Science and Arts degree is
                    conferred to Jane Smith by Example University."
  }]  
``` 

Items for further consideration at RWoT 11 include:

*   Should a phoneme-based mechanism, such as the [Speech Synthesis Markup Language (SSML)](https://www.w3.org/TR/speech-synthesis11/) be provided to ensure proper pronunciation of the text content?
*   The authors of this paper have very minimal accessibility training and requires expert assistance in order to ensure that the proper considerations are made for an audio-based rendering mechanism for Verifiable Credentials.

### Tactile Rendering (Braille-based, etc)

There are times when both visual and audio rendering are not possible. For these scenarios, a braille-based rendering might be appropriate. Consider the following rendering instruction:

```js  
  "render": [{
    // An rendering hint
    "type": "BrailleRenderingHint",  
    "mediaType": "application/braille",
    "description": ",? ,ba\*elor ( ,sci;e & ,>ts degree is 3f}r$ 6,jane ,smi? 0,example ,univ}s;y4"
  }]  
``` 

### Visual Rendering - DIF Wallet Rendering  

[DIF Wallet Rendering](https://identity.foundation/wallet-rendering/) specifies a data model for displaying (rendering) credentials, which is used as part of [DIF Credential Manifest](https://identity.foundation/credential-manifest/). The render object mechanism we propose could enable new use of DIF Wallet Rendering.  

In DIF Wallet Rendering and Credential Manifest, [Entity Style Descriptors](https://identity.foundation/wallet-rendering/#entity-styles) define image and color properties for styling entities; these styles are applied to credential issuers in [Credential Manifest](https://identity.foundation/credential-manifest/#general-composition) issuer styles property, and in [Output Descriptor Object](http://identity.foundation/credential-manifest/#output-descriptor-object) styles property. [Data Display Descriptors](https://identity.foundation/wallet-rendering/#data-display) ([Output Descriptor Object](https://identity.foundation/credential-manifest/#output-descriptor-object) / [Output Descriptor Display Object](https://identity.foundation/credential-manifest/#term:output-descriptor-display-object)) are used to extract text properties from credentials for displaying. A render object could include Entity Style Descriptors and Output Descriptors such as would be found in a Credential Manifest. Consider the following example:

```js
{  
  "type": "DIFWalletRenderingHint",  
  "mediaType": "application/json",  
  "styles": {  
    "thumbnail": {  
      "uri": "https://example.org/degree.jpg",  
      "alt": "The Degree"  
    },  
    "hero": {  
      "uri": "https://example.org/library.jpg",  
      "alt": "A photo of books in a library"  
    },  
    "text": {"color": "#ffffff"},  
    "background": {"color": "#000000"},  
  },  
  "display": {  
    "title": {  
      "path": \["$.credentialSubject.degree.name"\],  
      "schema": {"type": "string"},  
      "fallback": "this degree"  
    },  
    "subtitle": {  
      "path": \["$.credentialSubject.degree.institution"\],  
      "schema": {"type": "string"},  
      "fallback": "this university"  
    },  
    "description": {  
      "text": "Degree from institution"  
    },  
    "properties": \[  
      {  
        "label": "Student",  
        "path": \["$.credentialSubject.name"\],  
        "schema": {"type": "string"},  
        "fallback": "this student"  
      }  
    \]  
  }  
}  
```

## Algorithms  

### Credential Rendering Algorithm  

Applications that want to render a credential to an end-user may use the following algorithm to determine an appropriate renderer:  

Summary  

*   render using the end-user's user-agent settings for a preferred render for the credential (custom user settings override all others)  
    
*   render using one of the credential types render values  
    
*   render using one of the credentials's render values  
    
*   if any renderer was used that the end-user has not explicitly trusted, warn the user of the potential for Misleading Rendering (see Security Considerations), and afford for them to compare the output of all available renderers  
    

## Security Considerations  

### Misleading Rendering  

It's possible to use these renderers to render credentials in a way that is misleading when the rendering is compared to the actual data in the credential. For example, the credential issuer could include a renderer that rendered a VIP Ticket, when actually the credential only encodes a General Assembly (lower privilege) ticket. The end-user may think they are accepting a VIP ticket and, for example, remunerate at a higher VIP price than is warranted for what they think they are receiving.  

To mitigate this, user-agents can help end-users make decisions about trusted issuers (e.g. Trusted Issuer Lists), and warn them to be careful when analyzing a rendering from an untrusted issuer. User-agents may also afford for the end-user to use more than one renderer at the same time so the end-user can compare the renderings to make sure they are all in line. It may be a good idea to have an SSI Trust Framework for trusted renderers (i.e. so renderers themselves can be credentialed as trustworthy within a trust framework).  

### Link Integrity  

As always on the web and with linked data, if you follow a link (i.e. dereference it), you should ask why you trust the result of the dereferencing. A malicious link resolver could reply with a referent contrived to cause trouble, sometimes known as a [MITM (manipulator-in-the-middle) attack](https://en.wikipedia.org/wiki/Man-in-the-middle_attack).  

For example, a potential-holder may think they are being issued a credential representing a receipt that they helped fund an artist's cool art project. At type of issuance, the credential may render to show off the cool art project. Later, the controller of the host serving one of the links might change what the link refers to and replace the artist's visual art with another less popular work of art. For more elaboration on attacks like this, [read moxie.org](https://moxie.org/2022/01/07/web3-first-impressions.html).  

This can be mitigated by including a cryptographic hash of the referent of the link along with the link. Then, the result of dereferencing the link can be hashed, and a consumer can assert that the two hashes match. This technique is coloquially known as 'hashlinking' for 'data integrity', and can be implemented using [Cryptographic Hyperlinks](https://datatracker.ietf.org/doc/html/draft-sporny-hashlink-05), [Data Integrity 1.0](https://www.w3.org/community/reports/credentials/CG-FINAL-data-integrity-20220722/), [magnet://](https://en.wikipedia.org/wiki/Magnet_URI_scheme) or [ipfs://](https://www.iana.org/assignments/uri-schemes/prov/ipfs) URIs, [IPLD Links](https://ipld.io/docs/schemas/features/links/), or any of several other similar techniques. Developers building web pages that render linked data SHOULD use [subresource integrity](https://www.w3.org/TR/SRI/) when possible to instruct the user-agent to verify integrity.  

The digestMultibase property in the SVGRenderingTemplate render type exemplified in this document is meant to provide a hash that can be used to verify data integrity.  

### Link Dereferencing Traffic Analysis  

Many linked identifiers, especially identifiers using DNS or TCP/IP, can only be dereferenced by systems controlled by the identifier host. In these situations, the system that serves the identifier's referent may be able to infer unexpected information about the holder (et al) by performing [traffic analysis](https://en.wikipedia.org/wiki/Traffic_analysis) on data collected about how and when the links are fetched. A purported benefit of VCs in some use case is a lessened risk of surveillance by a credential isser, so while this traffic analysis security consideration applies anywhere links are used, it may particularly unexpected in VC use cases.  

The hashlinking technique mentioned in the "Link Integrity" consideration does \*not\* mitigate the traffic analysis consideration.  

Avoiding traffic analysis entirely is always a challenge on the internet. Risk can be mitigated by properly using a [mixnet](https://en.wikipedia.org/wiki/Mix_network), or by using a data storage system with 'private reads' e.g. using techniques like [PIR](https://en.wikipedia.org/wiki/Private_information_retrieval), [ORAM](https://en.wikipedia.org/wiki/Oblivious_RAM), [PSA](https://en.wikipedia.org/wiki/Private_set_intersection), or other ways of obscuring the traffic.  

### Embedded Media Denial of Service  

If a VC or Renderer embeds rendered media (or templates of media) directly in its serialization (e.g. via a \`data:\` URI), the media might be quite large in byte size, e.g. a high-resolution image from popular phones can now be 50 MB, and videos can be orders of magnitude bigger. These large VCs or other linked data objects could be intentionally or unintentionally result in a [denial of service attack](https://www.cisa.gov/uscert/ncas/tips/ST04-015) against a system.  

To mitigate this, system should avoid loading entire VCs into memory all at once, and instead prefer streaming algorithms or other techniques whose memory cost scales sublinearly with the size of the VC.  

### Sandboxing  

Often times the renderer and its configuration will not be authored by the issuer, holder, verifier, or even the developer of applications facilitating these roles. Depending on how the renderer works, this means rendering may involve executing untrusted code or executing trusted code with untrusted inputs. Mitigate against the risks of this by using any sandboxing mechanisms available (e.g. iframes, Content-Security-Policy, Subresource Integrity, WebAssembly modules) to constraint the capabilities of untrusted code. Sandbox walls are frequently escapable, so also practice [layered defense](https://www.ibm.com/docs/en/i/7.3?topic=security-layered-defense-approach) by using other techniques too.  

### Injection Attacks  

When rendering templates using untrusted inputs, be careful to mitigate against [code injection](https://en.wikipedia.org/wiki/Code_injection) by validating all inputs use proper syntax and using [encoding and escaping](https://owasp.org/www-project-proactive-controls/v3/en/c4-encode-escape-data) where possible.  

To illustrate the potential for these kind of attacks, please consider the SVGRenderingTemplate type defined in this document. If the template was like \`<svg><text>{{$.credentialSubject.degree.name}}</text></svg>\`, an attacker could contrive an example with name like \`</svg><script>globalThis.pwn()</script><svg>\`. If the implementation's template engine didn't apply proper svg-escaping or html-escaping, this could be used in various [cross-site-scripting (XSS)](https://owasp.org/www-community/attacks/xss/) attacks  

## Implementations / Demos

*   [https://celehner.com/2022/09/vc-render/](https://celehner.com/2022/09/vc-render/)
    *   [https://envs.sh/ZR](https://envs.sh/ZR) SVG
    *   [https://envs.sh/Z1](https://envs.sh/Z1) HTML
*   [https://celehner.com/2022/09/vc-render/1/](https://celehner.com/2022/09/vc-render/1/)
    *   [https://envs.sh/Z4](https://envs.sh/Z4) HTML with render object

## Next Steps  

*   Propose handling templates (vs pre-rendered)
*   Propose work item to CCG / VCWG? (propose properties be added to VC @context)
*   The authors of this paper have very minimal accessibility training and requires expert assistance in order to ensure that the proper considerations are made for a braille-based rendering mechanism for Verifiable Credentials.  
    

### References  

*   Handlebars
*   Json Path  
    
*   [https://identity.foundation/wallet-rendering/](https://identity.foundation/wallet-rendering/)  
    
*   [https://medium.com/mattr-global/rendering-credentials-in-a-human-friendly-way-e47f4a32fd4b](https://medium.com/mattr-global/rendering-credentials-in-a-human-friendly-way-e47f4a32fd4b)  
    
*   [https://gitlab.grnet.gr/essif-lab/infrastructure\_2/gataca/Verifier\_Universal\_Interface](https://gitlab.grnet.gr/essif-lab/infrastructure_2/gataca/Verifier_Universal_Interface)  
    
*   [https://identity.foundation/credential-manifest/](https://identity.foundation/credential-manifest/)  
    
*   [https://cryptpad.fr/code/#/2/code/edit/l8fIB1njuJzhI-Lr1Szaf0cz/](https://cryptpad.fr/code/#/2/code/edit/l8fIB1njuJzhI-Lr1Szaf0cz/) (markdown...)  
    
*   [https://github.com/THCLab/oca-ecosystem/issues/10](https://github.com/THCLab/oca-ecosystem/issues/10) OCA Presentation Layer  
    
*   [https://docs.google.com/document/d/17n8hfdPfqfpbPj4ss-ep4nCkpp9ZBoy6U2Q1t7j-knI/edit](https://docs.google.com/document/d/17n8hfdPfqfpbPj4ss-ep4nCkpp9ZBoy6U2Q1t7j-knI/edit) LDUX  
    
*   [https://www.w3.org/Submission/2014/SUBM-osapi-20140314/#rfc.section.C.15.5](https://www.w3.org/Submission/2014/SUBM-osapi-20140314/#rfc.section.C.15.5)  
    

# [](https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/advance-readings/rendering-verifiable-credentials.md#the-render-property)

# [](https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/advance-readings/rendering-verifiable-credentials.md#audio-rendering)

# [](https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/advance-readings/rendering-verifiable-credentials.md#physical-rendering)

# [](https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/advance-readings/rendering-verifiable-credentials.md#collaboration-at-and-beyond-rwot-11)

## Context

https://example.org/vc-rendering/v1.jsonld

{
  "@context": {
    "@protected": true,
    "vcr": "https://example.org/vc-rendering/#",
    "renderer": "vcr:renderer",
    "SvgRenderingTemplate2022": {
      "@type": "@id",
      "@id": "vcr:SvgRenderingTemplate2022"
    },
    "": {
    }
  }
}  
\--------  

# Collaboration at and Beyond RWoT 11

The author(s) of this paper seeks individuals that are interested in rendering Verifiable credentials in many forms. It would be good to explore more use cases such as the display of 1-D barcodes (PDF417 data), 2D barcodes (QR Codes), optically scanned data (MRZ), and other interaction patterns used by people that need to exchange credential information..  

The team that furthers this work will also need to coordinate with organizations such as the Web Accessibility Initiative (WAI) at the World Wide Web Consortium as well as other national and international bodies that focus on ensuring that people with accessibility needs are not excluded from using technologies such as Verifiable Credentials.  

# Appendicies  

## Example Test Fixtures  

The following are examples of objects using the rendering semantics described in this document. They are provided so that implementations can use the same test fixtures and reach a baseline of interoperability more efficiently.  

### Example Fixture 1: Renderable UniversityDegreeCredential  

{
  "@context": \[
    "https://www.w3.org/2018/credentials/v1",
    "https://www.w3.org/2018/credentials/examples/v1",  
    "https://example.org/vc-rendering/v1.jsonld"
  \],
  "id": "http://example.edu/credentials/3732",
  "type": \[
    "VerifiableCredential",
    "UniversityDegreeCredential"
  \],
  "issuer": "https://example.edu/issuers/565049",
  "issuanceDate": "2010-01-01T00:00:00Z",
  "credentialSubject": {
    "id": "did:example:ebfeb1f712ebc6f1c276e12ec21",
    "name": "Jane Smith",
    "degree": {
      "type": "BachelorDegree",
      "name": "Bachelor of Science and Arts",
      "institution": "Example University"
    }
  },
  "render": \[
    {
      "id": "https://svg.example/degree.svg",
      "type": "SvgRenderingTemplate2022",
      "digestMultibase": "zQmAPdhyxzznFCwYxAp2dRerWC85WTemp6wFl9G270iEu5h6JqW"
    }
  \],
  "proof": {}
}

### Example Fixture 2 - Minimal Renderable Credential  

`{     "@context": [       "https://www.w3.org/2018/credentials/v1"     ],     "id": "http://example.com/credentials/4643",     "type": ["VerifiableCredential"],     "issuer": "https://example.com/issuers/14",     "issuanceDate": "2018-02-24T05:28:04Z",     "credentialSubject": {       "id": "did:example:abcdef1234567",       "name": "Jane Doe"     },`  `"render": {       ...     }   }`  

Example Q  

{  
   "@context": \[  
    "https://www.w3.org/2018/credentials/v1",  
    "https://www.w3.org/2018/credentials/examples/v1"  
  \],  
  "id": "http://example.edu/credentials/3732",  
  "type": \["VerifiableCredential", "UniversityDegreeCredential"\],  
  "issuer": "https://example.edu/issuers/565049",  
  "issuanceDate": "2010-01-01T00:00:00Z",  
  "credentialSubject": {  
    "id": "did:example:ebfeb1f712ebc6f1c276e12ec21",  
    "name": "Jane Smith",  
    "degree": {  
      "type": "BachelorDegree",  
      "name": "Bachelor of Science and Arts",  
      "institution": "Example University"  
    }  
  },  
  "render": \[{  
    "type": "WebRenderingTemplate2022",  
    "contents": "<div style=\\"width:300px; height:100px; border: 2px solid black; text-align:center\\">\\n  <div>\\n    This {{credentialSubject.degree.name}} is conferred to\\n  </div>\\n  <strong style=\\"font-size: 16px\\">\\n    {{credentialSubject.name}}\\n  </strong>\\n  <div>\\n    by {{credentialSubject.degree.institution}}.\\n  </div>\\n</div>"  
  }\]  
}  

.
