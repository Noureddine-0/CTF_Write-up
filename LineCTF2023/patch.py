content  = open("fishing.exe","rb").read()
content =  bytearray(content)


for i in range(len(content)):
	if content[i:i+2] == b'\xeb\xff':
		for j in range(3):
			content[i+j] = 0x90

with open("patched.exe" , 'wb') as f :
	f.write(bytes(content))
