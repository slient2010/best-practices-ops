#!/bin/bash
###############################################
# Author        : Nelson
# EMail         : os4uinfo@gmail.com
# Created Time  : 2021-03-10 14:07:44
# File Name     : use-ssh-to-expose-inner-service.sh
# Description   : Expose inner server to outside.
#                 Alternative, you can use autossh to keep reconnecting when the network interupt.
###############################################

public_ip="xxx.xxx.xxx.xxx"
remote_user="username"
local_ip="yyy.yyy.yyy.yyy"
remote_port="8088"
inner_port="22"

num=`ps aux |grep "ServerAliveInterval=180 ${remote_user}@${public_ip}"| grep ${remote_port} |grep -v grep |wc -l`
[ ${num} -eq 0 ] && ssh -o ServerAliveInterval=180  ${remote_user}@${public_ip} -p 22 -R 0.0.0.0:${remote_port}:${local_ip}:${inner_port} -fN
n=`sudo /sbin/iptables -L -n -t nat |grep ${inner_port}| grep -v grep |wc -l`
[ ${num} -eq 0 ] && sudo /sbin/iptables -t nat -A PREROUTING -d ${local_ip} -p tcp --dport ${inner_port} -j DNAT --to ${local_ip}:${inner_port}
