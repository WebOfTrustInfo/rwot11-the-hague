from flask import Flask
from pprint import (pprint, pformat)
from flask import request
import json
import pickle
import re
import subprocess
import asyncio
from copy import deepcopy
from keymgr import sign_with_did
import json
import pickle
from datetime import datetime
from pipes_lib import ( INPUT_DIR, OUTPUT_DIR, linked_claim_context, template, remove_non_ascii )

app = Flask(__name__)

@app.route("/")
def simple_inputs():
    return """<html><title>Linked Claim inputs</title>
              <body>
             <a href="/">Record a claim</a> | Find claim:<form action="/filter" method="get"><input name="search"/></form>
             <H2>Record your observations</h2>
              <form name='get_data' action='/create' method=POST>
<p>
              Who or what did you observe something about? (MUST BE URI) 
             <input name="to" size=100/>
</p><p>
              How did you observe it?
              <select name="source_type"/>
              <option name="firsthand"/>First-hand</option>
              <option name="secondhand"/>Second-hand (someone told you)</option>
              <option name="research"/>I read it somewhere</option>
              </select>
</p><p>
              What was the source (if not yourself):
              <input name="source" size="100"/>
</p><p>
              What aspect of the subject does this relate to?
              <select name="aspect"/>
              <option name="rating:quality"/>Quality
              <option name="impact"/>Impact
              <option name="risk"/>Risk 
              </select>

</p><p>
              Ok, in your own words, what is your observation?
              <textarea name="statement"></textarea>
</p><p>
             Until we have metamask login working...

              Who are you? <input name="you" size=50/>
             <input type="submit"/>
         </form></body></html>"""


LOCAL_DIR = '/Users/gv/rwot11-the-hague/draft-documents/vc-le/compose-py'


async def make_vc(claim, name, effdate):
    vc = deepcopy(template)
    vc['effectiveDate'] = effdate or datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ") 
    vc['credentialSubject']['id'] = claim['to']
    vc['credentialSubject']['linkedClaim']['source'] = [claim['source'], claim['from']]
    #vc['issuer']['name'] = meta['name']
    vc['credentialSubject']['linkedClaim']['statement'] = remove_non_ascii(claim['statement'])
    vc['credentialSubject']['linkedClaim']['aspect'] = claim['aspect']
    vc['credentialSubject']['linkedClaim']['source_type'] = claim['source_type']

    return await sign_with_did(vc, name)

def save_vc(vc, fname):
    with open(OUTPUT_DIR + '/' + fname + '.json', 'wt') as f:
        pprint(json.loads(vc), stream=f)
    with open(OUTPUT_DIR + '/' + fname + '.pickle', 'wb') as f:
        pickle.dump(vc, f)

@app.route("/create", methods=["POST"])
async def create_claim():
    data = { 'to': request.form['to'],
             'from': request.form['you'],
             'source_type': request.form['source_type'],
             'source': request.form['source'],
             'aspect': request.form['aspect'],
             'statement': request.form['statement']}

    effdate = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
    name = effdate

    vc = await make_vc(data, name, effdate)

    save_vc(vc, name)
    return str(vc) 


@app.route("/filter")
def filter_claims():
    term = request.values['search']
    output = subprocess.check_output("grep -l " + term + " ./data/claims/*.json", shell=True)
    res_list = output.split(b'\n')
    res = ''
    for fname in res_list:
        print("On : " + str(fname))
        try:
            fname = fname.decode('utf-8')
            fname = re.sub(r'json', 'pickle', fname)
            with open(LOCAL_DIR + '/' + str(fname), 'rb') as f:
               data = pickle.load(f)
               res +=  '<p>' + str(data) + '</p>'
        except:
           pass
    return res
    #res = `grep ${term} ./data/claims`
              
     
              

