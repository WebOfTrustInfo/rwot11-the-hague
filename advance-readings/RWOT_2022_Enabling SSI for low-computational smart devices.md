# Enabling SSI for low-computational smart devices
By: Caspar Roelofs, [Gimly](https://github.com/Gimly-Blockchain)

Date: 24th of August 2022

## Summary
*SSI in general and verifiable credentials (VCs) and decentralized identifiers (DIDs) specifically present major privacy and security benefits in managing, sharing and verifying data in the future cyber-physical world that merges digital and physical realities. However, a large part of current SSI effords are geared towards personal consumer identities and personal information that are contingent on the use of personal smartphones and internet. Meanwhile, the potential of implementing DIDs and VCs for physical objects, smart devices and IoT data which remains largely untapped. [^1] This paper aims to address what the major hurdles and potential solutions are to implementing SSI in a cyber-physical system that includes low computational devices and restricted data transmissions such as NFC smartcards and IoT devices (BLE trackers and sensors, LoRaWan sensors).*

## Background and literature
A major issue here is that many SSI protocols, such as DIDComm and DID resultions, are too computational and data heavy for the limited computational power of the devices such as NFC smartcards, BLE trackers or other IoT sensors and transmitters) and the low bandwith of the data transmission protocols (NFC, BLE, LoRa). Fedrechski et al. have proposed a low-overhead approach for self-sovereign identity in IoT, with an adapted did method and DIDcomm protocol for IoT devices (DIoTComm). [^2]

## Research questions
What 'realms' of identity subjects other than human and organizational identity are part of our worlds cyber-physical system?
What are the known requirements and limitations for these identity subjects in an SSI sytem?
What could be potential solutions to their restrictions such as limited computational power and data bandwidth?
What requirements need to be met for proposed adapted SSI components and protocols, such as DIDcomm and DIoTComm, to interoperate within an cyber-physical SSI system?

## References
[^1]: Fedrecheski et al. (2020). [Self-Sovereign Identity for IoT environments: a Perspective](https://github.com/Gimly-Blockchain/literature/blob/main/G%20Fedrecheski%20et%20al%202020_Self-Sovereign%20Identity%20for%20IoT%20environments%20-%20A%20Perspective.pdf).
[^2]: Fedrecheski et al. (2021). [A low-overhead approach for self-sovereign identity in IoT](https://github.com/Gimly-Blockchain/literature/blob/main/G%20Fedrecheski%20et%20al%202021_A%20low-overhead%20approach%20for%20self-sovereign%20identity%20in%20IoT.pdf).
