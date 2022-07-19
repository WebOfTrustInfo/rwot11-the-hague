[Revisiting Usefulness of Centralized System for Establishing Trust](./revisiting-usefulness-of-centrailzed-system.md)

   * by [Shigeya Suzuki](mailto:shigeya@wide.ad.jp), Ph.D, Project Professor, Graduate School of Media and Governance, Keio University, Japan
   * Using DNS as root of trust with help of ICANN's virtualized decentralized governance mechanism
   * #RootOfTrust #DNS #DNSSEC #ICANN #VirtualizedDecentralization #MultistakeholderGovernance

This is a proposed collaborative paper to be completed at [RWOT 2022](https://rwot11.eventbrite.com/), Den Haag, Netherlands, 26-30 September. Advance reading: see [here](https://github.com/WebOfTrustInfo/rwot11-the-hague/tree/master/advance-readings).

# Revisiting Usefulness of Centralized System for Establishing Trust

The web is currently overwhelmed with the buzzword "Web3," "Web 3.0." or similar. Proponents believe that decentralization can solve problems in centralization, especially on "Trust." Unfortunately, it is hard to identify a person to digital identity without relying on some trusted third party. Of course, most activities in the cyber world can be closed within the cyber world, but as physical beings, we often need to bind digital identities to us. 

In this paper, we design suitable guidance to bootstrap Trust. The paper provides background on how we use a centralized system by revisiting how it works and how to use it. We use DNS/DNSSEC as a Root of Trust and apply the DNS's hierarchical delegation mechanism to implement an appropriate governance mechanism.

Firstly, we review what so-called "Centralized Trust" is currently in use. In our past work [1], we modeled how a component of Trust is influenced by governance and how an entity controls Small Data to achieve its goal. Each administrative domain controls Small Data;  Maintaining such Small Data is a concern from a governance point of view. The Policy for the Small Data decides Operation on it, and the Governance mechanism defines the Policy, often controlled by Regulation. In this paper, we expand the discussion as the background material.

Secondly, design a scheme based on DNS as a basis to establish Trust. For Domain Name System (DNS), zone administrators control administrative zones. Each of the zones operates independently, and these zones are organized hierarchically.

ICANN maintains the root of the DNS hierarchy in multistakeholder governance, designed by people worldwide. ICANN spent more than twenty years establishing an appropriate governance mechanism without centralized power [2]. While ICANN as an organization has control of the root zone, its multistakeholder governance virtually decentralizes members' influence. We see ICANN's elimination of centralized power as far fair decentralization than the current status of DAOs' distribution of voters[3]. Moreover, ICANN never allows somebody to have a superpower, distinct from the current DAOs' design. We still need to have a mechanism to patch software-based systems since a human can't develop bug-free software, and it doesn't seem easy to eliminate a superpower for the patching within the foreseeable future. Thus, virtually decentralized multistakeholder governance of the root of Trust seems a vital and appropriate mechanism.

Thus, Relying on DNS to bootstrap Trust is reasonable and adequate. What we need to do is how we can use DNS's characteristics to bootstrap Trust, especially for Digital Identity. We already have technological tools like Decentralized Identifiers with multiple DID methods like `did:web` and `did:dns,` and Verifiable Credentials. We need a helpful framework or guidance to implement Trust based on DNS.

## References

* **[1]** Dependency among Data, Code, Governance, and Operation in Trust,
    Shigeya Suzuki, Tatsuya Kurosaka, Jun Murai, Keio University,
    Symposium on Designing the New Cyber Civilization,
    Cyber Civilization Research Center, Keio Univesity, January 2022.

    Online: https://www.ccrc.keio.ac.jp/wp-content/uploads/2022/02/Suzuki-Kurosaka-Murai-Dependency-among-Data-Code-Governance-and-Operation-in-Trust.pdf

* **[2]** A Study on Governance for Decentralized Finance Systems Using Blockchain Technologies,
    Joint Research of Keio University and Japan Financial Services Agency, May 2020,

    Online: https://www.fsa.go.jp/en/policy/bgin/information.html

    Note: The author of this short paper is one of the report's authors.

* **[3]** Research Report of JFSA Multilateral Joint Research on the Chain of Trust of Decentralized Finance, 
    Joint Research of QUNIE Corporation and Japan Financial Services Agency, June 2022,

    Online: https://www.fsa.go.jp/en/policy/bgin/information.html

    Note: The author of this short paper is one of the observers of the research.
