#!/bin/bash

tput setaf 6
echo " * * * *  Installing Docker, Please wait...!! * * * * "

tput setaf 3
cd /etc/yum.repos.d/ &> /dev/null

wget download.docker.com/linux/centos/docker-ce.repo &> /dev/null

yum list docker-ce &> /dev/null

yum install docker-ce --nobest	&> /dev/null

systemctl start docker &> /dev/null

echo " "
rpm -q docker-ce

echo " "
tput setaf 6
echo "* * * * Successfully installed ..!! * * * *"
