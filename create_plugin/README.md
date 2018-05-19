# Volatility/create_plugin
A small script to initialize Volatility plugin for malware detection.

The initial script created by this supports the following commands ("Malware" should be replaced with given malware name):

* MalwareScan
  * Detect malware infected process
* MalwareConfig
  * Parse malware configuration data on memory

Both commands support text and JSON output as below:

```
$ vol TestScan -f test.vmem --profile=Win7SP1x64
Volatility Foundation Volatility Framework 2.6
PID      Image Name           Base Address      
-------- -------------------- ------------------
    1111 test.exe             0x0000000000400000
```

```
$ vol TestConfig --output=json -f test.vmem --profile=Win7SP1x64
Volatility Foundation Volatility Framework 2.6
{'processes': [{'pid': 1111, 'image_name': 'test.exe', 'base_address': 4194304}]}
```

## How to use
```
$ python create_plugin.py Himawari
[*] initialize himawari.py
[*] saved as ./himawari.py
```
