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
        data = self.__gen_data()
        self.__transmit(data)
        return data

    def __gen_data(self):
        logger.debug("Generate data")
        data = bytes(random.getrandbits(8) for _ in range(self._size))
        logger.info(data)
        return data

    def __transmit(self, data):
        logger.debug("Transmit data")
        self._serial.write(data)
