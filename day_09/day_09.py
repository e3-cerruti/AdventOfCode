import queue

from intcode_machine import IntcodeMachine

TEST_MODE = 1
SENSOR_BOOST_MODE = 2
input_queue = queue.Queue()
output_queue = queue.Queue()
computer = IntcodeMachine(input_queue, output_queue)
computer.load_program_from_file('BOOST.dat')
input_queue.put(SENSOR_BOOST_MODE)
computer.run()
while not output_queue.empty():
    print(output_queue.get())


