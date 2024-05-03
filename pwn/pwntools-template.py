import sys
from pwn import *

BINARY_NAME = ""
CONN_ADDR = ""
OFFSET = 16

elf = context.binary = ELF(BINARY_NAME)

if len(sys.argv) > 1:
    ip = CONN_ADDR.split(" ")[0]
    port = int(CONN_ADDR.split(" ")[1])
    p = remote(ip, port)
else:
    p = process()
    context.terminal = ['tmux', 'splitw', '-h']
    # TODO: gdb.attach(p, gdbscript="break *function+line\ncontinue")

payload = b'\x69' * OFFSET

p.clean()
p.sendline(payload)
p.interactive()
