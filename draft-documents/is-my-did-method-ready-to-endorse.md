Is This DID Method Ready to be Endorsed?  Useful Rubric Criteria / (RWOT11 phase: drafting)
=================================================

Purpose: To enable the implementors or standards bodies to focus on choosing the applicable DID Method (or discount the ones unapplicable).

Audience: Our audience is all of:
  - product owners defining requirements;
  - implementors gauging feasibility of delivery; and
  - standards bodies considering suitability to their mission, interoperability of independent implementations, and long-term maintenance.

Keywords: DID Methods; Rubric for DID Method choice

How do we educate someone tasked with implementing a DID Method in an application? 

  Deciding to implement or support a DID Method for a given application requires an evaluation of whether the DID Method reaches the level of a proper standard with support for the relevant features. 

  The existing Rubric provides a number of criteria and metrics, however they cover a broad set of interests oriented towards a user of a DID Method. All stakeholders first have a narrower question of whether a DID Method is sufficiently well standardized along various axes.
  
Additionally, certain kinds of DID methods are simply unsuitable for particular applications and usage patterns, whether it be because of regulations or technological requirements/restrictions. Non-domain-expert stakeholders of every kind would benefit from a simplified set of considerations and guidelines when choosing a set of DID Methods to support.
  
We expect the standardization question to focus on several categories of questions:
* What is the complete description allowing the interoperability of bytes on the wire between two independent implementations (when following the text of the specification);
* Are the cryptographic verification mechanisms supported by the DID method are compliant with certain regulations or requirements;
* What usage is "important" based on guidelines such as:
  * Existing key material usage;
  * Enabling applications; and
  * Users expressing their value; and
* Do the adoption and scaling characteristics fit with the implementor's or standardization body's expected target audience?

Authors: Charles Cunningham, Diogo Chaves Franco, Ryan Grant.


---


# Q&A / What's the Newness Offered?

The existing DID Method Rubric "presents a set of criteria which an Evaluator can apply to any DID Method based on the use cases most relevant to them". Many of these criteria are focused on decentralization.  However, for purposes of measuring standardization, decentralization does not help or hurt.

In this paper, we aim to select some of the criteria of the Rubric that do matter for standardization, and add some new relevant questions, resulting in a set of decision-making guidelines aimed at implementors whose task is not necessarily perfectly aligned with the themes covered in the existing Rubric. 

Existing educational materials on DID Methods are often difficult to comprehend immediately, making decisions hard to justify for newer members of the space. This document should help narrow down some of the concerns that implementors and standards bodies will encounter.

# Creative Brief

## Audience

We have three main types of readers that we'd especially like to connect with.

### Implementors Picking DID Methods

The question we want to avoid is: "I can't tell if this DID Method is part of the standard."

Our implementors are creating web browser features, standalone wallets, and back-end issuer and verifier services which require a choice of DID method(s) for basic functionality. While they can pick freely among existing libraries and can use an external resolver service to retrieve DID Documents for DID Methods that they do not natively support, security in the ecosystem ultimately relies on careful review of complex code and specifications that has many users and many interested reviewers. Non-domain experts can benefit from a set of clear guidelines for making and justifying such decisions.

### Standards Bodies Considering Whether a DID Method is Worthy of Publishing

DID method specifiers have historically been unsure about how well-specified a DID method needs to be, given that many are missing required normative sections to rely on.

### Product Owners and Architects designing applications

The DID ecosystem can mix together many 

#### When is a Standard Complete?

The W3C DID WG has received (through formal objections) feedback that in order to know whether the DID standard is complete, implementors need standardized DID Methods. However, the DID WG picking winners and losers in a serialized review process is antithetical to the nature and intent of the DID Specification.

This document promotes a specific set of critera that a standards body may use to judge whether a DID Method is ready to be called a Standard.

#### Can a parent DID 1.0 standard help implementors even if the DID Methods are not blessed by the same standards bodies?

There are several places that could work on a DID Method's standardization:

- W3C
- CCG
- DIF
- Hyperledger
- Trust over IP Foundation
- ESSIF

It can however be difficult to independantly assess the actual quality of DID Methods without relying on the reputation of the parent organisation. Such bodies are also not in the habit of endorsing each other's DID Methods, reducing the maximum degree of confidence one can have in a specification.

### Product Owners defining architectural features which must be feasible and well-supported


## Change in Behavior

Instead of analysing every DID method one-by-one, this rubric helps implementors find the applicable DID method faster and with less iterations, thus reducing the time cost of such decision and implementations.

Instead of demanding a centralized stamp of approval for DID Methods, implementors can use existing resources to evaluate how standards-ready a DID Method is.

## Key Points

* #### Standards bodies are tightly constrained in time and can only make decisions that fit their consensus profile, which operates under competing interests.  If they (ill-advisedly) line up DID Methods for their standardization stamp of approval, then only politics can order the winners and losers;

* #### The DID Method Rubric is an excellent resource of evaluation criteria that helps organize a decentralized system;

* #### Remind the Internet that URLs are a decentralized standard ([not all URLs are http](https://en.wikipedia.org/wiki/Talk:List_of_URI_schemes) - there are more than 200 of these as well!);

* #### Reducing the cognitive overhead on making this decision;

* #### Provide a structure for explaining to others how a decision was made;

* #### Provide an alternative to getting into the ecosystem by creating a new DID Method;

* #### Without centralizing the approval of concrete DID Method specifications (as leaf standards), providing the structure that a standard normally offers.

* #### We've discovered that that approach to this document will differ depending whether the reader is a stakeholder, implementor, or standards body.

---

# Problems that we can help solve

## Proliferation of DID Methods

People come to the DID ecosystem and don't know how to map their use case to an existing DID Method. Seeing the proliferation of DID Methods, they think that creating their own is the first step in participation. 

### How This Document Provides an Alternative

By making the existing Rubric tool more obvious to use for the purpose of extending the ecosystem by choosing an existing DID Method to build on, incomplete and ad-hoc proliferations may fall out of style.

# Example Criteria

## General thoughts on the sections

### Regulations

There are different regulations that are important in different jurisdictions. To that extent, each implementor needs to consider and accomodate the different applicable regulations, when choosing a DID Method. In applications involving global contexts and accessibility,  the focus should be on supporting as wide a variety of compliant options as possible. Regulatory compliance is a special case of criteria which an implementor or system architect should be particularly aware of, if it is relevant to their application.

## A Selection of Specific Criteria

We've split [the criteria - explained in the Rubric Document](https://w3c.github.io/did-rubric/) - into three main categories:

# Considerations
DID Method endorsement typically requires many points of consideration along several axes, and so can be difficult to succinctly express. Stakeholders involved in such a process can benefit from a set of steps to follow when considering if a DID Method is suitable for their purposes.

## Standards Organisations and Reviewers

## Implementors
Implementors are parties building a system or application which relies on integration with one or more DID Methods. Implementors are typically responsible for making technical decisions for their application based on requirements. Importantly implementor recommendations presented here are based on technical restrictions and considerations only, NOT any concern for the trust, privacy and cost mechanics of a DID Method except where they influence the implementation process.

### Ecosystem Integration
It is important to note that the following steps are important for use cases involving only features which any DID Method can support (those defined in the core spec and extension registries). Use cases involving specific integration with existing ecosystems (e.g. requiring a DID to perform work on-chain) are bound to have requirements which cannot be fulfilled by the vast majority of use cases.

This is to say, if there are non-DID related reasons to choose a DID Method there are probably very few options to choose from, so further feature selection and relevant criteria evaluation become unnecessary.

### Feature Selection
Implementors SHOULD express technical feature requirements as a set of supported sections from the DID Core spec and the DID Method Specification Registries.Implementors SHOULD select DID Methods to include in their system based on the features required to support their use case.

DID Method features are expressed as sections of the DID Core spec and the DID Method Spec Registries. Implementors SHOULD explicitly mark additional features not covered by the Registries as application or ecosystem specific.

### Relevant Criteria Selection
Implementors with requirements that are not DID-level technical features SHOULD express their requirements as a subset of acceptable criteria from the DID Method Rubric and SHOULD evaluate their prospective DID Methods against said criteria. Additional non-Rubric criteria SHOULD be expressed in terms roughly conformant to the Rubric criteria system.

#### Recommended Criteria
While Implementors must enumerate their own criteria relevant to their application, it is RECOMMENDED that they consider at least the following criteria from the DID Method Rubric:
* 3.1.5. Cost: DID Methods with associated costs are much more complicated to integrate with due to requireing support for whichever payment might be required.
* 3.2.2. Interoperability: Interoperability is a key goal of using DIDs, DID methods which are not conformant to the DID Spec are effectively new silos.
* 3.2.1. Permission: DID Methods which require permission to use will have special characteristics which will have to be supported by implementors (typically some method-specific integration with the DID Method provider).
* 3.2.3. Scope of Usage: Scope is a very important characteristic of DID Methods and different scopes can imply vastly different usage models, intended purposes and even runtime characteristics.
* 3.3.2. Resolution Resource Consumption: Implementors must be conscious of the resources consumed by a resolver if they are to include one or more in their architecture.
* 3.5.3. Platform Support and 3.5.4. Language Support: Saving effort by reusing existing implementations can be important. Methods should not necessarily be disregarded for lacking support, but lacking support will often reduce the priority of supporting said methods in practice.
* 3.7.x. All Security criteria: DIDs and their signatures are designed to secure applications. Implementors should be very conscious of the security features of the DID Methods they examine and if they are sufficient.
    * Especially 3.7.9. Regulatory Compliance: In practice, most security decisions will be made by evaluating the regulatory needs of the application.
* 3.8. Privacy: Privacy is often a heavily regulated characteristic, and so Implementors should be careful to examine the privacy properties of a DID Method against the regulatory framework they work within (e.g. many DID Methods are not GDPR compliant).
* 3.8.1. Visibility: Similarly to 3.2.3, Visibility can affect the usage and runtime characteristics of a DID Method. For example, pairwise DIDs can only be resolved directly from the DID Controller, massively affecting the possible usage situations of the DID Method.


## Product Owner

### Requirement Definition


### raw



    3.The criteria
    3.1Rulemaking
    3.1.1Open contribution (participation)
    3.1.2Transparency
    3.1.3Breadth of Authority
    3.1.4Public v private economies
    3.1.5Cost
    
      Diogo and Charles vote for and consider ongoing operational
        cost critical for the program manager's point of view for use cases involving DID creation/updating.

      Ryan votes (from the standards body perspective) against all rulemaking because you can implement an
        authoritarian rulemaking process, and consider it well
        specified.

    3.2Design
    3.2.1Permissioned operation
    
      "To use the DID Method, do you need permission?"
    
      standards bodies
      
        Ryan votes yes.  In standards bodies that are value-driven, even though the DID ecosystem allows the choice of DID Methods that are permissionless, the inclusion of permissioned DID Methods could confuse the message that the standard body's values are meant to provide guidance on.
      
      product owners
      
        Ryan votes yes.  This is a major question of freedom for users, and those with enough information will change how they approach various product options.
      
      implementors

        Ryan votes yes.  Chosing a DID Method with permissioned gating changes the design options available.
    
    3.2.2Interoperability
    
    "Does the DID Method restrict access or functionality to particular wallet implementations per the specification? (Whether or not any given wallet works with the resolver or registry is covered elsewhere.)"
    
      standards bodies 
      
        Our concern in this area is whether the standard is clear, not how well the DID Method works or how many interoperable implementations exist.  Retrieving a DID Document on a lone DID Method - by any means, including an external third-party resolver - will still allow interoperable key material (such as an RSA key) to be returned.
        
        However, the fact that a DID Method will be usable only by a specific implementor is critical to a satndards body's considerations.
        
        Ryan votes yes.
        
      product owners
        
        Ryan votes yes.  this is a major factor in competitive analysis.
        
      implementors
      
        Ryan votes yes.  this can mean an implementation could fail to operate without permission.
    
    3.2.3Scope of usage
    
      this rubric-question should be updated to "how are DIDs communicated between the parties?"
    
      standards bodies
      
        Ryan votes yes.  how DIDs are communicated is a matter of privacy and this matters to some standards bodies.
      
      product owners
      
        Ryan votes yes.  customers who are aware of the issue will care.
      
      implementors
      
        Ryan votes yes.  some implementation patterns will be enabled or disabled by limitations on communications.
    
    3.3Operation
    3.3.1Financial accountability
    
      Ryan votes no for standards bodies.   although low marks here might make for a scammy DID Method, it could still be implemented clearly.
      
      Charles: no.
      Diogo: this depends on whether this rubric is being approached from a technical perspective (so from a builder/implementor) or from a business/organization perspective, where topics such as cost, financial accountability and regulation are seen as substantially more important. 
      
    3.3.2Limited resource resolution

      Ryan votes (from the standards body perspective) yes because if a spec is not computable in a reasonable amount of time on the desired hardware, then it is not implementable.
      Diogo votes yes, based on above.

    3.3.3Limited resource registration
    yes from an architectural perspective (Diogo)
    
    3.4Enforcement
    Diogo votes yes since regulatory bodies will most likely request a possibility of enforcement of such actions, hence this needs to be developed from the ground up into the DID Method (So managers / architects would require this)
    
    3.4.1Auditability
    Diogo votes yes since, similarly to 'Enforcement', governing bodies or implementors might require auditability capabilities to assess any potential (insert another word for wrongdoing or mistake) (see above)
    
    3.5Alternatives 
    
    3.5.1Active implementations
    
    3.5.2Market share 
    Diogo votes yes IF the final product requires limited downtime or needs a backup connection method (hence, bigger market share should equate to more potential backup)
    
    3.5.3Platform support  - The question on the DID Method Rubric v1.0 is not particularly clear. To that extent, the authors have decided to consider a different question. The reformulated approach was more of "do current platforms have support for DID Method implementation?" 
    
    Diogo votes yes, because this is a rather important question for implementors that may not be experts or have substantial funding to seek that expertise.
    
    Charles votes yes for practical concerns, if developers do not want to spend the time creating an implementation from scratch (also for 3.4.5). 
    
    3.5.4Language support - The question on the DID Method Rubric v1.0 is not particularly clear. To that extent, the authors have decided to consider a different question. The reformulated approach was more of "do current languages offer support for DID Method implementation?" 
    
    Diogo votes yes, because this is a rather important question for implementors that may not be experts or have substantial funding to seek that expertise.
    
    
    3.5.5Rogue risk
    
    
    3.5.6Forkability
    
    Forkability may be interesting for an implementor with reduced resources.
    
    Depending on the type of project?
    
    3.6Adoption (and diversity)
    
    3.6.1Acceptance
    
    3.6.2Users
    
      Ryan votes (from the standards body perspective) no because this is the popularity contest.
    
    3.6.3International adoption
    
    3.6.4In which countries?
    
    3.6.5Language support
    
    3.7Security
    
    3.7.1Robust Crypto
    
      Ryan votes (from the standards body perspective) yes because if there is not robust crypto then the community should make it robust.
    
    3.7.2Expert Review
    
      Ryan votes (from the standards body perspective) yes because a response of C or D would prevent the specification from moving forward in any standards body.
    
    3.7.3Future Proofing
    
      Ryan votes (from the standards body perspective) no because many critical systems currently in use do not address post-quantum cryptography.  However, some standards bodies are beginning to only consider techniques with post-quantum solutions.
    
    3.7.4Self Certification
    
      Ryan stopped here.
    
    
    3.7.5Availability
    
    3.7.6Evolution
    
    3.7.7Many Eyes
    
    3.7.8Diffuse Control
    
    3.7.9Regulatory Compliance
    
    Charles votes yes, to this in particular and as an umbrella concept for all the 3.7 section (except for 3.7.5) (each criteria is relevant insofar as there exist applicable regulations requiring certain properties of them)
    
    3.8Privacy
    
    Charles votes yes on the principal that it's usually a heavily regulated characterstic,
    
    3.8.1Per-DID constraints on visibility
    
    3.8.2Cross-DID Leakage
    
    3.8.3Incentives for Multicontext DIDs
    
    3.8.4Revocation of Consent
    
    3.9Other criteria


### Reasons that other criteria did not make the cut:



## Holistic  grouping of criteria
This grouping of individual criteria is based on the paper "Decentralised Identifiers (DIDs) v1.0":

### Decentralisation

### Control

### Privacy

### Security

### Proof-based

### Discoverability 

### Interoperability

### Portability

### Simplicity

### Extensibility 

## DID Specification Registries Support
The DID Specification Registries "serves as an official registry for all known global parameters, properties, and values used by the Decentralized Identifier ecosystem". Support for many values is marked as "MAY" in the DID core specification, but a higher degree of support for the primitives of the DID ecosystem indicates a more complete and coherent specification.

Extended support of certain DID parameters provides properties which implementors may find useful. For instance, support for the [Bls12381G1Key2020](https://www.w3.org/TR/did-spec-registries/#bls12381g1key2020) Verification Method type parameter enables the issuance of selective-disclosure based Verifiable Credentials based on the [BbsBlsSignature2020](https://w3c-ccg.github.io/ldp-bbs2020/) linked data proof type, while support for the Ed25519VerificationKey2018 does not enable any selective disclosure functionality.

Instead of committing to a single DID Method, it is prudent for implementors and product owners to support as wide a variety of appropriately-well specified methods as is practical which implement the DID functionality required for their purpose within an application.

Product owners building on top of DID Methods should first consider exactly which features of a DID they must rely on to implement an application. Mapping of use case requirements to suitable DID Ecosystem Specifications is outside the scope of this document and any selection should be justified by said requirements. A thorough guide to exactly how different DID features and extension mechanisms relate to use case requirements is a goal for future work.

---

## Lessons from other uses of DID Method Rubric in specific evaluations

Two of the lessons from specific evaluation of DID Methods are that:
* DID Methods have their own reasons for existing and their own specific concerns, and any Rubric-based evaluation that only uses existing criteria (as of 2022) is incomplete.
* The best way to use the Rubic is to extend it with criteria that specific evaluations have uncovered.

## Review of URI Scheme Requirements ([RFC4395](https://datatracker.ietf.org/doc/html/rfc4395#section-2.1))

> ### 2.1.  Demonstratable, New, Long-Lived Utility
> 
> The use and deployment of new URI schemes in the Internet infrastructure is costly; some parts of URI processing may be scheme-dependent, and deployed software already processes URIs of well-known schemes.  Introducing a new URI scheme may require additional software, not only for client software and user agents but also in additional parts of the network infrastructure (gateways, proxies, caches).  URI schemes constitute a single, global namespace; it is desirable to avoid contention over use of short, mnemonic scheme names.  For these reasons, the unbounded registration of new schemes is harmful.
>
> New URI schemes SHOULD have clear utility to the broad Internet
community, beyond that available with already registered URI schemes.
>
> [name=RFC4395] [time=February 2006] [color=#907bf7]

## Relevant Criteria for Standards Bodies

### Complies with DID spec requirements
### Listed in DID registry
### Author contacts are available and updated
### two independent implementations
### clear IP-assignment of all parties adding to spec
### independent security reviews (and other specific Rubric criteria)
### multiple independent rubric evaluation reports
### relevance to the mission of the standards org 

### passes a relevance test / "Demonstratable, New, Long-Lived Utility"

#### not spam
#### (claimed) no better way to do a specific thing for specific people who want that thing
#### funding organizations that can handle ongoing change (or security alerts) to the specification

  * for a member org, does it have multiple sponsors?
  * for open source, does it have multiple active contributors, from different interest groups?

### the principles from above

#### What is the complete description allowing the interoperability of bytes on the wire between two independent implementations (when following the text of the specification);
#### Are the cryptographic verification mechanisms supported by the DID method are compliant with certain regulations or requirements;
#### What usage is "important" based on guidelines such as:
  * Existing key material usage;
  * Enabling applications; and
  * Users expressing their value; and
#### Do the adoption and scaling characteristics fit with the implementor's or standardization body's expected target audience?

---

| Criteria | Standards Bodies | Product Owners | Implementors |
|           ----------- | ------------- | ----------- | ----------- |
|3.1 Rulemaking|✓|✓||
|3.1.1 Open contribution (participation)|✓|||
|3.1.2 Transparency|✓|||
|3.1.3 Breadth of Authority|✓|||
|3.1.4 Public v private economies|✓|||
|3.1.5 Cost||✓||
|3.2 Design||||
|3.2.1 Permissioned operation||||
|3.2.2 Interoperability|||✓|
|3.2.3 Scope of usage|||✓|
|3.3 Operation||||
|3.3.1 Financial accountability||✓||
|3.3.2 Limited resource resolution|||✓|
|3.3.3 Limited resource registration||✓|✓|
|3.4 Enforcement|✓|✓||
|3.4.1 Auditability|✓|✓||
|3.5 Alternatives||||
|3.5.1 Active implementations||||
|3.5.2 Market share|||✓|
|3.5.3 Platform support  |||✓|
|3.5.4 Language support|||✓|
|3.5.5 Rogue risk||||
|3.5.6 Forkability|✓|||
|3.6.1 Acceptance ||||
|3.6.2 Users ||||
|3.6.3 International adoption ||||
|3.6.4 In which countries? ||||
|3.6.5 Language support ||||
|3.7 Security|||✓|
|3.7.1 Robust Crypto||✓|✓|
|3.7.2 Expert Review|||✓|
|3.7.3 Future Proofing ||✓|✓|
|3.7.4 Self Certification |||✓|
|3.7.5 Availability ||||
|3.7.6 Evolution  |✓|✓|✓|
|3.7.7 Many Eyes |||✓|
|3.7.8 Diffuse Control |||✓|
|3.7.9 Regulatory Compliance |||✓|
|3.8 Privacy ||||
|3.8.1 Per-DID constraints on visibility ||||
|3.8.2 Cross-DID Leakage ||||
|3.8.3 Incentives for Multicontext DIDs ||||
|3.8.4 Revocation of Consent ||||
|3.9 Other criteria||||

