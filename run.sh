#!/bin/bash
tput setaf 6
echo "			To launch an stopped container. . . . "
echo ""
tput setaf 3
echo "Listing Stopped containers: "
docker ps -f "status= exited"
echo""
echo "Name of stopped container to start: "
read n

echo""
tput setaf 1
echo "Starting the container. . ."
docker start $n

echo""
tput setaf 6
echo "		Container started, Letting you inside the container. . . . "
tput setaf 7
docker attach $n
