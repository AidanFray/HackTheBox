![](./logo.png)

# USER

`nmap` scan shows a `http` endpoint. Links redirect to `apocalyst.htb`. Going to add to the `/etc/hosts` file

`http://10.10.10.46` server seems to have a weird endpoint where english words are redirected to a page with an image


We have a `/department` endpoint with a login. Looking at the source we can see a message:

```
<!-- @admin! MySQL is been installed.. please fix the login page! ~amrois -->
```

BULLSHIT: Only on the `/Rightiousness​` you can find an stego image. Not on the other endpoints

Running `steghide` on the weird image gives us a wordlist

Found a username using ``WPScan``

Using the word list we found ealier with the username we found the combination:

```
falaraki:Transclisiation
```

On the Wordpress site we upload a simple malicious plugin to get shell!

# ROOT

In the `/home` there is a `.secret` that gives the user password

Running `LinEnum.sh` we can see we have `rw` on the `/etc/passwd`!

To create a password hash:
```
openssl passwd -1 password1
```

Giving us:

```
$1$ht4ERcPM$HSTZjvt10wlym/G8bwHaA/
```

Adding this to the end of the `passwd` file:

```
user:\$1\$ht4ERcPM\$HSTZjvt10wlym/G8bwHaA/:0:0:root:/root:/bin/bash
```

Gives us the ability to login as root!