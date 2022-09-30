import asyncio
from copy import deepcopy
from keymgr import sign_with_did
import json
import pickle
from pprint import pprint

INPUT_DIR = './data/raw'
OUTPUT_DIR = './data/claims'

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
                "statement": {"@id": "lc:statement"},
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
                  "statement": "",
                  "source_type": "discord scrape",
                  "source": []
                }
       }
}

def remove_non_ascii(string):
    return ''.join(char for char in string if ord(char) < 128)

async def make_vc(claim, meta):
    vc = deepcopy(template) 
    vc['effectiveDate'] = meta['effdate'] 
    vc['credentialSubject']['id'] = 'discord:' + claim['to']
    vc['credentialSubject']['linkedClaim']['source'].append(claim['from'])
    #vc['issuer']['name'] = meta['name']
    vc['credentialSubject']['linkedClaim']['statement'] = remove_non_ascii(claim['text'])
 
    return await sign_with_did(vc, meta['name'])

    #print(json.dumps(vc))
   
async def run_pipe():
    claim_num = 0
    for source in sources:
        with open(INPUT_DIR + '/'+source['file'], 'r') as f:
            data = json.load(f)
        for raw_claim in data['attestations']:
            vc = await make_vc(raw_claim, source)
            fname = source['name'] + '_' + str(claim_num)
            with open(OUTPUT_DIR + '/' + fname + '.json', 'wt') as f:
                pprint(json.loads(vc), stream=f)
            with open(OUTPUT_DIR + '/' + fname + '.pickle', 'wb') as f:
                pickle.dump(vc, f)
            claim_num += 1


