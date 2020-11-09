#!/bin/bash
tput setaf 6
echo "	* * *	To launch any container, first select the image : * * * "
tput setaf 3
echo "Listing available images:"
docker images

echo ""
echo "Enter Image name with version(eg.: ubuntu:14.04):"
read i
echo""
echo "Give name of your container: " 
read n

tput setaf 6
echo "			  Letting you inside the Container...."
tput setaf 3
docker run -it --name $n $i 
