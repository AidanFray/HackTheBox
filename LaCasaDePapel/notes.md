# LaCasaDePapel

10.10.10.131

# User

After an nmap scan it can be seen that the server is running vsftpd 2.3.4.
This version has a ```:)``` backdoor.

Msfconsole:
```
exploit/unix/ftp/vsftpd_234_backdoor
```

This opens the port ```6200``` to give us:

```
Psy Shell v0.9.9 (PHP 7.2.10 â cli) by Justin Hileman
```

This seems like a debugging cli for PHP