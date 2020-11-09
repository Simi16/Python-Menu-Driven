import os
import getpass

os.system("tput setaf  3")
print("\t\t\tWelcome to Docker")
os.system("tput  setaf  7")
print("\t\t\t---------------------")

os.system("tput  setaf  6")
r = input("Where to run this menu ? (local/remote) : ")
print(r)

while True:
	os.system("clear")
	os.system("tput  setaf  2")
	print("""
	\n
	Press 1 : To Install & Configure Docker.
	Press 2 : To download image.
	Press 3 : 
	Press 4 : For Logical Volume Partitions
	Press 5 : For Ansible
	Press 6 : To Exit
	""")

	os.system("tput  setaf  3")	
	ch = input("Enter Your Choice : ")

	if r == "local":	
		if int(ch) == 1:
			os.system("bash /root/arth/task8/idocker.sh")
		elif int(ch) == 2:
			os.system("bash /root/arth/task8/docker/image.sh")
		elif int(ch) == 3:
			print(" * * Configuring yum !! * *")
			os.system("yum repolist")
		elif int(ch) == 4:
			print(" * * Listing hard disks/storage !! * *")
			os.system("fdisk -l | less")
		elif int(ch) == 5:
			os.system("df -h")
		elif int(ch) == 6:
			os.system("hadoop-daemon.sh start datanode")
			os.system("jps")

