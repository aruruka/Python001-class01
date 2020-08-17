#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pretty_errors
import subprocess
import shlex
import multiprocessing
import ipaddress
import socket
import functools
import argparse
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


print_lock = multiprocessing.Lock()


def validate_ip(ip):
    # ip = 'abc'
    return ipaddress.IPv4Address(ip)


def get_ip_list_in_range(start, end):
    ip_range = ipaddress.summarize_address_range(start, end)
    print(f'ip_range is: {ip_range}')
    # for ips in ipaddress.summarize_address_range(start, end):
    
    # ips_list = [ips for ips in ip_range]
    # print(len(ips_list))
    for ips in ip_range:
        print(type(ips))
        # print(len(ips))
        yield from ips


if __name__ == "__main__":
    args_ip = '192.168.1.100-192.168.1.128'
    # args_ip.split("-")
    # ['192.168.1.100', '192.168.1.128']
    # ip_gen = (validate_ip(ip) for ip in args_ip.split("-"))
    # next(ip_gen)
    ip_list = get_ip_list_in_range(*(validate_ip(ip)
                                     for ip in args_ip.split("-")))
    
    print(f'ip_list is: {ip_list}')
    next(ip_list)
