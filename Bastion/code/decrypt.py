from Crypto.Cipher import AES
import base64
import sys
import re

KEY = b"\xc8\xa3\x9d\xe2\xa5\x47\x66\xa0\xda\x87\x5f\x79\xaa\xf1\xaa\x8c"


if len(sys.argv) != 2:
    print("Usage: python decrypt.py <PASSWORD_STRING>")

confPath = sys.argv[1]

data = None
with open(confPath, "r") as file:
    data = file.read()

nodes = re.findall(r"<Node.+/>", data)


for node in nodes:

    username = re.findall(r"Username=\".+\" ", node)
    password = re.findall(r"Password=\".+\" ", node)[0]

    print(username, password)

data = base64.b64decode(sys.argv[1])

iv = data[:16]
passwordEnc = data[16:]

aes = AES.new(KEY, AES.MODE_CBC, iv)

passwordDec = aes.decrypt(passwordEnc)

print(passwordDec)