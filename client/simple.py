import httpx
import base64
import json
import string
from random import choice

def decode_jwt(jwt_token):
    header, payload, signature = jwt_token.split(".")

    decoded_header = base64.urlsafe_b64decode(header + "=" * (-len(header) % 4))
    decoded_payload = base64.urlsafe_b64decode(payload + "=" * (-len(payload) % 4))

    return json.loads(decoded_header), json.loads(decoded_payload)

def rndstr(size=16):
    # Pick a random string of size `size` from the alphabet
    alphabet = string.ascii_letters + string.digits
    return "".join([choice(alphabet) for _ in range(size)])



with httpx.Client() as client:
    # authroization
    res = client.post('http://localhost:8080/realms/master/protocol/openid-connect/auth',
        params={
            'client_id': 'image-client',
            'response_type':'code',
            'scope': 'openid',
            'redirect_uri': 'http://localhost:8000/auth/callback',
            'state': rndstr()
        }
    )
    print(res.url,res.status_code, res.headers)



    resp =  httpx.post(
        'http://localhost:8080/realms/master/protocol/openid-connect/token',
        data={
            "client_id": 'image-client',
            "client_secret": 'gfJvQ2kgnpFamo5VWhOR5vJIwqPkYhSG',
            "grant_type": "authorization_code",
            "code": '7901f723-6b5d-4692-9d43-d28459194d56',
            "redirect_uri": f'http://localhost:8080/auth/callback'
        },
    )

    print(resp.status_code, resp.json())
    headers,payload = decode_jwt(r['id_token'])
    access_token = r['access_token']
    identity = client.get(
        f'http://localhost:8080/realms/master/protocol/openid-connect/userinfo',
        headers={"Authorization": f"Bearer {access_token}"},
    )
    print({
        'status': resp.status_code, 
        'token_response':r,
        'id_token_headers': headers,
        'id_token_payload':payload, 
        'userinfo': identity.json()
    })
    # res = client.get("http://localhost:8080",follow_redirects=True)
    # print(res.status_code, res.content.decode())
    # print(client.cookies)