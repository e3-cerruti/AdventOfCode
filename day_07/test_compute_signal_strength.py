from unittest import TestCase

from day_07.day_07 import init_amplifiers, compute_signal_strength
from day_07.intcode_machine import IntcodeMachine


class TestComputeSignalStrength(TestCase):
    def setUp(self):
        init_amplifiers()

    # Max thruster signal 43210 (from phase setting sequence 4,3,2,1,0):
    #
    # 3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0
    def test_43210(self):
        program = IntcodeMachine.get_program_from_file('amp_test_43210.dat')
        signal = compute_signal_strength([4, 3, 2, 1, 0], program)
        self.assertEqual(43210, signal)

    # Max thruster signal 54321 (from phase setting sequence 0,1,2,3,4):
    #
    # 3,23,3,24,1002,24,10,24,1002,23,-1,23,
    # 101,5,23,23,1,24,23,23,4,23,99,0,0
    def test_01234(self):
        program = IntcodeMachine.get_program_from_file('amp_test_01234.dat')
        signal = compute_signal_strength([0, 1, 2, 3, 4], program)
        self.assertEqual(54321, signal)

    # Max thruster signal 65210 (from phase setting sequence 1,0,4,3,2):
    #
    # 3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
    # 1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0
    def test_65210(self):
        program = IntcodeMachine.get_program_from_file('amp_test_65210.dat')
        signal = compute_signal_strength([1, 0, 4, 3, 2], program)
        self.assertEqual(65210, signal)
