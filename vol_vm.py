#!/usr/bin/env python

import subprocess
import os, sys
import glob
import argparse
from collections import namedtuple

VIRTUAL_MACHINE = namedtuple('VIRTUAL_MACHINE', "name path profile")
VIRTUAL_MACHINES = [
    VIRTUAL_MACHINE('WIN7', '/PATH/TO/YOUR/VM.vmx', 'Win7SP1x64')
]
DEFAULT_VIRTUAL_MACHINE = "WIN7"
VMRUN = "/Applications/VMware Fusion.app/Contents/Library/vmrun"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PLUGIN_DIR = BASE_DIR + '/plugins'
VOLATILITY = BASE_DIR + '/vol.py'

parser = argparse.ArgumentParser(description='A simple wrapper to analyze vmem files with Volatility Framework')
parser.add_argument("COMMAND", help="Volatility command to execute")
parser.add_argument("-n", "--name", action="store", dest="vm_name", default=DEFAULT_VIRTUAL_MACHINE, help="Specify virtual machine name which you want to scan (Default: {})".format(DEFAULT_VIRTUAL_MACHINE))
parser.add_argument("-j", "--json", action="store_true", dest="json", default=False, help="Output as JSON")
args = parser.parse_args()

def is_active(vm_path):
    return vm_path in subprocess.check_output([VMRUN, 'list'])

def find_vmem(dir_name):
    vmems = glob.glob(dir_name + '/*.vmem')
    if len(vmems) == 0:
        return False
    vmem = max(vmems, key=os.path.getatime)
    return vmem

def main():
    if args.COMMAND == 'vmlist':
        print('[*] Supported virtual machines:')
        for vm in VIRTUAL_MACHINES:
            if vm.name == DEFAULT_VIRTUAL_MACHINE:
                print('[*] {} (Default): {}'.format(vm.name, vm.path))
            else:
                print('[*] {}: {}'.format(vm.name, vm.path))
        return

    for vm in VIRTUAL_MACHINES:
        if vm.name == args.vm_name:
            break
    else:
        print('[!] {} does not exist'.format(args.vm))
        print('[!] use -l option to show supported virtual machines')
        return

    if is_active(vm.path) == True:
        subprocess.call([VMRUN, 'suspend', vm.path])
        if is_active(vm.path) == True:
            print('[!] could not suspend {}'.format(vm.name))
            return
        print('[*] suspended {}'.format(vm.name))

    vmem = find_vmem(os.path.dirname(vm.path))
    if vmem == False:
        print('[!] could not find vmem file')
        return

    print('[*] volatility output:')
    if args.json == False:
        subprocess.call([VOLATILITY, '--plugins=' + PLUGIN_DIR, args.COMMAND, '-f', vmem, '--profile=' + vm.profile])
    else:
        subprocess.call([VOLATILITY, '--plugins=' + PLUGIN_DIR, '--output=json', args.COMMAND, '-f', vmem, '--profile=' + vm.profile])

    return

if __name__ == '__main__':
    main()
