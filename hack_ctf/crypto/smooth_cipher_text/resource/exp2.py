import string
cipher=open('cipher.txt').read().split('{')[1][:-2]


alpha=string.letters

for i in range(26):
	cnt=0
	key=[11,i,0]
	print(key)
	flag=''
	for ch in cipher:
		if ch in alpha:
			if ord(ch) - key[cnt%3] < ord('a'):
				flag+=chr(ord(ch)+26-key[cnt%3])
				cnt+=1
			else:
				flag+=chr(ord(ch)-key[cnt%3])
				cnt+=1
		else:
			flag+=ch
	print(flag)