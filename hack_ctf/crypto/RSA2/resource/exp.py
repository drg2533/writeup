import gmpy2

n=675517326695494061190287679557796696358902817969424171685361
c=0xe3712876ea77c308083ef596a32c5ce2d7edf22abbc58657e

p=804811499343607200702893651293
q=839348502408870119614692320677

e=65537

phiN=(p-1)*(q-1)
d=gmpy2.powmod(e,-1,phiN)

key=gmpy2.powmod(c,d,n)
print(hex(key)[2:].decode('hex'))