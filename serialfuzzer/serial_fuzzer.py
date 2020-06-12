import serial
import os
import random

import logging
logger = logging.getLogger(__name__)


class SerialFuzzer():

    def __init__(self, serial, size, seed=0):
        self._serial = serial
        self._size = size
        self._seed = seed

        random.seed(self._seed)

    def fuzz(self):
        input = self.__gen_input()
        logger.debug("Generated input: " + str(input))
        self._serial.write(input)
        return input

    def __gen_input(self):
        return bytes(random.getrandbits(8) for _ in range(self._size))