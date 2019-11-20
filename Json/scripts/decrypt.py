import base64
import hashlib
from Crypto.Cipher import DES3

SecurityKey = "_5TL#+GWWFv6pfT3!GXw7D86pkRRTv+$$tk^cL5hdU%"

password = "oQ5iORgUrswNRsJKH9VaCw=="
username = "4as8gqENn26uTs9srvQLyg=="

def decrypt(string, hashing):

    base64_data = base64.b64decode(string)

    SecKeyBytes = SecurityKey.encode("utf-8")

    if hashing:
        numArray = hashlib.md5(SecKeyBytes).digest()
    else:
        numArray = SecKeyBytes

    cipher = DES3.new(numArray, DES3.MODE_ECB)

    d = cipher.decrypt(base64_data)

    print(d.decode())

decrypt(username, hashing=True)
decrypt(password, hashing=True)