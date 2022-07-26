# SSI and internet communications or internet communications and SSI: comparing different solutions to the same problem
By: Alex Blom, [Bloqzone](bloqzone.com)

Date: 24th of July 2022

*One of the things people enjoy the most about the internet, is that it enables them to talk to others remotely almost without limit. Unfortunately, remotely often means that parties are not sure who they are communicating with.
There are different solutions to this problem, and the ones offering identified communications by involving SSI can be differentiated by what they start from: is it SSI/DIDComm or an internet communications protocol.*

## 1. Adding SSI to internet communications in 4 steps 
One example of identified communications starting from a communications protocol is the project, [*“Adding SSI to internet communications”*](https://essif-lab.eu/adding-ssi-to-internet-communications-using-sylk-suite-by-bloqzone-b-v/), SSIComms for short, which is part of eSSIF-Lab. SSIComms makes use of DIDComm and of the SIP protocol, the protocol that underlies most VOIP telephony. The SIP protocol (and SSIComms) supports so called rich communications, meaning voice and video calling, chat sessions, desktop sharing, group sessions, etc. 
SSIComms enables the exchange of verifiable credentials by introducing a DIDCOMM session parallel to the communications session in 4 major steps:
1. First, Alice and Bob start a SIP session, for instance by Alice calling Bob using the SIP protocol.
2. Then, after Bob answers, he and Alice establish a DIDComm connection by Bob sending Alice an out-of band-message. As a means of transport, Bob chooses the active SIP session between him and Alice, and sends Alice the message as an encrypted SIP message.
3. With the DIDComm connection in place, they can now use DIDComm to exchange credentials.
4. The credentials proven to be satisfactory, Bob and Alice continue their SIP session and exchange voice, video or text messages.

Because of its “SIP first approach”, SSIComms is able to facilitate identified communications sessions with both participants behind a firewall. Under these circumstances, DIDComm by itself would not enable Alice to contact Bob.
What is more, the clients from the SSIComms project have the advantage of backward compatibility with 100s of millions of devices (like office desk phones) and software clients, and allows them to set up various unidentified communications sessions with most of these out of the box.

## 2. Adding internet communications to SSI
Starting from SSI is the other way to approach this problem. In this case, Alice and Bob first establish a DIDcomm connection through for instance the echange of a QR code, after which they use DIDComm messaging as the basis for communications.
An example of this approach can be found at [*Hearro*](hearro.com), which developed a call center solution based on DIDComm messaging, and there is also [*the advanced reading paper submitted for this conference*](https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/advance-readings/advanced-didcomm-messaging.md) by Karim Stekelenburg  from Animo (and by the way a collaborator on the SSIComms project). Karims paper is interesting because it explicitly lists some of the issues such as group chat that need to be solved in order for DIDComm to support a full featured chat solution.

## 3. Comparing the two
This paper hopes to answer the question under which circumstances one solution is preferable to the other, how each of them could evolve, and whether DIDComm and internet communications protocols could learn from each other, for instance in the way communications are encrypted, for which the chat protocol offers a plethora of solutions.
