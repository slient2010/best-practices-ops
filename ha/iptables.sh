#!/bin/bash

/sbin/iptables -t nat -A POSTROUTING -o enp0s3 -j MASQUERADE
/sbin/iptables -A FORWARD -i enp0s3 -o enp0s8 -m state --state RELATED,ESTABLISHED -j ACCEPT
/sbin/iptables -A FORWARD -i enp0s8 -o enp0s3 -j ACCEPT

# /sbin/iptables -t nat -D POSTROUTING -o enp0s3 -j MASQUERADE
# /sbin/iptables -D FORWARD -i enp0s3 -o enp0s8 -m state --state RELATED,ESTABLISHED -j ACCEPT
# /sbin/iptables -D FORWARD -i enp0s8 -o enp0s3 -j ACCEPT

# /sbin/iptables -t nat -A POSTROUTING -o enp0s8 -j MASQUERADE
# /sbin/iptables -A FORWARD -i enp0s8 -o enp0s3 -m state --state RELATED,ESTABLISHED -j ACCEPT
# /sbin/iptables -A FORWARD -i enp0s3 -o enp0s8 -j ACCEPT

# /sbin/iptables -t nat -D POSTROUTING -o enp0s8 -j MASQUERADE
# /sbin/iptables -D FORWARD -i enp0s8 -o enp0s3 -m state --state RELATED,ESTABLISHED -j ACCEPT
# /sbin/iptables -D FORWARD -i enp0s3 -o enp0s8 -j ACCEPT

