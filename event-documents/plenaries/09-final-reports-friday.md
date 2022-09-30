# Final Report Out

## Composable Credentials

A lot of VCs are enormous and combined, which require selective disclosure. So instead suggesting small, composable micro-credentials, which are all in the same format.

Have some working code to go with paper.

## Holder Binding

VC Data models don't express a way to presenter prove that they are the proper holders! 

Community process will be required for any changes to go forth!

## On Trust (The Codependency of Trust & Community)

Started out studying how trust is created. Looked at trust in different aspects of world: propose that community frames definition of trust. Then tried to deconstruct what it means for two individuals to build trust. Also built up "entrusted" as an alternative for "trustless", because "trustless" doesn't really mean what it says.

## Selective Correlation

Without desirable correlation, our software doesn't do its job, because identity is correlation(!) [per an RWOT2 paper]. So we need to describe desireable correlation (and thus "selective correlation").

## Identity Threats

Went through DID methods to find attacks or potential attacks. The goal is to encourage DID designers to think about these attacks. We chose to talk about five threats.

* The DID Creation Switcheroo
* The Poop Emoji DID Doc
* Don't Talk About Fight Club (Unless You Want to Compare DIDs)
* The Latency Cyberwar Attack

## Is My DID Method Ready for Endorsement?

If you're trying to evaluate DID methods, it can be difficult to evaluate methods, because it can be difficult figuring out what you care about.

## did:merkle

How can you use a merkle tree or a merkle root as an identifier? It identifies a _group_ and the group is what's in the tree! Proving group membership as part of participation. Doesn't provide group actions (like a threshold signature might), but you can prove you were in the set.

Have started with did:method and codebase. Will have a working example in Jupyter Notebook.

## Trust Lists

We need lists of entities who can be trusted, such who can be trusted to verify.

## Anoncreds Specifications

Putting Anoncreds from Hyperledger into specification, broken out from Hyperledger. Want to create data models that be used by different leder types.

## On-Chain Identity Proof Verification

Wanted to map heteregeneous solutions: cross-educational to described Web3 options with SSI terminology.

## Credential Format Comparison

Collaborative work that started out at IIW thanks to talk on "What's the Best Credential Presentation", and from there created a big matrix of 40 criteria for credential formats.

Also created paper on how to use the matrix, which is the actual paper for this workshop!

Will go into more details at IIW in November.

## Rendering Verifiable Credentials

How to display verifiable credentials through display hints.

Hope to send paper on to credentials community group.

## Scalable Multiparty Pairwise Communication 

Proposed a new mesh network with scalable onion-like routing.

Includes concept of broadcasters who make it easier to send widespread messages.

# Shared Patterns

What shared patterns have we seen?

* We're now using a shared language over DIDs and VCs that didn't exist in early RWOT events.
* Similarly, terms like "selective disclosure" have come into more common usage: fundamental tools that also weren't commonly used in early RWOTs.
* More focus on user experience, what are the edge cases, it feels like an evolution toward the end-user, going beyond the basics.
* Excited by cross-pollination of problems & solutions, with surprising answers coming out of work.
