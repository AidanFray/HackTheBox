from Crypto.Cipher import AES
import base64
import sys
import re

KEY = b"\xc8\xa3\x9d\xe2\xa5\x47\x66\xa0\xda\x87\x5f\x79\xaa\xf1\xaa\x8c"

enc_pass = "w7nDgMKow73CuCU7XsOkScuGXsKrw51Rwq4="

data = base64.b64decode(enc_pass)

iv = data[:16]
password = data[16:]

padding = 16 - (len(password) % 16)

password_padded = password + b"\x00" * padding

aes = AES.new(KEY, AES.MODE_CBC, iv)

passwordDec = aes.decrypt(password_padded)

print(passwordDec)