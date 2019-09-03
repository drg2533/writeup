cipher=open('cipher','r').read().split()[-1]

print(cipher)

flag=''
for i in range(5):
	flag+=cipher[6*i+3]
	flag+=cipher[6*i+5]
	flag+=cipher[6*i+4]
	flag+=cipher[6*i+0]
	flag+=cipher[6*i+2]
	flag+=cipher[6*i+1]

print(flag)