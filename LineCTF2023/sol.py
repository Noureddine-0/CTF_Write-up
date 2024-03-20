#The initial key is not that , it got transformed and we got that
key  =  'm4g1KaRp_ON_7H3_Hook'

output = [0]*41
compare_with = L = [0xD0,0xBE,0x9F,0x5A,0xBD,0xF0,0x34,0xB5,0xD0,0x6F,0xFB,0xE2,0x99,0xBA,0xAE,0xD7,0x36,0xD5,0x2D,0xC2,0x22,0x45,0xB0,0x03,0x9D,0x63,0x66,0x53,0xC7,0x28,0xCC,0x2A,0x2B,0x14,0xBB,0x09,0x9B,0xE3,0x60,0x46,0x3A]



#first transformation is a xor
def first(char):
	return char ^ 0x21

#Second transformation is executed on the exception handler
def second(char):
	return ((char >> 5 ) | (8*char)) %256

#Third trandformation is after the return of the exception handler and is a simple substraction

def third(char):
	return (char -34) % 256

#Initial permuation of RC4 algorithme
S = [i for i in range(256)]
K = [ord(key[i%len(key)]) for i in range(256)]

j = 0
for i in range(256):
	j = (j + S[i] + K[i]) %256
	S[i] ,S[j] = S[j] ,S[i]


#start bruteforcing
v12 = 0
v11 = 0
for i in range(41):
	saved_v12 = v12
	saved_v11 = v11
	saved_S = S[:]
	for char in range(32 , 128):
		transformed_char = third(second(first(char)))
		v12 = v12+1
		v11 = (S[v12] + v11) % 256
		v9 = S[v12]
		S[v12] = S[v11]
		S[v11]=v9
		v8 = S[(S[v12]+S[v11]) % 256]
		output[i] = ((v11 - 24 ) ^ v8 ^ transformed_char) % 256
		if (output[i] == compare_with[i]):
			print(chr(char),end="")
			break
		v12 = saved_v12
		v11 = saved_v11
		S = saved_S[:]
