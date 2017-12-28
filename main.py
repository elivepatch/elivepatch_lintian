#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import urllib.request


def build_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--id', type=str, help='kernel git repository patch id')
    parser.add_argument('--file', type=str, help='Patch file local pc location')
    return parser


def dispatch_cmd(args):
    if args.id:
        cmd_a(args.id)
    elif args.file:
        cmd_b(args.file)
    else:
        pass


def cmd_a(patch_id):
    print ("Dowloading patch file")
    print (patch_id)
    print('Downloading patch from the kernel repository...')
    url = 'https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git/patch/?id=' + patch_id
    urllib.request.urlretrieve(url, '/tmp/temporary.patch')  


def cmd_b(args):
    print ("Opening local patch file")
    print (args)


def main():
    args = build_argparser().parse_args()
    print (args)
    dispatch_cmd(args)


if __name__ == "__main__":
    main()
