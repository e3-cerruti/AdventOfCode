from unittest import TestCase

from day_07_2 import init_amplifiers, compute_signal_strength
from intcode_machine import IntcodeMachine


class TestComputeSignalStrength(TestCase):
    def setUp(self):
        init_amplifiers()

    # Max thruster signal 139629729 (from phase setting sequence 9,8,7,6,5):
    #
    # 3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
    # 27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5
    def test_98765(self):
        program = IntcodeMachine.get_program_from_file('feedback_test_98765.dat')
        signal = compute_signal_strength([9, 8, 7, 6, 5], program)
        self.assertEqual(139629729, signal)

    # Max thruster signal 18216 (from phase setting sequence 9,7,8,5,6):
    #
    # 3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
    # -5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
    # 53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10
    def test_97856(self):
        program = IntcodeMachine.get_program_from_file('feedback_test_97856.dat')
        signal = compute_signal_strength([9, 7, 8, 5, 6], program)
        self.assertEqual(18216, signal)
