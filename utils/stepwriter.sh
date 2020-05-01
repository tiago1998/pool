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
	
while :
do
	printf "${blue}step${normal}: " && read one_step
	echo "$one_step" | grep -i "done|exit" > /dev/null && break
	echo "$one_step" | grep -iE "x=|delay=|text=" > /dev/null && {
		step="$step;$one_step"
	} || {
		printf "${green}exp-1.1: ${cyan}text=\${random_number} word\n"
		printf "${green}exp-1.2: ${cyan}text=\${random_number} \${random_text[n]} (n=size of text)\n"
		printf "${green}exp-1.3: ${cyan}text=hello world\n"
		printf "${green}exp-2: ${cyan}x=10&y=10\n"
		printf "${green}exp-2: ${cyan}delay=10\n"
		printf "${green}exp-3: ${cyan}done\n"
		printf "${green}exp-3: ${cyan}exit\n"
	} 
done

echo $step >> $1
