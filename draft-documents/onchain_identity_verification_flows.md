# On-chain identity proof verification design patterns: an evaluation of different strategies to inject digital identity into decentralized applications.

[![hackmd-github-sync-badge](https://hackmd.io/U25XEx75SAqLH4cfVBzNVA/badge)](https://hackmd.io/U25XEx75SAqLH4cfVBzNVA)


## Editors: 
- Juan Caballero ([Centre.io](https://Centre.io))
- Egidio Casati ([NymLab.it](https://NymLab.it))
- Robert Mao ([ArcBlock.io](https://ArcBlock.io))
- Martin Riedel ([identity.com](https://identity.com)) 
- Fabrice Rochette ([2060.io](https://2060.io))
- Andrea Scorza ([LTOnetwork.com](https://LTOnetwork.com))

## Abstract

On August 8th, 2022, the US Department of Treasury brought regulation against a decentralized application (dApp) for the very first time, by bringing the liability for interactions with OFAC-sanctioned entities to ALL ethereum wallets that interacted with the Tornando Cash on chain mixer.

This is a once-in-a-lifetime opportunity to leverage on-chain digital identity as a way to anticipate the regulation trajectory and unlock adoption of decentralized applications (including decentralized finance) with sophisticated compliance and reporting/auditing strategies.

In this paper we want to analyze different on-chain credential  / proof verification as part of a process for validating transactions involving digital assets (i.e. “DeFi transactions”).

Our analysis includes solutions with different privacy strategies, ranging from on-chain tokenized identities (i.e. “Soulbound Tokens”) to on-chain validation of Proofs derived from anonCreds.

This paper is intended for the following audience:
- Asset Originators / Minter / issuers
- Communities / DAOs
- Policy makers / Regulators
- dApp developers

This paper isn’t intended for asset holders and final users in general, as we expect they should benefit from sound regulation unlocking mass adoption via usability, while preserving on-chain privacy.


## Mapping the space of on-chain identity verifications

We grouped architectures into four high-level categories and analyzed them.  Here is a high-level summary of relative use-case fits and challenges.

## Public On-Chain Badges that represent off-chain verifications
Contracts can directly interpret on-chain badges to make decisions (Web 2.0 authentication or Web3 transaction authorization). This specifically can include information that is found within the Token itself. For example, all NFTs on a given blockchain containing a specific trait are allowed to execute an instruction on a specific smart contract. No additional calls to other data sources (elsewhere on-chain or off-chain) are required to accept or reject a transaction or make authentication decisions.

While multiple ERC draft standards are being used, these are generally referred to in the market and in blockchain discussions as access based on [Soul-bound Tokens (SBTs)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4105763) [1,2], i.e. an ERC721 without a transfer function badging the account.

### Diagram 
![](https://i.imgur.com/SRGnIWH.png)
https://swimlanes.io/d/KWnh1JOTh 


## Opaque On-Chain Badges that verify off-chain identities (trusted intermediary)

In order to minimize identifying information in relation to the public approach, one solution is to minimize the exposed information to a well-defined minimum. Access decisions are still made by a smart contract combining badge metadata with additional data fetched just before and submitted at time of decision, whether that additional data comes from: 
1. an API call from a dApp front-end to issuer or other intermediary, 
1. an oracle call, 
1. another smart contract, or 
1. A valid transaction signed by the issuer or other trusted intermediary and delivereddeliver via the wallet. 

In this approach, the additional call (which might be “expensive” computationally or in gas/transaction fee terms) is “validated” by the first, while the older data (status at time of issuance) is confirmed or updated (status at time of additional call). 

### Replayability 
Auditing and replaying transactions that involve a second data source pose real issues for these architectures– at a later time, the second-data source call needs to be verifiable and/or replayable. In some sense, the trust model and security model is the “worst of two worlds” of the two data sources.  For example,
1. An API must allow “historical queries,” i.e. the API call needs to be replayable and verifiable after the underlying state changes (which changes the trust model for some use-cases). One way of strengthening this replay on a technical level is to include current block_height in query and response. Historical query could also be protected or authorized per-wallet by an off-chain signature from the wallet, i.e. a CACAO session receipt.
1. Oracles must similarly maintain and verify historical state in the case of future replay.
1. Dependencies on additional smart contracts increase code-auditing surface and trust threshold.
1. If the second data source passes information to first transactions as an off chain transaction (a message that could be written to the chain by the first smart contract but is not executed), the first contract needs to somehow store and access this non-executed transaction for the entire flow to be replayable. 

### Diagram 
Simple Diagram for case #2

![](https://i.imgur.com/DHZ8pW8.png)
https://swimlanes.io/d/4221tERaE

## Blinded Off-Chain Proof Verified On-Chain 
Smart Contracts receive a ZK proof generated elsewhere (i.e. off-chain, in-wallet, in-dapp, etc), which is verifiably derived from a previously issued (capable) credential. The proof is generated by the credential holder within the bounds of the ZK framework, proofing one or more predicates and/or attributes about the credential against a static credential schema. A smart contract receives the given proof and verifies its correctness (against the same credential schema) and determines if the transaction can be effectively processed or not. This is often referred to as an “Anonymous Credential” (because it relies on a correlation-resistant credential of the same name) or, more precisely, as a “Fully pseudonymous proof” because it links an anonymous credential to a pseudonymous identifier (i.e. a blockchain account). 

### Diagram 
![](https://i.imgur.com/qD3Wq0q.png)
https://swimlanes.io/u/TukH4NaJU

## P2P Off-Chain Verification
Alice wants to send funds to Bob. Alice sends Bob a signed transaction authorizing a transfer to Bob. Before deciding whether or not to forward this valid transaction to the Asset Smart Contract, Bob would like to validate Alice according to some criteria. Bob requests a proof against that criteria (or Bob already received it with the authorization). Bob verifies proof to determine if he will send Alice’s transaction to the chain and thus accept the transaction. This use case applies when Alice would like to verify funds paid back by a decentralized service.

### Diagram 
![](https://i.imgur.com/kxV6kDT.png)
https://swimlanes.io/d/rVMZY7dTb 

## Terminology
Because the solution space for the same problem is fresh and terminology is still shifting, it is important to align to a common nomenclature within the scope of the analysis. This will be defined below.


#### Credential Issuer
- AKA Issuer (context sensitive)
- Party that issues credentials to an holder (in these use-cases, the holder can be assumed to be the data subject)

#### Asset Issuer
- AKA Token Issuer / Minter
- Party responsible for a tokenized asset, i.e. an ERC-20 token

#### Trusted Credential Issuer
- AKA Trusted Issuer
- A credential issuer that is within the scope of trust defined for the protocol by a configurable element (out of scope) which the verifier uses to filter credentials.  I.e., a Credential Issuer trusted by a given consumer of credentials.

#### Decentralized Application
- dApp
- 1 or more front-end and 1 or more decentralized protocols such as on-chain smart contracts, IPFS, or P2P protocols, interact with deployed contracts and/or chain state

#### Gated Access
- Token-gating 
- Restrict access and/or provide exclusive content, right or membership.

#### dApp front-end 
- AKA Decentralized front-end
- A user interface that communicates with 1 or more decentralized protocols such as on-chain smart contracts, IPFS, or other P2P protocols

#### dApp Smart Contract
- AKA Smart Contract (Ethereum, EVM compatible L1, L2 chains),  - On-chain program (Solana), Chain code (Hyperledger), or similar concepts etc. On-chain component of a dApp, which executes business logic and results in on-chain state changes (e.g. a DEX contract, a lending protocol, etc.)

#### Asset Smart Contract
- AKA Token, Fungible Token, Non Fungible Token, Composite Token
- On-chain building block that governs ownership and transfers of an on-chain asset such as a stablecoin, an NFT, etc. These often predate and are separately controlled from dApp smart contracts

#### On-chain Badge
- AKA On-Chain Flag, Permissioned Token (Identity.com), Human-Bound Token (violet.co), Opaque Identity Token (KYCDAO), Passport NFT(ArcBlock)
- A verifiable onchain badge that makes some off-chain identity data verifiable.  Note that this has no relation to OpenBadges.

#### Gatekeeper
- AKA Gatekeeper (Identity.com) Verifier (Verite), White-lister (Aave Arc), Identity Oracle, Validator Node (ArcBlock), Proofi (LTONetwork)
- Enforcer of a “checkpoint” for actors in a system, in this case accounts in a pseudonymous asset system like a blockchain
 
#### Data Custodian 
- AKA Data Controller (GDPR), Identity Provider (OIDC), KYC Custodian
- Storer and controller of data needed to verify identity of an actor (can be internal or outsourced). Some wallets interact directly with a custodial data store (encrypted data vault, decentralized web node, personal data store, locker, etc) which can also be considered custodial, though more regulated custodians with complex authorization may be needed for some regulated use cases.

## Use cases 

- Regulated protocol would like to restrict or gated access to a smart contract (or even to a dApp frontend) to wallets that have been cleared against a predetermined wallet-controller criterion relevant to its regulators
    - Example criteria: Only wallets whose controllers have been KYC-onboarded by trusted KYC custodian can provide KYC information for a given transaction upon jurisdictionally unambiguous subpoena or other authenticated request
    - Real-world examples: Verite.id ecosystem issuers like Circle and Violet; KYCDAO  ; aka “KYC-gated DeFi”
- Allowlist/denylist for NFT mint events - Regulated criteria encoded as offline VC, checked before mint transaction
- Regulated protocol would like to restrict or gated access to a smart contract or a dapp  to wallets that have been cleared against a predetermined account-history criterion relevant to its regulators
    - Example criteria: “account has never transacted with Tornado Cash” or “account not flagged as suspicious by X, Y or Z machine-learning algorithm trusted by regulators”
- Tokenized security would like contract-level enforcement of wallet-holder requirements
    - Example requirements: wallet controller must be KYC’d or KYB’d with known jurisdictional competent authority and, if required, have verifiable affidavit of Investor Accreditation
    - Example enforcement mechanism: only transact SALES (or only transact TRANSFERS) to wallets that can deliver verifiable proof to the smart contract; 
    - Less popular enforcement mechanism: “interventionist” smart contract which can freeze, revoke, or seize asset held by non-conformant (or sanctioned) wallet aka“SEC accredited investor” (for fund raising) 


## Further Research Directions
- Composable verification systems: 
    - Egidio’s architecture where smart contract checks the information for example egidio showcased the idea of having the lower level smart contract checking the credentials, instead of the DApp
- API DDoS/AuthN model discussions, CACAOs
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



