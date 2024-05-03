import sys
from pwn import *

BINARY_NAME = ""
IP = ""
PORT = 6969
OFFSET = 16

elf = context.binary = ELF(BINARY_NAME)

if len(sys.argv) > 1:
    p = remote(IP, PORT)
else:
    p = process()
    context.terminal = ['tmux', 'splitw', '-h']
    # TODO: gdb.attach(p, gdbscript="break *function+line\ncontinue")

payload = b'A' * OFFSET

p.clean()
p.sendline(payload)
p.interactive()
