# Forget issuance, just witness and confirm
***by Eric Welton, Korsimoro***

## Digital Chickens and Eggs

I remain troubled by the chicken-and-egg problem inhibiting adoption of
digital credentials in broad society.  I suspect that adoption of
digital credential technology is hampered by design - our focus on a
hyper-connected future does not accommodate the reality of the present.

We hobble ourselves, as an industry, by requiring the existence of a complete
ecosystem of issuers, verifiers, and point-of-contact consumption applications.

Even though we all know that such an ecosystem will inevitably come to be,
we have blocked the emergence of the ecosystem by focusing on problems and
solutions that assume we have passed a critical threshold.  Appropriate
cryptographic curves, multi-party signatures, or even the fundamental
extensibility of the DID document are all second-fiddle concerns.

## Doctors and Lawyers and Such

Consider a physician soliciting patients and advertising services based on
their existing credentials - or a lawyer offering their skills negotiating
the morass of our overlegislated lives.  This happens today, in the absence
of digital credentials - patients see doctors and individuals retain lawyers.
It is a slippery and sloppy system - a convicted Texas pedophile can still
wind up practicing pediatrics in California and a shady taxi operator can
become a personal legal advisor to the president of the united states.

Digital credentialing improves this sad state of affairs, but it requires that
the entire economy suddenly and spontaneously adopt the crystalline purity of
unproven, untested, nascent future technology.

If you've just quit smoking, you should not try to run a marathon the next week.
Prudence suggests you at least try a simple 3K first - and if you live through
that then slowly build yourself up to a 26 mile jog.

## Issuance is a big ask

I believe the problem is issuance - asking an organization to author digital
equivalents of the credentials they currently produce seems like a no-brainer,
but is, in fact, a tremendous obstacle.  In the absence of a pre-existing
ecosystem this option is only available to innovators and risk takers.  The
bulk of institutions are ready to be fast-followers and rapid-adopters - very
few institutions are interested in being the first to land on the Normandy beach.
Many more institutions are willing to join the second wave - once the beachhead
is secure.

How can we secure the beachhead of digital credentials and create an environment
that rewards prudence?

## Why is Issuance a problem

The problem with issuance is that it creates liability.  In order to issue digital
credentials the institution must craft and review a tedious set of terms and
conditions - they must evaluate the technology and make a prudent judgement
based on well established best practices.  Since the ecosystem does not yet
exist, these best practices do not yet exist.  This creates enormous risk for
an institution - they must venture into the unknown, using unproven technology,
and they must sculpt their legal position based on first principles rather than
pointing to established practices and well tested case law.

## Change the game

Given that institutions currently issue all manner of physical credentials,
we benefit by changing the digital credential game to leverage their existing
investment in legal and regulatory technology.

We can do this by asking institutions to confirm a credential rather than
issue a credential.  The institutional ask changes from the demand to provide
a digital form of credential-X, bound to individual-Y, to the verification
task "did you issue credential-X to individual-Y".

In the former case, strong cryptographic tradecraft needs to be employed by
both the institution and the individual.  Both must be well versed in private
key management - from genesis through rotation and recovery, and this key
management needs to be enshrined in tomes of legalese which establishes the
firm legal basis that clearly establishes the liability frontier of
the institution relative to the individual.  This does not yet exist.

The question "did you provide this credential to this individual" is something
that institutions can address - they do so regularly, using the non-digital
credentials.  This is not fundamentally new territory - it is a change of
form.

It is the difference between playing a game of chess with black-and-white
pieces and playing the same game with green-and-red pieces.  If this seems
silly, consider the challenge that such a trivial change poses
to the color blind.  Something seemingly trivial can, and often does, have
vast unintended consequences - this is a component of the fear that
drives institutions away from the digital credential beachhead.

## OCR & Verification

With modern OCR software it is possible to take a quick snapshot of a credential,
perhaps using one of those ubiquitous smartphone cameras that are all the rage
with young people these days, and generate an approximation of an equivalent
digital credential.

The owner of the credential can verify the transcription, making
changes as necessary, and submit the bundled photograph + transcription to the
issuing institution and ask them to verify it.  This taps and existing pathway
of institutional credential verification.

The authentication and authorization challenge seen by the institution does
not change - it can be enhanced through the use of digital identity technologies,
but the core liability and legal infrastructure does not change.

The response of the institution becomes "to the best of our ability, under
the current best practices and congruent with our existing legal envelope,
we believe that this is, or is not, the credential we previously issued to you
on really cool, expensive, tamper-proof paper" - the binding requirements
between the holder of the credential, or the requester of verification is
much lighter than the issuance case - there is no strong binding between
the credential and the subject.

Instead of saying "This is Mr. Pink's Degree" - the institution is only
confirming that "we believe you have a reasonable justification for asking
if this is Mr. Pink's degree, and we will confirm that we did give Mr. Pink
the degree that you are presenting"

The institution "bears witness" to the credential - establishing a digital
twin, but avoids liability entanglement or the need to validate
the identity of the parties involved.  The tradecraft requirements supporting
the institutional signing key are likewise reduced - instead of being the
public, undeniable, legally binding authority they might be as simple as
"Sally, in Records."  Eventually, and ideally, the signing key would become
part of the institutional context - but that will happen only as the supporting
legal and administrative context, the practices, and the practice of practices,
evolves.

This is not a full solution to the problem of digital credentials, but it is
very attainable stepping stone.  This solution is scaffolding, but perhaps it
is the scaffolding necessary to build the edifice.


## RWoT 10 tasks

For RWoT 10 I would like to form a group that critically and deeply evaluates
the question of how "verifying a pre-existing credential" differs from primary
issuance.

* How can the act of "bearing witness" to a credential become part of the
digital ecology - or does it have no place at all?
* Can we relate this to models of Trust Framework such as Aires 289/ToIP?
* How does "bearing witness" measure up in terms of Assurance?
* What existing legal culture might inform our commentary?
