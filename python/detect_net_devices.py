#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###############################################
# Author        : Nelson
# EMail         : os4uinfo@gmail.com
# Created Time  : 2021-01-04 12:53:06
# File Name     : detect_net_devices.py
# Description   : 
###############################################
import nmap3
import requests
import time

# 排除已知的网络设备
exclude_net_devices= [
   '192.168.1.1',
   '192.168.1.253',
   '192.168.6.1',
   '192.168.6.253',
]

# nmap ping扫描net网段中的所有网络设备
# 返回： 网络设备的IP地址数组
def nmap_scan(net):
    alive_devices = []
    nmap = nmap3.NmapScanTechniques()
    result = nmap.nmap_ping_scan(net)
    for datas in result:
        for data in datas['addresses']:
            if data['addrtype'] == 'ipv4':
                alive_devices.append(data['addr'])
    # 打印扫描到的存活主机
    print(alive_devices)
    return alive_devices

# 过滤数据
def filter_devices():
    net_1 = nmap_scan("192.168.1.0-254")
    net_2 = nmap_scan("192.168.6.0-254")
    alive_devices = net_1 + net_2
    # 数据取交集，有点问题
    # alive_hosts = set(exclude_net_devices)^set(alive_devices)
    alive_hosts = []
    for device in alive_devices:
        if device not in exclude_net_devices:
            alive_hosts.append(device)
    print(alive_hosts)

    if len(alive_hosts) > 0:
        msg = '当前时间(北京时间)：' + str(current_time) + '\r\n有 '+ str(len(alive_hosts)) + ' 台电脑未关机。\r\n详细IP如下：' + str(alive_hosts) + '\r\n请使用完后，及时关机！'
        print(msg)
        send_msg(msg)

def send_msg(offline_devices):
    headers = {"Content-Type": "text/plain"}
    data = {
       "msgtype": "text",
       "text": {
          "content": offline_devices,
       }
    }
    r = requests.post(
       url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxx-xxxxx-xxxxxxxx-xxxx',
       headers=headers, json=data)
    print(r.text)

if __name__ == '__main__':
    current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    filter_devices()

