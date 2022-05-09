# Quantum Secure DIDs

### How to make a given DID method post quantum secure with existing cryptographic primitives?

Author: Dr. Carsten Stöcker \([Spherity GmbH]("mailto:carsten.stoecker@spherity.com")\), Co-author (editor): Dr. Juan Caballero \([Spherity GmbH]("mailto:juan.caballero@spherity.com")\)

January 19, 2020, Düsseldorf, Germany

Keywords: decentralized identity, W3C DIDs, Digital Signatures, Key Rotation, Hash Functions, DAD, Key Event Receipt Logs (KERL), Key Event Receipt Infrastructure (KERI), Bitcoin P2PKH, Factorization, Hash Collisions, Quantum Computing, Cryptography

### Abstract

The cyberworld in which we spend our days — and on which our lives depend — is not safe and is becoming more dangerous all the time. From nation-states trying to sway elections with fake news to ransomware that shuts down hospitals, we are living in a \"**Wild West**\" in which any data, or any transaction, may be attacked at any time. And like travellers in a lawless frontier, we are left to scan the horizon constantly for trouble, scrambling to plug the leaks in defences we don’t quite trust.

We are vulnerable not just because of intelligent social engineering techniques, the increasing sophistication of hackers, who are today as likely to be well-funded criminal organizations or governments as petty thieves or amateurs out for the thrill of attacking an individual or an enterprise. Now even greater risk will materialize from the development of new offensive tools such as quantum computers, which might soon be powerful enough to crack many of today’s most widely used cryptographic ciphers. 

Today’s “world class” security is based on our (over)confidence in the math underlying our existing cryptographic primitives. This is inherently vulnerable to a mind like that of **Alan Turing**, whose singular brilliance proved decisive in breaking the German Enigma code in World War II [1]. Unfortunately, we don’t know how many big enterprises or governments are developing special-purpose (quantum) computers engineered to break existing ciphers. When such quantum computers become available (in years or even months), our digital identity systems will be significantly more vulnerable than they are now.

To address the risk of the advent of quantum computers for decentralized identity solutions, we propose to introduce a simple method using one-time signing keys and key rotation to protect our digital identity while using existing cryptographic ciphers for signing and hashing. This method shall allow us already today to prepare for the age of **quantum attacks on our identity infrastructure**. 

The objective of this paper is to describe a mechanism to protect DIDs using existing ciphers for signing during the transition phase to a fully post-quantum secure decentralised identity infrastructure. This mechanism is designed to support DIDs but its core is identifier-independent and DID:method-independent.  Analysis of quantum-resistant ciphers for signing and secure key management solutions for multiple keys are not in the scope of this paper, and assumed to progress in parallel.

### Background: Motivation for our work

When practical quantum computing finally arrives, it will likely power ways to crack the standard cryptographic ciphers for signing and encryption that safeguard our online privacy. The goal of quantum-computer engineering is to directly build qubits as physical devices that can efficiently and reliably carry out quantum operations. Thanks to “quantum error correction,” perfect reliability is not required.

Currently intractable computational problems that protect widely-deployed cryptosystems, such as RSA and Elliptic Curve-based schemes, are expected to become solvable in the **post quantum age**. This is why NIST has challenged researchers to develop a new generation of quantum-resistant cryptographic algorithms [2].

Many experts don’t expect a quantum computer capable of performing the complex calculations required to crack modern cryptography standards to become a reality within the next 5 to 10 years [3].  We all do not really know the special-purpose quantum developments of government crypto shops in Beijing, Fort Meade, Cheltenham, Langley, Moscow, Pyongyang or Tehran. And, we might be subject to the quantum threat even earlier than expected. 

As so much is at stake **– from personal safety, enterprise security to our civil order –** the cryptographer community is working on quantum resistant ciphers [4] [5]. The RWOT community shall stay ahead as well by getting solutions in place to protect the decentralized identity instruments we are all working on. 

### Cost analysis of factorization and hash collisions using Quantum Computers

Public-key cryptography has not only been at the centre of internet communication and online transactions for decades, it is also at the centre of RWOT’s decentralized identity work. 

With computing power growing at an exponential rate, some of the most widely used encryption schemes are starting to show their limits. Decentralized identity implementations are often based upon **intractability of certain discrete logarithm problems** such as ECDSA or Schnorr. 

Elliptic curve cryptography is vulnerable to attacks by classical and quantum computers. In the classical case, the most efficient algorithms have purely exponential running time. In the quantum case, however, there exists a variant of **Shor’s algorithm** which can solve the elliptic curve discrete logarithm problem through factorization in polynomial time [6].

Our paper is founded on the research of Daniel J. Bernstein and his work on the cost analysis of factorization and hash collisions using quantum computers [7]. It is based on the following conclusions of his work:
1) Quantum computer will be much more scalable than number-factorization hardware, and therefore much more cost-effective than number-factorization hardware. 
2) All known quantum algorithms to find collisions in hash functions are less cost effective than traditional cryptanalytic hardware, even under optimistic assumptions regarding the speed of quantum computers.
3) Quantum computers win for sufficiently large factorizations, but they do not win for collision searches.

The conclusion does not depend on the engineering difficulty of building quantum computers; it will remain true even in a world full of quantum computers. Within the space of known quantum collision algorithms, the most cost-effective algorithms are tantamount to non-quantum algorithms.  **Hash collision algorithms** should be implemented with standard bits rather than with qubits. If hash algorithms can be considered secure with regards to classical computing, they can be considered secure in the post quantum area as well.

We consider one-way hash functions such as SHA512 to be pre- and post-quantum secure.

### Inspiration from Bitcoin

Since Google announced that it achieved quantum supremacy [8], the topic of security of cryptographic systems in general and Bitcoin in particular is being picked up in a broader public debate [9].  Interestingly, Bitcoin is offering multiple address schemes for peer-to-peer transactions of which we compare two: 

**Pay to public key (p2pk):** This address type was the first instrument programmed into Satoshi’s BTC protocol. Since all transactions are public, anyone can obtain the public key and solve the factorization problem with a sufficiently powerful quantum computer to discover the private key in order to unlock a BTC wallet. 

**Pay to public key hash (p2pkh):** The address of the recipient’s wallet is derived from a one-way hash-function of the public key. The public key is not directly revealed by the address. It will only be revealed for the first time if the recipient signs and initiates a BTC transaction. This means that if BTCs have never been transferred from a p2pkh address, the public key is not known, and the private key cannot be derived using a quantum computer. When BTCs are transferred for the first time, the public key is revealed and the wallet cannot be considered quantum-secure any more.

An unused BTC p2pkh address can be considered quantum secure, i.e. it is impossible or many, many orders of magnitude harder – and therefore practically impossible – to derive the private key from a public key one-way hash compared with a situation where the public key is directly exposed. As long as I just have a wallet that was never used to transact BTC, a malicious actor cannot derive my private key, even with access to a theoretical quantum computer infrastructure powerful enough to calculate private from public keys.

### Making DID methods quantum-secure

Like BTC, Ethereum adopted the one-way hash function approach for creating an Ethereum Wallet address and DID method ETHR following the BTC approach respectively. Similar approaches are also adopted by other DID methods such as Sovrin. 

Using the Ethereum lightweight identity standard ERC-1056, a default (un-configured) DID document can be considered quantum secure. But when the DID document is configured, a blockchain transaction is signed and the public key is revealed. Unless the public key is deactivated by rotation, the DID document cannot be considered post quantum secure anymore.

The public signing key is also exposed when issuing a verifiable credential or signing a verifiable presentation. Reconceiving PKI infrastructure to minimize public key exposure would add significant complexity to all SSI systems.

DID C.R.U.D. mechanisms generally rely on the cryptographic primitives of the underlying DID method and DLT implementation (e.g. ECDSA in case of Ethereum). A malicious actor enabled by quantum computing could take control of a DID document by using the public key information. We therefore consider the respective private key as insecure in a post quantum world in both cases, regardless of whether signing happens on-chain or off-chain.

In order to mitigate a theoretical possible quantum-computing attack, we propose the following measures:
-	to register one-way hashed public keys as authorization attributes for all DID document operations, and
-	to simultaneously **deactivate and/or rotate** the public key hash used every time the respective public key is exposed either in on-chain or off-chain signing process. 

To enable a quantum secure DID method we propose to apply **key rotation** mechanisms after each on-chain or off-chain signing transaction. This approach is independent of the DID method implementation, which can either depend on anchoring DIDs on a blockchain or using a key-event receipt infrastructure (KERI) for creating verifiable, linked key rotation logs from a consensus of nodes [10].

KERI mechanisms do not depend on block confirmation times and are designed for efficient key rotation and pre-rotation. They are therefore a promising candidate for enabling a quantum secure DID that can combine a verifiable credential / presentation signing transaction and a key rotation transaction in their event log.

### Recipe for post-quantum secure DIDs 

Our proposed recipe to make DIDs quantum-secure with existing cryptographic ciphers is based on the following user journeys: 

#### 1. Initializing a new DID

As a user of DIDs and a new holder of a DID of which I am the subject or subject's guardian, I would like to initialize a new DID from high-quality entropy by performing the following steps:
* Generate initial public/private key-pair from high-quality randomness, preferably using a quantum random number generator (QRND [11]), and use that keypair to derive the DID identifier through a secure one-way hash function (e.g. SHA512 in multihash format)
* Generate **key pair tuples** for signing on behalf of the DID and performing key rotation operations
* Create and configure the genesis DID document or genesis key event log entry while simultaneously configuring one or more **public key pair tuples hashes**

#### 2. Signing Operations

As a user of DIDs and a holder of a DID's controlling private key, I would like to sign a transaction, credential or presentation and I do not want to be vulnerable to a quantum attack leveraging the disclosed public key.  I should:
* Sign DID-document or verifiable credential / presentation transactions with private key 1 of a key pair tuple
* Simultaneously sign key rotation transaction to deactivate with private key 2 of a key pair tuple in order to deactivate the public key pair tuple hashes.

Notes: 
* In the case of a DID-document transaction, the DID-document update and key rotation transactions can be signed with the same private key.
* In the case of a DID holder running out of unused key pair tuples for a given DID subject identifier, the holder might need to deactivate public key pair tuples hashes and to register new key pair tuple hashes at the same time.
* Simultaneous signing of credential (or presentation) issuance and key deactivation (or rotation) requires precision synchronization among the signing transactions and the issuing time stored in the credential (or presentation). Timing and security parameters should be considered with reference to the response times of the key rotation methods as well as the time needed to retrieve a private key from a public key through attack with a quantum computer.
* The mechanism described here can be nicely supported with KERI.

#### 3. Verifying a Credential

As an inspector of credentials, I would like to verify a verifiable credential or presentation. I should:
* Verify the expiration and the revocation information in accordance to the W3C standards and a relevant revocation method 
* Verify the issuing time of the credential as well as validity and deactivation time of the public key hash in the DID document and/or KERI event log.

### Conclusion 
Quantum computers win for sufficiently large factorizations, but they do not win for collision searches. Therefore, existing cryptographic primitives for signing can be considered as vulnerable to quantum attacks. Hashing algorithms can be considered as resilient against quantum attacks. These different vulnerabilities allow us to design methods for making DIDs much more quantum-secure while using existing cryptographic primitives. This approach can be considered for the transition period from existing ciphers being potentially vulnerable to quantum factorization to quantum resistant ciphers for signing. 

In particular, the KERI design allows cryptographic verifiable and very efficient key deactivation and rotation operations. We propose considering a more rotation-intensive paradigm for DIDs, particularly high-stakes DIDs like those used for natural person and legal person identities, as one method of quantum-proofing SSI infrastructure as whole. It may well make snese to embed the proposed method for enabling post-quantum secure DID as a standard mechanism in a KERI reference implementation. 

A more generic, standard definition might some day be considered for the W3C DID working group.

### References

[1] Wikipedia, Alan Turing, https://en.wikipedia.org/wiki/Alan_Turing
[2] NIST, G. Alagic et al, 01/2019, Status Report on the First Round of the NIST Post-Quantum Cryptography Standardization Process, https://nvlpubs.nist.gov/nistpubs/ir/2019/NIST.IR.8240.pdf 
[3] IEEE Spectrum, J. Hsu, 09/2019, How the United States Is Developing Post-Quantum Cryptography, https://spectrum.ieee.org/tech-talk/telecom/security/how-the-us-is-preparing-for-quantum-computings-threat-to-end-secrecy
[4] MIT, J. Wohlwend, 2016, Elliptic Curve Cryptography: Pre and Post Quantum, https://math.mit.edu/~apost/courses/18.204-2016/18.204_Jeremy_Wohlwend_final_paper.pdf
[5] Fraunhofer, R. Niederhagen et al, 10/2017, Practical Post-Quantum Cryptography, https://www.sit.fraunhofer.de/fileadmin/dokumente/studien_und_technical_reports/Practical.PostQuantum.Cryptography_WP_FraunhoferSIT.pdf?_=1503992279
[6] Cornell University, C. Zalka, 1998, Fast versions of Shor’s quantum factoring algorithm, http://arxiv.org/abs/quant-ph/9806084
[7] University of Illinois at Chicago, Daniel J. Bernstein, 08/2009, Cost analysis of hash collisions: Will quantum computers make SHARCS obsolete?, https://cr.yp.to/hash/collisioncost-20090823.pdf
[8] Google, John Martinis et al, 10/2019, Quantum Supremacy Using a Programmable Superconducting Processor, https://ai.googleblog.com/2019/10/quantum-supremacy-using-programmable.html
[8] Deloitte, I. Barmes et al, 2019 Quantum computers and the Bitcoin blockchain
https://www2.deloitte.com/nl/nl/pages/innovatie/artikelen/quantum-computers-and-the-bitcoin-blockchain.html
[9] Bitcoin Wiki, Bitcoin Address, https://en.bitcoin.it/wiki/Address
[10] Cornell University, S. Smith, 07/2019, Key Event Receipt Infrastructure (KERI), https://arxiv.org/ftp/arxiv/papers/1907/1907.02143.pdf
[11] Medium, C. Stöcker et al, 09/2017, Randomness: The Fix for Today’s Broken Security, 
https://medium.com/@cstoecker/randomness-the-fix-for-todays-broken-security-39ea7dc3a89b

