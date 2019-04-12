![](./logo.png)

# USER

Initially scanning the box with nmap it can be seen that there're a lot of open ports. 

I will begin to enumerate them.

### SMB

```
$ smbclient -L 10.10.10.125

Enter WORKGROUP\main_user's password: 


	Sharename       Type      Comment
	---------       ----      -------
	ADMIN$          Disk      Remote Admin
	C$              Disk      Default share
	IPC$            IPC       Remote IPC
	Reports         Disk      
```