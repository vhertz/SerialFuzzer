import serial
import os


class SerialFuzzer():

    def __init__(self, serial, size):
        self._serial = serial
        self._size = size

    def fuzz(self):
        input = os.urandom(self._size)
        self._serial.write(input)
        return input
