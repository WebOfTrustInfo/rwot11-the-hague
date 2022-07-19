# Identity Bridge: Verifiable Credentials from European Digital IDs

Fabio Tagliaferro - [commercio.network](https://commercio.network/) & [University of Verona](https://www.di.univr.it/) (Italy)

*...inviting other Italian SPID Service Providers and European stakeholders to contribute!*

## Abstract

The principle stating that an individual (or a company, an object, an online entity...) should own and control their identity without the intervention of administrative authorities stands among the pillars of SSI [[1]](http://www.lifewithalacrity.com/2016/04/the-path-to-self-soverereign-identity.html).
Still, leveraging national / European identity systems as a source of trusted information is certainly a step towards SSI adoption.

*Identity Bridge* aims to leverage the power of national European identities to easily obtain SSI credentials.
We start from the Italian SPID ecosystem [[2]](https://www.spid.gov.it/) (some background is provided at the end of the page) but our approach can be adapted to other kind of European identities, and beyond.

The requirement for the *wanna-be-issuer* is being a **SPID service provider** with a public DID.
The *wanna-be-holder* is a **SPID user** selecting which attributes should be included in the wanted verifiable credential.
The issuance happens after user log in through the usual SPID authentication.
Potentially, the user could ask to include in the VC all the SPID attributes.
Then, perform presentations with selective disclosure of just what is needed, in a pure SSI data minimization fashion.

## Architecture

**(WIP)**

## Research questions

**(WIP)**

## Background: SPID

The *Public Digital Identity System* (SPID) is an Italian digital identity consisting of a pair of strictly personal credentials (username and password), with which it is possible to access online services of the public administration and private members [[3]](https://www.spid.gov.it/en/frequently-asked-questions/). 
This national digital ID reached (in July '22) the 30 million users milestone [[4]](https://www.biometricupdate.com/202205/italian-national-digital-id-scheme-reaches-30-million-users-milestone), that is, half of the Italian citizens can authenticate themself using any device with their digital identity. Most of the login forms in public service websites and apps have been replaced with the “Enter with SPID” bluish button.

### How is the SPID ecosystem composed?
Three different actors [[3]](https://www.spid.gov.it/en/frequently-asked-questions/):

1. **digital identity provider (or IdP)** are private entities authorized by *Agency for Digital Italy* (AgID) [[5]](https://www.agid.gov.it/en) for the creation and management of users' digital identities;
2. **service providers (or SP)** are public or private organizations, which by enabling access to their online services through digital identity allow fast, safe and secure use of services;
3. **users (citizens and businesses)** who have their own digital identity, certified by one or more managers, to access online services of the Public Administration and private members.

### SPID login

From a user perspective, logging in with SPID to a service provider looks something like this:
- choose among the list of digital identity providers the one used to create a SPID identity;
- use the credentials to access, usually with 2-factor authentication;
- check the list of attributes that should be revealed to the service provider, continue if everything sounds right;
- all done, the service provider could recognize the user and authorize access to the services.

## References

[1] [The Path to Self-Sovereign Identity](http://www.lifewithalacrity.com/2016/04/the-path-to-self-soverereign-identity.html)

[2] [SPID Italian Public Digital Identity System](https://www.spid.gov.it/)

[3] [SPID Frequently Asked Questions](https://www.spid.gov.it/en/frequently-asked-questions/)

[4] [Italian national digital ID scheme reaches 30 million users milestone](https://www.biometricupdate.com/202205/italian-national-digital-id-scheme-reaches-30-million-users-milestone)

[5] [Agency for Digital Italy](https://www.agid.gov.it/en)

