# Credential Types for Compliance

For the purpose of this paper, we postulate the existence of an "SSI infrastructure", i.e. an electronic infrastructure for the exchange of (verifiable) credentials/(personal) data to which an arbitrary party can and may connect, and use it in each of the SSI roles 'issuer', 'holder' and 'verifier'. We expect a party to do this when its (individual) business case shows that (electronic) business transactions become cheaper, faster, and easier to conduct. For many of them, (provable) compliance with applicable laws, regulations and policies is also required, e.g. in the financial and governmental domains. 

This paper aims to come to grips with this latter, compliance aspect, serving purposes such as:

- helping parties that (want to) use the SSI infrastructure exploit it to the max, by showing how credentials can be used not only for conducting transactions (we knew that already), but also for becoming and remaining compliant with applicable rules and regulations. 
- helping parties that 'make the rules' improve the rules they make. For example, many governments have laws that require verifiable (personal) data to be exchanged in very specific ways, e.g. by showing legal (mostly paper-based) documents such as passports and driving licenses, thus preventing them to optimally exploit an SSI infrastructure.
- finding out what, if any, credential types may be designed the existence of which would help 'rule makers' make rules that are inclusive of SSI/VCs and can readily be complied with. We might even start developing (some of) them. Suggestions include credential types for guardianship, delegation, mandates, roles etc.. 

I'm not fixing where this is going (so the paper currently has no proposed structure). I merely want to contribute to write a paper that serves these and associated purposes.

## Background

To illustrate where I am currently thinking of where this is going, let's consider the [Mya use-cases](https://drive.google.com/file/d/10sfYKp6Ohi_rLsNqb1GBrhuE0IuoBX2k/view) used in the [whitepaper](https://sovrin.org/wp-content/uploads/Guardianship-Whitepaper.pdf) “On Guardianship in Self-Sovereign Identity” of the [Sovrin Guardianship Task Force](https://docs.google.com/document/d/1ymWzCwu2Ud6FMGZdU8md03KCvaxmT41-gQYIRXo09Xw/edit#heading=h.8oej31ec0two). 

In this use case, UNICEF has established a refugee camp and Sofia and Malcolm are two of the camp staff. At some point, a little girl (Mya) and her grandmother (Zo) arrive. Sofia registers them as refugees. She also registers Zo (a person) and UNICEF (an organization) as Mya's guardian. Then the use-case describes how Zo can get food rations for Mya, how Mya is enrolled in the camp school, and more.

Let's focus on transactions of a single type, i.c. 'food ration distribution'. The procedure for conducting such transactions is simple: there are two actors, one of which plays the [refugee] role, that will request a food ration and hopefully obtain one. The other plays the [shopkeeper] role, and will (possibly) issue the food rations. 

Side note: we use square brackets to distinguish between role names and regular text. We do this to avoid confusion between *being* something (e.g. a refugee) and fulfilling a role (e.g. [refugee]). Using square brackets for roles also suggest that they serve as a placeholder for an actual actor. 

The procedure for the  'food ration distribution' transaction is quite straightforward:

1. [refugee] enters the shop and requests [shopkeeper] to issue a food-ration for a specific refugee.
2. [shopkeeper] checks whether or not this transaction, if it were executed, complies with the rules that UNICEF (the party on whose behalf he will be servicing the request) has determined to be applicable.
3. If compliant, [shopkeeper] issues a food ration to [refugee] and records the event; otherwise, [shopkeeper] denies the request.

Further down, we will show that 'food ration distribution' transactions can completely be specified by the rules that govern them - we will provide these rules. As a consequence, 'compliance' w.r.t. transactions of this type means that UNICEF should be able to convincingly argue compliance to its governing rules. In the rules we provide we will see how we can collect the necessary data in the procedure itself.

To do this, we classifying the rules in terms of preconditions, boundary conditions and post conditions . This allows us to construct a (generic!) process engine that is capable of running transactions of any kind. Such an engine works as follows:

- whenever all preconditions and boundary conditions associated with a transaction type are fulfilled, and at least one of the post conditions is not fulfilled, a new transaction of that type is created;
- an activity that is part of a transaction can only execute while every boundary condition is fulfilled, and at least one of the post conditions is not fulfilled. 
- when all post conditions of a transaction are fulfilled, the transaction terminates.

Note that the actual work that is done in any of its activities is not specified, but it is confined to what the boundary conditions allow, which is the very purpose of what 'compliance' intends to achieve.

Here is what this means for 'food ration distribution' transactions (and this is its specification in terms of rules):

1. preconditions. Compliance with these rules means showing that every one of them is fulfilled at the start of the transaction. For 'food ration distribution' transactions, the following preconditions would apply:

   - the refugee for which a food ration is requested, is a person that is registered as a refugee.
   - a request for issuing a food ration for the specified refugee has not serviced earlier on the day that the request has been received.
   - there is at least one food ration in stock that can be provided.
   - the current time is within the opening hours of the shop, or the [refugee] has claimed an probable and acceptable emergency.

2. boundary conditions. Compliance with these rules means showing that every one of them is fulfilled  both at the start of the transaction, as well as during any activity that takes place in the transaction. For 'food ration distribution' transactions, the following boundary conditions could apply: 

   - the role of [shopkeeper] is performed by a person that is registered as camp staff and has a UNICEF mandate for performing this role;
   - the role of [refugee] is performed by a person that satisfies any of the following conditions:
     - it is registered as the refugee for which the food ration is requested;
     - it is registered as a refugee that is a guardian of the refugee for which the food ration is requested;
     - it is registered as camp staff and it has a UNICEF mandate for acting as a guardian of the refugee for which the food ration is requested.

3. post conditions. Compliance with these rules means showing that every one of them is fulfilled when the transaction terminates. For 'food ration distribution' transactions, the following post conditions would apply:

   - [refugee] has been provided with a food ration for the refugee mentioned in the request;

   - the transaction log of the 'food distribution process' contains an entry that shows at least the following items:

     - the times at which the transaction started and terminated, 
     - the refugee for which a food ration has been issued,
     - the actors that played the roles of [shopkeeper] and [refugee],
     - any role-assignments, mandates or guardianships that have been used in the evaluation of any precondition or boundary condition of the transaction.

     unless such an item can at any later point in time (still) be derived from other registrations.

Critical for the construction of a compliance argument is the second post condition, as it ensures that all data that is necessary for that construction is actually available by explicitly specifying what this data is (for 'food ration distribution' transactions. And it is because we have specified such transactions exclusively in terms of rules that we are capable of explicitly specifying this data. 

## How might this be of any use?

The above suggests that parties may benefit by making and maintaining an inventory of the kinds of transactions they conduct, and for each of them a list of applicable rules in terms of preconditions, boundary conditions and post conditions:

- having a process engine that uses such rules and that keeps track of the data that is used to evaluate these conditions in a transaction provides a solid audit trail that can be used to prove compliance. 
- having such rules is a solid specification of the information that is, or may be needed for running transactions of various kinds. It can be used as a source for creating credential/presentation requests, as well as for specifying the purpose for which the data in presentations (responses to such requests) will be used. It also serves as a basis for arguing compliance with the minimization principle of the GDPR.

For the authors of this intended paper, it is my hope that the idea that credential data must be used in coherent rules will trigger some new thinking about designing credentials. As an example, some recent work we did at TNO shows that a credential with the following payload may be very helpful (forgive the notation - I'm not a trained JSON):

~~~json
{ "type": "guardianship-credential-payload",
  "guardianship-relation": 
    [ { "jurisdiction": "jurisdiction-identifier",
        "relation": 
         { "relation-type": "guardianship-relation-type",
       	   "guardian-type": "entity-class",
       	   "dependent-type": "entity-class"
         },
        "guardian": "entity-identifier",
        "dependent": "entity-identifier"
    } ]
}
~~~

This says that a guardianship relation is entirely defined by/within a specific jurisdiction. Also, a guardianship relation is typed, which means multiple kinds of guardianship can be accommodated within its jurisdiction. The construct `relation-type`(`guardian-type`, `dependent-type`) specifies a fully typed relation between two entities, whose meaning is defined in the authoring jurisdiction. Note that by 'meaning' we not only mean any constraints that a guardian instance and dependent instance should have, but also any consequences that being part of this relation implies according to the laws/rules and regulations of the jurisdiction.  

For example, consider a jurisdiction that has a law that defines 'natural guardianship' as the relation between a child and any of its (biological) parents, and continues by assigning powers, rights, etc. to the guardian and/or dependent. It is then easy to issue guardianship-relation credentials within that jurisdiction, and any party that uses these credentials will know exactly what it can and cannot do with it.  

This construct has many other applications. For example, think about `property ownership`(`natural person`,`property`), or `mandate`(`natural person`,`transaction type role`), or `delegation`(`natural person`, `transaction type role`), etc.``