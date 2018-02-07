# Volatility
Volatility Framework (http://www.volatilityfoundation.org/) related stuff

## vol_vm.py
A simple wrapper to analyze vmem files with Volatility Framework. Tested on macOS + VMware Fusion. This might be useful for malware analyst.

### How to use
1. Edit vol_vm.py according to your environment
2. Execute malware sample which you want to analyze on virtual machine
3. Execute vol_vm.py with Volatility command
  - vol_vm.py suspends your virtual machine then executes vol.py as below

```
$ python vol_vm.py redleavesconfig
[*] suspended WIN7
[*] volatility output:
Volatility Foundation Volatility Framework 2.6
config addr: 0035F788

----------------------------------------------------------------------
Lavender Settings:
...
```

## License
Apache License 2.0. See [LICENSE](/LICENSE).
