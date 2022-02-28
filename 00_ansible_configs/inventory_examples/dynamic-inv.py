#!/usr/bin/env python
import argparse
import json
import sys


def parse_args():
    parser = argparse.ArgumentParser(description="dynamic script")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--list', action='store_true')
    group.add_argument('--host')
    return parser.parse_args()


def main():
    args = parse_args()
    inventory = {}
    servers_list = [
        "server1.localdomain",
        "server2.localdomain"
    ]
    if args.list:
        inventory["nodes"] = {"hosts": servers_list}
        json.dump(inventory, sys.stdout)
    else:
        host = {"ansible_host": args.host}
        json.dump(host, sys.stdout)


if __name__ == '__main__':
    main()
