from binascii import hexlify
from binascii import unhexlify
import sys
from sys import argv

script_name, information_file, transfer_file = argv

# Khai bao cac list se su dung de luu giu thong tin
name = []
age = []
job = []
phone = []
email = []

# list contain info se chua cac thong tin cua tung doi tuong sau khi da nhap thong tin cua doi tuong do xong va gan cho class
list_contain_info = []

# Class getting info dung de luu lai thong tin cua cac doi tuong
class Getting_info():
	def __init__(self, name, age, job, phone, email):
		self.name = name
		self.age = age
		self.job = job
		self. phone = phone
		self.email = email

# Encrypting and decrypting define.

def Delete_file_when_encrypt_them(information_file):
	target = open(information_file, 'w')
	target.truncate()
	target.close()

def Hex_encrypter(inputdata):
	encrypted_data = hexlify(inputdata)
	return encrypted_data

def Hex_decrypter(inputdata):
	decrypted_data = unhexlify(inputdata)
	return decrypted_data

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
	Delete_file_when_encrypt_them(information_file)
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

# End of EaD define.

def Checking(counter):
	print ""
	print "Do you want to continue ?"
	Choice = raw_input(">>> ")
	if Choice == "No":
		main()
	elif Choice == "Yes":
		Printing_info_by_step(counter)
	elif Choice == "No and exit":
		Exit_program()
	else:
		print "Wrong input please try again !"
		Checking(counter)

def Printing_info_by_step(counter):
	print ""
	print "List of objects is below."
	for i in range(counter):
		print "The %d one is: " % (i), list_contain_info[i].name
	
	print "Enter the number of object you want to know."
	Choice_of_name = int(raw_input(">>> "))
	
	for i in range(counter):
		if Choice_of_name == i:
			print ""
			print "*" * 70
			print "Name of object is: ", list_contain_info[i].name
			print "Age of object is: ", list_contain_info[i].age
			print "Job of object is: ", list_contain_info[i].job
			print "Phone number of object is: ", list_contain_info[i].phone
			print "Email of object is: ", list_contain_info[i].email
			print "*" * 70
			Checking(counter)
			
def Show_all_info(counter):
	for i in range(counter):
		print ""
		print "*" * 70
		print "Name of object is: ", list_contain_info[i].name
		print "Age of object is: ", list_contain_info[i].age
		print "Job of object is: ", list_contain_info[i].job
		print "Phone number of object is: ", list_contain_info[i].phone
		print "Email of object is: ", list_contain_info[i].email
		print "*" * 70

def Update_file(information_file, number_of_people):
	target = open(information_file, 'a')

	for i in range(number_of_people):
		print ""
		print "*" * 70
	
		print "Enter the name of object at here."
		Name = raw_input(">>> ")
		target.write(Name)
		target.write("\n")

		print "Enter the age of object at here."
		Age = raw_input(">>> ")
		target.write(Age)
		target.write("\n")

		print "Enter the job of object at here."
		Job = raw_input(">>> ")
		target.write(Job)
		target.write("\n")

		print "Enter the phone number of object at here."
		Phone_number = raw_input(">>> ")
		target.write(Phone_number)
		target.write("\n")

		print "Enter the email of object at here."
		Email = raw_input(">>> ")
		target.write(Email)
		target.write("\n")

	target.close()
		

def Delete_file(information_file):
	print "Do you want to delete all information in this file ?"
	Choice = raw_input(">>> ")
	if Choice == "Yes":
		target = open(information_file, 'w')
		target.truncate()
		target.close()
	elif Choice == "No":
		pass
	elif Choice == "No and exit":
		Exit_program()
	else: 
		print "Wrong input please try again !"
		print ""
		Delete_file(information_file)

def Password_checking():
	Read_and_unlock(transfer_file, information_file)
	Password_counter = 0
	Default_password = "Khongcopass"
	while True:
		print ""
		print "Enter your password at here."
		Password = raw_input(">>> ")
		print ""
		print "*" * 70
		Password_counter += 1
		if Password != Default_password:
			if Password_counter == 5:
				target = open(information_file, 'w')
				target.truncate()
				target.close()
				print "Information file was deleted because you are not an administrator."
				print "If you are permitted to access this file please contact the administrator at ndth090500@gmail.com."
				break
			print "Password is wrong please try again."
		else:
			main()
			break
			
def Reading_info(information_file):
	global Objects_counter 
	Objects_counter = 0
	target = open(information_file, 'r')
	
	while True:
		read_info = target.readline()
		name.append(read_info)

		read_info = target.readline()
		age.append(read_info)

		read_info = target.readline()
		job.append(read_info)

		read_info = target.readline()
		phone.append(read_info)

		read_info = target.readline()
		email.append(read_info)

		if not read_info:
			break

		Objects_counter += 1

	target.close()

	for i in range(Objects_counter):
		Object = Getting_info(name[i], age[i], job[i], phone[i], email[i])
		list_contain_info.append(Object)

def Exit_program():
	Read_and_lock(information_file, transfer_file)
	print "System is shutting down."
	raw_input()
	sys.exit(0)

def help_function():
	print ""
	print "Program instruction:"
	print "1: Use >>> Update file >>> if you want to update some informations"
	print "2: Use >>> Delete file >>> if you want to delete all information in this file."
	print "3: Use >>> Show me all >>> if you want to see quickly all necessary information."
	print "4: Use >>> Only one >>> if you want to see just one information only."
	print "5: Use >>> Done >>> if you want to quit this program."
	print "6: Use >>> Help me >>> if you need some helps."
	print ""

def main():
	while True:
		print "Enter command at here."
		command = raw_input(">>> ")
		if command == "Update file":
			print "Enter the number of people you want to add."
			num = int(raw_input(">>> "))
			Update_file(information_file, num)
		elif command == "Delete file":
			Delete_file(information_file)
		elif command == "Show me all":
			Reading_info(information_file)
			Show_all_info(Objects_counter)
		elif command == "Only one":
			Reading_info(information_file)
			Printing_info_by_step(Objects_counter)
		elif command == "Help me":
			help_function()
		elif command == "Done":
			Exit_program()
		else:
			print "Commands is not defined."

if __name__ == '__main__':
	Password_checking()
