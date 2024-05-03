import sys
from pwn import *

BINARY_NAME = ""
IP = ""
PORT = 6969
OFFSET = 16

elf = context.binary = ELF(BINARY_NAME)

if len(sys.argv) > 1:
    p = remote(IP, PORT)
    context.terminal = ['tmux', 'splitw', '-h']
    gdb.attach(p, gdbscript="break *bof+25\ncontinue")
else:
    p = process()

payload = b'A' * OFFSET

p.clean()
p.sendline(payload)
p.interactive()
