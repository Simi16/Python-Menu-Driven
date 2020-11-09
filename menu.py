import os
import getpass

os.system("clear")
os.system("tput setaf  6")
print("\t\t* * * * * Welcome to Linux Basic Commands * * * * *")
os.system("tput  setaf  7")
print("\t\t---------------------------------------------------")

while True:
	os.system("clear")
	os.system("tput setaf  6")
	print("\t\t* * * * * Welcome to Linux Basic Commands * * * * *")
	os.system("tput  setaf  7")
	print("\t\t---------------------------------------------------")
	os.system("tput  setaf  3")
	print("""
	\n
	Press 1 : To see Current Time 
	Press 2 : To Configure Yum repolist
	Press 3 : To see attached hdd/storage
	Press 4 : To see Total amount of memory
	Press 5 : To see the running ports
	Press 6 : To check info of Docker
	Press 7 : To Open Python Prompt
	Press 8 : To Open Calculator
	Press 9 : To Open Firefox
	Press 10 : To Open Text Editor
	Press 11 : To Exit
	""")

	os.system("tput  setaf  7")	
	ch = input("Enter Your Choice : ")

	if int(ch) == 1:
		os.system("date +%T")
	elif int(ch) == 2:
		print(" * * Configuring yum !! * *")
		os.system("yum repolist")
	elif int(ch) == 3:
		print(" * * Listing hard disks/storage !! * *")
		os.system("fdisk -l | less")
	elif int(ch) == 4:
		os.system("free")
	elif int(ch) == 5:
		os.system("netstat -tnlp")
	elif int(ch) == 6:
		os.system("docker info | less")
	elif int(ch) == 7:
		os.system("python3")				
	elif int(ch) == 8:
		os.system("bc")				
	elif int(ch) == 9:
		os.system("firefox")				
	elif int(ch) == 10:
		os.system("gedit")
	elif int(ch) == 11:
		os.system("tput  setaf  7")
		exit()
	else:
		print("Not Supported")


	os.system("tput  setaf  5")
	input("\nPress Enter to continue . . . . . . . . . . . .")
	os.system("tput  setaf  7")

