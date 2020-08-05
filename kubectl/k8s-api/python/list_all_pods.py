#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###############################################
# Author        : Nelson
# EMail         : yangjun@tehang.com 
# Created Time  : 2020-08-05 13:03:36
# File Name     : list_all_pods.py
# Description   : 
###############################################
from kubernetes import client, config, watch

config.load_kube_config()

v1 = client.CoreV1Api()
print("Listing pods with their IPs:")

ret = v1.list_pod_for_all_namespaces(watch=False)

for i in ret.items:
    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

# watch on namespace object
count = 10
w = watch.Watch()
for event in w.stream(v1.list_namespace, _request_timeout=60):
    print("Event: %s %s" % (event['type'], event['object'].metadata.name))
    count -= 1
    if not count:
        w.stop()

print("Ended.")
