#!/bin/bash

normal="\033[0m"
red="\033[31m"
green="\033[32m"
yellow="\033[33m"
blue="\033[34m"
purple="\033[35m"
cyan="\033[36m"

if [[ $# -ne 1 ]]
then
	printf "use mode:\n\t$0 file.out\n"
	exit 127
fi

end() {
	printf "${normal}\r\033[J aborted\n"
	exit 127
}

trap end SIGINT SIGTERM

printf "${blue}link${normal}: " && read link
printf "${blue}display width${normal}: " && read width
printf "${blue}display height${normal}: " && read height
step="$link;width=$width&height=$height"
	
printf "${green}tap help or ? to see exaples!\n"
while :
do
	printf "${blue}step${normal}: " && read one_step
	echo "$one_step" | grep "exit" > /dev/null && break
	echo "$one_step" | grep -E "help|\?" > /dev/null && {
		printf "${green}exp-1: ${cyan}x=10&y=10\n"
		printf "${green}exp-2: ${cyan}delay=10\n"
		printf "${green}exp-3: ${cyan}exit\n"
	} 
	echo "$one_step" | grep -E "x|delay" > /dev/null && {
		step="$step;$one_step"
	}
done

echo $step >> $1
