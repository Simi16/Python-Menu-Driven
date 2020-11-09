#!/bin/bash

echo -n  "Enter the Image name : "
read i

docker pull $i
