

Resource for authorizing from scratch
https://spapas.github.io/2023/11/29/openid-connect-tutorial/

## Keyclock web ui steps

Enter http://localhost:8080/ in browser.
Proceed to clients tab and register client with:
- client-id: image-client
- 
You can find client secret in credentials tab. You'll need to pass it to `.env` file

## Prepare `.env`

``` bash
cp example.env .env
```