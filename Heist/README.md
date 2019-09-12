![](./logo.png)

# USER

The box has exposed a `http` endpoint with a login page. On further inspection the page allows us to log on as a guest.

We are then redirected to a page with a support chat. On it is a link to a Cisco IOS config file. Via some searching it is found that the passwords present can be easily decrypted using this [page](http://www.ifm.net.nz/cookbooks/passwordcracker.html)

Meaning these:
```
[..]
username rout3r password 7 0242114B0E143F015F5D1E161713
username admin privilege 15 password 7 02375012182C1A1D751618034F36415408
[..]
```

Can be converted into these:
```
rout3r:$uperP@ssword
admin:Q4)sJu\Y8qz*A3?d
```

This is due to a trivially reverseable algorithm being used to 'encrypt' the passwords


```
enable secret 5 $1$pdQG$o8nrSzsGXeaduXrjlvKc91
```

Cracking the level 5 password involves running it through rockyou. The command below was used:

```
openssl passwd -1 -salt <SALT> -table -in <rockyou.txt> | grep <hash_substring>
```

The cracking of this password gives:

```
stealth1agent	$1$pdQG$o8nrSzsGXeaduXrjlvKc91
```

This can be used with the username `hazard` to log into the SMB share.


# LINKS
https://github.com/Hackplayers/evil-winrm
