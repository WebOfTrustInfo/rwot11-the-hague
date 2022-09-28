# Demo Night

## TNO EASSI: An SSI Wallet Gatewawy

A gateway for SSI Wallets.

Solving the problem of: a large number of wallets.

Difficult for issuers and verifiers to support all the wallets!

EASSI connects to all the wallets and offers a simple API for issuers & verifiers.

## Data Exchange Agreements - Dexa Protocols

Solving two problems:

1. How to show compliance with GDPR?
2. How do individuals get auditable proof of data transactions?

* Issues credentials to a data wallet.
* As well as a Data Agreement Policy.
* Provides auditable proof that data was issued by company.

Can then share data, and can review clear history of what has been shared and to whom.

## SSI NFC Smart Contract Logic

Want to use NFC

1. As an alternative to QR Codes
2. Opens up use of NFC Smart Codes as alternative to Smart Phones

Smart Card as an SSI Hardware wallet.

The card contains own private/pubkey pair and so DID, can store additional credentials on card.
Can then _sign_ the prsentation for the credentials.

Thus, 2FA!

Right now mobile phone is necessary to create verifiable presentation; the next step is to allow that creation on the smart card itself.

## DID Connect

Inspired by Facebook Connect and OpenID.

UX user library.
Help developers to integrate DIDs, VCs, and Verifiable Presentations into applications.

Supports a wide variety of use cases.

## DID Science: DID Data Analysis

Analyzed which DIDs were being used at which times.

Analyzed DID document errors. (lots of them, mainly JSONld errors.)

Recognized some duplicate keys used to create DIDs.

## TRAIN: TRust mAnagement INfrastructure

Addresses trust & governance challenges
135 DID methods registered!

Allows for creation of Trust Lists and for organization to create Trust policies (or even use Trust policies from other people)

Depends on DNS.

## Trusted Issuers: Known Authority Lists

Allows governance for Known Authorities List through voting by Statekeepers, then SSI wallets retrieve that list.

Managed through an Ethereum Smart Contract.

## SSICOMMS: Identified Communications

Adding SSI to internet communications

In a telecomm session, asks if other person can do SSI (so backward compatible).
If so, can _verify_ each other!

## Trusted Crypto Asset

On-chain verifiers validate proofs to verify credentials

## Verifiable Credential Issuer Playground

We need _interoperability_

So released: chapi.io

CHAPI is Credential Handler API

The CHAPI playground lets you use a variety of wallets and switch among issuing backends

Support for VC API, soon support for OpenID

Demonstrates interoperability!

Community tooling that everyone here can use today!

## Image Hashing

Challenge: how to add an image into a verifiable credential.

1. Provide image out of band.
2. Verify image online
3. Use image hashing + machine learning
4. Solution works cross-substrate.

Image hashing caluculates a visual hash (32 bytes) of the image, and then that's embedded in VC! Then compare to hash of out-of-band image.

Shows comparison as a percentage.

Not biometric! It's image comparison!

## Rendering Verifiable Credentials 

Exploring idea of having a render property on a VC that says how to render VC in a specific media.

- Web-based Rendering (HTML, SVG, etc.)
- Video Rendering
- Audio Rendering
- Tactical Rendering

## SSI Credentials for Portal Login

SSI tech for authentication & authorization.

Read a QR, send back a credential!

SOWL allows for this integration

## Godiddy.com - Universal DID operations (eSSIF-Lab)

A hosted platform that makes it easy for SSI developers & solution providers to work with DIDs.

Only DIDs, not VCs

Things it can do:

1. Resolving & dereferencing DIDs
2. Creating & managing DIDs
3. Searching & tracking DIDs

## Blockchain Commons Interoperable Standards

Working to create bottom level interop standards for wallets

* Silicon Salons
* Blockchain Commons Specifications
   * Lifehash creates visual hashes
   * Shamir secret-recovery standards

Testing with NFCs

Big current project is seed-share storage (Collaborative Seed Recovery)







