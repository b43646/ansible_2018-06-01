#!/usr/bin/env python

import argparse
import json
import sys

def parse_args():
    parser = argparse.ArgumentParser(description="inventory script")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--list', action='store_true')
    group.add_argument('--host')
    return parser.parse_args()

def list_running_hosts():
    hosts = dict()
    hosts['demo']=get_host_details('')
    return hosts

def get_host_details(host):
    return {'ansible_ssh_host': 'localhost',
            'ansible_ssh_port': '22',
            'ansible_ssh_user': 'root',
            'ansible_ssh_pass': 'Happy123'}

def main():
    args = parse_args()
    if args.list:
        hosts = list_running_hosts()
        json.dump({'vagrant': hosts}, sys.stdout)
    else:
        details = get_host_details(args.host)
        json.dump(details, sys.stdout)

if __name__ == '__main__':
    main()
