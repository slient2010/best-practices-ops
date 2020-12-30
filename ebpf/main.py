#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###############################################
# Author        : Nelson
# EMail         : yangjun@tehang.com 
# Created Time  : 2020-12-30 13:02:37
# File Name     : main.py
# Description   : 
###############################################

from bcc import BPF
import time
device = "lo"
b = BPF(src_file="filter.c")
fn = b.load_func("udpfilter", BPF.XDP)
b.attach_xdp(device, fn, 0)
try:
    b.trace_print()
except KeyboardInterrupt:
    pass
b.remove_xdp(device, 0)
