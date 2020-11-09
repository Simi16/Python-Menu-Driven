import os
import getpass
os.system("clear")
os.system("tput setaf  6")
print("\t\t* * * * * Welcome to Python Automation * * * * *")
print("\t\t------------------------------------------------")

os.system("tput  setaf  1")
passwd = getpass.getpass("Enter password: ")

if passwd != "00":
	print("Incorrect Password !!")
	exit()

while True:
	os.system("clear")
	os.system("tput setaf  6")
	print("\t\t* * * * * Welcome to Python Automation * * * * *")
	print("\t\t------------------------------------------------")

	os.system("tput  setaf  2")
	print("""
	\n
	Press 1 : For Basic Linux Commands
	Press 2 : For Partitions in Linux
	Press 3 : For Docker
	Press 4 : For Hadoop
	Press 5 : To Exit
	""")

	os.system("tput  setaf  3")	
	ch = input("Enter Your Choice : ")

	if int(ch) == 1:
			os.system("python3 /root/arth/task8/menu.py")
	elif int(ch) == 2:
			os.system("python3 /root/arth/task8/demo.py ")
	elif int(ch) == 3:
			os.system("python3 /root/arth/docker.py")
	elif int(ch) == 4:
			os.system("python3 /root/arth/task8/hadoop.py")
	elif int(ch) == 5:
			os.system("tput  setaf  7")
			exit()
	else:
		print("Not Supported")


	os.system("tput  setaf  5")
	input("\nPress Enter to continue . . . . . . . . . . . .")
	os.system("tput  setaf  7")

