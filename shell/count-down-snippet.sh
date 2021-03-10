#!/bin/bash
###############################################
# Author        : Nelson
# EMail         : os4uinfo@gmail.com
# Created Time  : 2021-03-10 13:56:37
# File Name     : count-down-snippet.sh
# Description   : 
###############################################

function count_down() {
	for n in {10..1}; do
		printf "\r%s " $n
		sleep 1
	done
}

count_down
