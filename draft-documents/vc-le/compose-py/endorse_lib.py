import asyncio
from copy import deepcopy
from keymgr import sign_with_did
import json
import pickle
from pprint import pprint

OUTPUT_DIR = './data/endorsable_claims'

endorse_context = {
           "lc": "http://cooperation.org/credentials/Composable/v1",
           "effectiveDate": {
              "@id": "lc:effectiveDate",
              "@type": "xsd:dateTime"
            },
           "achievement": {"@id": "lc:achievement"},
           "criteria": {"@id": "lc:criteria"},
           "narrative": {"@id": "lc:narrative"},
           "citation": {"@id": "lc:citation"},
           "digestMultibase": {"@id": "lc:digestMultibase"},
           "endorser": {"@id": "lc:endorser"},
           "endorsement": {"@id":"lc:endorsement"},
           "linkedClaim": {"@id":"lc:linkedClaim"},
           "relevance": {"@id": "lc:relevance"},
           "source_type":{"@id": "lc:source_type"},
           "source": {"@id": "lc:source"},
           "statement": {"@id": "lc:statement"},
}

achieve_template = {
"@context": [
                "https://www.w3.org/2018/credentials/v1",
                endorse_context
              ],
  "type": [
    "VerifiableCredential",
    "OpenBadgeCredential"
  ],
  "issuer": "",
  "issuanceDate": "2022-05-01T00:00:00Z",
  "credentialSubject": {
    "type": "AchievementSubject",
    // Note that the subject of the VC is the issuer, hence self-issued
    "id": "",
    "achievement": {
      "id": "urn:uuid:",
      "type": "Achievement",
      "name": "",
      "description": "",
      "criteria": {
         "type": "Criteria",
         "narrative": ""
       }
    }
  },
}

endorse_template = {
        "@context": [
                "https://www.w3.org/2018/credentials/v1",
                endorse_context
              ],
              "type": [ "VerifiableCredential", "VerifiableEndorsement" ],
              "issuer": "",
              "issuanceDate": ""
              "effectiveDate": '',
              "credentialSubject": {
                "id": '',
                "digestMultibase": '',
                "endorsement": {
                  "type": "Endorsement",
                  "statement": "",
                  "endorser": {
                     "id": "",
                     "relevance": []
                  }
               }
            },
            "evidence": [], 
}

def remove_non_ascii(string):
    return ''.join(char for char in string if ord(char) < 128)


