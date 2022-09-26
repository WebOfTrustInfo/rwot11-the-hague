# An exploration into Verifiable Group Credentials

**By:** 
Lohan Spies (IOHK/DIDx) -- lohan.spies@iohk.io / lohan.spies@didx.co.za
**Date:** 21-09-2022
**Version:** 0.1

## Introduction

Group credentials are a feature that will be required in future to truly unlock verifiable credentials for more complex real-world scenarios.

The current verifiable credential trust triangle primarily focuses between three individual actors; issuer, holder and verifier. The trust triangle works well where we only have three parties in the trust relationship. However, some real-world use cases are more nuanced and require multiple parties to contribute to a single group credential.


## Why
Group credentials enable a  group of issuers to contribute to a single credential issued to holders. Holders won't be able to select which portion of the group credential to share and must present the group credential in its entirety.

For example, a group of issuers contributing to a group credential containing details of a holder's credit score or repayment history would require individuals to present verifiable credit repayment history to prospective creditors at the point of application for a loan or any other credit facility. Using the current verifiable credentials framework is problematic in this case since an individual can simply delete or choose not to share credentials that reflect poor repayment history.

To solve this, we would like to construct group credentials that ascribe to the following properties:
* Multiple issuers can contribute to a single credential
* Each issuer only has sight of the credential subcomponent that it issued and not the entire credential
* The credential holder can't delete or present only parts of the group credential. 
* The entire credential must be deleted or presented

## Example Use Cases

* A family wants a combined view of their expenditure. A family group is created, and transactional members’ transactional credentials are automatically accessible by the group
* Multiple parties contribute to a group credential representing a holder's credit score or payment history
* A group can be used to give multiple users access to a credit card and set daily spend limits per user
* Account recovery by using group credentials
* Health records can be issued by a group of medical service providers who are authorised to contribute to a health group credential
* A group credential to indicate multiparty property ownership
* Multiparty proxy proof of person group credentials

## Research questions

The following feature requirements provide input to the research question:

- Group DIDs
    - Create a group with multiple DIDs
        - Assign rights to members of the group
        - Assign rights to contribute to a group credential
        - Assign rights to revoke contribution in a group credential

- Issuer Groups
    - Contribute to a group credential according to defined rights
    - Ability to revoke issuer contribution to the group credential
- Holders
    - The holder can only present a group credential in its entirety
- Verifiers
    - Verification of a group credential against all contributing issuers in the group
    - Presentation of the entire group credential by holders

## Resources
[Verifiable Credentials Data Model](https://www.w3.org/TR/vc-data-model/)