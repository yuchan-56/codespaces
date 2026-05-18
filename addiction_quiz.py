from pwn import *

context.log_level = 'debug'

r = remote("host3.dreamhack.games", 23315)

for _ in range(50):
    a = int(r.recvuntil(b'+', drop=True))
    b = int(r.recvuntil(b'=?\n', drop=True))

    r.sendline(str(a + b).encode())

r.interactive()