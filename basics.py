import os
import getpass

os.system("clear")
os.system("tput setaf  6")
print("\t\t* * * * * Welcome to Linux Basic Commands * * * * *")
os.system("tput  setaf  7")
print("\t\t---------------------------------------------------")


os.system("tput  setaf  1")
passwd = getpass.getpass("Enter password: ")

if passwd != "00":
	print("Incorrect Password !!")
	exit()
os.system("tput  setaf  6")
r = input("Where to run this menu ? (local/remote) : ")
print(r)

while True:
	os.system("clear")
	os.system("tput  setaf  2")
	print("""
	\n
	Press 1 : To see the Running PORTS
	Press 2 : To Configure Webserver(Apache httpd)
	Press 3 : To Configure yum
	Press 4 : To see attached hdd/storage.
	Press 5 : To see the Mounted Partitions
	Press 6 : To 
	Press 7 : To check info of Docker
	Press 8 : To list the Running Containers	
	Press 9 : To list stopped+running Containers
	Press 10 : To list Container Images
	Press 11 : To Login to AWS CLI
	Press 12 : To Open Python Prompt
	Press 13 : To Open Calculator
	Press 14 : To Exit
	""")

	os.system("tput  setaf  3")	
	ch = input("Enter Your Choice : ")

	if r == "local":	
		if int(ch) == 1:
			os.system("netstat -tnlp")
		elif int(ch) == 2:
			os.system("bash /root/partition.sh|less")
		elif int(ch) == 3:
			print(" * * Configuring yum !! * *")
			os.system("yum repolist")
		elif int(ch) == 4:
			print(" * * Listing hard disks/storage !! * *")
			os.system("fdisk -l | less")
		elif int(ch) == 5:
			os.system("df -h")
		elif int(ch) == 6:
			
		elif int(ch) == 7:
			os.system("docker info |less")				
		elif int(ch) == 8:
			os.system("docker ps")				
		elif int(ch) == 9:
			os.system("docker ps -a")				
		elif int(ch) == 10:
			os.system("docker images")				
		elif int(ch) == 15:
			os.system("aws configure")
			print("AWS CLI is configured...!!")
		elif int(ch) == 18:
			os.system("tput  setaf  7")
			print("Opening python prompt: ")
			os.system("tput  setaf  3")
			os.system("python3")		
		elif int(ch) == 19:
			print("Opening Calculator: ")
			os.system("bc")	
		elif int(ch) == 20:
			os.system("tput  setaf  7")
			exit()
		else:
			print("Not Supported")

	elif r == "remote":
		ip = input("Enter remote ip : ")
		print(ip)
		if int(ch) == 1:
			os.system("ssh {} netstat -tnlp".format(ip))
		elif int(ch) == 2:
			os.system("ssh {} bash /root/partition.sh|less".format(ip))
		elif int(ch) == 3:
			print(" * * Configuring yum !! * *")
			os.system("ssh {} yum repolist ".format(ip))
		elif int(ch) == 4:
			print(" * * Listing hard disks/storage !! * *")
			os.system("ssh {} fdisk -l | less".format(ip))
		elif int(ch) == 5:
			os.system("ssh {} fdisk -l".format(ip))
		elif int(ch) == 6:
			os.system("ssh{}  hadoop-daemon.sh start datanode".format(ip))
			os.system("jps")
		elif int(ch) == 7:
			os.system("ssh {} docker info | less".format(ip))
		elif int(ch) == 8:
			os.system("ssh {} docker ps".format(ip))
		elif int(ch) == 9:
			os.system("ssh {} docker ps -a".format(ip))
		elif int(ch) == 10:
			os.system("ssh {} docker images".format(ip))
		elif int(ch) == 15:
			os.system("ssh {} aws configure".format(ip))
			print("AWS CLI is configured...!!")
		elif int(ch) == 18:			
			os.system("tput  setaf  7")			
			print("Opening python prompt: ")
			os.system("tput  setaf  3")
			os.system("ssh {}  python3".format(ip))		
		elif int(ch) == 19:
			print("Opening Calculator: ")
			os.system("ssh {}  bc".format(ip))		
		elif int(ch) == 20:
			os.system("tput  setaf  7")
			exit()		
		else:
			print("Not Supported")

	else:
		print("not valid options ...")


	os.system("tput  setaf  5")
	input("\nPress Enter to continue . . . . . . . . . . . .")
	os.system("tput  setaf  7")

