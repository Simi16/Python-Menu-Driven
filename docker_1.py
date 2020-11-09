import os
import getpass

os.system("clear")
os.system("tput setaf  6")
print("\t\t\t* * * * Welcome to Docker * * * * ")
os.system("tput  setaf  7")
print("\t\t\t---------------------------------")

while True:
	os.system("clear")
	os.system("tput setaf  6")
	print("\t\t\t* * * * Welcome to Docker * * * * ")
	os.system("tput  setaf  7")
	print("\t\t\t---------------------------------")
	os.system("tput  setaf  2")
	print("""
	\n
	Press 1 : To Install & Configure Docker.
	Press 2 : To download image of Container.
	Press 3 : To list all images.
	Press 4 : To list all available containers.
	Press 5 : To launch New Container.
	Press 6 : To launch Stopped Container.
	Press 7 : To Remove Container.
	Press 8 : To Remove Image.
	Press 9 : To Remove all Containers.
	Press 10 : To Exit.
	""")

	os.system("tput  setaf  3")	
	ch = int(input("Enter Your Choice : "))

	if ch == 1:
		os.system("bash /root/arth/task8/docker/idocker.sh")
	elif ch == 2:
		os.system("bash /root/arth/task8/docker/image.sh")	    
	elif ch == 3:
		os.system("docker images")
	elif ch == 4:
		os.system("docker ps -a")
	elif ch == 5:
		os.system("bash /root/arth/task8/docker/launchc.sh")
	elif ch == 6:
		os.system("bash /root/arth//task8/docker/run.sh")
	elif ch == 7:
		os.system("bash /root/arth/task8/docker/remove.sh")
	elif ch == 8:
		os.system("bash /root//arth/task8/docker/rmimage.sh")
	elif ch == 9:
		os.system("docker rm `docker ps -a -q`")	
		os.system("")
	elif ch == 10:
		exit()
	else:
		print("Not Supported")



	os.system("tput  setaf  5")
	input("\nPress Enter to continue . . . . . . . . . . . .")
	os.system("tput  setaf  7")


