import asyncio
import didkit
import pickle
import json
from pprint import pprint
from warnings import warn

def create_key(name):
    jwk = didkit.generate_ed25519_key()
    with open(name + '.jwk', 'wb') as f:
        pickle.dump(jwk, f)
    return jwk


async def sign_with_did(vc_json, name):
    try:
        with open(name + '.jwk', 'rb') as f:
            jwk = pickle.load(f)
    except:
         jwk = create_key(name)

    did = didkit.key_to_did("key", jwk)

    vc_json['issuer'] = did

    # TODO look up what other fields need did from credential type

    print("About to try to sign this cred: ")
    pprint(vc_json)

#    pprint(jwk)
    try:
        signed_cred = await didkit.issue_credential(
            json.dumps(vc_json),
            json.dumps({}),
            jwk)
        return signed_cred
    except Exception as e:
        warn(str(e))
        return "ERROR: " + str(e)


def link_creds(signed_cred1, signed_cred2, output_type):
    pass
    # TODO here
