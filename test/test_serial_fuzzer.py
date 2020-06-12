from unittest import TestCase
import serialfuzzer
import serial
import os


class TestSerialFuzzer(TestCase):

    def setUp(self):
        self.master, self.slave = os.openpty()

    def test_fuzz(self):
        with serial.Serial(os.ttyname(self.slave)) as se:
            with os.fdopen(self.master, "rb") as fd:
                fuzzer = serialfuzzer.SerialFuzzer(se, 1)
                input = fuzzer.fuzz()
                se.flush()
                output = fd.read(len(input))
                self.assertEqual(input, output)

