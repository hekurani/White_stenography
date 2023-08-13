import re
import time
from termcolor import colored

class snow:
	def __init__(this, fileName, message):
		this.fileName = fileName
		this.message = message

	def embedMessage(this):
		startTime = time.time()
		encodedMessage = encodeMessage(this.message)
		
		# Check if the message is longer than the available space
		if (len(encodedMessage) > this.countSpaces()):
			print(colored("The message is too long to embed in the text.", 'light_red'))
			return
			
		# Read the contents of the file and store them
		with open(this.fileName, "r") as file:
			content = file.read()
	
		# Loop through the array and replace each space character with an array element
		j = 0
		for i in range(len(content)):
			if (content[i] == " "):
				if (j < len(encodedMessage)):
					# Copy the content before and after the whitespace and add an element in the middle 
					content = content[:i] + encodedMessage[j] + content[i+1:]
					j += 1
				else:
					break
				
		# Write back the new contents to the file
		with open("output.txt", "w") as file:
			file.write(content)	

		print(colored("Text hidden successfully!", 'light_green'))
		print("Time elapsed: %s seconds" % (time.time() - startTime))

	def extractMessage(this):
		with open("output.txt", "r") as file:
			content = file.read()

		whitespaceArray = re.findall(r"[ \t]", content)
		# Iterate through array and create an array with subarrays consisting of 8 elements
		groupedArray = [ whitespaceArray[n:n+8] for n in range(0, len(whitespaceArray), 8) ]
		
		byte = ''
		byteArray = []
		# Convert every whitespace to it's corresponding bit
		for item in groupedArray:
			for i in range(len(item)):
				byte += toBit(item[i])
				
			byteArray.append(byte)
			byte = ''

		# Go through the array and convert every binary string to an ascii character
		extractedMessage = ''
		for byte in byteArray:
			extractedMessage += chr(int(byte, 2))

		return extractedMessage

	def countSpaces(this):
		with open(this.fileName, "r") as file:
			contents = file.read()
			# Count the amount of space characters
			whitespaces = contents.count(" ")
		return whitespaces
	
	
def encodeMessage(message):
	binaryArray = []
	encodedMessage = []

	for char in message:
		# Convert character to integer ascii value
		asciiValue = ord(char)
		# Convert integer to binary number, remove the 'Ob' prefix and fill with padding to make 8 bits
		binaryCharacter = bin(asciiValue)[2:].zfill(8)
		# Add to the array
		binaryArray.append(binaryCharacter)
	# Convert the binary array to an array of whitepace characters
	for byte in binaryArray:
		for bit in byte:
			encodedMessage.append(toWhiteSpace(bit))

	return encodedMessage

def toWhiteSpace(bit):
	# Spaces represent a 0 and tabs represent a 1
	if (bit == '1'):
		return '\t'
	else:
		return ' '
	
def toBit(whitespace):
    # Spaces represent a 0 and tabs represent a 1
    if whitespace == '\t':
        return '1'
    else:
        return '0'
