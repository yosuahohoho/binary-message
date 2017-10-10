# BinaryCode, Convert your message to binary representation

text = raw_input("Enter the text message:\n")

def to_binary(msg):
	
	for char in msg:
		char_code = ord(char)
		binary = format(char_code, 'b')
		output.append(binary)
	
	return ' '.join(output)

def to_string(msg):
	
	binaries = msg.split(' ')
	output = []
	
	for bit in binaries:
		char_code = int(bit,2)
		char = chr(char_code)
		output.append(char)
		
	return ''.join(output)

#print(to_string(text))
print(to_binary(text))
