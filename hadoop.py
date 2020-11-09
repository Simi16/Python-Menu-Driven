import os

a = input("Configure Namenode or Datanode: ")

print(a)

if a == "Namenode":
	ip = os.system("ifconfig enp0s3")
	print("IP of namenode : {}".format(ip))
	os.system("rm /etc/hadoop/hdfs-site.xml;rm /etc/hadoop/core-site.xml")
	dir = input("Enter directory name with path: ")
	os.system("mkdir {}".format(dir)) 
	NN_IP = input("Enter Namenode IP : ")
	datafile=open("/etc/hadoop/hdfs-site.xml", 'w')
	datafile.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?> 
<!-- Put site-specific property overrides in this file.-->


<configuration>
<property>
<name>dfs.name.dir</name>
<value>{dir}</value>
</property> 
</configuration>''')
	datafile1=open("/etc/hadoop/core-site.xml", 'w')
	datafile1.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?> 
<!-- Put site-specific property overrides in this file.-->


<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{NN_IP}:9001</value>
</property> 
</configuration>''')

	os.system("systemctl stop firewalld")
	os.system("systemctl disable firewalld")
	os.system("hadoop namenode -format")
	os.system("hadoop-daemon.sh start namenode;jps")
	
	os.system("tput setaf 6")
	print("\n\n--------Namenode Started---------")
	
	os.system("tput setaf 3")
elif a == "Datanode":
	NN_IP = input("Enter Namenode IP")
	os.system("rm /etc/hadoop/hdfs-site.xml;rm /etc/hadoop/core-site.xml")
	datadir = input("Enter directory name with path: ")
	os.system("mkdir {}".format(datadir)) 
	datafile=open("/etc/hadoop/hdfs-site.xml", 'w')
	datafile.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?> 
<!-- Put site-specific property overrides in this file.-->


<configuration>
<property>
<name>dfs.data.dir</name>
<value>{datadir}</value>
</property>
</configuration>''')
	datafile1=open("/etc/hadoop/core-site.xml", 'w')
	datafile1.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?> 
<!-- Put site-specific property overrides in this file.-->


<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{NN_IP}:9001</value>
</property> 
</configuration>''')

	os.system("systemctl stop firewalld")
	os.system("systemctl disable firewalld")
	os.system("rm -rf {}".format(datadir))
	os.system("mkdir {}".format(datadir))
	os.system("hadoop-daemon.sh start datanode;jps")

	print("\n\n--------Datanode Started---------")


else:
	print("Tata Bye Bye")	              

