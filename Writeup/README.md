![](./logo.png)

# USER

We can see from the `http-robots.txt` script that there is a `/writeup` endpoint

Content of the `robots.txt`

```
#              __
#      _(\    |@@|
#     (__/\__ \--/ __
#        \___|----|  |   __
#            \ }{ /\ )_ / _\
#            /\__/\ \__O (__
#           (--/\--)    \__/
#           _)(  )(_
#          `---''---`

# Disallow access to the blog until content is finished.
User-agent: * 
Disallow: /writeup/
```

Normal page has mention of `DoS` prevention
```
########################################################################
#                                                                      #
#           *** NEWS *** NEWS *** NEWS *** NEWS *** NEWS ***           #
#                                                                      #
#   Not yet live and already under attack. I found an   ,~~--~~-.      #
#   Eeyore DoS protection script that is in place and   +      | |\    #
#   watches for Apache 40x errors and bans bad IPs.     || |~ |`,/-\   #
#   Hope you do not get hit by false-positive drops!    *\_) \_) `-'   #
#                                                                      #
#   If you know where to download the proper Donkey DoS protection     #
#   please let me know via mail to jkr@writeup.htb - thanks!           #
#                                                                      #
########################################################################
```

This will stop the scanning of endpoints using `gobuster`

Reading around advised I install a tool called `wappalyzer` this gives information on the technologies used on the website.

The CMS used is `CMS Made Simple.`

Using an Unathenticated SQL Injection vulnerability from exploit-db we get the output:

```
[+] Salt for password found: 5a599ef579066807
[+] Username found: jkr
[+] Email found: jkr@writeup.htb
[+] Password found: 62def4866937f08cc13bab43bb14e6f7
```

Running the script with the crack options gives us:

```
[+] Password cracked: raykayjay9
```

This cannot be used to log onto the CMS but can be used over `ssh` to give us the `user.txt`!