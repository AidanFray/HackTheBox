# USB Ripper

```
There is a sysadmin, who has been dumping all the USB events on his Linux host all the year... Recently, some bad guys managed to steal some data from his machine when they broke into the office. Can you help him to put a tail on the intruders? Note: once you find it, "crack" it. 
```

The challenge involves a `auth.json` that contains three lists of `manafactuer`, `product` and `serial` numbers. The next file is the `syslog`. This contains a log of devices connected to the computer.

We need to scan through and check for the presence of all in the `auth.json`.

Doing this with the `check.py` script we get the value:

```
71DF5A33EFFDEA5B1882C9FBDC1240C6
```

Cracking this gives us the string:

```
mychemicalromance
```


```
FLAG: HTB{mychemicalromance}
```