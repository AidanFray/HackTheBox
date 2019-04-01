# HELP
10.10.10.121

# USER
Using DirBuster I found

```
http://10.10.10.121/support/
```

Further down there is a 
```
http://10.10.10.121/support/ticket/
```

Where you can submit files. 

The files are renamed by:

```
md5hash(filename+time).fileExtension
```

By uploading a file with a NULL (x00) between we're able to circumvent the file extension check and upload a
reverse shell

Navigating to this new found file name runs the reverse shell

# ROOT

The exploit for root is a kernel exploit found in ```kernel_priv_esc.c```