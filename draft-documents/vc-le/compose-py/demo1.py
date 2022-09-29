import asyncio
import didkit
import json
from pprint import pprint

jwk = didkit.generate_ed25519_key()
did = didkit.key_to_did("key", jwk)
good_credential = {
    "@context": "https://www.w3.org/2018/credentials/v1",
    "id": "http://example.org/credentials/3731",
    "type": ["VerifiableCredential"],
    "issuer": did,
    "issuanceDate": "2020-08-19T21:41:50Z",
    "credentialSubject": {
        "id": "did:example:d23dd687a7dc6787646f2eb98d0",
    },
}

mid8_cred1 = {'@context': ['https://www.w3.org/2018/credentials/v1',
              ],
 "type": ["VerifiableCredential"],
 'credentialSubject': {'id': "http://example.org/credentials/3731"},
 'issuanceDate': '2022-09-29T00:00:00Z',
 'issuer': did }

mid4_cred1 = {'@context': ['https://www.w3.org/2018/credentials/v1',
              ],
 'credentialSubject': {'id': "http://example.org/credentials/3731"},
 'issuanceDate': '2022-09-29T00:00:00Z',
 'issuer': did,
# 'issuer': {'id': 'did:key:z6Mkrk38THWmeFVvN9GfxH7qKwH5iP3FpNAK1qkdif7Y6AkK',
#            'name': 'olivers_spider'},
 'type': ['VerifiableCredential','LinkedClaim']}

mid_cred1 = {'@context': ['https://www.w3.org/2018/credentials/v1',

   {
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

              ],
 'credentialSubject': {
     'type': 'CanContainLinkedClaim',
     'id': 'discord:lewwwk#4227',

     'linkedClaim': {
        'type': 'LinkedClaim',
        'aspect': 'impact:community',
        'source_type':'heard it on the grapevine',
        'source':['thing', 'thing2'],
     },
 },
 'effectiveDate': '2022-09-28',
 'expirationDate': '2023-09-29T00:00:00Z',
 'issuanceDate': '2022-09-29T00:00:00Z',
 'issuer': did,
 'type': ['VerifiableCredential', 'LinkedClaim']}

bad_credential = {'@context': ['https://www.w3.org/2018/credentials/v1',

   {
        "LinkedClaim": {
          "@id": "http://cooperation.org/credentials/LinkedClaim/v1",
          "@context": {
            "lc":"http://cooperation.org/credentials/LinkedClaim/v1",
            "effectiveDate": {
              "@id": "lc:effectiveDate",
              "@type": "xsd:dateTime"
            },
            "expirationDate": {
              "@id": "lc:expirationDate",
              "@type": "xsd:dateTime"
            },
            "linkedClaim": {"@id":"lc:linkedClaim", "@type":"@id"},
            "aspect": {"@id": "lc:aspect"},
            "source_type":{"@id": "lc:source_type"},
            "sources": {"@id": "lc:sources"},
          }
        }
    }

  ],
 'credentialSubject': {'id': 'lewwwk#4227',
                       'linkedClaim': {'aspect': 'impact:community',
                                       'source_type': 'discord scrape',
                                       'sources': ['iviangita#3204'],
                                       'statement': '@David (please DYOR...) '
                                                    '@Guy James  @Yineisy Mota '
                                                    'for mentioning or '
                                                    'retweeting Commons Stack '
                                                    'on the socials the past '
                                                    'week! Thank you for '
                                                    'helping us grow the '
                                                    'Commons Stack community '
                                                    'and spreading the '
                                                    'message! 🙏🏼🌱 ',
                                       'type': 'endorsement'}},
 'effectiveDate': '2022-09-28',
 'expirationDate': '2023-09-29T00:00:00Z',
 'issuanceDate': '2022-09-29T00:00:00Z',
 'issuer': did,
 'type': ['VerifiableCredential', 'LinkedClaim']}

async def main():
#   for cred in [good_credential, mid8_cred1, mid4_cred1, mid_cred1, bad_credential]:
    for cred in [mid_cred1]:
       signed_credential = await didkit.issue_credential(
           json.dumps(cred),
           json.dumps({}),
           jwk)
       print(json.loads(signed_credential))
       print("OK")

asyncio.run(main())
