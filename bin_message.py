# Binary-message
# Using list comprehesions

<<<<<<< HEAD
from textwrap import dedent


def to_binary(msg):
	""" Convert ASCII characters to binary representation. """
=======
text = raw_input("Enter your text message:\n")

def to_binary(msg):
	
>>>>>>> bdf04483848492f06677dcb9186610097093d134
	output = [format(ord(char), 'b') for char in msg]
	
	return ' '.join(output)
	
	
<<<<<<< HEAD
def to_text(msg):
	""" Convert binary representation in string to ASCII. """
=======
def to_string(msg):
	
>>>>>>> bdf04483848492f06677dcb9186610097093d134
	binaries = msg.split(' ')
	output = [chr(int(byte, 2)) for byte in binaries]
	
	return ''.join(output)


<<<<<<< HEAD
print("Welcome to Binary Message Machine.")

while True:
	
	print(dedent(
	"""
	### INFO ###
	Enter 'e' to convert your text to binary
	Or
	Enter 'd' to convert your binary string to normal text.
	Enter 'q' to quit.
	"""))
	
	choice = raw_input('> ')
	
	if choice == 'e':
		user_msg = raw_input("Enter your text message:\n")
		print(to_binary(user_msg))
	
	elif choice == 'd':
		user_msg = raw_input("Enter your binaries message:\n")
		print(to_text(user_msg))
		
	elif choice == 'q':
		break
	
	else:
		print("Please read the info..")
=======
# testing
binary_message = to_binary(text)

print(binary_message)
print(to_string(binary_message))
>>>>>>> bdf04483848492f06677dcb9186610097093d134
