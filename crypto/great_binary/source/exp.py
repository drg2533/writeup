cipher=open('hoooo.txt','r').read()
cipher=cipher.split()

key=''
for i in cipher:
	key+=chr(int(i,2))
print(key)