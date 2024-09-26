import json
import base64
import string 
from random import choice

def rndstr(size=16):
    # Pick a random string of size `size` from the alphabet
    alphabet = string.ascii_letters + string.digits
    return "".join([choice(alphabet) for _ in range(size)])


def decode_jwt(jwt_token):
    header, payload, signature = jwt_token.split(".")

    decoded_header = base64.urlsafe_b64decode(header + "=" * (-len(header) % 4))
    decoded_payload = base64.urlsafe_b64decode(payload + "=" * (-len(payload) % 4))

    return json.loads(decoded_header), json.loads(decoded_payload)