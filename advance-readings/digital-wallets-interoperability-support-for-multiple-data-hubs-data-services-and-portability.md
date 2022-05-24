# Digital Wallets: Interoperability support for multiple data hubs, data services and portability

Ron Kreutzer <<ron@pillarproject.io>>

## Abstract

Multiple data hubs/vaults/lockers will likely exist in a user's identity ecosystem, and digital wallets must be able to interact with a variety of storage providers as well as data services that act upon this data. A set of standards or operating principles need to exist to allow interoperability as well as portability that allow a user to swap digital wallet providers.

## Problem
Many projects are being developed that aim to give ownership and control of personal data back to individuals. These projects may be for a specific industry, such as medical records, or for a specific service model, such as monetizing the individual's consent for using their personal data in research or marketing. These include both commercial and open source endeavors, with various revenue and token models.

The issue is that from a user perspective, an individual may need to install multiple software wallets to use the set of personal data services that they desire.  From the business’ perspective, each company must develop software to collect, store and maintain each individual’s identity, and to manage verified credentials and consents.

A services business doesn’t build a website, and then build a browser for people to access that website. Currently, however, a business that provides a service on top of personal data must build a user interface with common functions such as identity, key and consent management. 

## Solution
Just like a user’s choice of web browser is based on features and device support, so could digital wallets be chosen by the individual based on ease-of-use, features and supported services.

The separation of the “data service” from the “data vault" and from the "digital wallet" can provide efficiencies to the data service business as they need not be concerned with the common user interface and identity management functions that are provided by the digital wallet. Further, individuals gain efficiencies by installing their favorite digital wallet and attaching data vaults and data services to it based on their needs. 

The logical separation of the underlying personal data from the data service and from the digital wallet is also needed. This separation would allow for multiple data services to operate on the same set of personal data, and allow data services to be swapped out, based on an individual’s changing needs. This separation would also allow digital wallet providers to be easily swapped, and provide incentives for the digital wallet companies to continue to innovate and integrate data vaults and data services into their wallets to create mass adoption.

## Conclusion
A method to allow data vaults and data services to easily integrate into digital wallets can bring efficiencies and mass adoption to the personal data ownership/control marketspace. Many of these standards already exist, and it’s a matter of packaging them into an open set of methods that such companies can support and adopt.
