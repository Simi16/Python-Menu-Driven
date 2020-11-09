#!/bin/bash

tput setaf 6
echo "				To Remove image. . . ."
echo ""
tput setaf 3
echo "Listing all available Images"
docker images

echo ""
echo "Enter image name to remove: "
read i

tput setaf 6
echo ""
echo "			Removing image forcefully. . . "
docker rmi -f $i

tput setaf  7

