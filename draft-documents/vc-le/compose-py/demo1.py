import asyncio
import didkit
import json

jwk = didkit.generate_ed25519_key()
did = didkit.key_to_did("key", jwk)
credential = {
    "@context": "https://www.w3.org/2018/credentials/v1",
    "id": "http://example.org/credentials/3731",
    "type": ["VerifiableCredential"],
    "issuer": did,
    "issuanceDate": "2020-08-19T21:41:50Z",
    "credentialSubject": {
        "id": "did:example:d23dd687a7dc6787646f2eb98d0",
    },
}

async def main():
    signed_credential = await didkit.issue_credential(
        json.dumps(credential),
        json.dumps({}),
        jwk)
    print(json.loads(signed_credential))

asyncio.run(main())
