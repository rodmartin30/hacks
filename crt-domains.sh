#!/bin/bash

# Get the domains from crs.sh

if [ "$#" -ne 2 ]; then
	echo "Illegal number of parameters"
	echo "example: COMMAND target.com target"
	exit 1
fi;

curl -s https://crt.sh/\?q\=%25.$1 > $1.txt
cat $1.txt | grep -oi ">[a-z0-9\.\-]*$2\....\?<" | sed 's/^.//' | sed 's/^\*//' | sed 's/.$//' | sort -u | tee $1-domains.txt

