#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import argparse
import importlib

import iptools


def main():
    parser = argparse.ArgumentParser(
        prog='pmap.py',
        description="Network scanner script."
    )
    parser.add_argument(
        "-n", dest="thread_number",
        required=True, type=int,
        help="Concurrent threading number."
    )
    parser.add_argument(
        "-f", dest='detector', choices=['ping', 'tcp'],
        required=True, type=str, default='ping',
        help="ping the IP or telnet the IP(default: ping)."
    )
    parser.add_argument(
        '-ip', dest='ip_range',
        required=True, type=str,
        help="IP range for the function(e.g. 192.168.0.1-192.168.0.100)."
    )
    parser.add_argument(
        '-w', dest='write_out_file',
        default=None,
        type=str, help="The file to store the result(e.g. -w result.json)."
    )
    # parser.parse_args(['-n', '4', '-f', 'ping'])
    # parser.parse_args(['-h'])
    args = parser.parse_args(['-n', '4', '-f', 'ping', '-ip',
                              '172.21.85.191', '-w', 'result.json'])

    ip_range = None

    if args.thread_number <= 0:
        exit(Exception(
            'You must input legal thread number. Thread number must be greater than 0.'))
    try:
        ip_range_tuple = tuple(
            args.ip_range.strip().split(sep='-', maxsplit=2))

        if len(ip_range_tuple) == 1:
            ip_range_tuple += ip_range_tuple
        elif len(ip_range_tuple) == 0:
            exit(
                Exception('You must input legal IP address.(e.g. 192.168.0.1-192.168.0.100)'))

        ip_range = iptools.IpRangeList(ip_range_tuple)
    except:
        exit(Exception('You must input legal IP address.(e.g. 192.168.0.1-192.168.0.100)'))

    print(args)

    detector_module = importlib.import_module(
        ".{}_detector".format(args.detector),
        "detector_modules"
    )
    print(detector_module)

    detector = detector_module.Detector(
        thread_num=args.thread_number,
        ip_range=ip_range,
        write_out_file=args.write_out_file
    )

    print(detector)

    detector.get_detector_results()


if __name__ == "__main__":
    # ip_range_arg = '172.21.85.191'
    # ip_range_arg = 'abc.efg'
    # ip_range_tuple = tuple(ip_range_arg.split(sep='-', maxsplit=2))
    # if len(ip_range_tuple) == 1:
    #     ip_range_tuple += ip_range_tuple
    # # ip_range = iptools.IpRangeList(
    # #     ('10.0.0.1', '10.0.0.19')
    # # )

    # ip_range = iptools.IpRangeList(ip_range_tuple)
    # print(ip_range)
    # for ip in ip_range:
    #     print(f'current ip is: {ip}')
    main()
