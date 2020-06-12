# SerialFuzzer

a (dumb) fuzzer for serial interfaces.

## Usage (a sample script)

```
import serialfuzzer
import serial
import time

with serial.Serial("/dev/tty.usbmodem1421202", baudrate=115200) as se:
    fuzzer = serialfuzzer.SerialFuzzer(se, 1, 0)
    for _ in range(100):
        input = fuzzer.fuzz()
        time.sleep(0.5)
```
