#!/bin/bash
tput setaf 6

echo "			To remove any Container(Stopped + Running). . . "
echo""
tput setaf 3
echo "Listing all containers: "
docker ps -a

echo""
echo "Enter Container name to remove:"
read r

echo""
echo "	Removing Container Permanently. . . "
docker rm $r

tput setaf 6
echo "			Container removed Successfully. . . ."
tput setaf 7
