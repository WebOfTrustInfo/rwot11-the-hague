# On-chain identity proof verification design patterns: an evaluation of different strategies to inject digital identity into decentralized applications.

[![hackmd-github-sync-badge](https://hackmd.io/U25XEx75SAqLH4cfVBzNVA/badge)](https://hackmd.io/U25XEx75SAqLH4cfVBzNVA)


## Editors: 
- Juan Caballero ([Centre.io](https://Centre.io))
- Martin Riedel ([identity.com](https://identity.com)) 
- Egidio Casati ([NymLab.it](https://NymLab.it))
- Robert Mao ([ArcBlock.io](https://ArcBlock.io))
- Fabrice Rochette ([2060.io](https://2060.io))
- Andrea Scorza ([LTOnetwork.com](https://LTOnetwork.com))

## Abstract

In recent months, a problem space has been roughly delineated and widely
discussed under the rubric of "on-chain web3 identity." Marketing imperatives
and the lack of familiarity with compliance and liability issues particular to
identity have largely muddied the waters in the solution space, however,
resulting in a reductive three-way rivaly between "soul-bound tokens",
verifiable credentials, and a loosely-defined "zero knowledge" solutions.
Working at a high level, we tried to identify a taxonomy that would be more
useful for mapping this solution space according to high-level patterns and
tradeoffs. 

We defined the problem space at the highest level thusly: various architectures
deploy on-chain artefacts to aid in the verification of claims about a wallet's
controller. From there, we tried to bucket these into patterns before
identitying strengths and weaknesses of each against a short, exemplary list of
use-cases. The goal was not so much *evaluating* these exhaustively, as any
evaluation should be more squarely grounded in more detailed use-cases and non-
technical requirements. Instead, we strove to identify traits inherent to each
high-level pattern that could lead to high-level fitness-for-purpose
evaluations, i.e. the "strengths and weaknesses" of each.

### Historical Context

On August 8th, 2022, the US Department of Treasury applied sanctions law as
directly as it could against a decentralized application (dApp), by bringing the
liability for interactions with OFAC-sanctioned entities to ALL ethereum wallets
that interacted with the Tornando Cash on chain mixer. This precedent rightly
inflamed concerns about the scope of national compliance, governmental
overreach, and protocol neutrality. 

This precedent presents a once-in-a-lifetime opportunity to leverage on-chain
digital identity as a way to anticipate the regulation trajectory and unlock
adoption of decentralized applications (including decentralized finance) with
sophisticated compliance and reporting/auditing strategies. The impetus for this
paper was largely to analyze different ways of verifying and consuming identity
credentials on-chain as part of a process for validating, gating, or accepting
transactions involving digital assets (i.e. “DeFi transactions”).  

That said, we re-scoped the paper a bit to include other use-cases where a
fundamentally pseudonymous, decentralized PKI system could be used to prove and
verify realworld claims without necessarily deanonymizing the user in the
transaction or outside of it.

### Methodology

Our analysis considered diverse solutions with different privacy strategies,
ranging from on-chain tokenized identities (i.e. “Soulbound Tokens”) to on-chain
validation of Proofs derived from correlation-resistant verifiable credentials
(based on the `anonCreds` system of zero-knowledge presentation).

This paper strives to be informative as high-level overview and introduction for the following audiences:
- Originators of on-chain assets, i.e. minters and issuers
- Resellers of on-chain assets or operators of marketplaces and exchanges
- DAOs and other on-chain communities tryin
- Policy-makers and regulators surveying technical possibilities for compliance frameworks for on-chain assets
- Developers of "decentralized apps" (dapps) and other on-chain applications

This paper isn’t intended for asset holders or end-users in general, as we
expect they should benefit from sound regulation unlocking mass adoption via
usability, while preserving on-chain privacy and good-faith implementation of
such compliance frameworks.

## Terminology

Because the solution space for this problem is fresh and terminology is still
emerging, it was important for our group to align on a common nomenclature
within the scope of the analysis. This summarizes our aligned usage:

#### Credential Issuer

- AKA: Issuer (context sensitive)
- Def: Party that issues credentials to a holder (in these use-cases, the holder can be assumed to be the data subject)

#### Asset Issuer

- AKA: Token Issuer / Minter
- Def: Entity governing or otherwise responsible for an on-chain asset, i.e. an ERC-20 token

#### Trusted Credential Issuer

- AKA: Trusted Issuer
- Def: A credential issuer that is within the scope of trust defined for the protocol by a configurable element (out of scope) which the verifier uses to filter credentials.  I.e., a Credential Issuer trusted by a given consumer of credentials.

#### Decentralized Application

- AKA: dApp
- Def: 1 or more front-end and 1 or more decentralized protocols such as on-chain smart contracts, IPFS, or P2P protocols, interact with deployed contracts and/or chain state

#### Gated Access

- AKA: Token-gating
- Def: Restrict access and/or provide exclusive content, right or membership to some kind of service. In the dapp/DeFi context, this can refer to "front-end gating" (access control in the browser to a web resource regardless of origin) or "back-end gating" (wallet checks done by smart-contracts on originating/signing accounts)

#### dApp front-end 

- AKA: Decentralized front-end, DeFi front-end
- Def: A user interface that communicates with 1 or more decentralized protocols such as on-chain smart contracts, IPFS, or other P2P protocols

#### dApp Smart Contract

- AKA: On-chain program (Solana), Chain code (Hyperledger), or similar concepts etc.  
- Def: A deployed piece of persistent code executing on a blockchain virtual machine environment, regardless of EVM-compatibility, L1/L2 structure, etc. This is sometimes modeled as the "on-chain component" of a dApp, which executes business logic and results in on-chain state changes (e.g. a DEX contract, a lending protocol, etc.)

#### Asset Smart Contract

- AKA: Token, Fungible Token, Non Fungible Token, Composite Token
- Def: On-chain building block that governs ownership and transfers of an on-chain asset such as a stablecoin, an NFT, etc. These often predate dApp smart contracts and are controlled separately.

#### On-chain Badge

- AKA: On-Chain Flag, Permissioned Token (Identity.com), Human-Bound Token (violet.co), Opaque Identity Token (KYCDAO), Passport NFT(ArcBlock), or Badge Token (Swirlds Labs)
- Def: A verifiable onchain badge that makes verifiable one or more claims made by an authoritative/known issuer minting/publishing those badges. Note that this has no relation to OpenBadges qua specified technical system.

#### On-chain Relationship Token

- AKA: Sismo token, ENS NFT, etc.
- Def: An opaque on-chain artefact identifying an account as having a relationship with an authoritative issuer, data custodian, etc. Unlike a badge token, these do not convey any claim about the bearer other than a relationship relative to the token's issuer, which has to be queried separately (via API, on-chain, or otherwise) for claims about the subject.

#### Gatekeeper

- AKA: Gatekeeper (Identity.com) Verifier (Verite), White-lister (Aave Arc), Identity Oracle, Validator Node (ArcBlock), Proofi (LTONetwork)
- Def: The enforcer of a “checkpoint” for actors in a system, in this case accounts in a pseudonymous asset system like a blockchain (whether UTXO-based, account-based, or some other)
 
#### Data Custodian 

- AKA: Data Controller (GDPR), Identity Provider (OIDC), KYC Custodian
- Def: Storer and controller of data needed to verify identity of an actor (can be internal or outsourced). Some wallets interact directly with a semi- or self-custodial per-user data store (encrypted data vault, decentralized web node, personal data store, locker, etc) which can also be considered custodial in a technical sense, although more mapping to a more regulated custodial actor via complex authorization system(s) may be needed for some regulated use cases that specify legally the definition and obligations of a custodial role for data per se.


## Architecture A: Public Badge Token directly represent real-world claims (`badge-only`)

Contracts can directly interpret on-chain badges to make decisions (Web 2.0
authentication or Web3 transaction authorization). This specifically can include
information that is found within the Token itself. For example, all NFTs on a
given blockchain containing a specific trait are allowed to execute an
instruction on a specific smart contract. No additional calls to other data
sources (elsewhere on-chain or off-chain) are required to accept or reject a
transaction or make authentication decisions.

While multiple ERC draft standards are being used, these are generally referred to in the market and in blockchain discussions as "access/gating based on [Soul-bound Tokens (SBTs)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4105763) or Account-bound Tokens, i.e. an ERC721 without a transfer function interpreted as a badge representing a claim.

### Replayability 

Since all data is on-chain and fully public, all logic can be replayed or audited on-chain.

### Diagram 

![diagram of architecture A from https://swimlanes.io/d/EVjTr690X?e](https://hackmd.io/_uploads/r1X-8Ajai.png)



## Architecture B: Opaque Relationship Token triggers query to intermediary (`trusted intermediary`)

In order to minimize identifying information in relation to the public approach, one solution is to minimize the exposed information to a well-defined minimum. In this sense the access decisions are still made by a smart contract combining badge metadata with additional data fetched just before and submitted at time of decision, whether that additional data comes from: 
1. an API call from a dApp front-end to issuer or other intermediary, 
1. an oracle call, 
1. another smart contract, or 
1. A valid transaction signed by the issuer or other trusted intermediary and delivered via the wallet. 

In this approach, the later/just-in-time call (which might be “expensive” computationally or in gas/transaction fee terms) is validated along with the first; any claims implied by the relationship token (status at time of issuance) are not considered valid until confirmed or updated (status at time of last-minute query). 

### Replayability 

Auditing and replaying transactions that involve a second data source pose real
issues for these architectures: at a later time (long after transaction), the
second-data-source call needs to be verifiable and/or replayable, at least in
combination with on-chain records. In some sense, the trust model and security
model is the “worst of two worlds” of the two data sources.  For example,

1. An API must allow “historical queries,” i.e. the API call needs to be replayable and verifiable after the underlying state changes (which changes the trust model for some use-cases). One way of strengthening this replay on a technical level is to include current `block_height` or other ledger-time information in query and response. Historical query could also be protected or authorized per-wallet by an off-chain signature from the wallet, i.e. a CACAO session receipt.
1. Oracles must similarly maintain and verify historical state in the case of future replay.
1. Dependencies on additional smart contracts increase code-auditing surface and trust threshold.
1. If the second data source passes information to the smart contract validating or generating the gated transaction in the form of an off-chain transaction (a message that could be written to the chain by the first smart contract but is not intended to be executed), at least one of the two actors (data source and/or smart contract) needs to  store and access this non-executed transaction for the entire flow to be replayable, and both may need to store some kind of record identifier to insure end-to-end completeness of the records.

### Diagram 

![diagram of architecture B from https://swimlanes.io/d/3ZXqzGe0h](https://hackmd.io/_uploads/HJc8o8zTi.png)



## Architecture C: Blinded Off-Chain Proof Verified On-Chain 

Smart Contracts receive a ZK proof generated elsewhere (i.e. off-chain, in-
wallet, in-dapp, etc), which is verifiably derived from a previously issued
credential. The proof is generated by the credential holder within the bounds of
the ZK framework, proofing one or more predicates and/or attributes about the
credential against a static credential schema. (Note: not all verifiable
credentials are capable of and useful to these kinds of proofs; the VCWG has yet
to specified standardized data models for these credential schemata and
requisite credential proofing mechanisms such as per-property signatures, etc.;
for ongoing incubation work on protocols, see the [Applied Cryptography working
group at DIF](https://identity.foundation/working-groups/crypto.html),
[Blockchain Commons](https://github.com/BlockchainCommons/WIPs-IETF-draft-
envelope), and other community groups).

A dapp-specific smart contract receives the given proof and verifies its
correctness (against a known and/or static credential schema) and determines
whether the transaction can be effectively processed or not. This is often
referred to as an “Anonymous Credential” (because it relies on a correlation-
resistant credential rather than one authenticated by direct reference to a
static public identifier). The authors note that it would be more precise in
this use-case to refer to it as a “Fully pseudonymous proof” because it links an
anonymous credential to a pseudonymous identifier (i.e. a blockchain account).
Note the division of labor between application-specific verification (against
application-specific compliance requirements) in a distinct smart contract from
the underlying asset contract; this is typical of many regulated assets.

### Replayability 

The full pseudonymity of the proof presented to a verifier requires the verifier
to trust the ZK proof generation and the [potentially unknown] issuer of the
underlying credentials (depending on schema and proofing mechanism used). Since
minimizing logic onchain is often a constraint or design goal of these systems,
"trust establishment" (deciding which issuers are adequate at time of proofing
and/or at time of verification) may introduce an additional intermediary and/or
record-keeping obligation. Replaying the entire flow requires the proofing
mechanism and/or schema to include record locators (or at least routing
information on how to get the relevant records from the parties involved).

### Diagram 

![diagram of architecture C from https://swimlanes.io/d/8p8Ua7zK9?e](https://hackmd.io/_uploads/HyqiTLMps.png)



## Architecture D: P2P Off-Chain Verification

Alice wants to send funds to Bob. Alice sends Bob a signed transaction
authorizing a transfer to Bob. Before deciding whether or not to forward this
valid transaction to the Asset Smart Contract, Bob would like to validate Alice
according to some criteria. Bob requests a proof against that criteria (or Bob
already received it with the authorization). Bob verifies proof to determine if
he will send Alice’s accept the transaction and thus forward it on to the chain.
This use case can apply in many P2P use-cases, such as when Alice would like to
verify funds paid by a decentralized service, DAO, or other actor of unknown
legal organization or jurisdiction.

### Replayability

As in FATF use cases, fully P2P use-cases can be the hardest from which to
produce and guarantee adequate record-keeping. The authors remark that perhaps
per-user data stores or custodial services could conceivably emerge in the
coming years that process, store, and make queryable records of such off-chain
interactions and proofs.

### Diagram 

![diagram of architecture D from https://swimlanes.io/d/84YZKRttH?e](https://hackmd.io/_uploads/HJUHzPfaj.png)



## Use cases 

1. Regulated protocol would like to restrict or gate access to a smart contract
(or even just to a dApp frontend) to wallets that have been cleared against a
predetermined wallet-controller criterion relevant to its regulators
    - Example criteria: Only wallets whose controllers have been KYC-onboarded
    by a trusted KYC custodian
   - Real-world examples: Verite.id ecosystem issuers like Circle and Violet;
   KYCDAO; aka “KYC-gated DeFi”
    - Auditing requirement: some smart-contract interactions require all parties
    trusting/relying on a custodian to be able to query custodian for underlying
    PII in case of subpoena, etc
2. Allowlist/denylist for NFT mint events - Regulated criteria encoded as
offline VC, checked before by front-end at time of mint transaction
    - Example criteria: “account has never transacted with Tornado Cash” or
    “account not flagged as suspicious by X, Y or Z machine-learning algorithm
    trusted by regulators”
    - Real-world examples: see [guest Blog Post by Justin Hunter
    (Pinata)](https://verite.id/blog/NFT-allowlists-with-verifiable-credentials-
    and-verite)

3. Tokenized security would like contract-level enforcement of wallet-holder
requirements to guarantee ledger-wide compliance
    - Example requirements: wallet controller must be KYC’d or KYB’d with known
    jurisdictional competent authority and, if required, have verifiable
    affidavit of Investor Accreditation
    - Variant: only transact SALES (or only transact TRANSFER methods) to
    wallets that can deliver verifiable proof to the smart contract at time of
    any sale or transfer; enforced by EIP712 or other metatransaction/multisig
    mechanism requiring proof to be checked before transaction is accepted
    - Less popular variant: “interventionist” smart contract which can freeze,
    revoke, or seize asset held by non-conformant (or sanctioned) wallet aka
    “SEC accredited investor” (for fund raising) 

## High-Level Analysis & Conclusions

We grouped architectures into four high-level categories and analyzed them.  Here is a high-level summary of relative use-case fits and challenges.

### Use Cases Chart

|Use Case|Arch A|Arch B|Arch C|Arch D|
|:---:|:---|:---|:---|:---|
|1||||
|2||||
|3||||

### Properties Chart

|Architecture|How Reconstruct Audit Trail|Trusted Intermediaries|Simplicity|Implementation complexity|Flexibility|
|:---:|:---:|:---:|:---:|:---:|:---:|
|A|On-chain receipts + Issuer records|None|High|Low|Low|
|B|All parties (issuer+verifier) must be subpoenad/cooperate|Verifier must be trusted by relying party and wallet controller|Low|High|High|
|C|Issuer & Wallet Controller need to cooperate to reconstruct (poss. also circuit-building middleware)|Whoever combines ZK inputs into a "circuit" needs to be trust by all|Medium|Medium (depends on SDKs & middleware used)|Medium|
|D|Issuer & 2 Wallet Controllers need to cooperate to reconstruct|Routing/Messaging infra, possibly also proofing/dereferencing support for complex VCs|High|High (until DIDComm is more mature?) |High|

(Same info axis-flipped:)

|Properties|Arch A|Arch B|Arch C|Arch D|
|:---:|:---|:---|:---|:---|
|Audit Trail|On-chain receipts + Issuer records|All parties (issuer+verifier) must be subpoenad/cooperate|Issuer & Wallet Controller need to cooperate to reconstruct (poss. also circuit-building middleware)|Issuer & 2 Wallet Controllers need to cooperate to reconstruct|None|Verifier must be trusted by relying party and wallet controller|
|Trusted Intermediaries|Whoever combines ZK inputs into a "circuit" needs to be trust by all|Routing/Messaging infra, possibly also proofing/dereferencing support for complex VCs|
|Simplicity|High|Low|Medium|High|
|Implementation complexity|Low|High|Medium (depends on SDKs & middleware used)|High (until DIDComm is more mature?)|
|Flexibility|Low|High|Medium|High|


### Architecture/Use Cases Applicability

|Use Case|Arch A: Badge Token|Arch B: Identity Token + Intermediary|Arch C: On-Chain Verification|Arch D: P2P Verification|
|:---:|:---|:---|:---|:---|
|1|Fastest to implement|Most reasonable for compliance in today's EVM|Verification-capable VMs and business models emerging|
Best for single-jurisdiction/single-criterion minting contexts and E2E single-vendor use-cases|Somewhat unrealistic short-term|
|2|1:N relationship of badge token to verifiers difficult unless verifiers harmonize requirements/logic, which is currently very unrealistic|May be too complex for today's use cases, e.g. NFT market|May be too technically demanding for today's NFT industry and usecases|Depends on business & regulatory model of NFT mint context|
|3|Moving beyond API-based architecture may require as-yet theoretical tooling (i.e. Oracle connection to verifier/intermediary)|Good building block of a compliance-built-in stack/VM/etc|Possibly a good fit for FATF-conformant reporting, esp. for self-custody wallets, if FATF protocols enable P2P/self-custody solutions|

(Same info axis-flipped:)

|Architecture|Use case 1|Use Case 2|Use Case 3|
|:---:|:---|:---|:---|
|A: Badge Token|Fastest to implement|Best for single-jurisdiction/single-criterion minting contexts and E2E single-vendor use-cases|1:N relationship of badge token to verifiers difficult unless verifiers harmonize requirements/logic, which is currently very unrealistic|
|B: Identity Token + Intermediary|Most reasonable for compliance in today's EVM|May be too complex for today's use cases, e.g. NFT market|Moving beyond API-based architecture may require as-yet theoretical tooling (i.e. Oracle connection to verifier/intermediary)|
|C: On-Chain Verification|Verification-capable VMs and business models emerging|May be too technically demanding for today's NFT industry and usecases|Good building block of a compliance-built-in stack/VM/etc|
|D: P2P Verification|Somewhat unrealistic short-term|Depends on business & regulatory model of NFT mint context|Possibly a good fit for FATF-conformant reporting, esp. for self-custody wallets, if FATF protocols enable P2P/self-custody solutions|


## Further Research Directions
- Composable verification systems: Egidio & Nym are working on an architecture where general-purpose verification smart contracts can check credentials and/or proofs against passed configuration variables
- API DDoS/AuthN model discussions, based on [CACAO][] or otherwise
- Considerations of consent - mention Violet.co badge contract 
- “Non-consensual Airdrop” - many of today’s asset blockchains allow assets to be “dropped” into wallets without meaningful and/or verifiable consent. How non-consensual or non-verifiably consensual asset ownership or badging can be applied to these technologies should be considered

## References: 

- [Soulbound Whitepaper][SBT]
- [DeSoc Whitepaper][DeSoc]
- [How To Use Verifiable Credentials And Verite To Build An Off-Chain NFT Allowlist][NFTallowlist] (Verite docs)
- [Pre-print draft of Chainlink Labs Research on ZK Circuit-based Verification][defiZK] (iacr / Chainlink)
- [NFT metadata fragility][poopMOJI] (the verge)
- [MetaMask snap for VC/VP handling in crypto wallets][metamaskSNAP] (medium / BlockchainLAB UM)
- [Proof-of-concept for verifying VCs on-chain on EVM chains][EVMonchainVC] (Violet.co research)

[SBT]: https://vitalik.ca/general/2022/01/26/soulbound.html 
[DeSoc]: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4105763
[NFTallowlist]: https://docs.centre.io/blog/NFT-allowlists-with-verifiable-credentials-and-verite 
[defiZK]: https://eprint.iacr.org/2022/321.pdf 
[poopMOJI]: https://www.theverge.com/2021/10/14/22726556/signal-founder-moxie-marlinspike-nft-whim-change-platform-shit-emoji-fragility  
[metamaskSNAP]:  https://medium.com/@blockchainlabum/its-time-to-prove-your-worth-in-dao-ssi-using-metamask-snaps-part-2-3-17eb98678054
[EVMonchainVC]: https://twitter.com/RaphaelRoullet/status/1567553217915138048?s=20&t=wAj9fa4S3OoqJZukOm2Esg
[CACAO]: https://chainagnostic.org/CAIPs/caip-74


