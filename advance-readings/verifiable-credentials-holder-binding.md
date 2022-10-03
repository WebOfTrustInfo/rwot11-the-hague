# W3C Verifiable Credentials Holder Binding Specification

by [Oliver Terbu](mailto:oliver.terbu@spruceid.com) - Spruce, [Paul Bastian](mailto:paul.bastian@bdr.de) - Bundesdruckerei, [Snorre Lothar von Gohren Edwin](mailto:snorre@diwala.io) - Diwala, [Rieks Joosten](mailto:rieks.joosten@tno.nl) - TNO, [Antonio Antonino](mailto:antonio@kilt.io) - KILT Protocol, [Nikos Fotiou](mailto:fotiou@aueb.gr) - AUEB, [Zaïda Rivai](mailto:zaida.rivai@danubetech.com) - DanubeTech, [Stephen Curran](mailto:swcurran@cloudcompass.ca
) - Cloud Compass, [Ahamed Azeem](mailto:azeem.ahamed@danubetech.com) - Danube Tech

# Working notes
This will be removed when done
**Dont use authorization or delegation**

First things to do after RWoT

**Define more usecases:**
- [ ] Paul writes two cases online offline case
- [x] Antonio redefines his current use case (bank example -> flight booking + boarding, title to change to something like "Deferred verification process")

**Clean words an clarify termninology**
- [ ] Rieks goes around and chops and pushes for better definition

**Get a better working platform**
- [ ] Oliver moves our document to a better place to be able to collaborate more contextual.

**Editor management**
- [ ] We need someone who can summarize a bit where we are now, and clarify unclear parts so that we can discuss and find paths forward for the unclearity. --> Zaïda can do this



# Target Audience

- The W3C VC community, specifically those that take an interest in the VCDM/PresentationDM std (or perhaps: the group doing Presentation Exchange).
- Implementers of Verifialbe Credentials based Use Cases that need proof that the counterparty is the intended or rightful holder of the time of presentment of the credentials. 

# Message (Call to Action)

- Inform the audience about the problem we're trying to solve, define terminology, inventory solutions that might work (with or without VCs), and make the case for having some VC support for this. - The call to action is to have the VCDM community modify the standard to accommodate this.
- Another call to action is to inform the ToIP Architecture WGs about context/use-cases that are relevant to their work.

# Abstract

<!--Nikos, this RFC includes useful terminology
 https://www.rfc-editor.org/rfc/rfc7800.html
-->

The W3C Verifiable Credentials Data Model (VCDM) does not define how to bind a W3C Verifiable Presentation to the Subject of the verifiable credentials included in the presentation, so that the Verifier can ensure that the Holder of the presentation is the **designated**, **rightful** or **intended** holder of the verifiable credential. This includes the ability to validate that included and potentially multiple credentials in the presentation relate to the same Subject or the designated Holder of the Subject without the necessity to disclose or require unique identifiers for Holder and Subject. For the sake of this paper, this ability is called **Holder Binding**. This paper describes the context, use cases, limitations of and extensions to the existing VCDM as well as specific types of Holder Binding to faciliate interoperability across vendors and domains. The proposed solution acknowledges that types of Holder Binding can vary depending on usecase, domain and requirements which is the reason why the proposed solution includes a registry as an extension mechanism. 

<!-- Rieks note: there is a difference in the mental model of AnonCreds (that are issued to a M-Secret, which is important, the holder) and in VC there's the idea of claims (in a VC) and the holder isn't all that important (doesn't appesar in VC)

RJ2: We need some text about how holder binding for VCs would differ from that for AnonCreds (perhaps others - X.509 attribute certs)
 
Snow note: can't anon cred just be a type of binding? -->

# Introduction

The remainder of this paper is structured as follows:
- The problem to solve
- Context
- Use cases
- Proposal
- Conclusion and next steps

## The Problem to solve

The verifier may need assurances that the person (or organization - which we from henceforth refer to as a [party](https://essif-lab.github.io/framework/docs/essifLab-glossary#party)) <!-- (maybe entity? No, because anything that exists is an entity, so a stone or a cow are also entities; I would like to not include them here) --> on whose behalf a wallet(like) component has sent a presentation to the verifier, relates to a specific subject<!-- may talk aboUt wallets aswell here as our use case shows it-->  in one (or more) claims of the VCs in the presentation. The problem is that there currently is no well-defined method that the verifier can apply to obtain the assurances that it needs while leaving the (person or organization) in control for ???.

To achieve this, we want to have a data model to represent a way how to ... should consider the following:
- binding should link to a specific credential subject to support VCs that have multiple credential subjects
- verify that the holder relates to a credential subject (intended holder)
- verify that the presenter was involved in the issuance process
- verify that the holder is authorized(rightful presenter) to present the credential
- support binding to identifier-based and non-identifier-based credential subjects.
- support cases where binding is included in the VC directly (bbs+, anoncreds?) but VC presented as a VP.
- support cases where credential subjects have identifiers that are not based on DIDs (e.g., https://domain.com)
- support for cryptographic linking of verifiable credentials if verifier has that requirement
- ...

Notes from bottom
- verify that the holder relates to the credential subject (intended holder) or was involved in the issuance process
- verify that the holder is authorized to present the credential
- ...

TBD: A method to validate that the intended Holder presented a set of VCs wrapped in a VP.

It binds the following together:


Subject of the VC (even if vc.credentialSubject.id is undefined)
Claims made about the Subject by the Issuer
Holder of the VC (even if vp.holder.id is undefined)
Proof in the VP
Proof in the VC

Verifying a verifiable presentation does not include verifying the binding between the verifiable credential subject and the verifiable presentation holder. There is no normative reference for any existing approach.

For these reasons, this paper describes a mechanism and a data model that allows Holders and/or Issuers to indicate how the Holder Binding can be verified at the time of presentment. Binding multiple Verifiable Credentials to a Holder should be possible. The W3C Verifiable Credentials Data Model 1.1 specification which is essentially equivalent to no guidance on the Holder Binding is provided. This mechanism is fully backward compatible with existing verifiable credentials and verifiable presentations. This paper does not mandate a specific form of holder binding or W3C Verifiable Credential proof type or format. Instead it provides a framework for Issuers, Holders and Verifiers to provide guidance on how Holder Binding can be checked deterministically according to their intentions.

## Context 

<!-- @Rieks, @Zaida: what does it mean for Parties if holderbinding stuff gets included in VCs and VPs, and in the VPs only! -->

All SSI technologies exist to support individuals and organizations (which we will collectively refer to as [parties](https://essif-lab.github.io/framework/docs/essifLab-glossary#party)) as they need exchange [information](https://essif-lab.github.io/framework/docs/essifLab-glossary#information) which takes the form of digital components that act in their behalf exchanging [data](https://essif-lab.github.io/framework/docs/essifLab-glossary#data).

So, every [party](https://essif-lab.github.io/framework/docs/essifLab-glossary#party) will need to control a set of digital components, such as mobile phones, apps in the cloud, etc. that provide functionalities that have a role in such data exchange. Within SSI, we are familiar with functionalities that we call:
- issuing: i.e. receive a request for the issuing of a VC, decide whether to accept or reject that request, and if accepted: take the data so as to construct the requested (kind of) VC, add metadatsign it on behalf of the party on whose behalf they act (their [principal](https://essif-lab.github.io/framework/docs/essifLab-glossary#principal))and send it to the requester in response to its request.
- holding: i.e.:
    1. send requests for obtaining credentials (to digital components of other parties that have issuing functionality), get  the credentials out of the response, and store them in a EDV-component
    2. receive presentation requests, decide whether or not to accept the request, then send requests for appropriate VCs to the EDV, and construct a presentation from these VCs, addding metadata and a signature on behalf of its [principal](https://essif-lab.github.io/framework/docs/essifLab-glossary#principal), and send it to the requester.
    3. securely storing VCs on behalf of its principal, and providing access to these VCs according to an access policy of its principal (which we assume here wouuld allow any wallet component to read/write VCs)
- verifying: i.e. create presentation requests (which include requests for specific (claims from) VCs that are issued on behalf of possibly multiple parties), sending such requests to wallet components, receiving responses and testing/verifying the various proofs to ensure the contents hasn't been tampered with and the credentials/claims provably originate from designated parties.

We use the following terms to refer to digital components that have at least the following functionality:
- EDV: holder functionality #3 (storing VCs)
- Issuer component: issuing functionality
- Wallet: holder functionalties #1 and #2
- Verifier component: verifiying functionality

Parties typically have digital components that together provide all of the issuing, holding and verifiying functionalities, i.e. wallets, issuer- and verifier components and EDVs. When we say that a party issues a VC, this means that an issuer-component of that party is doing the actual work related to that issuing.

It is up to the parties (and NOT: the digital components) to decide which (kinds of) VCs to issue, determine the keys that are to be used, as well as what (kinds of) VCs to request (and from whom), etc. In order for the appropriate digital component to operate as intended by its principal, it will need some kind of [policy](https://essif-lab.github.io/framework/docs/essifLab-glossary#policy) that it can use such that it would actually act in accordance with its principals intentions. The creation and maintenance of such policies is part of the party's [governance](https://essif-lab.github.io/framework/docs/essifLab-glossary#governance) and out of scope of this paper.

Note: when we say that a party does something, this should be understood to mean that the party has/controls a component that does the operational work involved. So, when we say that a party has issued a credential to another party, this should be understood to mean that there is an issuing component that has construted this credential on behalf of the first party, and sent it to a wallet component that requested it, received it and stored it on behalf of the second party. Phrases such as "Party Z has requested a presentation", "Alice has created a presention", etc., should also be understood to mean that the party has/controls a component that has the appropriate functionality for the task, and also has a [policy](https://essif-lab.github.io/framework/docs/essifLab-glossary#policy) (authored by that party) that guides the details of how the actual work needs to be done. 

In order for parties to realize some objective of theirs, they may need data and process that to obtain results that constitute the realization thereof. This data must be valid to be (further) processed in order for the result to be valid (useful). In order to be able to construct policies that verifier components need (to construct presentation requests), a party must know which other parties offer to issue credentials that contain such data, and also they must be able to decide (based on the details of the offering), whether or not the data will be valid for the purpose it would be requested. 

This means that parties that offer to issue credentials, need to 'advertise' their offering, and make sure such 'advertisements' refer to any assurances that the party can provide and a party that looks for it can use to decide whether or not the offering can be used (would result in valid data to be obtaind.)

Such assurances could, e.g. be a statement saying how the data that is in a VC has been obtained (e.g. personal data comes from a KYC process, a diagnosis has been made by a official doctor). In this paper we focus on a specific assurance that can be provided, and that consists of the ability for verification components to check wether a presentation that it receives has been created by the component and/or on behalf of the party to which one or more of the VCs have been issued.

Since it is the party on whose behalf the verification component will be making such checks will suffer any adverse consequences (risks), it is the duty of that party to ensure the verification policy is constructed such that the verification component makes the intended checks.

### Definitions/glossary  

Holder Binding is providing the verifier the means to verify that the presentation was done by the credential subject or the holder designated by the credential subject. this may or may not include authentication. 

### Implications

<!-- what does it mean for Parties if holderbinding stuff gets included in VCs and VPs, and in the VPs only! 
* difference in semantics -->

TBD 

### On-site and remote holder binding

There is a variety of use cases that include different types of holder binding and can usually be distinuished into two categories, "on-site" and "remote" as the location of the verifier has a significant influence on the trust relationship between the holder and the verifier. In the "on-site" case, holder binding works like identification processes equivalent to classical, analog ID documents: The verifier requests a credential and the holder transmits a verifiable presentation of his VC. The communication channel here can take place "offline" via connections such as NFC, Bluetooth or Wifi, or "online" if both the wallet of the holder and the verifier are connected to the Internet. If there is visual contact, the verifier can perform a simple identification of the holder using biometric data verified by the issuer and stored as claims in the VC. The transmission of biometric data is always critical from a privacy point of view and should be avoided if possible. However, direct physical contact allows the holder to easily authenticate the verifier so that he can better assess the implications of his data being released. Holder binding (e.g. with biometric identification) in the remote use case introduces significant technical complexity and privacy risks. A wallet must authenticate the holder itself or leave it to a trusted verifier, depending on the use case. At the same time, it must enable unique identification of the communication partner so that it provides the holder with the tools for a self-sovereign decision.

### holder binding with multiple VCs
linking credentials with
 - holder DIDs
 - link secrets
 - matching attributes/claims
to leverage  holder binding 

tbd Paul

## Use Cases

This section will contextualize the problem with usecases that has come from the community.

### Multiple wallets and issuers

![](https://i.imgur.com/d1TvdNW.png)
Source: https://drive.google.com/drive/folders/1L9oW1QP1fi3iOoiANoWFly0eYscrVFHN

***Note: the texts in the figure needs to be aligend with that below. The text below is authoritative in this respect.***

The figure above illustrates this use-case, where a person (Alice) has multiple 
wallets WX, WY and WZ (e.g. an app on her mobile phone, one in the cloud via a web app, and one as a browserplugin). Alice has an Encrypted Data Vault (EDV) that holds the credentials that her wallets obtain, and can provide them to any of her wallets as they need them to construct a presentation.

The figure also shows two [parties](https://essif-lab.github.io/framework/docs/essifLab-glossary#party), Party X and Party Y, that have electronic components for issuing credentials on their behalf to wallets that work on behalf of other parties, such as Alice.

Wallets WX and WY have requested a VC from party X and Party Y respectively, obtained such credentials (let's call them CredX and CredY respectively), and stored them in Alice's EDV.

The figure shows another party (Party Z), whose verifying component has sent a request to WZ to return a presentation that contains the two credentials that WX and WY obtained and stored in Alice's EDV. So, WZ will access Alice's EDV, get both credentials, turn them into a presentation that it then sends it in response to the request.

The current VCDM does not provide party Z with a mechanism that enables it to know to which party a VC has been issued, nor to which component it has been issued (where AnonCreds have the implicit property that everything that is sent from a wallet to a verifying component is guaranteed to have been issued to that same wallet). While there are many use-cases in which this is of no importance, there are also situations where it *does* matter.

Here are some examples:
<!-- Perhaps we could just do a one/two-line summary of each, and refer to another section of the paper where they are elaborated -->
1. [***summary of use-case xxx to be written***]. In this case, party Z would want to be sure that CredX has been issued to the same party as CredY.
2. [***summary of use-case yyy to be written***]. In this case, party Z would want to be sure that CredX has been issued to the same wallet as CredY.
3. [***summary of use-case zzz to be written***]. In this case, party Z would want to be sure that CredX has been issued to the party on whose behalf the presentation was constructed.
4. [***summary of use-case ...(etc.) to be written***]. In this case, party Z would want to be sure that ....

We propose to (optionally) add two properties to a VC, and another two (optional) properties to a VP, with the following semantics:
- the property: `holderComponent` specifies the component to which the VC/VP has been issued, by providing a number of mechanisms that a verifier can use to identify and authenticate the component to which the VC was issued, c.q. that created the VP;
- the property:`holder` specifies the [party](https://essif-lab.github.io/framework/docs/essifLab-glossary#party) - NOT: the component - on whose behalf the `holderComponent` to which the VC was issued, c.q. that created the VP, by providing a number of mechanisms that a verifier can use to identify and authenticate that party;

In this use-case, we see that wallet WX has received a VC that was issued by an issuer component that acted on behalf of party X. The `holderComponent` property provides a means for verifier components to identify (and authenticate if needed) wallet `WX` as the wallet to which the VC was issued. The `holder` property provides a means for verifier components to identify (and authenticate if needed) Alice as the party on whose behalf wallet `WX` requested and received the VC. We might phrase this in a more human-friendly way by saying that the `holderComponent` property says the VC was issued to WX, and the `holder` property says the VC was issued to (party) Alice. However, care should be taken that we do not lose the actual semantics when using such human-friendly phrases.

Similarly, a second VC was issued on behalf of party Y, of which the `holderComponent` property says it was issued to wallet `WY` and `holder` says this wallet acted on behalf of Alice.

When parties that issue VCs c.q. construct VPs were to include these properties in their VCs/VPs, this would enable parties that verify VPs such as those mentioned in the examples above, to obtain the assurances they need for the purpose they have requested the VP.

Note that parties that add these properties, do this as a service to verifying parties, not to serve (or create) some legal obligation. Issuing parties would mention this in the advertisement (as expalined in the introduction)A party would add these properties to a VC, and advertise this,


#### What
In this scenario we want to make sure that the verifier can trust that the credentials presented to them is provided to the rightful controller, Alice, even if the holder-component(wallet) is different. Also potentially any identifier provided in the issuance exchange.

The proposal provided in this document, can make this feasable with a specific holder-binding type, defined for a scenario like this. Meaning this mechanism does not hinder any specific use cases.



### Deferred Verification

Alex works at Anon Corp. in Amsterdam and needs to fly for business to Milan.
In order for the HR department to book a ticket for her, the airline company requires Alex's proof of vaccination against Covid-19 issued by one of the trusted European government health agencies.

Alex's proof of vaccination contains Alex's name and surname, birthdate, vaccine brand, number of vaccinations (i.e., one, two, three, four) and a unique identifier and has been issued to her by the Dutch National Institute for Public Health and the Environment (RIVM).

To avoid unnecessary correlation, Alex removes the unique identifier from her certificate, which the verifier does not require on the website, and sends over to the HR department only the claims that are relevant for the booking to continue, in a way that still provides the verifier guarantees about the authenticity of those claims and the issuer of the certificate.
The HR department then fills in the information required to continue with the booking of the flight ticket, which is then sent to Alex.
The flight ticket is also modeled as a Verifiable Credential, and contains Alex's name, surname and birthdate *as specified on the provided Covid-19 certificate*, seat reserved, flight number, date and time.

A reasonable solution would allow Alex and nobody else to prove, at boarding time, the relation between Alex’s person and the claims in the flight ticket, without necessarily revealing more information than required for the airline company to let Alex on the plane.
Hence, at boarding time, Alex presents to the gate steward her picture, name, surname, and birthdate from her digital ID document.
The only digital ID document that can be considered valid by the gate steward is the one with a profile picture that matches Alex's face, along with a matching name, surname, and birthdate as on the flight ticket.
Because the booking system made sure that the name, surname and birthday on the ticket match those in the Covid-19 certificate provided at booking time, there is no need for Alex to present again her vaccination certificate, as a valid ticket already implies a valid vaccination certificate for a person with the specified name, surname, and birthdate.

A valid presentation allows Alex to prove she is the rightful owner of the flight ticket and board on the plane.

### Verifiable credentials for objects

A VC can be used for asserting claims about an object, e.g., VCs for food and raw materials are used for enhancing [supply chain security](https://www.ledgerinsights.com/homeland-security-dhs-blockchain-credentials-imports-transmute/), or even as enabler of [circular economy](https://epub.wupperinst.org/frontdoor/index/index/docId/7940). However, such objects not only lack the computational capabilities required for generating a Verifiable Proof, but they also have multiple owners during their lifetime.

Let's consider for example the case of a VC used in each package of coffee "Espresso Italiano". This VC  includes information related to the coffee type, country of origin, production and expiration date. That VC is issued by the packaging factory "Best Coffee" and it is printed in the corresponsing packaging itself using a QRcode.

Alex, a lorry driver, transfers from "Best Coffee" factory a pallet that includes 1000 packages of "Espresso Italiano", therefore Alex becomes the holder of the corresponding VCs. Alex delivers the pallet to super maket "Billy's market". At the same time, Alex "presents" the credentials to the stock manager system of "Billy's market" 

"Billy's market" stock management system must be sure that Alex was authorized to present these credential. Furthermore, the stock manager system now becomes the holder of the credentials.

- Supply chain where VC subject is an object where this object cannot create VPs or proofs, so it is up to the current holder to generate the VP.

  Example:
  
```json
  {
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://w3id.org/traceability/v1"
  ],
  "id": "urn:uuid:326c74c8-f4d7-4c1b-b158-2683deb8768e",
  "type": [
    "VerifiableCredential",
    "CertificationOfOrigin"
  ],
  "name": "Certificate of Origin",
  "issuanceDate": "2019-12-11T03:50:55Z",
  "issuer": {
    "type": [
      "Organization"
    ],
    "id": "did:key:z6MktHQo3fRRohk44dsbE76CuiTpBmyMWq2VVjvV6aBSeE3U",
    "name": "North Italy Chamber of Commerce"
  },
  "credentialSubject": {
    "items": [
      {
        "type": [
          "TradeLineItem"
        ],
        "name": "Espresso Italiano",
        "description": "Premium Prosumer Espresso Makers - Model Dolce",
        "product": {
          "type": "Product",
          "commodity": {
            "type": [
              "Commodity"
            ],
            "commodityCode": "851671",
            "commodityCodeType": "HS"
          }
        }
      }
    ]
  },
  "manufacturingCountry": "IT",
  "dateOfExport": "2022-02-02T09:30:00Z",
  "proof": {
    "type": "Ed25519Signature2018",
    "created": "2022-09-13T20:06:59Z",
    "verificationMethod": "did:key:z6MktHQo3fRRohk44dsbE76CuiTpBmyMWq2VVjvV6aBSeE3U#z6MktHQo3fRRohk44dsbE76CuiTpBmyMWq2VVjvV6aBSeE3U",
    "proofPurpose": "assertionMethod",
    "jws": "eyJhbGciOiJFZERTQSIsImI2NCI6ZmFsc2UsImNyaXQiOlsiYjY0Il19..cBX-PaBA-I3GJgnF829iuKFXGdQAruXIT3YvQJsOVDUF0Mr4vxWRy2iuC6vKpnCbgOhh9woiL9nMD7AIUjXWAQ"
  }
}
```

### Parents-Child Relationship

:::warning
TBD: perhaps dog and dog holder is a better example?
:::

Notes from bottom: Parent that want to enroll child into primary school, then little child is not gonna present VC stating claims about them, but the parents can do. So, we would need to establish the link of the VC of the child and the parent presenting it. which is another kind of relationship similar to the supply chain case. not the same but similar. we are looking for presentation to encode that. 

### more ...

:::warning
TBD: add more examples
:::

## Proposal

Because there are many different options, a Verifier usually needs to guess the intended method for Holder Binding which is an issue for interoperability. Having the Verifier to have this knowledge pre-populated would prevent interoperability as well. Guessing the method is prone to side effects which might compromise security.

To acknowledge the diversity of the different options, this proposal assumes there For these reasons, this specification introduces a new property that allows a Verifier to determine the intended Holder Binding between the VP and the presented VCs based on a new property which removes the necessasity of guessing the Holder Binding method. Since different options are possible, this specification also introduces an extension mechanism. Uniquly identifying the type of Holder Binding will also allow Verifiers to give Holders guidance on what types of Holder Bindings the Verifier can support.

This proposal defines the a `holderBinding` property for the determination of the Holder Binding method between the VP and included VCs to allow verification of the intended/rightful/designated Holder of the VCs at the time of presentment. The `holderBinding` MAY be included in VCs and/or in VPs. If the `holderBinding` property is included in one VC and in the VP, verifiers MUST ensure the `holderBinding` in the VP is allowed by the `holderBinding` type of the VC.

**holderBinding**
If present in the VP or VC, the value of the `holderBinding` property MUST include the following:
- `type` property, which expresses the Holder Binding method type. It is expected that the value will provide enough information to determine the Holder Binding method between the VP and included VCs.
- TBD: (OPTIONAL) linked VCs, index/id?

:::warning
**TBD:** we might put the a `binding` property into the `holder` property and redefine `holder` as URI or object where the object MAY have an `id` and MUST have a `binding` property which is an object or an array of objects where each has a `type`.
::: 

The precise contents of the Holder Binding information is determined by the specific `holderBinding` type definition, and varies depending on the Holder Binding method. The Holder Binding information MAY also include information about for which VC in the VP the Holder Binding applies. For example, this can be done by including a reference of the VC such as the `id` of the VC.

Each Holder Binding method MUST define how Holder Binding for an input VP and one or more input VCs contained in the VP can be deterministically verified. For example, a simple Holder Binding method might define that for a given input VP Holder Binding could be verified based on checking that the holder property matches the `credentialSubject.id` property in every `verifiableCredential` object in the VP.

Each Holder Binding method MUST define how Holder Binding for an input VP and one or more input VCs contained in the VP can be deterministically verified. For example, a simple Holder Binding method might define that for a given input VP Holder Binding could be verified based on checking that the holder property matches the `credentialSubject.id` property in every `verifiableCredential` object in the VP.

### Relationship to existing VC Data Model

:::warning
TBD: why proof property in VP is not sufficient. to enable reusage of existing data integrity proof types for holder binding without changing data integrity proof suites or JWT algorithms etc., and seggregation of semantic concerns, e.g., data integrity vs ...
:::

:::warning
TBD: relationship between embedded/external proof, VC, VP, Subject and Holder. Subject with/without an identifier, holder with/without an identifier.
:::

:::warning
TBD: some diagram that shows some graph between VC, VP, etc.
:::

:::warning
TBD: verifiers will get the ability to map holder binding types to policies, e.g., authentictation assurance levels (NIST, ISO, eIDAS etc.), and ask for specific types in VC/VP requests.
:::

### Implementer Considerations

Typically, implementers use 

```
vp.verify(...)
```

Holder binding validation is typically implemented on top.

We wanna enable that implementers can use something like

```
registerBinding(type1, type2, type3)
vp.verifyBinding(...)
```

### Examples

#### Subject-Holder Correlation Binding
:::warning
TBD: description (oliver)

simplest binding where holder.id == vc.credentialSubject.id and isValid(vp.proof) and isAuthMethod(vp.proof.verificationMethod, holder.id)
:::

:::warning
TBD: data model (oliver)
:::

#### Relationship Credentials Binding

:::warning
TBD: description (snorre)

included VCs have different credential subject identifiers but binding is established through verification of proof/signature of the VP, correlating the VP.proof.verificationMethod with the identifiers in the vc[].credentialSubject and correlating specific relationship VCs between the identifiers (could assume a dedicated `type` in the `types` array in the VP credentials array)
:::

:::warning
TBD: data model
:::

#### Out-of-band Binding

:::warning
TBD: description (mohammed)
type: binding is done based on matching claims in VC against some out of band document, e.g, passport.

e.g., credentialSubject.firstName/lastName/... equals claims in a passport.
:::

:::warning
TBD: data model (mohammed)
:::

#### DID-based Binding

:::warning
TBD: description (mohammed)

e.g., verification of the VP proof and checking whether the resolved DID of the verificationMethod has alsoKnownAs which equals the identifiers in the credentialSubject or vice versa.
:::
The ```alsoKnownAs``` is an attestation property defined in the DID document, which refers to other DIDs controlled by the DID subject.
```jsonld=
{
  "@context": ["https://www.w3.org/ns/did/v1"],
  "id": "did:example:123",
  "alsoKnownAs": "did:key:123"
  ...
}
```

The VC is issued to one of the DID controlled by the subject of the verifiable credential. The presentation proof is derived from another DID controlled by the subject. Hence, the binding can be verified using the ```alsoKnownAs``` property from the DID document of the verifiable presentation holder or verifiable credential subject.

```jsonld=

"vp": {
    "holder":"did:example:123"
    "vc" :{
      "issuer": "did:example:789",
      "credentialSubject":{
            "id":"did:key:123"
        }
    }
    "proof": [{...}]
}

```


### Bearer Credential

:::warning
TBD: description (mohammed)
type: binding is done based on purelely possessing the VC
:::

:::warning
TBD: data model
:::

### Delegation-based Binding

:::warning
TBD: description (oliver)
:::

:::warning
TBD: data model (oliver)
:::

### AnonCreds

This mechanism might be able to be used in the following way for AnonCreds.

In each VC, the issuer would include the signed, blinded link secret as in the "holderBinding" item.

vc (issuer -> holder):

``` json
{   
     "issuer": "...",
     "issuanceDate": "...",
     "holderBinding": {
       "type": "AnonCredsLinkSecret2022",
       "blinded_link_secret": "...", 
     },
     "proof": { ... }
}
```

In each VP, the holder would provide proof that they possess the link secret that was used to generate the issued blinded link secret in each included verifiable credential. This would also prove that the same link secret was used for each of the included VCs.




## Data Models

```

vc (issuer -> holder):
{   
     "id": "urn:uuid:22342323424",
     "issuer": "...",
     "issuanceDate": "...",

     "holderBinding": {
       "type": "...",
       "abc": "..."     
     },
     "proof": {
     
     }
}
   
derived vc (holder -> holder):
{   
     "id": "urn:uuid:3r43343443",
     "issuer": "...",
     "issuanceDate": "...",

     "holderBinding": {
       "type": "...",
       "abc": "..."     
     },
     "proof": {
     
     }
}

vp:
{
   "holder": {
      "binding": [{
         "type": "LinkedSecretBinding2022",
         "whatever": "...",
         "linkedVCs": [

         ],
         "other": {
         
         },
         "proof": {
         
         }
      }]
   },
   "verifiableCredential": [{   
     "id": "urn:uuid:22342323424",
     "issuer": "...",
     "issuanceDate": "...",
     "type": [ "VerifiableCredential", "MoreSpecificType", ...]

     "holderBinding": {
       "type": "...",
       "abc": "..."     
     },
     "proof": {
     
     }
   }],
   "proof": [{
      "verificationMethod": "did:key:1234#key-1",
      "type": "Ed25519Signature2018",
      "jws": "...", ...
   }]
}
```
# Future work
Delegation

# Appendix

### Whiteboard statement

Holder shall prove control of VC/claims/subject identifier, verifiers should be **guided** to how and what risks...

NOTE: should we also mention issues in this formulation?



## Terminology

### Holder
TBD:


### Holder Binding


### Requirements

TBD: 

- ...
- giving the holder the means to present the credentials in a certain way.
- giving the issuer the means to restrict how the verfiiable credential can be used, e.g., just with registered readers. 

### Credential Binding?
TBD: perhaps not needed

### Credential Linking?
TBD: distinction between binding and linking


## Credential Format Considerations

### Data Integrity Proofs

### VC-JWT

### AnonCreds

AnonCreds differs from the W3C VC Data Model in the following three important ways in relation to holder binding. In AnonCreds:

- there is no concept of a "subject",
- there is a very specific meaning to the term "holder", and
- there is no concept of a verifiable credential being transferred amongst holders.

An AnonCreds credential is issued to a specific holder, and consists of a simple list of name/value pairs with no constraints on the names or values (hence no required "subject" or even "issue_date"). The holder-binding is accomplished by the automatic, required addition of an extra attribute (called "master_secret") added to each credential. The extra attribute provides a specific cryptographic binding between the holder and the credential.

The result of the enforced holder binding alters how an AnonCreds presentation is interpreted by the verifier. In addition to knowing who issued the source credential(s) and that the claims were not tampered with, the verifier can also assume that a verified presentation was generated from verifiable credentials specifically issued to the holder. No one else can present the claims.

This difference from the W3C VC Data Model makes the need for holder binding fundamental to the AnonCreds approach. In generating a presentation, the holder must demonstrate to the verifier that the credential was issued to them, and built into AnonCreds is a very specific way to do that.

#### AnonCreds Holder Binding Process

The following is a summary of the AnonCreds holder binding process.

- During setup/initialization, the holder creates a "link secret", a UUID that is managed as a secret.
  - The same link secret is used for all credentials that the holder wants to prove in a single verifiable presentation. In the common case, that means the holder has only a single link secret.
- During the issuance process, the holder provides the issuer with a blinded link secret generated using the link secret.
- The issuer puts the blinded link secret into the extra signed attribute ("master_secret") in the verifiable credential.
- When generating a verifiable presentation, the holder uses claims from one or more verifiable credentials that were issued with the same link secret, and generates a ZKP that proves the holder possesses the link secret that produced the blinded link secret without sharing the link secret itself.

The cryptographic process that is used is a [Pederson Commitment](https://crypto.stackexchange.com/questions/64437/what-is-a-pedersen-commitment).

#### AnonCreds Holder Binding in the W3C VC / VP Data Model

It should be possible in the VC Data Model / VP to include some sort of "holder binding" item with a type of related data, much like the "CredentialStatus" field. In the VC, the AnonCreds link secret could be a supported type, with the blinded link secret data value embedded in the structure. In the VP, a supported type can again be AnonCreds link secret, with the related data being the ZKP proof of being able to unblind the link secret. A cavaet on where the data would go is whether or not the link secret ZKP proof can standalone or must be integrated with the overall proof of the verifiable presentation.

It is not clear what the `subjectId` in an AnonCreds verifiable credential/verifiable presentation provided using the W3C VC Data Model would. It would make some sense that it be related to the "link secret", but as noted, that is more about the **holder** than the subject. Since an important goal of AnonCreds is to NOT provide a correlatable ID for the holder, anything used as the `subjectId` cannot be a correltable identifier.

### BBS+

TBD

## Considerations

- multiple wallet types (as must be expected under eIDAS 2)
- 