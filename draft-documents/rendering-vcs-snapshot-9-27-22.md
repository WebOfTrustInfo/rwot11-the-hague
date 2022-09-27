# Rendering Verifiable Credentials

## Authors

*   Charles Lehner @cel
*   Dmitry Zagadulin @dmitrizagidulin      
*   Ben Goering @bengo

## Abstract  

In the Verifiable Credentials ecosystem, wallets and verifiers have expressed a strong preference for a consistent rendering mechanism because they will simplify the implementation of applications that are safe and easy to use. Several specifications have proposed credential rendering methods for a specific set of use-cases, but no interoperable scheme has emerged across use-cases. In this paper, the authors survey existing methods and propose a unified data model for rendering hints, renderer descriptions, and security considerations to keep in mind when using them.  

## Ideas  

*   propose a registry (or meta-type) of renderers as a work item in ccg  
*   wasm  
*   ways of improving data model  
*   Security Consideration of pre-baked rendered image vs template  
*   html5 custom element renderer  
*   and/or '3D renderer' (webgl, css 3d)

## Links  

*   Manu's [advanced reading](https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/advance-readings/rendering-verifiable-credentials.md) for this RWoT   
*   [https://identity.foundation/wallet-rendering/](https://identity.foundation/wallet-rendering/)  
  *   [https://github.com/decentralized-identity/wallet-rendering](https://github.com/decentralized-identity/wallet-rendering)  
      *   [https://lists.w3.org/Archives/Public/public-credentials/2022Jul/0054.html](https://lists.w3.org/Archives/Public/public-credentials/2022Jul/0054.html)
  *   offshoot of [https://identity.foundation/credential-manifest/](https://identity.foundation/credential-manifest/)  
*   [https://medium.com/mattr-global/rendering-credentials-in-a-human-friendly-way-e47f4a32fd4b](https://medium.com/mattr-global/rendering-credentials-in-a-human-friendly-way-e47f4a32fd4b)  
*   [https://gitlab.grnet.gr/essif-lab/infrastructure\_2/gataca/Verifier\_Universal\_Interface](https://gitlab.grnet.gr/essif-lab/infrastructure_2/gataca/Verifier_Universal_Interface)  
*   [https://cryptpad.fr/code/#/2/code/edit/l8fIB1njuJzhI-Lr1Szaf0cz/](https://cryptpad.fr/code/#/2/code/edit/l8fIB1njuJzhI-Lr1Szaf0cz/) (markdown...)  
    
## References  

*   Gataca paper (is it part of the [VUI](https://github.com/gataca-io/vui-core)?) from eSSIF-LAB interop work   
*   DIF's medium-stale (but being rebooted soon!) [wallet rendering](https://identity.foundation/wallet-rendering/) spec that grew out of the Credential Manifest and Presentation-Exchange architecture/use-cases  
