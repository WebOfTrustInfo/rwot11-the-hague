import asyncio
import didkit
import pickle
import json

def create_key(name):
    jwk = didkit.generate_ed25519_key()
    with open(name + '.jwk', 'wb') as f:
        pickle.dump(jwk, f)
    return jwk


def sign_with_did(vc_json, name):
    try:
        with open(name + '.jwk', 'rb') as f:
            jwk = pickle.load(f)
    except:
         jwk = create_key(name)

    did = didkit.key_to_did("key", jwk)

    vc_json['issuer']['id'] = did

    # TODO look up what other fields need did from credential type

    import pdb; pdb.set_trace()
    signed_cred = didkit.issue_credential(
        json.dumps(vc_json),
        json.dumps({}),
        jwk)
    return (did, signed_cred)


def link_creds(signed_cred1, signed_cred2, output_type):
    pass
    # TODO here
