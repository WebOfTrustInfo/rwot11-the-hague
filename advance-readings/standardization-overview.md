# An Overview of all SSI Standardization

By [Maaike van Leuken](mailto:maaike.vanleuken@tno.nl) (TNO)\
Date: 26-07-2022

## Introduction
Various groups of people, such as [DIF](https://identity.foundation/), [W3C](https://www.w3.org/), [eSSIF-Lab](https://essif-lab.github.io/framework/), [Sovrin](https://sovrin.org/), etc. are working on standardizing SSI-related technologies. We see work being done that ranges from high-level concepts such as [guardianship](https://sovrin.org/library/guardianship-white-paper/), to models ([ToIP](https://trustoverip.org/toip-model/), [VC Data Model](https://www.w3.org/TR/vc-data-model/), [eSSIF-Lab mental models](https://essif-lab.github.io/framework/docs/essifLab-pattern-list)) to actual technology such as peer-to-peer protocols ([DIDComm](https://didcomm.org/)), [DIDs](https://w3c.github.io/did-core/), etc. Currently, it can be quite a task to figure out how one standard _x_ connects to another _y_. Can standard _x_ be used for SSI? Are standards _x_ and _y_ competing with each other? Is standard _x_ dependent of _y_? By making an overview of SSI-related standards and by making connections between the standards, these questions can be answered more easily.

## Making an Overview
Below you can see my first attempt to create an overview of the standards I have encountered so far, structured along the ToIP stack. The ToIP stack is divided into four layers, as can be seen on the right of the image. In **layer 1: trust anchors**, we have various technologies that serve as a trust anchor for the higher layers. The type of identifier (DIDs, link secrets, ...) and registry (blockchain, no blockchain, Ethereum blockchain, ...) influence the type of peer-to-peer protocol that is used in **layer 2: secure DID-to-DID connections** which in turn influences the choice of issuing or verifying protocol in **layer 3: data exchange protocols**. Whether one choice of technology influences another, how much and in what way is to be investigated. 
![standardisation-overview](media/standardisation.png)
This overview is not complete and it needs to be checked for correctness. I could use the help of the RWOT community to come to a correct and complete overview.
