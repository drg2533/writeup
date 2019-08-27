import string

cipher=open('cipher.txt','r').read()
flag_cipher=cipher[-49:-1]

flag='HackCTF'
flag_cipher=flag_cipher.upper()
flag=flag.upper()

for i in range(len(flag)):
	tmp=ord(flag[i])-ord(flag_cipher[i])
	if tmp <0 :
		tmp+=26
	print(tmp)
#22, 2, 16

key=[22,2,16]
flag=''
cnt=2
for i in cipher:
	if i in string.letters[:26]:
		tmp=ord(i)+key[cnt%3]
		if tmp > ord('z'):
			tmp-=26
		flag+=chr(tmp)
		cnt+=1
	elif i in string.letters[26:]:
		tmp=ord(i)+key[cnt%3]
		if tmp > ord('Z'):
			tmp-=26
		flag+=chr(tmp)
		cnt+=1
	else:
		flag+=i

print(flag)