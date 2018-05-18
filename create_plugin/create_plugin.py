#!/usr/bin/env python

import subprocess
import os, sys
import glob
import argparse
from collections import namedtuple

PLUGIN_DIR = None
TEMPLATE_FILE = 'malware_template.py'

parser = argparse.ArgumentParser(description='Create initial Volatiliy plugin script for malware detection')
parser.add_argument('MALWARE_NAME', help='Malware name')
parser.add_argument('-o', '--outdir', action='store', dest='outdir', default=None, help='Specify output directory')
args = parser.parse_args()

def main():
    Malware_Name = args.MALWARE_NAME
    MALWARE_NAME = args.MALWARE_NAME.upper()
    malware_name = args.MALWARE_NAME.lower()
    print('[*] initialize {}.py'.format(malware_name))

    with open(TEMPLATE_FILE, 'rb') as fp:
        out_data = fp.read()
    out_data = out_data.replace('Malware_Name', Malware_Name)
    out_data = out_data.replace('MALWARE_NAME', MALWARE_NAME)
    out_data = out_data.replace('malware_name', malware_name)

    if args.outdir:
        out_file = args.outdir + '/' + malware_name + '.py'
    elif PLUGIN_DIR:
        out_file = PLUGIN_DIR + '/' + malware_name + '.py'
    else:
        out_file = './' + malware_name + '.py'
    with open(out_file, 'w') as fp:
        fp.write(out_data)
    print('[*] saved as {}'.format(out_file))

if __name__ == '__main__':
    main()
