# Binary-message
# Using list comprehesions

text = raw_input("Enter your text message:\n")

def to_binary(msg):
	
	output = [format(ord(char), 'b') for char in msg]
	
	return ' '.join(output)
	
	
def to_string(msg):
	
	binaries = msg.split(' ')
	output = [chr(int(byte, 2)) for byte in binaries]
	
	return ''.join(output)


# testing
binary_message = to_binary(text)

print(binary_message)
print(to_string(binary_message))
