from rave_python import Rave
from flask import Flask, request
import json
import sys

app = Flask(__name__)


@app.route('/pay', methods=['POST'])
def pay():
    try:
        mRes = request.json
        print(type(mRes))

        rave = Rave("FLWPUBK_TEST-9b7e67b3f92743577a71e213ae831c30-X",
                    "FLWSECK_TEST-d7c930ee491d6e2664ec55eba9d1082d-X", usingEnv=False)

        r = json.dumps(mRes)
        payload = json.loads(r)
        res = rave.Card.charge(payload)
    except Exception as e:
        print("An error occured: " + str(e))

        return ("An error occured: " + str(e))

    return str(res['txRef'])
