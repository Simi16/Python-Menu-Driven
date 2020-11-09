import os
os.system("tput setaf  6")
print("\t\t* * * * * Welcome to Partition Main Menu * * * * * ")
print("\t\t----------------------------------------------------")
os.system("tput  setaf  3")
while True:
	os.system("clear")
	os.system("tput  setaf  2")
	print("""
	\n
	Press 1 : To Create Partiton
	Press 2 : To Check Disk Space
	Press 3 : To see all the information about block devices.
	Press 4 : To Back to Main Menu
	Press 5 : To Exit
	""")
	os.system("tput  setaf  3")	
	ch = input("Enter Your Choice : ")
	if int(ch) == 1:
		os.system("python3 /root/arth/task8/phycial_partition.py ")
	elif int(ch) == 2:
		os.system("df -h")
	elif int(ch) == 3:
		os.system("lsblk")			
	elif int(ch) == 4:
		print("Back to Main Menu")
		os.system("python3 /root/arth/task8/main.py")		
	elif int(ch) == 5:
		os.system("tput  setaf  7")
		exit()
	else:
			print("Not Supported")


	os.system("tput  setaf  5")
	input("\nPress Enter to continue . . . . . . . . . . . .")
	os.system("tput  setaf  7")


