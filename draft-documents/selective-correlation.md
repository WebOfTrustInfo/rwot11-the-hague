Selective Correlation 
==================================
***Data Minimization, Selective Disclosure, and Progressive Trust***

# To Do

* [ ] Enumerate and describe "capabilities" of various technologies, with regard to correlation
  * [ ] ASSIGNED @peacekeeper 
* [ ] Progressive trust
    * [ ] @Brent @ChristopherA 
* [ ] Use Cases
    * [ ] Educational @ChristopherA 
    * [ ] Healthcare @elenachachkarova
* [ ] Definitions
    * [ ] @fabtagliaferro
* [ ] @ChristopherA would like to see if we can explore WHY parties (in particular holders≠subject) are motivated to elide and otherwise protect personal data they hold, other than because regulators or a contract requires it. Such as to avoid legal costs (discovery, subpoenas, etc.), avoid competitive risks (employee poaching, front-loading transactions), etc. With this we might be able address positive incentives.
    * [ ] The is related to the concept of "non-designated holders" of verified credentials that received a VC, verified it, but also keeps it and could send it to yet another party. I currently am recieving spam mail offers for Holland events since clearly my airline has sold that I've arrived here.

# Authors

* Brent Zundel (lead author) - @brentzundel (GitHub), brent.zundel@gendigital.com, [Gen Digital](https://www.gendigital.com/)
* Christopher Allen - @ChristopherA (GitHub & Twitter), ChristopherA@LifeWithAlacrity.com - [Blockchain Commons](https://www.BlockchainCommons.com)
* Markus Sabadello - @peacekeeper (GitHub), [Danube Tech](https://danubetech.com/)
* Elena Chachkarova - @elenachachkarova (GitHub), [Nymlab](https://www.nymlab.it/#/)
* Fabio Tagliaferro - @fabtagliaferro (GitHub), [University of Verona](https://www.di.univr.it/?ent=persona&id=39578&lang=en), [Commercio.Network](https://commercio.network/)

# Selective Correlation

## Introduction

The goal of this paper is to enable decision makers, particularly non-technical
ones, to gain a nuanced grasp of correlation. We will explore the concept of
selective correlation, introduce a threat model, and propose a framework within
which policies such as Data Minimization can be successfully actualized. We will
strive to do so in plain English, but with some rigor. This will enable readers
of this paper to better understand correlation best practices, to adopt correct
approaches for their use cases, and to assess techniques that enable these best
practices.

## Corellation and Identity

Correlation lies at the heart of identity. The concept of identity cannot exist
without some obverver who identifies by correlating different data points about
the subject being identified, whether the subject is a person, group, or thing.
Thus Identity is correlation across contexts: the subject being identified is
recognized as the same subject from a different context. Therefore, control of
correlation is directly tied to control of identity, or rather, tied to control
of how identifiable the subject is.[?]

Correlation in and of itself isn't evil, or bad — it is a required function
of any identity system. However, corellation historically also has been misused
by adversaries to threaten or harm people.

To prevent that misuse of correlation, in the context of the self-sovereign
identity principles[?], when correlation is used to identify people, the power
to correlate must also be self-sovereign. That is, the power to correlate must
be, as much as possible, in the hands of the person being correlated, as the
relative risks to the individual is greater.[?]

In most systems, people have little control about what information they provide.
Much of the information that will allow them to be correlated lies outside of
their consent. In a self-sovereign system, people have more opportunities to
manage what data will be correlated.

## Correlatable Data

We define correlatable data as any data than can be used to identify a subject
across contexts. A context may be siloed, as when data is shared with two
different verifiers. Or it may be temporal, as when data is shared with the same
verifier over time.

We define an observer as an entity who collects correlatable data about a
subject. An observer may collect data directly from subjects, from the process
used to collect data about subjects, or from other observers. The more
correlatable data that is available, the easier it will be for an observer to
identify subjects without their consent. Therefore, a reduction in the set of
available correlatable data is necessary. To accomplish this we recommend in
general the practice of data minimization.

## Data Minimization

Data Minimization is the practice of limiting the amount of shared data to the
minimum necessary: just enough for parties to successfully transact, accomplish
a task, or otherwise meet a goal with each other, while minimizing risks to all
parties by omitting unnecessary content. 

Though essential as part of security best practices (along with
[Least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege), a
topic for a future musing), Minimimal Disclosure is, in particular, is mandated
practice for maintaining the privacy of people using digital identities and thus
requires special attention  when collecting and sharing, to curtail personal
information to only that which is absolutely necessary.

The best practices of Data Minimization guide the design and implementation of
personal data protection regulations, such as the General Data Protection
Regulation (GDPR) in the European Union. They include:

* Service providers must only collect the minimum amount of personal information
  necessary to perform a specific task or service.
* Service providers must imit the length of time personal information is
  retained and must delete it when it is no longer needed.
* Individuals should only share personal information with third parties when it
  is necessary to perform a task or service.

The GDPR supports these best practices by requiring companies to have a legal
basis for collecting and processing personal information and by giving
individuals the right to access, correct, and delete their personal information.
The GDPR also requires companies to implement appropriate security measures to
protect personal information and to notify individuals and authorities in case
of a data breach.

Other regulations that require some form of Data Minimization include:

* The California Consumer Privacy Act (CCPA) in the United States, which
  requires businesses to disclose the categories of personal information that
  they collect, use, disclose, and sell and also to obtain consumer consent for
  the sale of personal information.
* The Payment Card Industry Data Security Standard (PCI DSS), which is a set of
  security standards for organizations that handle credit card information and
  which requires merchants to limit the amount of cardholder data that is
  stored, processed, or transmitted.
* The Personal Information Protection and Electronic Documents Act (PIPEDA) in
  Canada, which requires organizations to collect only the personal information
  that is necessary for the identified purpose.
* The Health Insurance Portability and Accountability Act (HIPAA) in the United
  States, which requires healthcare organizations to protect the privacy of
  patient health information and to collect only the minimum necessary
  information to provide care.
* The Cybersecurity Information Sharing Act (CISA) in the United States, which
  encourages organizations to share information about cybersecurity threats, but
  also requires companies to protect personal information and to limit the
  collection of data to that which is necessary to address the threat.

In general, Data Minimization is enacted by policy decisions that limit the
amount, duration, and scope of data collection and use.

* **Content minimization (amount)** involves collecting only the minimum amount
  of data necessary.
* **Temporal minimization (duration)** involves retaining data only for the
  minimum amount of time necessary to execute the task.
* **Scope minimization (scope)** involves using data only for the specific
  purpose of the active task.

In the digital credentials ecosystem, data minimization is primarily implemented
through policy decisions made by stakeholders: credential issuers ensure that
credentials can be presented in a way that enables data minimization, and
credential inspectors establish policies in advance regarding the minimum data
necessary to accomplish a task, the minimum time data can be stored, and the
processes that ensure data is only applied to the task at hand.

Subjects may desire data minimization for various reasons, such as reducing the
risk of undesired correlation or providing information gradually
([Progressive Trust](https://www.blockchaincommons.com/musings/musings-progressive-trust/)).
Verifiers may also desire data minimization for other reasons, such as avoiding
appearing threatening, protecting from "I told you so" situations, avoiding
potential collection of "toxic" GDPR data, and reducing the cost of storing
information.

ISO (International Organization for Standardization) has several standards
related to data protection and privacy that include principles of data
minimization. Some examples include:

* **ISO/IEC 27001:2013 - Information security management systems (ISMS)**
  provides a framework for managing sensitive information and includes a
  requirement for organizations to minimize the amount of sensitive information
  that is collected, used, and retained.
* **ISO/IEC 29100:2011 - Privacy framework** provides a framework for protecting
  personal information and includes a requirement for organizations to only
  collect personal information that is necessary for the specific purpose for
  which it is being collected.
* **ISO/IEC 27701:2019 - Extension to ISO/IEC 27001 and ISO/IEC 27002 for
  privacy information management** provides a framework for managing personal
  information and includes a requirement for organizations to minimize the
  amount of personal information that is collected, used, and retained.
* **ISO/IEC 29151:2012 - Information technology - Security techniques -
  Data-at-rest protection** provides guidance for protecting data when it is
  stored and includes a requirement for organizations to minimize the amount of
  sensitive information that is stored.
* **ISO/IEC 27040:2015 - Storage security** provides guidance for protecting
  data when it is stored and includes a requirement for organizations to
  minimize the amount of sensitive information that is stored.

Data minimization can be challenging to implement due to a number of factors,
such as:

* **Difficulty in determining the minimum necessary data:** It can be difficult
  to determine exactly how much data is necessary to accomplish a specific task
  or goal, especially when dealing with complex systems and processes.
* **Balance of data minimization with other goals:** Organizations may be torn
  between the need to collect and retain data for legitimate business purposes
  and the need to minimize data to protect privacy and security.
* **Usage of data silos:** Data may be collected and stored across multiple
  systems and departments, making it difficult to identify and remove
  unnecessary data.
* **Lack of user consent:** Data minimization may not be possible if users are
  not willing to share their personal information, which can make it difficult
  to implement privacy-enhancing technologies such as selective disclosure.

## Selective Disclosure

"Selective Disclosure" is one of a number of privacy-enhancing techniques that
go beyond Data Minimization to also protect against correlation. Selective
Disclosure allows individuals or organizations to share only specific pieces of
information, rather than sharing all of them, and prevents using correlation
inappropriately to merge information from different contexts without consent.
Selective Disclosure offers approaches that balance the need to share
information for legitimate purposes against the need to protect the privacy and
security of people and to minimize risks. 

GDPR does not mandate the use of Selective Disclosure, but the GDPR does gives
individuals the right to control their personal information, the right to
access, correct, and delete their personal information, and the right to object
to certain processing activities. The California Consumer Privacy Act (CCPA)
also allows individuals to know what personal information is being collected and
shared and to opt out of the sale of their personal information.

In addition, some organizations have developed their own standards for Selective
Disclosure, such as the Platform for Privacy Preferences (P3P) which provides a
mechanism for websites to disclose their data collection and sharing practices
and for individuals to set their privacy preferences.

Some requirements for Selective Disclosure include:

* **Granularity:** Allow individual or organizations to share only specific
  pieces of information, rather than sharing all of their personal information.
  This enables users to share only the information that is necessary to
  accomplish a specific task or goal.
* **Control:** Give users more control over their personal information by
  allowing them to decide what information they want to share, and with whom
  they want to share it.
* **Transparency:** Allow users to see what information is being shared and with
  whom, which enhances trust and transparency in the sharing process.
* **Security:** Use cryptographic techniques to secure the information shared,
  ensuring that only authorized individuals or organizations can access the
  information.
* **Privacy:** Minimize the amount of personal information that is shared,
  reducing the risk of data breaches or unauthorized access to personal
  information.
* **Compliance:** Help organizations to comply with data protection regulations,
  such as GDPR, by minimizing the amount of personal data collected, used and
  retained.
* **Auditability:** Allow organizations to track and audit information-sharing
  activities, providing transparency on how the data is being used.
* **Flexibility:** Allow organizations to adapt the sharing process to different
  scenarios and use cases, providing necessary flexibility.

More specifically, Selective Disclosure can help address some of the challenges
of Data Minimization mentioned above:

*  **Difficulty in determining the minimum necessary data:** By allowing users
  to share only the specific information needed to accomplish a task or goal,
  Selective Disclosure can limit the data collection to only necessary
  information, avoiding additional information that is sensitive and potentially
  toxic.
* **Balance of data minimization with other goals:** By requiring granulatity in
  Selective Disclosure, the different goals of different groups can be evaluated
  and addressed.
* **Usage of data silos:** Selective Disclosure can help with data silos by
  allowing users to share information from different systems and departments
  while ensuring that only authorized individuals or organizations can access
  the information and that it is not shared or stored for longer than necessary.
  This can also help organizations to comply with data protection regulations
  such as GDPR.
* **Lack of user consent:** By giving users more control over their personal
  information, Selective Disclosure allows organizations to obtain user consent
  for information sharing in a more effective way. Users can choose what
  information they want to share and with whom, giving them control over what
  information an organization has access to. This can also increase trust and
  transparency between the organization and its users.

## Cryptographic Techniques for Selective Disclosure

Cryptographic selective disclosure leverages cryptography to allow individuals
to selectively share specific pieces of their information while keeping the rest 
of their information private. It allows parties to prove certain attributes
about themselves, without revealing their entire identity.

There are three important approaches to cryptographic selective disclosure: 

* "Hash-based Elision (or Redaction)": A hash is cryptographic fingerprint of a
  set of data — it takes an input and creates a unique output. In Hash-based
  Elision, one party (the prover) presents to another party (the verifier) a
  hash of a piece of personal information (redacts it), without revealing the
  actual information. One advantage of using cryptographic hashes for selective
  disclosure is that they are relatively simple and efficient method for hiding
  personal information, don't require complex mathematical calculations, and it
  doesn't require a trusted third party. A disadvantage of using cryptographic
  hashes is that without multiple round-trips they do not provide any
  cryptographic guarantees that the prover knows the original data (they may be
  just passing the hash forward). Another disadvantage is that there is a
  correlation risk if the same hash is given to multiple parties, which requires
  techiques like salting.

* "Zero-Knowledge proof (ZKP): This cryptographic technique allows one party
  (the prover) to prove to another party (the verifier) that they possess
  certain information, without revealing the actual information. This is done by
  allowing the prover to demonstrate that they know the information, without
  revealing the actual data. ZKP can be used to prove a wide range of attributes
  like knowledge of a password, possession of a private key, and membership of a
  group, etc. As compared to cryptographic hashes, ZKP is a method for proving
  knowledge of a subset of information without revealing the actual information
  behind it, while cryptographic hashes are a way to hide part of the actual
  information, but not the knowledge of it. A disadvantage of ZKP is that it can
  be computationally expensive, or requires a large amount of communication
  between the prover and verifier, both can be a bottleneck in certain scenarios
  where low latency is a concern or on constrained hardware.

* Blind Signature: As the name implies, this is a technique in which a signature
  is "blinded" before it is signed, hiding the identity of the signer. This
  allows the signer to prove that they possess a certain attribute, such as
  being over 18 years old, without revealing their name or other personal
  information. The signature can then be "unblinded" to reveal the identity of
  the signer. This makes it useful in scenarios where it is important to prove
  that a document has been signed by a specific individual without revealing
  their identity. One disadvantage of blind signatures is that they rely on a
  trusted third party, which can be a bottleneck and a centralization or
  security risk.

There are other possible approaches to leverage cryptography for selective
disclosure, but these are not as broadly being investigated today.

* Secret Sharing: This technique allows a secret to be divided into specific
  number of shares, sent to to parties, from which a specific number of shares
  are required (a quorum) to reconstruct the secret. A disadvantage is that
  restoring original secret requires one party to be entrusted to restore the
  quorum.
* Secure Multi-Party Computation (MPC): This technique allows multiple parties
  to jointly compute a function without revealing their inputs to each other.
  This solves the problems inherent to secret sharing, but at the cost of
  multiple rounds of interaction between the parties, and computational
  complexity.
* Homomorphic encryption: This technique allows computations to be performed on
  ciphertext, resulting in the same plaintext output as if the computation was
  performed on the plaintext. This y allowing computations to be performed on
  encrypted data without decrypting it first or revealing the actual data.
  However, these techniques are extremely computationally expensive (by multiple
  orders of magnitude).

====

## A Classification System for Correlatable Data
Using the context of a verifiable credential ecosystem, we classify data
according to its relationship to the subject. For this classification we imagine
the following system:

1. There are credentials, which contain **claim data** about a subject, e.g.,
  the claims contained in the `credentialSubject` property of a Verifiable
  Credential[^2]. Claim data may include things like a subject's name,
  identifier, or date of birth.
2. The credentials are created by an issuer. **Credential data** is data about
  the credential, e.g., the data in the `issuer` and `id` properties of a
  verifiable credential. Credential data may include metadata about the claims
  themselves, e.g., the value of the `evidence` property in a verifiable
  credential or some of the claims in the `credentialSubject` property.
  Credential data may be an identifier for the issuer, or the name of the doctor
  who delivered the child named in the birth certificate credential.
3. The credentials are exchanged by some protocol from the issuer to a holder,
  and from the holder to a verifier. **Protocol data** is data related to the
  protocols used to exchange credentials or make a presentation of them, e.g.,
  the `authorization_details` in OIDC4VC[^3] or `created_time` in DIDComm[^4].
4. The protocol operates upon some existing internet insfrastructure.
  **Infrastructure Data** is data related to this infrastructure, e.g., the IP
  address of the client device which receives the issued credential.

The classification uses examples from existing components to help illustrate and
clarify, but the intent for the classification to be generally applicable.

## Correlation

There are seven types of correlation:
* Desirable Correlation — the association between the party's datasets is
  necessary for the process, either for identification, authentication,
  authorization, or provenance.
* Risky Correlation - the association between the parties' datasets could be
  used against the benefit of the parties.
* Temporary Correlation - the correlation can be repudiated in the future
  easily.
* Transient Correlation - the correlation can be observed for a limited amount
  of time and thus is not permanent.
* Transitive Correlation - the observer correlates the subject indirectly, that
  is, without the subject being involved in the collection of data for example
  by passing a credential.
* Correlation Using Neither Identifiers Nor Consent -
* Quasi Correlation - correlation that is not certain, usually based on
  experience of the observer about particular characteristics of the data
* Spontaneous Correlation - 
* Unwanted or Ambient Correlation - the correlation can be observed from the
  environment where the subject is included, usually observing the (digital)
  footprint -> example:
  [Am I Unique - Learn how identifiable you are on the Internet](https://amiunique.org/)

TODO
* can it even be avoided?
* herd privacy: (see below) https://w3c.github.io/did-core/#herd-privacy &
  https://github.com/w3c/did-core/issues/539
* differential privacy (see below, but can we even do it\)
  https://privacytools.seas.harvard.edu/differential-privacy

# Data Minimization
Data minimization is the act of limiting the amount of shared data strictly to
the minimum necessary in order to successfully accomplish a task or goal while
minimizing risk.

[//]: # (@ChristopherA: Data Minimization is a privacy-preserving practice that
only reveals what is necessary and sufficient for parties to trust each other
and transact together to minimize risk.)

There are three types of minimization:

* Content minimization – the amount of data should be strictly the minimum
  necessary.
* Temporal minimization – the data should be stored by the receiver strictly for
  the minimum amount of time necessary to execute the task.
* Scope minimization – the data should only be used for the strict purpose of
  the active task. 

[//]: # (@ChristopherA: should we explain why for each these? herd privacy?
avoid potential collection of "toxic" GDPR data; ??)
[//]: # (@fabtagliaferro: GDPR added to verifier desires for data minimization
below, herd privacy explained in short definition below)

Data minimization is enacted primarily by policy decisions made by stakeholders
in the credentials ecosystem:
* Credential issuers ensure that credentials may be presented in such a way as
  to enable data minimization. This may require issuing multiple, related,
  granular sub-credentials. 
* Credential inspectors establish in advance policies regarding the data they
  will examine: 
	* what is the minimum data necessary to accomplish the task or goal?
	* what is the minimum time the data can be stored to execute the task?
	* what processes ensure that the data is applied only to the task at hand
      and does not, by a process of scope creep, become applied to other tasks
      or goals?

[//]: # (@ChristopherA: I'd love to see reasons that subjects desire data
minimization, and even better, when holders/verifiers ≠ subject desire data
minimization.)

A subject desires data minimization for various reasons:
* Subjects can wait to share some information and provide them gradually
  (Progressive Trust)
* Reduce the risk of undesired correlation 

A verifier desires data minimization for various reasons:
* Not appearing threatening (requesting unrelevant information will confuse the
  user and let him consider refusing to share any information at all)
* Protection from "I told you so" situations
* Avoid potential collection of "toxic" GDPR data
* Reduce the cost of storing information


Data minimization policies impact selective disclosure, the next privacy
enhancement.

## Definitions / Terminology

**Correlatable**: Data is said to be correlatable if by examining it that
there is a way to determine whether it is associated with sets of other data
stored elsewhere. This also includes lossy projections of the sets of data such
as deterministic hashes that demonstrate that assocation.

**Decorrelation**: A general term for any process that is used to reduce
correlation within data, or cross-correlation with other sets of data, while
preserving other useful aspects of the data. 

**Differential Privacy**: A decorrelation process for sharing information about
sets of data by describing the patterns of groups within the dataset while
withholding information about individuals in the dataset. The idea behind
differential privacy is that if the effect of making an arbitrary single
substitution in the database is small enough, the query result cannot be used to
infer much about any single individual, and therefore provides privacy. For
instance, adding a random number (say 4) from one part of the set and
subtracting 4 from another part of the set when the business purpose of the
data is total or average.

**Elide/Elision**: The term elide means "to leave out", and elision is the act
or instance of ommitting something. (Redaction is a related term

**Herd Privacy**: The decorrelation choices made by one set vs other data sets
may result in correlation. Herd privacy process ensures that this doesn't happen
by making them indistiguishable from other data sets.

**Non-correlatable**: If there is no practical way to learn whether a set of
data is a projection of a other data, they are said to be noncorrelatable.

**Nonce**: aka "Number Used Once". This is an arbitrary number that is used just
once in a cryptographic function such as signatures or encryption, to prevent
correlation. Note that this is not necessarly a random number, simply a number
that is never used again, and in some cases it can be quite valuable for a nonce
to be generated deterministically.

**Quasi-correlatable**: Between projections that are definitely correlatable and
definitely noncorrelatable, there are projections that may leak a little
information about their data. In particular (in no particular order), size,
order, use of particular formatting, date/time, location, algorithm usage, and
other identifiable patterns.

**Salt**: This is random data (values and length) that are used as an additional
input to a cryptographic function such as a hash of data, encryption, signature,
to prevent correlation.

## Capabilities and Techniques

### Elision
Elision is the ability of an individual to derive from a credential another
credential with some attributes removed. Stakeholders in the credentials
ecosystem enable elision capabilities in the following ways:
* Credential issuers negotiate with the holder to enable elision, by issuing
  credentials with a subset of attributes already included in another
  credential. 
* Credential inspectors ensure that the elided credentials can be verified with
  the usual procedure, but they won't be able to know if any kind of elision has
  been performed if they cannot correlate them with the starting credentials. 

### Selective disclosure
Selective disclosure is the ability of an individual to granularly decide what
information to share. Stakeholders in the credentials ecosystem enable selective
disclosure capabilities in the following ways:
* Credential issuers format the credential and its attributes in such a way as
  to enable selective disclosure. As with the strategy of data minimization,
  they may issue multiple, related, granular sub-credentials. Each attribute and
  the overall credential may be formatted to support cryptography, a capability
  described in more detail below. 
* Credential inspectors ensure the request is framed in such a way as to enable
  selective disclosure, using the cryptographic tools required. 

Once data minimization policies and selective disclosure are in place, the third
and last enhancement can be applied. 

### Progressive Trust
Progressive trust is the process usable by an individual to gradually increase
the amount of relevant data revealed as trust is built or value generated. 

To enable progressive trust capabilities, stakeholders in the credentials
ecosystem act in the following ways:
* Issuers format the credential(s) in such a way as to enable progressive trust.
  This may require issuing multiple, related, atomic sub-credentials. It also
  may require formatting the credential to support mathematical queries and
  cryptographic proofs. Finally, the issuer's data model may express how the
  various sub-credentials are related in a scenario involving progressive trust. 
* Inspectors ensure that requests are framed in such a way as to enable
  progressive trust. They structure the communication in order to to gradually
  escalate credential requests in order to enable a subject to progressively
  trust the inspector more and more, revealing the minimum data necessary to
  accomplish each step of the task or goal and revealing more and more as the
  mutual communication progresses. 

### Progressive Disclosure
Progressive disclusure is one of the possible ways for an individual to let the
progressive trust with another party proceed. The individual starts anonymously
and continues to provide information, recognizing that the more data is
revealed, the more risk that the other would be able to correlate. But with the
gained trust, the risk will be considered a benefit, instead.

To enable progressive disclosure capabilities, stakeholders in the credentials
ecosystem act in the following ways:
* Issuers format the credential(s) in such a way as to enable progressive
  disclosure. This requires issuing credentials that can be selectively
  disclosed multiple times. Each presentation will share attributes that have
  not been shared before. 
* Inspectors ensure that requests are framed in such a way as to enable
  progressive trust. This requires presentation protocols that can link together
  some previously made presentations, forming a progressive trust instance.

## Technology Characteristics

In this section, we can develop a list of technical characteristics with regard
to (anti-)correlation, and try to map how different technology choices can
fulfill them.

TODO:
- Maybe better differentiate between disclosure of data on various levels:
  credential, identifier, protocol, environment ("ambient correlation"?). On
  which layer does the (anti-)correlation happen, e.g. does it happen in the
  cryptographic signature, or on the identifier (DID) layer, etc.?
- How does salting fit in? Who does the salting?
- How do "sub-holders" fit in?

Characteristics:
* **[C1]** The Holder can selectively disclose data with a Verifier.
* **[C2]** The Holder can selectively disclose data with a Verifier, without
  requiring interaction with the Issuer during the disclosure process.
* **[C3]** The Holder can selectively disclose data with different Verifiers,
  without requiring interaction with the Issuer during the disclosure process.
* **[C4]** The Holder can arbitrarily choose which subset of data to selectively
  disclose with Verifiers, without requiring interaction with the Issuer during
  the disclosure process.
* **[C5]** When disclosing data to multiple different Verifiers, the Verifiers
  cannot correlate the subject via any single, unique identifier.

[//]: # (@ChristopherA: With Gordian, issuers can do to this, but not holders)

* **[C6]** When disclosing data to the same Verifier in multiple different
  interactions, the Verifier cannot correlate the subject via any single, unique
  identifier.
* **[C7]** The Verifier can verify that the Holder who is disclosing the data is
  the same entity that has received the data from an Issuer. *<-- Note: Maybe
  reference the work of the other RWoT11 group that's working on "holder
  binding"*
* **[C8]** The Holder can selectively disclose data that is derived (using
  predicates) from the original data they have received from an Issuer.

Choices:
* **[PLAINSIG]** Plain signatures: Ed25519Signature2020, RSA signatures, etc.
* **[SUBCREDS]** Issuing multiple, granular "sub-" credentials separately, which
  the Holder can then use as appropriate for interactions with Verifiers.
* **[SINGLEUSECREDS]** Issuing single-use "bearer" credentials intended to be
  used for a single interaction between a Holder and a Verifier.
* **[BBS2020-LD]** BBS+ Signatures 2020: https://w3c-ccg.github.io/ldp-bbs2020/
* **[BBS-SIG]** BBS Signature Scheme: https://identity.foundation/bbs-signature/draft-looker-cfrg-bbs-signatures.html
* **[ANONCREDS]** AnonCreds: https://anoncreds-wg.github.io/anoncreds-spec/
* **[SD-JWT]** SD-JWT: https://github.com/oauthstuff/draft-selective-disclosure-jwt
* **[JWP]** JWP: https://www.ietf.org/archive/id/draft-jmiller-jose-json-web-proof-00.html
* **[REDACTION2016-LD]** Redaction Signature Suite 2016: https://w3c-ccg.github.io/lds-redaction2016/
* **[MERKLE2021-LD]** Merkle Disclosure Proof 2021: https://w3c-ccg.github.io/Merkle-Disclosure-2021/
* **[COCONUT]** Coconut: https://arxiv.org/abs/1802.07344
* **[GORDIAN]** Gordian Envelopes: https://github.com/BlockchainCommons/Gordian/blob/master/Docs/Envelope-Tech-Intro.md
* **[GORDIAN-IETF]** IETF I-D (draft will be submitted December): https://blockchaincommons.github.io/WIPs-IETF-draft-envelope/draft-mcnally-envelope.html

Mapping of Characteristics and Technologies

| Technology      | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 |
| ---             | -- | -- | -- | -- | -- | -- | -- | -- |
|PLAINSIG         | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✓ | ✕ |
|SUBCREDS         | ✓ | ✓ | ✓ | ✕ | ✕ | ✕ | ✓ | ✕ |
|SINGLEUSECREDS   | ✓ | ✕ | ✕ | ✕ | ✓ | ✓ | ✕ | ✕ |
|BBS2020-LD       | ✓ | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✕ |
|BBS-SIG          | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ | ✕ |
|ANONCREDS        | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|SD-JWT           | ✓ | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✕ |
|JWP *            | ✓ | ✓ | ✓ | (✓) | (✓) | (✓) | ✓ | (✓) |
|REDACTION2016-LD | ✓ | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✕ |
|MERKLE2021-LD    | ✓ | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ | ✕ |
|COCONUT          | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ | ✓ |
|GORDIAN **       | ✓ | ✓ | ✓ | ✓ | (✓) | ? | (✓) | ? |

\* C4, C5, C6, C8 depend on the underlying JSON Proof Algorithm (JPA).

\** C5 can be done by issuers, but not holders. C7 can be achieved via
encryption techniques.

# Use Cases
[//]: # (We'd like to have a progressive set of use case to demonstration
desireable and undesirable correlation, but also avoid government focused
scenarios -- in particular the overused over-21 mobile driver's license example)

These use cases focus at their core a single credential, presented by various
parties to others, with desirable correlation as well as threats if undesirable
correlation occurs. An actual decentralized system probably has more trust
assurance, multiple credentials and more verifiable presentation metadata than
what is discussed below.

Educational / Professional Use Case:

The Educational Use Cases are drawn in part from
https://github.com/BlockchainCommons/Gordian/blob/master/Docs/Envelope-Use-Cases-Educational.md,
which was itself informed by discussions related to this paper.

1) DANIKA ENTERS SCHOOL: Danika, a citizen of the Czech Republic, desires
  comprehensive training in a highly paid building construction specialty:
  plasma welding. She applies to Czech-PAW, a professional trade school, and is
  accepted. Danika offers Czech-PAW a DID, and adds details such as a photo that
  will allow others to authenticate her using a Student ID. Students of
  Czech-PAW are also qualified to receive students loans from Raiffeisenbank,
  so Danika applies and receives a loan, and payments are deferred until she
  graduates.
    * TRANSACTIONS: Danika becomes a student of Czech-PAW. Danika receives 
      Student ID. Danika applies for student loan and pays for schooling.
    * DESIRABLE CORRELATION: Danika desires to be correlated as a student to
      attend classes and events, to get a loan to pay for classes, and to access
      other benefits such as student discounts.
    * CORRELATION THREAT: Danika might wish to keep her studies private from a
      current employer.
    
2) DANIKA GETS AN EDUCATIONAL CREDENTIAL: Danika (the subject) obtains
  comprehensive training from Czech-PAW (the issuer) on plasma welding,
  including a number of advanced techniques along with a variety of workplace
  safety topics. Czech-PAW issues an education credential to Danika (the subject
  & holder) with all of these details that confirm Danika has all the proper
  training and experience for this complex technical discipline.
    * TRANSACTIONS: Danika completes schooling. Danika finishes payment for
      schooling. Danika receives educational credential from Czech-PAW.
    * DESIRABLE CORRELATION: Danika desires to be correlated as a graduate of
      school and qualified for various job prospects.
    * CORRELATION THREAT: Danika may wish to keep her educational credentials at
      Czech-PAW separate from other educational credentials, lest the attainment
      of "blue collar" professional credentials be a barrier to other sorts of
      jobs.

3) EXAMPLE OF ELISION BY A DANIKA (SUBJECT/HOLDER): Danika moves to the United
  States, when she applies for a plasma welding gig at Erickson's Construction
  in New York. They require a workplace safety certification. Danika (the
  subject & holder) offers her Czech-PAW educational credential with details on
  the training and safety certification (the desired correlation as being
  qualified for the job) but elides her name and the name of institute, as she's
  learned from prior applications that revealing her Eastern European origins
  can cause discrimination. She can still prove ownership of the certification
  by signing with her DID, and she can still prove the accreditation of her
  trade school with EU-level certifications.
    * TRANSACTIONS: Danika applies for employment with educational credential.
    * DESIRABLE CORRELATION: Danika desires to be correlated as a qualified
      graduate and for her school to be correlated as a legitmate accredited
      school. 
    * CORRELATION THREAT: Danika does not wish to be discriminated against for
      his familial name or for the location of her school.

4) EXAMPLE OF PROGRESSIVE TRUST: Erickson's Construction offers Danika a
  temporary gig at a reasonable hourly rate, pending additional verification of
  identity at the workplace. Danika (subject & holder) presents her Czech-PAW
  (issuer) educational credential again, but this time with additional
  information (most notably, her last name!) so that Erickson's Construction
  (verifier) can issue a pass to enter the workplace and fill out a W2 for tax
  purposes. Danika must also provide certain United States tax credentials,
  including her Individual Taxpayer Identification Number (ITIN), to finalize
  that process. 
    * TRANSACTIONS: Danika receives offer, accepts offer. Gives ITIN, legal
      name.
    * DESIRABLE CORRELATION: Danika presents her educational credential again,
      with less elision, to satisfy workplace requirements.
    * CORRELATION THREAT: Danika's ITIN could now be correlated with her Czech
      origins if Erickson's were to misuse the information; Danika must trust
      they will not. Nonethless, this is a real threat that has emerged due to
      the need to use government identification that does _not_ support elision.

5) EXAMPLE OF ELISION BY A HOLDER: Erickson's Construction (holder≠subject)
  needs to prove to Three Towers Corporation (verifier) that they have
  sufficient number of qualified employees for a contract. They provide
  Danika's (subject) educational credential (already partially elided by the
  subject) to Three Towers but they further elide all of Danika's personal
  information, including her full name and picture, to obey regulations
  regarding the distribution of PII and more pragmatically to prevent poaching
  by other firms. Three Towers can verify that the school (Czech-PAW but elided
  by Danika) is accredited thanks to the EU-level certifications, but they don't
  learn anything about her individually. The same is true for other elided
  credentials that Erickson's sens to Three Towers.
    * TRANSACTIONS: Erickson's Constructions (holder) presents Three Towers
      (verifier) multiple elided employee educational credentials.
    * DESIRABLE CORRELATION: Erickson's Construction is able to repackage and
      further elide the credentials to provide correlation that they have
      sufficient and properly trained staffing, from accredited schools.
    * CORRELATION THREAT: Erickson simply wishes to prove the count of its
      accredited staff, not to reveal their PII to a third party, which could be
      correlated.
    
6) EXAMPLE OF HASH-BASED CORRELATION: Czech-PAW desires to renew their
  relationship with Raiffeisenbank to allow their students to continue to
  receive loans. To do so, they must provide information on their past and
  present students, such as Danika, so that Raiffeisenbank can assess that a
  sufficient number of their loan holders are graduating. However, under
  Europe's GDPR rules, Raiffeisenbank doesn't want to receive PII of
  non-loanholders, because it would be toxic. To resolve this problem,
  Czech-Paw produces a list of all of its graduates, all of its drop-outs over
  the last 10 years, and all of its students, but entirely elides each student's
  information, leaving behind only a hash derived from the student's PII.
  Raiffeisenbank can then create hashes from the PII that it already possesses
  for loan holders and compare that to the hashes in the elided lists. This will
  allow them to see which category each of their loan holders falls into,
  without either them receiving PII about non-loanholders or Czech-PAW receiving
  PII about non-students.

    * TRANSACTIONS: Czech-PAW (issuer) presents Raiffeisenbank (verifier)
      multiple elided student educational credentials. Danika's (subject)
      educational credential is one of those credentials, on the list of
      graduates.
    * DESIRABLE CORRELATION: Both Czech-PAW and Raiffeisenbank need to correlate
      educational credentials with loan holders.
    * CORRELATION THREAT: Raiffeisenbank wants to avoid accepting correlatable
      personal data of non-loanholders, while Czech-PAW wants to avoid accepting
      correlatable personal data of non-students.

7) EXAMPLE OF HERD PRIVACY USING HASH-BASED CORRELATION: Czech-PAW allows for
  remote learning for continuing education, focusing on safety instructions and
  updates to codes, regulations, and laws, none of which require hands-on
  training like its core offerings do. However, the lack of in-person
  interaction can create a somewhat less secure environment for the transmission
  of the PII used in credentials and the quantity of students involved can
  create administrative problems in the creation and maintenance of individual
  credentials. Czech-PAW has resolved both of these issues with herd-privacy
  credentials. When Danika logs in to the continuing education, she supplies a
  new DID. When she and other students complete the course, Czech-PAW then
  creates a massive credential that contains the continuing education
  information for all of the supplied DIDs. However, each DID is elided and
  replaced with a hash: students are given individual "paths" to their personal
  DID, which they can combine with that DID to prove that a specific hash
  belongs to them, demonstrating their continuing education. Danika ultimately
  chooses not to: immediately following the course, Czech-PAW is involved in a
  massive scandal involving gas ionization, and she fears it might damage her
  career prospects if she was known to be still involved with the institute.
  Fortunately, the structure of the herd-privacy certificate ensures that no one
  can know that Danika is part of the certificate unless she reveals it herself
  (not even Czech-PAW, if Danika used the best practice of providing a new DID,
  since her continuing education didn't need to independently correlate to her
  original training).

   * TRANSACTIONS: Danika takes a continuing education course. Czech-PAW
     (issuer) produces a massive but elided credential following the course and
     provides Danika with enough information to prove her presence within.
     Danika (subject) chooses whether to reveal that she is part of the
     certificate or not.
   * DESIRABLE CORRELATION: If Danika opts to prove her presence in the mass
     credential, it will correlate her continuing education to her existing
     credentials.
   * CORRELATION THREAT: However, the mass credential can also correlate
     Danika's continuing interactions with Czech-PAW, which she ultimately
     decides to avoid.

Healthcare Use Case:

1) ALEX STARTS A NEW JOB: Alex starts a new job at Company A and provides the
  Human Resources team at his new company with a DID to be issued an employment
  credential with his job positions and further details.
    * TRANSACTIONS: Alex becomes an employee of Company A and is issued an
      employment credential.
    * DESIRABLE CORRELATION: Alex wants to be correlated as an employee of
      Company A so he can get access to pension plans, employees' benefits and
      so on.
    * CORRELATION THREAT: 

2) ALEX SIGNS UP FOR A HEALTHCARE SERVICE PROVIDER: Alex joins a new healthcare
  provider. Alex can get a discount as an employee of Company A, due to a
  partnership between his company and the healthcare service provider. Alex
  presents his employment credential to the provider with eluded data.
    * TRANSACTIONS: Alex uses his employee credential to prove he works at
      Company A but eludes any irrelevant personal information.
    * DESIRABLE CORRELATION: Alex wants to be correlated as an employee of
      Company A.
    * PRIVACY THREAT: Alex does not want to share any further personal
      information with his new healthcare provider.

3) COMPANY A WANTS TO CHECK ON THE PARTNERSHIP WITH HEALTHCARE PROVIDER: Company
  A wants to check if the partnership with the healthcare provider is worth it
  to continue investing in. Company A requests data from the healthcare provider
  on the use of their employees.
    * TRANSACTIONS: Company A requests a data report from the healthcare
      provider.
    * DESIRABLE CORRELATION: Healthcare provider wants to correlate clients with
      employees of Company A.
    * CORRELATION THREAT: Healthcare provider does not want to accidentally
      reveal private information of their clients to Company A; Healthcare
      provider wants to only send data related to employees of Company A.

4) HEALTHCARE PROVIDER SENDS INFORMATION BACK TO COMPANY A: In order to reduce
   correlation, the healthcare provider decides to send back only the number of
   credentials with eluding of the employee's name so they can be sure to
   preserve privacy.
    * TRANSACTIONS: Healthcare provider sends data back to Company A with the
      number of clients that are verified employees of Company A without showing
      their names.
    * DESIRABLE CORRELATION: Healthcare provider correlates clients to be
      employees of Company A.
    * ELISION BY HOLDER: Healthcare provider eludes the names of the clients.
    
## Correlation Adversary from Smart Custody

![](https://github.com/BlockchainCommons/SmartCustodyBook/raw/master/manuscript/resources/image3.png)

***Motivation.** “I want information. I watch cryptocurrency transactions with
an eagle eye, ready to swoop in on any mistake. If you keep making the same
payments or receiving the same payments or using the same addresses, I’ll figure
it out. I want to connect the dots to determine who is spending cryptocurrency
for what, and I can figure that puzzle out if you give me enough pieces.”*

***Key Words:** Active, Technological.*

Cryptocurrency use is pseudo-anonymous and somewhat private. However, it’s not
totally so: it’s possible to build up correlation. Through statistical analysis
and through the discovery of accidental revelations, a third-party could tie
together an asset holder’s usage of various funds to paint a larger picture of
their finances and contacts.

***Abstract Case Study: Correlating over Coffee.*** Alice is sloppy with her
bitcoins and tends to use one address for everything. She goes out to buy a
coffee with bitcoins; while she sips away at the café, working at her laptop,
the barista notes the huge number of bitcoins going into the address. She
follows Alice home, planning larceny.

***Abstract Case Study: Correlating Identities.*** Carol uses the same online
identity on bitcointalk and on twitter. Eastern European hackers monitor
twitter, see her talking about bitcoins, track that back to bitcointalk, and
find wallet addresses mentioned there that reveal her bitcoin wealth. They then
set their scripts lose, hoping to break into her computer and steal her keys.

{pagebreak}

***Risks:***

1. **Funds Revelation.** An asset holder’s ownership of various funds can be
  revealed. This can make it possible to track what they spent funds on and who
  they’re associated with. It also puts them in greater danger from any number
  of other adversaries.
2. **Cascade: Censorship.** If they know who you are, they can block you.
3. **Cascade: Coercion.** If they know who you are, they can threaten you.
4. **Cascade: Legal Forfeiture.** If they know who you are, you can become a
  target for a nation-state or for a civil action.
5. **Cascade: Loss of Fungibility.** If funds have been correlated, they may
  lose fungibility.
6. **Cascade: Sophisticated Theft.** If they know who you are, you can become a
  target for thieves.

***Process Solutions:***

1. **Practice Anonymity.** Do not let people know you have bitcoins; ensure
  that you in no way ever link your key to your real persona.
2. **Practice Anonymizing Your Funds.** Occasionally use methods like CoinJoin,
  SendShared, or Zerocoin to anonymize your transactions. On Blockstream’s
  Liquid, always make use of Confidential Transactions.
3. **Practice Key Hygiene.** Follow the best practices of using different
  addresses for every transaction that you conduct. Each time you make a
  transaction with the same address, you are leaking information to your
  counterparty, which could be used to identify and either censor or correlate
  future transactions.


# Conclusion/Summary
TODO

[//]: # (We encourage policy makers to be awesome and do good, not evil.)

# Acknowledgements

We would like to acknowledge the following persons who contributed ideas that
helped define the ideas in and the shape of this paper:
* Adrian Gropper
* Joe Andrieu

We also acknowledge the contributors to
[the 2019 paper](https://w3c-ccg.github.io/data-minimization/):

* Lionel Wolberger, Platin.io
* Brent Zundel, Evernym/Sovrin
* Zachary Larson, Independent
* Irene Hernandez, Independent 
* Katryna Dow, Meeco
* Christohper Allen, Blockchain Commons

# References

## Related RWOT Advance Readings & Topics
* [Elision, Redaction, and Noncorrelation in Smart Documents](https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/advance-readings/elision-redaction-correlation-smart-documents.md)
* [Reducing Correlation: To What Degree is it Necessary?](https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/advance-readings/reducing-correlation.md)

## Links to other related documents
* [Engineering Privacy for Verified Credentials: In Which We Describe Data Minimization, Selective Disclosure, and Progressive Trust](https://github.com/w3c-ccg/data-minimization)
  (last updated Apr 12, 2022, released by W3C-CCG Apr 4, 2019)
* [Formalising Linked-Data based Verifiable Credentials for Selective Disclosure](https://ssr2022.com/slides/FormalisingLinkedDataBasedVerifiableCredentials.pdf)
* Recent PRs on [VC Data Integrity spec](https://w3c.github.io/vc-data-integrity/) in [W3C VC WG](https://www.w3.org/groups/wg/vc):
    * About unlinkability: https://github.com/w3c/vc-data-integrity/pull/52
    * About selective disclosure: https://github.com/w3c/vc-data-integrity/pull/53
* [Progressive Trust](http://www.lifewithalacrity.com/2004/08/progressive_tru.html)
  From Life With Alacrity by Christopher Allen 2004
* [W3C Credentials Community Group Home Page](https://www.w3.org/community/credentials/)
* Camenisch, Lysyanskaya. [An Efficient System for Non-transferable Anonymous Credentials with Optional Anonymity Revocation](http://www.cs.ru.nl/~jhh/pub/secsem/camenish2001idemix-clean.pdf)
* Pfitzmann, Hansen. 2010. [A terminology for talking about privacy by data minimization: Anonymity, Unlinkability, Undetectability, Unobservability, Pseudonymity, and Identity Management](https://www.researchgate.net/publication/234720523_A_terminology_for_talking_about_privacy_by_data_minimization_Anonymity_Unlinkability_Undetectability_Unobservability_Pseudonymity_and_Identity_Management)
* Cooper, Tschofenig, Aboba, Peterson, Morris, Hansen, Smith, Janet. 2013. [RFC6973](https://tools.ietf.org/html/rfc6973).
  The draft can also be helpful, "This document focuses on introducing terms
  used to describe privacy properties that support data minimization." 
* Hansen, Tschofenig, Smith, Cooper. 2012 [Privacy Terminology and Concepts. Network Working Group Internet-Draft Expires: September 13, 2012](https://tools.ietf.org/html/draft-iab-privacy-terminology-01)

## Citations
[^1]: [Identity Crisis: Clearer Identity Through Correlation](https://github.com/WebOfTrustInfo/ID2020DesignWorkshop/blob/master/final-documents/identity-crisis.pdf)
[^2]: [Verifiable Credentials Data Model](https://www.w3.org/TR/vc-data-model/)
[^3]: [OpenID for Verifiable Credential Issuance](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html)
[^4]: [DIDComm Messaging Specification](https://identity.foundation/didcomm-messaging/spec/)
