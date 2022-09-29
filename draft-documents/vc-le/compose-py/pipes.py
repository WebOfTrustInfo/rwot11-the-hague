import asyncio
from copy import deepcopy
from keymgr import sign_with_did
import json

linked_claim_context = {
           "effectiveDate": {
              "@id": "lc:effectiveDate",
              "@type": "xsd:dateTime"
            },
            "CanContainLinkedClaim": {
                "@id":"http://cooperation.org/credentials/LinkedClaimCapability/v1",
                "@context": {
                    "linkedClaim": {"@id":"http://cooperation.org/credentials/LinkedClaimCapability/v1#linkedClaim"}
                }
            },
           "LinkedClaim": {
             "@id": "http://cooperation.org/credentials/LinkedClaim/v1",
             "@context": {
                "lc":"http://cooperation.org/credentials/LinkedClaim/v1",
                "aspect": {"@id": "lc:aspect"},
                "source_type":{"@id": "lc:source_type"},
                "source": {"@id": "lc:source"},
             }
          }
    }


sources = [
 { 'file': 'tec.json',
   'type': 'tec',
   'effdate': "2022-09-28T00:00:00Z",
   'name': 'olivers_spider'
 },
 {
 },
]

template = {
        "@context": [
                "https://www.w3.org/2018/credentials/v1",
                linked_claim_context
              ],
              "type": [ "VerifiableCredential", "LinkedClaim" ],
              "issuer": None,
              "issuanceDate": "2022-09-29T00:00:00Z",  # TODO replce w today
              "expirationDate": "2023-09-29T00:00:00Z", # TODO replace w next year
              "effectiveDate": '',
              "credentialSubject": {
                'type': 'CanContainLinkedClaim',
                "id": '',

                "linkedClaim": {
                  "type": "LinkedClaim",
                  "aspect": "impact:community",
#                  "statement": "",
                  "source_type": "discord scrape",
                  "source": []
                }
       }
}



async def make_vc(claim, meta):
    vc = deepcopy(template) 
    vc['effectiveDate'] = meta['effdate'] 
    vc['credentialSubject']['id'] = 'discord:' + claim['to']
    vc['credentialSubject']['linkedClaim']['source'].append(claim['from'])
    #vc['issuer']['name'] = meta['name']
    #vc['credentialSubject']['linkedClaim']['statement'] = claim['text']
 
    return await sign_with_did(vc, meta['name'])

    #print(json.dumps(vc))
   
async def run_pipe():
    for source in sources:
        with open('./data/raw/'+source['file'], 'r') as f:
            data = json.load(f)
        for raw_claim in data['attestations']:
            print(json.dumps( await make_vc(raw_claim, source)))


async def main():
    await run_pipe()

asyncio.run(main())
