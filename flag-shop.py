from pwn import *

context.log_level = 'debug'

r = remote("host8.dreamhack.games", 9354)

for _ in range(50):
    a = r.recvuntil(b'. flag', drop=True).decode()[-1]
    r.sendline(a.encode())

r.interactive()