import queue
from unittest import TestCase

from day_07.intcode_machine import IntcodeMachine

DEFAULT_PROGRAM = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                   1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                   999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]


def test_input_output(computer, input_code):
    input_queue = queue.Queue()
    output_queue = queue.Queue()
    input_queue.put(input_code)
    computer.set_queues(input_queue, output_queue)
    computer.run_program(DEFAULT_PROGRAM.copy())
    return output_queue.get()


class TestIntcodeMachine(TestCase):
    def setUp(self):
        self.computer = IntcodeMachine()

    def test_addition(self):
        result = self.computer.run_program([1101, 100, -1, 4, 0])
        self.assertEqual(result, 1101)

    def test_multiplication(self):
        result = self.computer.run_program([1002, 4, 3, 4, 33])
        self.assertEqual(result, 1002)

    # Here's a larger example:
    # 3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
    # 1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
    # 999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99
    # The above example program uses an input instruction to ask for a single number.
    # The program will then output 999 if the input value is below 8, output 1000 if the input value is equal to 8,
    # or output 1001 if the input value is greater than 8.

    def test_low_input(self):
        self.assertEqual(test_input_output(self.computer, 7), 999)

    def test_equal_input(self):
        self.assertEqual(test_input_output(self.computer, 8), 1000)

    def test_high_input(self):
        self.assertEqual(test_input_output(self.computer, 9), 1001)

    def test_load_program_from_file(self):
        computer = IntcodeMachine()
        computer.load_program_from_file('intcode_test_program.dat')
        self.assertEqual(computer.program, DEFAULT_PROGRAM)
