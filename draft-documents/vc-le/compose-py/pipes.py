from copy import deepcopy
from keymgr import sign_with_did
import json

sources = [
 { 'file': 'tec.json',
   'type': 'tec',
   'effdate': "2022-09-28",
   'name': 'olivers_spider'
 },
 {
 },
]

templates = {
   'tec': {
        "@context": [
                "https://www.w3.org/2018/credentials/v1",
                "https://www.w3.org/2018/credentials/examples/v1",
                "https://w3.id/vc/linked-claims" 
              ],
              "type": [ "VerifiableCredential", "LinkedClaim" ],
              "issuer": {
                "id": "",
                "name": ""
              },
              "issuanceDate": "2022-09-29T00:00:00Z",  # TODO replce w today
              "expirationDate": "2023-09-29T00:00:00Z", # TODO replace w next year
              "effectiveDate": '',
              "credentialSubject": {
                "id": '',

                "linkedClaim": {
                  "type": "endorsement",
                  "aspect": "impact:community",
                  "statement": "|TEXT|",
                  "source_type": "discord scrape",
                  "sources": []
                }
              }
            }
}



def make_vc(claim, meta):
    vc = deepcopy(templates[meta['type']]) 
    vc['effectiveDate'] = meta['effdate'] 
    vc['credentialSubject']['id'] = claim['to']
    vc['credentialSubject']['linkedClaim']['sources'].append(claim['from'])
    vc['issuer']['name'] = meta['name']
 
    return sign_with_did(vc, meta['name'])

    #print(json.dumps(vc))
   
def run_pipe():
    for source in sources:
        with open('./data/raw/'+source['file'], 'r') as f:
            data = json.load(f)
        for raw_claim in data['attestations']:
            print(json.dumps(make_vc(raw_claim, source)))


run_pipe()
