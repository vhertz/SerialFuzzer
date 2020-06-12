import serial
import os
class SerialFuzzer():

    def __init__(self, serial, size):
        self._serial = serial
        self._size = size

    def fuzz(self):
        input = os.getrandom(self._size)
        self._serial.write(input)
        return
