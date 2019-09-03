import string

flag=''

for i in cipher:
	if i in string.letters[:26]:
		tmp=ord(i)-7
		if tmp < ord('a'):
			tmp+=26
		flag+=chr(tmp)
	elif i in string.letters[26:]:
		tmp=ord(i)-7
		if tmp < ord('A'):
			tmp+=26
		flag+=chr(tmp)
	else:
		flag+=i
print(flag)