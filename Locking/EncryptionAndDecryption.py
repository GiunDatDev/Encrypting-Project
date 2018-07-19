from binascii import hexlify
from binascii import unhexlify
import sys 
from sys import argv
script, information_file, transfer_file = argv

def Hex_encrypter(inputdata):
	encrypted_data = hexlify(inputdata)
	return encrypted_data

def Hex_decrypter(inputdata):
	decrypted_data = unhexlify(inputdata)
	return decrypted_data

def Delete_file(information_file):
	target = open(information_file, 'w')
	target.truncate()
	target.close()

def Read_and_lock(information_file, transfer_file):
	target = open(information_file, 'r')
	transfer = open(transfer_file, 'w')

	while True:
		read_info = target.readline()
		The_data_returned = Hex_encrypter(read_info)
		transfer.write(The_data_returned)

		if not read_info:
			break
	target.close()
	Delete_file(information_file)
	transfer.close()

def Read_and_unlock(transfer_file, information_file):
	target = open(transfer_file, 'r')
	transfer = open(information_file, 'w')

	while True:
		read_info = target.readline()
		The_data_returned = Hex_decrypter(read_info)
		transfer.write(The_data_returned)

		if not read_info:
			break
	target.close()
	transfer.close()

def main():
	print "Enter command at here."
	command = raw_input(">>> ")

	if command == "Encrypting":
		Read_and_lock(information_file, transfer_file)
	elif command == "Decrypting":
		Read_and_unlock(information_file, transfer_file)
	else: 
		print "Please check your input again."
		main()	

if __name__ == '__main__':
	main()