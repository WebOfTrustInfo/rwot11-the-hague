# An Encrypted Data Vault Sprint
***by Manu Sporny, Digital Bazaar***

## Introduction

Encrypted Data Vaults (EDVs) enable us to safely store sensitive data online, such as Verifiable Credentials, trade secret documents, family pictures, and customer information. EDVs achieve this by encrypting and decrypting the
data on the client so that a service provider or an attacker can never see
the data in transit or at rest. This technology is particularly of interest
in a world where our data is searched, categorized, indexed, and then sold
to parties that may not have our best interests in mind.

This paper attempts to bring attention to the Encrypted Data Vaults 
specification in a way that moves it towards an official standards track 
activity by doing one or more of the following at Rebooting the Web of Trust
10 in Buenos Aries, Argentina:

* Write an EDV Primer.
* Write tutorials for EDVs.
* Review and raise issues against the specification.
* Add or prioritize Layer 1, 2, and 3 EDV features.
* Document how Encrypted Data Vaults use Authorization Capabilities.
* Implement a basic test suite and driver for EDV servers.

## EDV Primer

An EDV Primer would outline the problem solved and benefits of EDV 
implementations to a person that does not need to know the details of 
exactly how EDVs work. It could focus on the use cases that are solved by
using EDVs.

## EDV Tutorial

An EDV Tutorial would enable developers to create a did:key, create a
vault, create a document, update a document, and read the documents. This 
would provide developers with an accessible on ramp to using EDVs.

## Community Review of Specification

The Encrypted Data Vaults specification has not undergone extensive community
review. Given the number of participants at RWOT events, this would be a 
good opportunity to take interested participants through the specification
review process and have them log issues via Github.

## Add and Prioritize Features

There are a number of features that have been discussed over the past year
related to Identity Hubs and Encrypted Data Vaults. It would be useful to 
revisit those features and poll implementers and developers on their level of
interest with respect to each feature.

## Document Authorization Mechanisms

The core EDV specification does not specify an authorization mechanism, but
rather allows for multiple types of authorization mechanisms. There are at
least two implementations that use Authorization Capabilities (ZCAP-LD) and
it would be helpful to document how authorization is achieved using 
capabilities.

## Implement Test Suite

One of the things that is necessary when ratifying a global standard is 
establishing that there are interoperable implementations. A group of 
individuals might want to focus on the creation of a test suite at RWoT to 
check the functionality of existing implementations. Having a test suite will 
reduce the time it will take to get the specification through the standards
process.

## Conclusion

The current specification editors would like to form small teams of 2-4 
people that can make progress on as many of these items as possible during RWoT10. 

