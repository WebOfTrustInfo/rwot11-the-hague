## Building a Self-Issued OpenID Connect Provider (SIOP)

What is the smallest step towards adopting a system of decentralized credentials?

### The Authentication protocols of today

The standard for authentication and authorization today is OAuth 2.0 and its extension Open ID Connect (OIDC).
These are currently used by many applications on the web.

The fact these protocols have been used over several years and in many applications shows that they are useful.
Their continued existence demonstrates that they are sufficient for many usecases.
Developers understand them, or at least how to use them.

Importantly developers know to look for these protocols.
The majority may not care about about the details, e.g. why OAuth 1.0 got replaced with OAuth 2.0.
However, what is understood is that they can use them to solve Authentication and Authorization in applications.

So, developers' familiarity of these protocols is one of their strengths.
A downside is, in today's world, they are often used to further centralize the web.
In fact, social logins, a contract few understand, greatly extends the reach of these companies to track their customers around the web.

## The Authentication protocols of tomorrow

What if the privacy respecting applications of tomorrow could work within these protocols.
There would be less wheels to reinvent and adoption would be closer.

Specifically an application using OIDC to fetch a decentralized identity would be able to reuse much of the connecting infrastructure that exists now.
For example: OIDC client libraries.
Most ecosystems have OAuth and OIDC integrations.

So is it possible to build a compelling, decentralized identity system within the constraints of today's protocols?
To be compelling it must compromise neither security or convenience of the existing solutions.

## Self-Issued OpenID Provider

The OIDC specification supports the idea of a Self-Issued OpenID Provider (SIOP)[1].
Theoretically, therefore, the ability to issued decentralized identities exists within the current protocols.

The application that makes use of the identity from an OpenID Provider is the Relaying Party.
A key reason why a Relaying Party (RP) might offload it's authentication to an OpenID Provider is so they can delegate (some of) their security concerns to that service.

When switching to a SIOP, some of the security concerns that were previously delegated switch back to being the responsibility of the RP.

For example:

- email verification, a SIOP can add the claim of email and email_verified but their is no entity validating this to be true.
- spam accounts, a SIOP can issue as many identities as they want, there is no rate limiting.
- account recovery, what happens if a key is lost, is the identity lost with it?

These problems hold back the adoption of SIOP's, so it is sensible to ask if they can be fixed and how.
I believe the answer is yes and with minimal effort real benefits could be realised.

For example an email provider could issue a claim to the SIOP.
This claim could assert that the SIOP has an email with the provider.
The SIOP can now use this claim to authenticate with an RP.
The RP may still have to rely on the provider's assertion that the email check has been carried out.
But the holder of the SIOP and claim can use them to authenticate with the RP without revealing to the email provider when or where they are using the claim to authenticate.

This example doesn't require a fully fledged Decentralized ID (DID) ecosystem.
It has concrete benefits for the end user, like reduced tracking but while fitting in with much of the existing infrastructure.
The email provider is identified via DNS and the public signing keys it uses are at the `jwks_uri` endpoint that is already in existence as part of the OpenID configuration.

## Goals

The challenge I wish to explore is what are the smallest useful steps towards digital credentials.

For RWoT 10 I would like to discuss what would need to exist for businesses to add a Self-Issued OpenID Provider to the OAuth options they already support.
Having a button to select self issue next to the login with Facebook/Google buttons would at least offer another option.

- What service could provide the verified claims that make a SIOP useful.
- Can a secure SIOP be built in the browser?
- How does a SIOP have claims added to it?
- What organisation should host it?
- Do existing libraries support self issued as part of the OIDC spec.
- How do end users upgrade their SIOP to one of their own preference, for example one that creates a new identity for every Relaying Party.

(1) https://openid.net/specs/openid-connect-core-1_0.html#SelfIssued
