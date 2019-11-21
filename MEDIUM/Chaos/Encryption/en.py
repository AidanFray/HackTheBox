from Crypto.Hash import SHA256
from Crypto.Cipher import AES
import Crypto.Random as Random
import base64
import os

path = "/home/user/Documents/Chaos/Encryption/"


def encrypt(key, filename):
    chunksize = 64*1024
    outputFile = "en_" + filename
    filesize = str(os.path.getsize(path + filename)).zfill(16)
    IV = Random.new().read(16)

    encryptor = AES.new(key, AES.MODE_CBC, IV)

    with open(path + filename, 'rb') as infile:
        with open(path + outputFile, 'wb') as outfile:
            outfile.write(filesize.encode('utf-8'))
            outfile.write(IV)

            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - (len(chunk) % 16))

                outfile.write(encryptor.encrypt(chunk))


def getKey(password):
    hasher = SHA256.new(password.encode('utf-8'))
    return hasher.digest()


def decrypt(key, filename):

    chunksize = 64*1024
    outputFile = "de_" + filename

    output = b""

    with open(path + filename, 'rb') as infile:

            # Reads the file name
            filesize = int(infile.read(16))
            IV = infile.read(16)

            dAES = AES.new(key, AES.MODE_CBC, IV)

            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break
                
                # Padding?
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - (len(chunk) % 16))

                output += dAES.decrypt(chunk)

            return output

x = decrypt(getKey("sahay"), "enim_msg.txt")

b64 = base64.b64decode(x.decode("utf-8").strip())

print(b64.decode("utf-8"))
