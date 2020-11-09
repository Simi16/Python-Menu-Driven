import os
#import getpass


while True:
	os.system("clear")
	os.system("tput setaf  6")
	print("\t\t* * * * * Welcome to the Partiton Sub-Menu * * * * *")
	print("\t\t-----------------------------------------------------")
	os.system("tput  setaf  7")
	os.system("tput  setaf  2")
	print("""
	\n
	Press 1 : To Create Physical Partiton.
	Press 2 : To Format Partition.
	Press 3 : To Mount Partition.
        Press 4 : To Back for Partition Menu.
	Press 5 : To Exit.
	""")

	os.system("tput  setaf  3")	
	ch = input("Enter Your Choice : ")
	if int(ch) == 1:
		os.system("fdisk -l")
		k=input("Type Your Partion Name: ")
		os.system("tput  setaf  3")
		os.system("fdisk {}".format(k))
	elif int(ch) == 2:
		os.system("lsblk")
		k=input("Type Your Partion Name: ")
		os.system("mkfs.ext4 {}".format(k))
	elif int(ch) == 3:
		os.system("lsblk")
		k=input("Type Your Partion Name: ")			
		s=input("Enter Directory Name:")
		os.system("mkdir {}".format(s))
		os.system("mount {} {}".format(k,s))			
	elif int(ch) == 4:
		print("Successfully Back partiton Menu")
		os.system("python3 demo.py")		
	elif int(ch) == 5:
		os.system("tput  setaf  7")
		exit()
	else:
			print("Not Supported")


	os.system("tput  setaf  5")
	input("\nPress Enter to continue . . . . . . . . . . . .")
	os.system("tput  setaf  7")
