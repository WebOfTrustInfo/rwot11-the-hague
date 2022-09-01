# CESR-adapter-for-sophisticated-multisig.md

[![hackmd-github-sync-badge](https://hackmd.io/GbQO3p6QTge-8eQMGuMaeQ/badge)](https://hackmd.io/GbQO3p6QTge-8eQMGuMaeQ)

Study CESR adapter for aggregated Schnorr, musig and/or frost\
By: Henk van Cann\
Date: July 2nd 2022\
Version: 0.8

**Mary Blockchain Commons (BCC) projects and KERI ToIP-projects. That's it.**

Because I am a supporter of both organizations and I'd like to level the playing field for more exchange on content.

## Advanced-Reading Paper; not OR but AND.

- [x] A specific problem related to identity or trust; AND
- [x] A specific critique of existing identity or trust systems; AND
- [x] A specific topic whose discussion will help advance understanding of identity or trust systems; AND
- [x] A specific solution using decentralized identity or a web of trust; AND
- [x] A specific questions not addressed by current solutions.

As a preparation for the RWOT in september 2022, 
I'd like to deep dive to fullfill a long-standing wish: 

> Bridge Keep wallet of KERI / ACDC and the much more sophisticated solutions at BCC for incepting and managing keys, and for keeping secrets secret.

And at the same time:

> KERI, CESR and ACDC can support sophisticated multisignature schemes. There's simply no demand yet. But don't tell me it can't be done.

## Why me?
Open Public Blockchain tech, Bitcoin purist, Self Sov IDs, #BlockchainCommons, #KERI, open source.
My hands-on work is documentation: Q&As and articles explaining hard-to-understand autonomic identifier system concepts in more accessible stuff.

See my Medium publications for results:\
https://medium.com/happy-blockchains

See github for activities in SSI projects:\
https://github.com/henkvancann

See my LinkedIN profile:\
https://linkedin.com/in/henkvancann

My donation-vehicle and open source contribution organisation:\
https://www.blockchainbird.org

## Why trying to bridge?

Christopher Allen (BCC founder - May 20 2022): "I’m still concerned with lack of support for aggregated Schnorr, musig & frost in KERI."

Samuel Smith (KERI founder):
"The point is to be used, not to use the latest, coolest technique that is also very difficult to implement properly.\
That's the principle of KERI: solve a problem in the real world with the minimum techniques needed."

> Smith:\
> "The dumber the technology, but still sufficient to solve the problem, the better. 'Dumb technology' is freely available, understandable to everyone and easy to implement. In our case: just hashes and digital signatures."

## It takes two to tango?
No, I don't care who likes to dance. I'll start to put on the music. It comes from two sides. Feel free to tap into them:
1. https://github.com/WebOfTrust/keri Focus on KERI, CESR and KEEP.
2. https://github.com/blockchaincommons/ Focus on SeedTool.

If you listen carefully, you might be able to hear the harmonics in the distance:
1. BCC keeping secrets secret for Keep wallet of KERI / ACDC.
2. CESR adapter for aggregated Schnorr, musig and/or frost

## Preparatory work
Resources I studied to prepare for the design:
- https://suredbits.com/schnorr-applications-frost/

Articles I wrote about CESR:
- [CESR Proof Signatures are the “Segwit” of Authentic Data in KERI.](https://medium.com/happy-blockchains/cesr-proof-signatures-are-the-segwit-of-authentic-data-in-keri-e891c83e070a)
- [CESR, one of Sam Smith’s inventions, is as controversial as it is genius.](https://medium.com/happy-blockchains/cesr-one-of-sam-smiths-inventions-is-as-controversial-as-genius-d757f36b88f8)
More details in draft: https://hackmd.io/a4oU3TmSSveRJYIQjuSgOQ