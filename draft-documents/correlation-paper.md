# RWOT Correlation Paper 

[![hackmd-github-sync-badge](https://hackmd.io/1rGIb8kmSKWE7QYWfVR_rw/badge)](https://hackmd.io/1rGIb8kmSKWE7QYWfVR_rw)

Syncs to -> https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/draft-documents/correlation-paper.md

Contact @ChristopherA if you want push a change from HackMD.

## To Do

* [ ] What will final paper name?
  * [ ] What do you think of Selective Correlation?
  * [ ] What about Self-Sovreign Correlation?
* [ ] Review old paper and grab relevant and discard irrelevent
  * [ ] How much is this a update vs refactor of old paper. 
    * @Brent Suspect more refactor
  * [ ] refactor use cases
  * [x] remove old and 
  * [ ] add new technical examples
    * [ ] Enumerate and describe "capabilities" of various technologies, with regard to correlation
* [ ] Progressive trust
    * [ ] 
* [ ] Use Cases
    * [ ] Educational @ChristopherA 
    * [ ] Healthcare @elenachachkarova
    
## Creative Brief
* Who's your audience?
  
  Policy-makers

* What change in their behavior do you want to induce? (Call to Action)

  To establish policies that take into consideration the impact of correlation, informed by a fuller understanding of self-correlation and the the capabilities provided by modern techniques.

* What are the key points you're going to include?

  * Different aspects of data minimization, such as selective disclosure and progressive trust.
  * That various technology choices exist today, which exhibit different characteristics for (anti-)correlation.
  * Use cases to illustrate each of the capabilities.



## Abstract

The goal of this paper is to enable decision makers, particularly non-technical ones, to gain a nuanced grasp of self-correlation. We will describe the properties in plain English, but with some rigor. This will enable readers of this paper to better understand self-correlation best practices, to adopt the correct approaches for the appropriate use cases, and to assess techniques that enable those enhancements.

We begin with an exploration of data minimization as a principle, then discuss techniques that support data minimization such as selective disclosure and progressive trust. 

Data Minimization was previously a topic of an [RWoT paper](https://github.com/WebOfTrustInfo/rwot5-boston/blob/master/draft-documents/DataMinimization/Data%20Minimzation%20and%20Selective%20Disclosure.md), later published by W3C-CCG as a [Draft Community Group Report](https://w3c-ccg.github.io/data-minimization/).

This work may be considered a 're-boot' of that paper. It expands and clarifies the topics of that paper, while removing examples and appendices that may no longer be as pertinant and replacing them with new ones. A significant addition is an update of the use cases provided as a means to explore the need for reducing correlation in different circumstances.

Once complete, this paper may serve as input to a Verifiable Credentials Working Group Note related to this topic.


## Raw Notes

Use cases: we'd like to have a progressive set of use cases to demonstrated privacy issues of correlation, but also avoid government focused scenarions (thus avoid the common mobile driver's license over-21 example).

Educational / Professional Use Case:

1) DREW WANTS A PROFESSIONAL SKILL: Drew, a member of a minority, desires comprehensive training in a high-paid building construction specialty — plasma welding. He applies to Acme Professional School, and is accepted. Students of Acme Professional School are qualified to receive government-backed students loans from Burton Bank — Drew applies, and receives a loan, and payments are deferred. Drew offers the school a DID, and adds details to allow for others to authenticate Drew (such as a photo) in a Student ID.
    * TRANSACTIONS: Drew becomes a student of Acme Professional School. Drew applies for student lown and pays for schooling. Drew receives Student ID.
    * CORRELATION: Drew desires to be correlated as a student to attend classes and events, get a loan to pay for classes, and misc. services such as get student discounts.
    * THREAT: ?
    
2) DREW GETS AN EDUCATIONAL CREDENTIAL: Drew (the subject) obtains comprehensive training from a Acme Professional School (the issuer) on plasma welding, including a number of advanced techniques along with a variey of workplace safety topics. The Acme Professional School issues an education credential to Drew (the subject & holder) with all of these details that confirm Drew has all the proper training in this complex technical discipline.
    * TRANSACTIONS: Drew completes schooling, Drew finishes payment for schooling, receives educational credential.
    * DESIRABLE CORRELATION: Drew desires to be correlated as a graduate of school and qualified for various job prospects.
    * CORRELATION THREAT: ?

3) EXAMPLE OF ELISION BY A DREW (SUBJECT/HOLDER): Drew applies for a plasma welding gig at Erickson's Construction, that requires a workplace safety certification. Drew (the subject & holder) offers their Acme Professional School educational credential with details on the training and safety certification (they desire correlation as being qualified for the job) without personal information (such as ethnic name, photo as they do not wish to be correlated as a minority).
    * TRANSACTIONS: Drew applies for employement with educational credential.
    * DESIRABLE CORRELATION: Drew desires to be correlated as a qualified graduate, and school is correlated as a legitmate accredited school. ((Elena suggest is that sometimes you might want to elide the school name, for instance if it was accredited but was based in eastern europe it might be discrimiated against.))
    * CORRELATION THREAT: Drew does not wish to be descriminated against for his family origin.

3) EXAMPLE OF PROGRESSIVE TRUST: Erickson's Construction offers Drew a temporary gig at a reasonable hourly rate, pending additional verification of identity at the workplace. Drew (subject & holder) presents his Acme Professional School (issuer) educational credential again, but this time with sufficient authentication (such as photo), so that Erickson's Construction (verifier) can issue a pass to enter the workplace.
    * TRANSACTIONS: Drew receives offer, accepts offer. Gives tax information, legal name, photo. 
    * DESIRABLE CORRELATION: This same credential that the job was offered to is presented again, with less elision, to satisify workplace require.
    * CORRELATION THREAT: 

4) EXAMPLE OF ELISION BY A HOLDER: Erickson's Construction (holder≠subject) needs to prove to Three Towers Corporation (verifier) that they have sufficient number of qualified employees for the contract. They provide Drew's (subject) educational credential (already partially elided) to Three Towers. Three Towers can verify that the the school (Acme Professional School but elided by Drew) is accredited, but in addtions Erickson Construction further elides the names of the employees (to prevent pouching by other firms). 
    * TRANSACTIONS: Erickson Constructions (holder) presents Three Towers (verifier) multiple elided employee educational credentials.
    * DESIRABLE CORRELATION: Erickson Construction proves sufficent and properly trained staffing, from accredited schools.
    * CORRELATION THREAT:  * CORRELATION THREAT: Erickson Construction may not wish to be digital known as hiring minorities. Erikson Construction does not employees be 
    * MISC. is there an insurance or courts elision use case beyond this?

## Technology Characteristics and Choices

In this section, we can develop a list of technical characteristics with regard to (anti-)correlation, and try to map how different technology choices can fulfill them.

TODO:
- Maybe better differentiate between disclosure of data on various levels: credential, identifier, protocol, environment ("ambient correlation"?). On which layer does the (anti-)correlation happen, e.g. does it happen in the cryptographic signature, or on the identifier (DID) layer, etc.?
- How does salting fit in? Who does the salting?
- How do "sub-holders" fit in?

Characteristics:
* **[C1]** The Holder can selectively disclose data with a Verifier.
* **[C2]** The Holder can selectively disclose data with a Verifier, without requiring interaction with the Issuer during the disclosure process.
* **[C3]** The Holder can selectively disclose data with different Verifiers, without requiring interaction with the Issuer during the disclosure process.
* **[C4]** The Holder can arbitrarily choose which subset of data to selectively disclose with Verifiers, without requiring interaction with the Issuer during the disclosure process.
* **[C5]** When disclosing data to multiple different Verifiers, the Verifiers cannot correlate the subject via any single, unique identifier.
* **[C6]** When disclosing data to the same Verifier in multiple different interactions, the Verifier cannot correlate the subject via any single, unique identifier.
* **[C7]** The Verifier can verify that the Holder who is disclosing the data is the same entity that has received the data from an Issuer. *<-- Note: Maybe reference the work of the other RWoT11 group that's working on "holder binding"*
* **[C8]** The Holder can selectively disclose data that is derived (using predicates) from the original data they have received from an Issuer.
* Type(s) of crypthography used.
* ...

Choices:
* **[PLAINSIG]** Plain signatures: Ed25519Signature2020, RSA signatures, etc.
* **[SUBCREDS]** Issuing multiple, granular "sub-" credentials separately, which the Holder can then use as appropriate for interactions with Verifiers.
* **[SINGLEUSECREDS]** Issuing single-use "bearer" credentials intended to be used for a single interaction between a Holder and a Verifier.
* **[BBS2020-LD]** BBS+ Signatures 2020: https://w3c-ccg.github.io/ldp-bbs2020/
* **[BBS-SIG]** BBS Signature Scheme: https://identity.foundation/bbs-signature/draft-looker-cfrg-bbs-signatures.html
* **[ANONCREDS]** AnonCreds: https://anoncreds-wg.github.io/anoncreds-spec/
* **[SD-JWT]** SD-JWT: https://github.com/oauthstuff/draft-selective-disclosure-jwt
* **[REDACTION2016-LD]** Redaction Signature Suite 2016: https://w3c-ccg.github.io/lds-redaction2016/
* **[MERKLE2021-LD]** Merkle Disclosure Proof 2021: https://w3c-ccg.github.io/Merkle-Disclosure-2021/
* **[GORDIAN]** Gordian Envelopes: https://github.com/BlockchainCommons/BCSwiftSecureComponents/blob/master/Docs/02-ENVELOPE.md

Mapping of Characteristics and Technologies

| Technology      | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 |
| ---             | -- | -- | -- | -- | -- | -- | -- | -- | -- |
|PLAINSIG         | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✓ | ✕ | ? |
|SUBCREDS         | ✓ | ✓ | ✓ | ✕ | ✕ | ✕ | ✓ | ✕ | ? |
|SINGLEUSECREDS   | ✓ | ✕ | ✕ | ✕ | ✓ | ✓ | ✕ | ✕ | ? |
|BBS2020-LD       | ✓ | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✕ | ? |
|BBS-SIG          | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ | ✕ | ? |
|ANONCREDS        | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ? |
|SD-JWT           | ? | ? | ? | ? | ? | ? | ? | ? | ? |
|REDACTION2016-LD | ✓ | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✕ | ? |
|MERKLE2021-LD    | ✓ | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✕ | ? |
|GORDIAN          | ? | ? | ? | ? | ? | ? | ? | ? | ? |



### Correlation Adversary from Smart Custody

![](https://github.com/BlockchainCommons/SmartCustodyBook/raw/master/manuscript/resources/image3.png)

***Motivation.** “I want information. I watch cryptocurrency transactions with an eagle eye, ready to swoop in on any mistake. If you keep making the same payments or receiving the same payments or using the same addresses, I’ll figure it out. I want to connect the dots to determine who is spending cryptocurrency for what, and I can figure that puzzle out if you give me enough pieces.”*

***Key Words:** Active, Technological.*

Cryptocurrency use is pseudo-anonymous and somewhat private. However, it’s not totally so: it’s possible to build up correlation. Through statistical analysis and through the discovery of accidental revelations, a third-party could tie together an asset holder’s usage of various funds to paint a larger picture of their finances and contacts.

***Abstract Case Study: Correlating over Coffee.*** Alice is sloppy with her bitcoins and tends to use one address for everything. She goes out to buy a coffee with bitcoins; while she sips away at the café, working at her laptop, the barista notes the huge number of bitcoins going into the address. She follows Alice home, planning larceny.

***Abstract Case Study: Correlating Identities.*** Carol uses the same online identity on bitcointalk and on twitter. Eastern European hackers monitor twitter, see her talking about bitcoins, track that back to bitcointalk, and find wallet addresses mentioned there that reveal her bitcoin wealth. They then set their scripts lose, hoping to break into her computer and steal her keys.

{pagebreak}

***Risks:***

1.  **Funds Revelation.** An asset holder’s ownership of various funds can be revealed. This can make it possible to track what they spent funds on and who they’re associated with. It also puts them in greater danger from any number of other adversaries.
2.  **Cascade: Censorship.** If they know who you are, they can block you.
3.  **Cascade: Coercion.** If they know who you are, they can threaten you.
4.  **Cascade: Legal Forfeiture.** If they know who you are, you can become a target for a nation-state or for a civil action.
5.  **Cascade: Loss of Fungibility.** If funds have been correlated, they may lose fungibility.
6.  **Cascade: Sophisticated Theft.** If they know who you are, you can become a target for thieves.

***Process Solutions:***

1.  **Practice Anonymity.** Do not let people know you have bitcoins; ensure that you in no way ever link your key to your real persona.
2.  **Practice Anonymizing Your Funds.** Occasionally use methods like CoinJoin, SendShared, or Zerocoin to anonymize your transactions. On Blockstream’s Liquid, always make use of Confidential Transactions.
3.  **Practice Key Hygiene.** Follow the best practices of using different addresses for every transaction that you conduct. Each time you make a transaction with the same address, you are leaking information to your counterparty, which could be used to identify and either censor or correlate future transactions.






paper text below this line
==============================================================
Engineering Privacy for Verified Credentials: 
In Which We Describe Data Minimization, Selective Disclosure, and Progressive Trust 
==============================

# Authors

* Christopher Allen - @ChristopherA (GitHub & Twitter), ChristopherA@LifeWithAlacrity.com - [Blockchain Commons](https://www.BlockchainCommons.com)
* Fabio Tagliaferro - @fabtagliaferro (GitHub), [University of Verona](https://www.di.univr.it/?ent=persona&id=39578&lang=en), [Commercio.Network](https://commercio.network/)
* Markus Sabadello - @peacekeeper (GitHub), [Danube Tech](https://danubetech.com/)
* Brent Zundel - @brentzundel (GitHub), [Avast](https://www.avast.com/)
* Elena Chachkarova - @elenachachkarova (GitHub), [Nymlab](https://www.nymlab.it/#/)

# Introduction

# Self-Correlation

## Problem Statement
TODO
* what is correlatable data
* what is a data broker
* Data Broker costs should be high as possible.
* The more correlatable data that is available, the easier it will be for a data broker to accumulate useful data. Therefore, a reduction in the set of available verifiable data 

## Identity & Correlation

It is important to recognize that 

> *“We argue that, when discussing identity systems, “correlation” enables a more concise discussion and clearer understanding of how identity is created and used[8]. It’s not that “identity” is incorrect, it’s that the mechanisms of identity are inherently mechanisms of correlation and, therefore, we can be clearer by focusing the discussion how correlation is managed.<br/>*
> …<br/>
> *“Using “correlation” to describe identity systems provides a simpler, more coherent view of mechanisms, capabilities, and risks. The term doesn’t change the nature of the system. It is simply more concise and more accurate. It results in discussions that are more rigorous and easier to understand.*
> …<br/>
> *“When you find yourself in a project where the definition of “identity” seems to be a repeating source of challenging conversations, try describing the role of identity in terms of correlation.* 
> …<br/><br/>
> *“We believe that every identity system can be fully characterized by how it manages correlation across contexts."* <br/><br/>
> — **from "Identity Crisis: Clearer Identity through Correlation" from @RWOT2-ID2020, by Joe Andrieu, et al.**

In the past, individuals had little control about what information they provide will be correlated. In a self-sovereign future, individual will have more opportunities to manage or make choices as to what data will be correlated or protected.

## Principles

### Correlation Concepts
TODO
* what is it, why is it good or bad?
* can it even be avoided?

### Data Minimization
Data minimization is the act of limiting the amount of shared data strictly to the minimum necessary in order to successfully accomplish a task or goal. There are three types of minimization:
* Content minimization – the amount of data should be strictly the minimum necessary.
* Temporal minimization – the data should be stored by the receiver strictly for the minimum amount of time necessary to execute the task.
* Scope minimization – the data should only be used for the strict purpose of the active task. 

Data minimization is enacted primarily by policy decisions made by stakeholders in the credentials ecosystem:
* Credential issuers ensure that credentials may be presented in such a way as to enable data minimization. This may require issuing multiple, related, granular sub-credentials. 
* Credential inspectors establish in advance policies regarding the data they will examine: 
	* what is the minimum data necessary to accomplish the task or goal?
	* what is the minimum time the data can be stored to execute the task?
	* what processes ensure that the data is applied only to the task at hand and does not, by a process of scope creep, become applied to other tasks or goals?

Data minimization policies impact selective disclosure, the next privacy enhancement.

## Capabilities and Techniques
### Elision
### Selective disclosure
Selective disclosure is the ability of an individual to granularly decide what information to share. Stakeholders in the credentials ecosystem enable selective disclosure capabilities in the following ways:
* Credential issuers format the credential and its attributes in such a way as to enable selective disclosure. As with the strategy of data minimization, they may issue multiple, related, granular sub-credentials. Each attribute and the overall credential may be formatted to support cryptography, a capability described in more detail below. 
* Credential inspectors ensure the request is framed in such a way as to enable selective disclosure, using the cryptographic tools required. 

Once data minimization policies and selective disclosure are in place, the third and last enhancement can be applied. 

### Progressive Trust
Progressive trust is the ability of an individual to gradually increase the amount of relevant data revealed as trust is built or value generated. 

To enable progressive trust capabilities, stakeholders in the credentials ecosystem act in the following ways:
* Issuers format the credential(s) in such a way as to enable progressive trust. This may require issuing multiple, related, atomic sub-credentials. It also may require formatting the credential to support mathematical queries and cryptographic proofs. Finally, the issuer's data model may express how the various sub-credentials are related in a scenario involving progressive trust. 
* Inspectors ensure that requests are framed in such a way as to enable progressive trust. They structure the communication in order to to gradually escalate credential requests in order to enable a subject to progressively trust the inspector more and more, revealing the minimum data necessary to accomplish each step of the task or goal and revealing more and more as the mutual communication progresses. 


# Use Cases

# Conclusion/Summary

# Acknowledgements

We would like to acknowledge the following persons who contributed ideas that helped define the ideas in and the shape of this paper:
* Adrian Gropper
* Joe Andrieu

We also acknowledge the contributors to [the 2019 paper](https://w3c-ccg.github.io/data-minimization/):

* Lionel Wolberger, Platin.io
* Brent Zundel, Evernym/Sovrin
* Zachary Larson, Independent
* Irene Hernandez, Independent 
* Katryna Dow, Meeco
* Christohper Allen, Blockchain Commons

# References
[1] [Identity Crisis: Clearer Identity Through Correlation](https://github.com/WebOfTrustInfo/ID2020DesignWorkshop/blob/master/final-documents/identity-crisis.pdf)

## Related RWOT Advance Readings & Topics
* [Elision, Redaction, and Noncorrelation in Smart Documents](https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/advance-readings/elision-redaction-correlation-smart-documents.md)
* [Reducing Correlation: To What Degree is it Necessary?](https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/advance-readings/reducing-correlation.md)

## Links to other related documents
* [Engineering Privacy for Verified Credentials: In Which We Describe Data Minimization, Selective Disclosure, and Progressive Trust](https://github.com/w3c-ccg/data-minimization) (last updated Apr 12, 2022, released by W3C-CCG Apr 4, 2019)
* [Formalising Linked-Data based Verifiable Credentials for Selective Disclosure](https://ssr2022.com/slides/FormalisingLinkedDataBasedVerifiableCredentials.pdf)
* Recent PRs on [VC Data Integrity spec](https://w3c.github.io/vc-data-integrity/) in [W3C VC WG](https://www.w3.org/groups/wg/vc):
    * About unlinkability: https://github.com/w3c/vc-data-integrity/pull/52
    * About selective disclosure: https://github.com/w3c/vc-data-integrity/pull/53
* [Progressive Trust](http://www.lifewithalacrity.com/2004/08/progressive_tru.html) From Life With Alacrity by Christopher Allen 2004
* [W3C Credentials Community Group Home Page](https://www.w3.org/community/credentials/)
* Camenisch, Lysyanskaya. [An Efficient System for Non-transferable Anonymous Credentials with Optional Anonymity Revocation](http://www.cs.ru.nl/~jhh/pub/secsem/camenish2001idemix-clean.pdf)
* Pfitzmann, Hansen. 2010. [A terminology for talking about privacy by data minimization: Anonymity, Unlinkability, Undetectability, Unobservability, Pseudonymity, and Identity Management](https://www.researchgate.net/publication/234720523_A_terminology_for_talking_about_privacy_by_data_minimization_Anonymity_Unlinkability_Undetectability_Unobservability_Pseudonymity_and_Identity_Management)
* Cooper, Tschofenig, Aboba, Peterson, Morris, Hansen, Smith, Janet. 2013. [RFC6973](https://tools.ietf.org/html/rfc6973). The draft can also be helpful, "This document focuses on introducing terms used to describe privacy properties that support data minimization." 
* Hansen, Tschofenig, Smith, Cooper. 2012 [Privacy Terminology and Concepts. Network Working Group Internet-Draft Expires: September 13, 2012](https://tools.ietf.org/html/draft-iab-privacy-terminology-01)

# Appendix: Cryptography Support for Self-Correlation

## Introduction
Implementing privacy enhancements depends on organizational decisions. Determination of the data needed, with an eye towards data minimization, along with a clear model of how data is used over the lifecycle of engagement, goes a long way towards enabling progressive trust. However, policies are not enough.

When enhancing privacy online, some data parts must be revealed while others remain concealed. Concealment is achieved mostly by the art of cryptography. Cryptography enables us to achieve our goal by means of three primary enablers: secrets, difficult mathematical tasks, and zero-knowledge capabilities. The children's ["Where's Waldo?" illustrated book series](https://en.wikipedia.org/wiki/Where's_Wally%3F_(book)) helps us to describe these three enablers. In these books a distinctively dressed man appears only once on each page, wearing a striped hat. Readers are asked to scour the page and locate him. We can understand the three enablers by examining Where's Waldo one step at a time.

* **A Secret**: For the new reader, Waldo's location is a secret. The illustrator knows it, and the reader doesn't. The reader is encouraged to search the page and find Waldo, but that is a difficult task. Some readers give up and ask someone who has already found Waldo to show them his location. In essence, they are asking another reader to reveal the secret. Once found, a reader could keep the information secret by circling Waldo in red and storing the book in a safe. This amounts to storing the secret for future use. Secrets are essential to crypto. They are usually called keys, and they must be managed carefully. 
* **A Difficult Task**: Waldo is difficult to find on the page. The reader has to search everywhere and mistakenly identify many Waldo look-alike characters before reaching a satisfactory conclusion and finding him. Yet when he is finally discovered, or someone points Waldo out, it's easy to see where he is. That's why it's a fun task. This difference between the difficulty of conducting the task and the ease of verifying the task lies at the heart of cryptographic enablers.
* **A Zero Knowledge Enabler**: Can you prove you found Waldo without revealing the secret of his actual location on the page? There is a simple way to do so. Take a rectangular piece of white cardboard that is much larger than the book. Cut a hole exactly fitting Waldo to reveal his silhouette only, nothing else. You can now show Waldo to anyone, peeking out of the cardboard. Yet the cardboard is wide and opaque, hiding the book thoroughly, so a verifier has no idea where Waldo is on the page. The puzzle was solved and someone verified the achievement, without revealing any knowledge of how to solve the puzzle. The secret is still safe, the task still just as difficult as before. 

## Primary Objectives
The curious behavior of numbers is exploited to achieve four primary crypto objectives.

* **Confidentiality**: a hidden part of a credential cannot be understood by anyone for whom it is unintended. Often called "privacy," we avoid that word here since it can mean many things in addition to confidentiality. 
* **Authentication**: the identity of information shared can be validated as authentic. 
* **Integrity**: the revealed part of the credential cannot be altered without such alteration being detected. Also known as validity, fidelity or verifiability. 
* **Non-repudiation**: aka non-deniability, a credential's creator cannot deny at a later stage his or her involvement.

## Mathematical Basics
Cryptography is a huge field with highly specialized jargon, too much to cover here. But non-specialists may benefit from some understanding of relevant topics in order to make informed decisions. We begin with a brief overview of several concepts from number theory that serve as a foundation for other cryptography that enables this process. This is a curated list of topics progressing from the simple to the more complex. Notice how ideas are re-used and layered as you read on. 

### Number Theory
Number theory refers to the study of the behavior of integer numbers such as one, three, or two hundred. The following are behaviors of these numbers that make them useful for cryptography:

* **Prime**: Some numbers are only divisible by themselves and one. These are called 'prime.'
* **One-way function**: A function that takes a number x and computes another number y such that it is easy to go from x to y, but very difficult (if not impossible) to go from y to x. Like a one-way street, the computation goes only one direction. Given the computed value, it is hard to find the original number. Also called a trap-door function.
* **Modular arithmetic**: a system of arithmetic where numbers "wrap around" upon reaching a certain value. A familiar use is in the ordinary clock, in which our day is divided into twelve-hour periods. Using a 12-hour clock: if the time is seven o'clock now, then ten hours later it will be five o'clock. Cryptographic operations are often designed to operate within 
* **Groups and Finite Fields**: Some subsets of all integers form a "group" that behaves in ways very useful to the performance of cryptography. In extremely simplified terms, a group is a self-sufficient set of integers, where any possible manipulation returns an answer from within the group. Finite fields are types of groups that satisfy certain demanding properties. Notice how this relates to modular arithmetic, where the same numbers are used over and over again. 
* **Discrete Logarithms**: A logarithm is an equation of the following form: <code>log<sub>b</sub>a = x</code>, where x is an exponent such that <code>b<sup>x</sup> = a</code>. Modular exponentiation is an exponent calculated within a finite field. A discrete logrartithm is the inverse of modular exponentiation. There is no efficient method for computing discrete logarithms, they form a "difficult problem" and so are very useful in cryptography.

### Some Helpful Cryptographic Concepts
Over the decades hundreds if not thousands of crypto protocols, processes, algorithms and protocols have been innovated to achieve these objectives, by cobbling together the above six behaviors in different ways. We present here a brief tour of the ten most significant ones in our field of verifiable credentials:

* **PKI** or "public key infrastructure" is a system of public and private keys that lies at the heart of most relevant crypto since a publicly shared digital asset can be locked to, or encumbered by, a private key that is kept secret. Only the person with knoweldge of that private key can, with the right software, unlock that asset. This enables a broad range of activities such as "signature," "authentication," and "certificate validation." In general we call these activities PKI, a public key infrastructure. 
* **Signature**: a signature in this context is a use of PKI. A valid signature gives a recipient "authentication", confidence that the message was created by a known sender; "non-repudiation," that the sender cannot deny having sent the message; and "integrity," that the message was not altered in transit. Signatures enable every cryptographic objective except for confidentiality.
* **Key exchange**: exchange methods enable two parties that have no prior knowledge of each other to jointly establish a shared secret key over an insecure channel. This key can then be used to encrypt subsequent communications using a symmetric key cipher. Diffie–Hellman is a common example. 
* **Elliptic-curve cryptography** (ECC): an approach to PKI based on the numeric structure of elliptic curves over finite fields. ECC is useful as it requires smaller keys compared to non-ECC cryptography. There are many variants of ECC used including Edwards-curve Digital Signature Algorithm (EdDSA).
* **Hash or message digest**: one-way functions, such as SHA-256. A set of many one-way functions may be applied to a tree of data to form a Merkle Tree. 
* **Zero-Knowledge** (ZK): zero knowledge is defined above loosely as a set of practices where some data is revealed while other parts are kept secret. Many ZK methods are used in cryptography incuding Fiat Shamir, Proof of knowledge of discrete logarithms, ZK Snarks, and ZK Starks.
* **Accumulators**: a form of ZK, a cryptographic accumulator is a one-way membership function that answers a query as to whether a potential candidate is a member of a set without revealing the individual members of the set. Similar to a one-way hash function, cryptographic accumulators generate a fixed-size digest representing an arbitrarily large set of values. Some further provide a fixed-size witness for any value of the set, which can be used together with the accumulated digest to verify its membership in the set.  
* **Commitment**: a cryptographic commitment, which allows one to commit to a chosen value (or chosen statement) while keeping it hidden to others, with the ability to reveal the committed value later.
* **Witness**: a term that has different applications in cryptography. In this paper, a witness is a value used in a cryptographic accumulator. In Bitcoin the unlocking signature is called the "witness data." 
* **Quantum Computing** and Cryptography: as quantum computing is developed, it poses a threat to the difficulty of puzzles. For example, they are likely to be much faster at determining if a number is truly prime or not. 


## Correlation

From Identity Crisis
* Transitive Correlation
* Temporary Correlation
* Correlation Using Neither Identifiers Nor Consent
* Unwanted Correlation
* Spontaneous Correlation

* Quasi Correlation
* Ambient Correlation 


Old paper remains are below this line
=================================================

# Three Examples

Three examples of how people would like their privacy preserved in the process of sharing credentials help to illuminate these three techniques.

**Diego** attempts to use an online service and is asked to share his location in order to prove his geolocation. Diego hesitates, since the service doesn't need his location everyday, everywhere. He knows that the service may share this information with other parties without meaningful consent on his part. Thoughts pass through his mind: What location data does the service actually need? What will it read in future? Is there a way for him to share his location just this once, or to only share an approximate location? 

**Selena** hands her driver's license to a bouncer to prove she is of drinking age. As he looks it over, she sees him inspecting her date of birth and home address. He only needs to know that she is over 21. Is there a way to disclose that she is indeed old enough without revealing her actual age, along with her home address and city of residence as well? 

**Proctor**, negotiating with a real estate agent to purchase a home, reveals a letter from his bank stating his credit limit. He wanted to reveal its approximate amount only, but the agent insisted on verifying that the letter was authentic. Proctor feels the agent now has the upper hand in the negotiation, as the letter reveals more than just its authenticity. Could he have revealed only an approximate amount and reveal more details as the negotiations progress?

Each story features information that is verifiable: a home address, age, or credit limit. We call such information a credential, and a detail of a credential we call an attribute. We have three strategies for enhancing the privacy of digitally shared credential attributes, and each story highlights one. Diego's story highlights the need for "data minimization," Selena's for "selective disclosure," and Proctor's for "progressive trust." Let's examine each one in detail before discussing enablers. 



# Three Solutions

We now return to our opening examples, apply the privacy preserving strategies and enablers described, and describe the improved outcomes. 

The online service that **Diego** uses does an internal policy review and realizes (a) it only needs a location when a user signs up for an account, and (b) it does not need an exact address, only the county district. It changes its interface to request a Verifiable Credential for Diego's location. Diego's system creates this credential for him, which can be inspected to reveal the county district. The crypto to enable this would be similar to that described in Appendix C. With this data minimization, the online service has less risk of violating data protection rules, is less a target for hacking, and has lower overall costs, while at the same time preserving Diego's privacy. 

The bar seeking to verify **Selena**'s age uses selective disclosure as built into the Verifiable Claims system. Selena will no longer share her date of birth. Instead, Selena creates a secret that we harness to craft a crypto-formatted credential. This crypto makes it easy to verify her age, but difficult to determine her exact date of birth. The bouncer's system can perform a zero-knowledge proof to determine the credential is valid and that Selena is older than twenty-one, without revealing her birthday or her secret. The bouncer sees she is over twenty-one without seeing her date of birth, residence address, or any other unnecessary information. In Appendix C we show the process step-by-step. 

The real estate agency working with **Proctor** implements a data model specifying what is required at each step of the real estate negotiation. The first step requires only proof of being an account holder in good standing at a known bank, so Proctor does not have to reveal the detailed letter at this point. As their negotiation continues, Proctor reveals more and more information as required. Some steps of the process may share Verifiable Claims encoded with crypto. 


# Appendix A: Definition Sources

This section contains definitions we curated, based on research and oral interviews, to create the definitions of data minimization, selective disclosure and progressive trust. 

## Data Minimization
Definitions of data minimization that we considered in the formation of our definition above. 

* GDPR Rec.39; Art.5(1)\(c\) definition: “The personal data should be adequate, relevant and limited to what is necessary for the purposes for which they are processed. This requires, in particular, ensuring that the period for which the personal data are stored is limited to a strict minimum. Personal data should be processed only if the purpose of the processing could not reasonably be fulfilled by other means.”
* Reducing your overall footprint of data outside of your control. Can be accomplished by using selective disclosure. 
* Adequate, relevant and non-excessive.
* Reducing the amount of data you are sending in a payload to only the one ... needed. That prevents leakage of confidential information.
* Providing people with the information they need without revealing non necessary info. If I need to prove if I am old enough without revealing an actual birthdate.
* Best practices – your should deeply inspect your use case and come to a conclusion as to what is the minimum data you need to accomplish your goal. Don’t be greedy. Data has proven to be toxic.
* Mathematical – finding a way to express the data that you wish as an equation related to the data you have.
* Minimizing the amount of data to achieve your goal or communicate what you need to.
* Designing systems to operate efficiently in order to maximize privacy.
* Choosing to only share the minimal amount of data about yourself or something during an interaction. 
* Trying to keep the amount of info that is being disclosed as limited as possible to the requirements of the vulnerability. The minimum is what ... will lead them to move to action. 
* Always happens in a context: a relationship where the two parties are considering interacting in some way. Sending only the signals that I want to send and that are needed by the other party, hem to interact with me in a particular 
* The least amount of data needed for a system to function
* Collecting the least amount of date for the highest outcome. 
* Also known as minimal disclosure, data minimization is the principle of using the least amount of data to accomplish a transaction. This is incumbent on all three parties in an exchange. The holder should attempt to share the minimum. The issuer needs to create attributes designed for composition and minimal use, as opposed to monolithic credentials with all the data. The verifier needs to ask only for what they need. The motivation to minimize data is that unneeded data is potentially “toxic.” 

## Selective Disclosure

Definitions of selective disclosure that we considered in the formation of our definition above. 

* Ability to decide what info you give and how it can be used.
* Smart disclosure, allows [selecting] what information to give based on logic. 
* Blind search. You can decide who gets to see what. 
* Means by which we achieve data minimization. Form of policies. Ability to mask attributes that you do not have to share.
* Relates to mathematical definition – the computational ability to reveal only parts of your data profile. 
* Act of communicating or revealing only what you intend to, and not any peripheric data
* Having granular control over the ways in which data is shared
* Is a pattern for user interfaces allowing people to choose what to share about them during an interaction
* Method for achieving data minimization where only certain signals are being shared and there is control of who it is being shared with. That control is never perfect. The communication channel matters.
* An entity having granular control on what’s revealed.
* The individual having the freedom to decide what to share, or the acquirer using data minimization approach requesting the minimum amount amount of data for the maximum impact

## Progressive Trust

Definitions of progressive trust that we considered in the formation of our definition above. Note that we included definitions of progressive trust and progressive disclosure as well. 

* Procedure for increasing revelation of relevant data as the communication proceeds. As we continue to communicate we decide to reveal more information. It becomes more generous as trust builds. 
* Being able to reveal more data as you need to given certain conditions
* Information is disclosed as needed when needed.
* You can choose to increase the amount of data you disclose over time as needed. 
* Taking as little vulnerability as possible at the beginning, then gaining information and becoming willing to take on additional vulnerability by revealing more information. 
* Trust is built through step by step interactions where we start making ourselves vulnerable in a very small way and we observe how this works out. Based on results we consider making ourselves further vulnerable or not. It is about increasing levels of familiarity and prediction making (I am better able to predict your behavior). 
* Releasing information as needed
* Escalation of the previous steps (data minimization, selective disclosure) in line with the value increasing. 
* Purpose binding is the auditable use of data, so I can audit the use of my data and determine that it was used for the purposes declared. Progressive trust is the feeling of assurance and safety that develops over time, based on a history of data used only for its bound purposes, and so based on this feeling a data holder will be ready to share more data or other data, if at some point in the relationship this other data is requested. 
* Trust is required when you depend on the actions of someone who you can't control. 


# Appendix C: Example Credential Implementation

The birthday of an individual is formatted into a verifiable credential, which can be inspected to reveal the age of the credential holder without revealing their birthdate. The flow described here is based on the developing Verifiable Claims standard of the W3C Credentials Community Group. It uses cryptography developed by Jan Camenisch, as implemented by Sovrin. 

This is a work in progress. Note that other types of crypto could be applied to achieve the same privacy preserving goals. 

## Communication Flow

The flow below may be copies and pasted into the [Web Sequence Diagram](https://www.websequencediagrams.com/) webpage to generate a flow diagram. 

### Verifiable Credential using Selective Disclosure
```sequence
participant Valid Time Oracle
participant Janet
participant ID Provider
participant Ledger
participant Bar

note over Janet:Prover
note over Bar:Validator

note over Janet,Bar: Preparation and Setup

note right of ID Provider:Infrastructure
ID Provider->Ledger: Define Schema (Name, Birthdate, Address)
ID Provider->Ledger: credential Definition (Pub Key, etc.)
ID Provider->ID Provider: Generate Prv Key for this credential
ID Provider->Ledger:Revocation Registry

note left of Bar: Prepare to accept credentials
Bar->Bar:Install Agent
Bar->Ledger: Check schema

note over Janet,Bar: Begin Use Case
Janet->ID Provider: Request ID
ID Provider-->Janet: ID will be issued as a digital credential
note right of Janet: Prepare to receive credentials
Janet->Janet: Install Agent
Janet->Janet: Prv Key Generate, Store
Janet->Ledger:Check Schema
Ledger->Janet:credential Definition
Janet-->ID Provider:Proof of Name, Birthdate, Address
Janet->ID Provider: Blinded secret
ID Provider->Janet: credential
Janet->Janet: Validate credential against credential Def

note over Janet,Bar: Janet goes to the bar
note left of Bar: Can Janet Enter?
Bar->Janet: Request Proof of Age
Janet->Valid Time Oracle: Get time
Valid Time Oracle->Janet: Time credential
Janet->Janet:Generate Proof (This person is over 21)
Janet->Bar: Provide Proof
Bar->Bar: Evaluate proof
Bar->Ledger: Verify on Ledger
Ledger->Bar: Verification
Bar->Janet: Come in

note left of Bar: Invite to club

Bar->Janet: Join loyalty club? (requires valid postal code)
Janet->Janet:Generate Proof (postal code)
Janet->Bar: Provide Proof
Bar->Bar: Evaluate proof
Bar->Ledger: Verify on Ledger
Ledger->Bar: Verification
Bar->Janet: Have Loyalty Card
```
