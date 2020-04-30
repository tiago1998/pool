#!/bin/bash

if [[ $# -lt '5' ]]
then
	printf "use mode:\n\t$0 step steps display width height\n"
	exit 127
fi


function click() {
	echo "click display=$1 x=$2 y=$3"
#	export DISPLAY=:$1
#	xdotool mousemove $2 $3 click 1
}

step=$1
steps=$2
display=$3
width=$4
height=$5

printf "step=$step steps=$steps display=$display width=$width height=$height\n"

exit 0 #TODO fixes-needed

#scale
st=`expr $step + 1`
swidth=`echo $steps | cut -d ';' -f1 | cut -d '&' -f1 | cut -d '=' -f2`
sheight=`echo $steps | cut -d ';' -f1 | cut -d '&' -f2 | cut -d '=' -f2`
sxy=`echo $steps | cut -d ';' -f$st`


sx=`echo $sxy | cut -d '&' -f1 | cut -d '=' -f2`
sy=`echo $sxy | cut -d '&' -f2 | cut -d '=' -f2`


type bc > /dev/null 2> /dev/null || apt install -y bc > /dev/null

x=`echo "scale=2; $sx * $width / $swidth" | bc`
y=`echo "scale=2; $sy * $height / $sheight" | bc`


#click on display x y
click $display $x $y
