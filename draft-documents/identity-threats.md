# Identity Threats

**Authors:** Shannon Appelcline (Blockchain Commons), Kate Sills (DCD) Carsten Stöcker (Spherity), Cihan Saglam (Danube Tech)

## Abstract

Decentralized identity solutions, such as DID methods, tend to be designed to protect against certain attacks, but the purpose of that design is not usually explicitly stated in any architectural description or threat documentation. In particular, some DID methods have costly on-chain requirements. We can today see that these DID methods were purposefully shaped, but it's not clear why such decisions were made. The purpose of this paper is to list attacks on DID methods so that we can better understand what threats a system might be vulnerable to (or not).

Although we focused on specific DID methods, we believe these attack vectors are more general, even for systems not using DIDs. The goal is support engineers and developers who are developing decentralized identity solutions to safeguard their work and make it secure and compliant.

## Creative Brief

1. Who's your audience?

Engineers & developers.

2. What change in their behavior do you want to induce? (Call to Action)

If there are costly mechanisms within the mechanisms of a decentralized solution, there should be a reason for it, and an explanation of that reason. We hope this will encourage developers & engineers to think about & document that reasoning.

We also hope that this will expand to the next level, giving end-consumers explanations of why decentralized identity is important.

3. What are the key points you're going to include?

### Possible Table of Contents

I. Frame: Why Threat Analysis is Important
II. An Overview of Categories
   a. We're not trying to be comprehensive, just offering examples
III. Categories
   A. Example Threats, Mitigations, and Controls
IV. Why decentralization is important
V. Summary
   A. (The Elevator Pitch)
   
### Planned Attack List

1. The DID Creation Switcharoo [C]
2. The Poop-Emoji DID Doc [R]
3. The Scapegoat DID Identity [R of U]
4. The Prescient Mempool Attack [U]
5. The Dishonorable DID Deletion [D]

## Current Draft

Security, as part of the software development process, is an ongoing process involving people and practices, and ensures application confidentiality, integrity, and availability. Secure software is the result of security aware software development processes where security is built in and thus software is developed with security in mind.[^OWASP1]

Security is most effective if planned, managed, tested and controlled throughout every stage of software development life cycle (SDLC), especially in critical applications concering health, safety, regulatory compliance or critical infrastructures. Government agencies and industries such as travel and transport, energy, or defenese all adhere to formal and strict SDLC processes. 

A cousin of SDLC is Computerized System Validation (CSV) which is widely used in the Pharmaceutical, Life Sciences and BioTech industries. 

Both, SDLC and CSV, are focusing on the process of testing/validating/qualifying a regulated computerized system to ensure that it does exactly what it is designed to do in a consistent and reproducible manner that is as safe, secure and reliable. The state of validated software systems and their electronic digital records and signatures 
shall be maintained, tested and controlled throught the entire life cycle until the software is end of life and the retention priod is fully expired. 

These processes include the following activities:
1. System classification wrt/ legal compliance applicability and a risk-based classification with impact on product quality, saftey and data integrity
2. Creation of a test/validation/qualification plan based on the risk-based categorisation
3. SLDC requirement definition and implementation 
4. Formal test verification, quality assurance and documentation 

It shall be understood that there are multiple legal compliance requirements that effect validated software. Examples are: eIDAS, GDPR, GxP, HIPPA, or PCI. These compliance requirements are defining controls and non-functional requirements (NFRs). Common attributes of the NFRs shall be in scope of security testing[^wikisectesting]. These common attributes include
* authentication, 
* authorization, 
* confidentiality incl. data privacy,
* availability, 
* integrity, 
* attributeability,
* non-repudiation, and 
* resilience. 

The underlying theme of these attributes is 'digital decentralizsed' and non-functional requirements for identity govenance, signing, hashing, encryption, and key management/rotation. We would like to highlight that key rotation is a common non-functional requirement which was introduced years ago for encryption keys and which is now getting more and more importance when system engineers move towards signed data.

The emergence of decentralised identity technology will soon be a foudational part of secure and compliant software development and security testing. 

A critical part of security test planning is threat modeling. In threat modeling a data flow model is created and vulnerabilities among different software compents as well as internal and external system and human user interfaces are analyzsed. 

Such a data flow model touches all aspect of the digital identity system and its interfaces. 

This paper focuses on a subset of the data flow model of an identity system that is related to the data flow interations with creating, reading, updating and deleting (CRUD) of DID documents, decribes threat categories of DID-methods and determines their vulnerabilities. 

## Threats

### The DID Creation Switcharoo [C]

Keywords: DID creation, derivation from public key, malicous derivation code injection into an open source repo

NFR Attributes: authentication, authorization, integrity

Summary: secure PKI

High latency in identity updates, combined with the ability to foresee those updates, can allow an attacker to make changes in advance of a victim.

User Story: Anastasia is dark net hacker. She managed to get access to 'DID-Mania', a popular open source software repo for managing the DID life-cycle for a variety of different methods. When she got access she managed to inject a tiny piece of malicious code into the DID creation feature.

Quentin, a senior software developer at 'Quick and Cheap SW Solutions' loves the DID-Mania library, because it does all the DID management job for him. DID-Mania is integrated into all his signature Trustziod ERP suites he is selling  to Fortune500 companies.  

'Fortune favours the Brave' (F²B) is a global market leader in DeFI. F²B's success is built on a solid foundation of security, privacy and compliance. F²B is proud to be the first DeFi company in the world to have ISO 22301:2019, ISO/IEC 27701:2019, ISO/IEC 27001:2013 and PCIDSS v3.2.1 Level 1 compliance, and independently assessed at Tier 4, the highest level for both NIST Cybersecurity and Privacy Frameworks, as well as SOC2 compliance. 

F²B is using the Quentin's Trustziod ERP suite for many years. At a certain point in time Anatasia's malicous code wakes up when F²B derives a new DID for an 'Account Receivable' process from a public key that was created with F²B world class PKI infrastructure. 

But this time Anastasia's code does not apply the simple derivation algorithm. Her code replaces the output of the deviation function with a DID that is controlled by Anastasia. Few ours later F²B triggers the AR process using the new DID in one data field of a legacy invoicing protocol. 

Matt, a wealthy celebrity and happy F²B customer, parses the invoice message, resolves the (malicous) DID and sends his payment to Anastasi's fake payment endpoint. 


**Risks**

**Mitigation**

### The Poop-Emoji DID Doc [R] 
    
**Keywords:** duplicity, read
**NFR Attributes:** attributeability, availability, integrity

**Summary:** Web-based DID documents are obviously mutable over time, but they can also be mutable based on the location of a viewer, creating serious problems with integrity.
    
**User Story:** Mark is running for political office. He's a well-known business man, but he has no political experience. He'd do a lot better if he could obtain an endorsement from a polished politician!
    
Cliff Clipse is a politician without strong business experience. So he in turn could use an endorsement from a business man, and he knows that Mark would happily offer him an exchange. The problem is that he hates everything that Mark stands for. Fortunately, he has a plan to get an endorsement while cheating Mark out of his!
    
Cliff sets up a DID using a method that encodes its DID doc on a web server. He then extends [Moxie's trick of creating a Poop-Emoji NFT](https://moxie.org/2022/01/07/web3-first-impressions.html) to the DID world: his DID document looks different when viewed from Mark's IP addresses (those registered to his political campaign and seen in his email) and when seen by the rest of the world! He signs the endorsement for Mark with the key shown to Mark, but not to the rest of the world.
    
Mark is able to see the endorsement, so he stands by his own endorsement to Cliff. The rest of the world sees a different public key in the DID document, and so they don't think that Cliff endorsed Mark, and so he receives no advantage from it.
    
(Cliff ultimately wins his political race; Mark does not.)
    
**Risks:**

1. **Mutable Information.** Any DID method that doesn't in some way timestamp or otherwise record its DID doc is vulnerable to unauditable changes to the DID doc over time.
1. **Simultaneously Mutable Information.** DID methods that store their DID docs on web sites are vulnerable to further attacks, such as the ability to show different pages to different people based on location, individual identification, software, or other factors. This can cause considerable compliance issues by destroying attributeability among multiple parties.
1. **Centralization.** In a situation where everyone is served a different DID doc, no one can cross-verify information. This creates a _de facto_ centralized authority. It could even be done openly, making everyone beholden to that single source.
1. **Fake Identities.** DID docs that are simultaneously mutable can also allow the creation of fake identities, where a fake identity is presented to the world, but hidden from someone who would recognize that it is fake.
    
**Mitigation:**

1. **Hash DID Doc.** DID Documents can be hashed and that hash can then be stored in an immutable ledger, such as a blockchain. This allows anyone to verify the current state of a DID doc, and also provides timestamping of when it was last changed.               
    
### Don't Talk about Fight Club (unless you want to compare DIDs) [R of U]
    
**Keywords**: bad reputation, double-spend identity, canonical update
    
**NFR Attributes**: attributeability
    
**Summary**
    
If a malicious identity controller can tell a victim that they've updated their identity to a new DID (e.g rotated their keys in key-based DID methods) while still maintaining their original identity, they can ensure that any negative feedback from the victim uses the new DID as the subject, not their main identity, thus potentially preventing bad reputation from attaching to their main identity.

**User Story**
George joins Fight Club, an underground men's group. At first, he's thrilled to be included, but as time goes on, he realizes that Tyler, the leader, is abusive. He leaves the group, but that's not enough - he wants to warn others. He writes a negative review of Tyler with Tyler's DID as the subject of the review.
    
Unfortunately, unbeknownst to George, Tyler has split his identity into two parts: his main identity and a DID known only to George. From George's perspective, it looks like Tyler has merely rotated his keys. Tyler is able to do this because the DID method he is using (an imaginary method similar to did:key except that updates are allowed) does not require canonical updates. At any point, Tyler can rotate his keys and thus carry over his reputation to a new identifier, while keeping the old identifier. Each new member sees Tyler's good reputation, whereas each disgrunted Fight Club member's review is attached to a new identifier, which is afterward discarded.
    
Because no one in Fight Club talks about Fight Club to outsiders, the updates are not discovered by the general public.
    
**Risks**
1. **Hiding Bad Reputation**: Reputation usually requires collecting information from multiple sources about the same subject. However, if the subject is able to selectively use a different identifier, software that naively correlates only based on identifier (and not on the entity that is the subject) will miss the bad reviews. 
    
**Mitigations**

1. **Canonical updates, such as transactions on a blockchain:** If all updates for a particular DID must be recorded in a particular location where the updates are checked for contradiction, then the subject cannot split off a new DID specifically for bad reviews while retaining their original DID as their main identity. While the subject can of course maintain multiple DIDs from the very beginning, by enforcing canonical updates, we can at least prevent the victim from seeing the new DID as a recent update of the main identity, carrying over the main identities reputation.
2. **Canonical bindings of DIDs to real world entities:** For particular use cases, it might be appropriate for a new kind of DID method where the identifier is not random. In this case, the identifier matches the human-readable reference--for example, the business name or address of a restaurant is used as the identifier. However, this is similar to a "real name" policy, which takes away the ability of the subject to create multiple identifiers or identify by a different name than determined by authorities. Additionally, governance of the identifier namespace and vulnerability to spoofing attacks are problems with this approach.
3. **Petnames and Web of Trust:** A more decentralized approach is to share knowledge of identity bindings. For example, if the Fight Club members shared their nicknames (petnames) for the DIDs, they would have learned that George had a different identifier for Tyler. Moreoever, with a Web of Trust-style solution, George would be able to know that no one else acknowledged the DID he had for Tyler, because no one had signed over it.

### The Latency Cyberwar Attack [U] 
    
**Keywords:** timing, update
**NFR Attributes:** authentication, authorization,  availability, confidentiality, data privacy
    
***Summary:*** High latency in identity updates, combined with the ability to foresee those updates, can allow an attacker to make changes in advance of a victim.
    
***User Story:*** Victor is a system adminstrator working for OVER, a critical infrastructure company that provides energy for a large portion of a country. The private key for his identity has been compromised, and he doesn't know it.
    
The key has been compromised by Arthur, a spy for a nearby country. They've been using the private key to engage in data theft, such as accessing the blueprints to the entire energy system, making it vulnerable to directed attacks. 

Every six months, Victor rotates his key in accordance with compliance requirements. When he does this, following the theft by Arthur, Arthur is able to spot the rotation in advance because transactions for DIDs have latency (such as the mempool in Bitcoin). 
    
Arthur is able to push a key rotation of his own before Victor's rotation goes through, and takes total control of the identity. Because his key rotation will expose him, Arthur is now willing to engage in much more explicit attacks. He takes down the entire IT/OT computer network that Victor has access to, also darkening much of the grid. The foreign country immediately attacks, targeting the locations they've already discovered due to the previous data theft.

**Risks:**
    
1. **Frontrunning.** The latency of updates or deletions to an identity network can create the opportunity for frontrunning, where an attacker can insert their own transactions ahead of the victims.
1. [**Advanced Persistent Threat.**](https://en.wikipedia.org/wiki/Advanced_persistent_threat) Because the attacker has foreknowledge of when they would otherwise lose access to an identity, they can increase their dwell time and potentially do more damage for a more extended period before beginning to engage in more explicit attacks.

**Mitigations:**
    
1. **Pre-rotation with Update Keys.** If rotations are defined in advance with update keys, then an attacker cannot frontrun a key rotation. (This does not stop them from escalating their attacks during the latency period and presumes that the update private keys are actually secure.) Examples: `did:ion`, KERI.
2. **Reducing Latency.** An instant blockchain confirmation methodology would end any front-running and attack escalation by instantly changing the key without warning. Of course, not all latency is technical (such as mempools): a compliance policy such as one that requires rotation precisely every six months could similarly offer advance notice of likely rotation. Examples: instant blockchain confirmation methodologies.
3. **Hash Commitments.** Frontrunning can also be foiled through hash commitments which commit a transaction to a block without revealing it until a later block. Examples: Submarine Sends [[research]].
    
### The Dishonorable DID Deletion [D]

**Summary:**  Deactivation is a crucial DID operation. The ethereum-based method, "did:ethr", can cause serious problems when the implementation follows the spec. When a DID has never been updated via the registry, its deactivation can not be distinguished from its created state.     

**User Story:**

Carlos is an early adaptor of Web3 technologies; he is a big fan of Ethereum and follows the self-sovereign identity movement. He is on multiple DeFi and Metaverse platforms. When Carlos's software wallet starts supporting the "did:ethr" method, he starts adding this login option to the decentralized platforms where possible.
    
Vladik is a friend of Carlos. He was envious of Calos's Web3 assets and compromised the private keys of his Ethereum accounts of Carlos.     

Vladik starts by transferring the Shib tokens to his address. Carlos notices transactions that are not unauthorized by him. Carlos begins with damage control, in which he also deactivates his did:ethr to prevent the attacker from accessing the platforms. Since the software wallet implementation has followed the did:ethr specs, and there were no updates on Carlos's DID, deactivation is not registered on-chain.
    
Vladik tried front-running Carlos's accounts where login via did:ethr was used, and he could take control of those since the deactivated did:ethr was still resolving with its create state. 
    
**Keywords:** deletion, reputability
