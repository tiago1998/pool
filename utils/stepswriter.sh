#!/bin/bash


if [[ $# -lt 4 ]]
then
	printf "use mode:\n\t$0 list-links width height list-cordinates\n"
	exit 127
fi

links=$1
width=$2
height=$3
cordinates=$4

[[ -f $links ]] || echo "file $link not exists"
[[ -f $cordinates ]] || echo "file $cordinates not exists"

for link in `cat $links`
do
	echo "$link:width=$width&height=$height;`cat $cordinates`"
done
