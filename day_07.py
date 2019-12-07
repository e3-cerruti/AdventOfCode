import queue

from intcode_machine import IntcodeMachine

queues = []
computers = []


def init_amplifiers():
    global queues, computers
    queues = [queue.Queue(),queue.Queue(),queue.Queue(),queue.Queue(),queue.Queue(),queue.Queue()]
    computers = [IntcodeMachine(),IntcodeMachine(),IntcodeMachine(),IntcodeMachine(),IntcodeMachine()]
    for i in range(5):
        computers[i].set_queues(queues[i], queues[i+1])


def compute_signal_strength(phases, file_name):
    global queues, computers
    program = IntcodeMachine.get_program_from_file(file_name)
    for i in range(5):
        queues[i].put(phases[i])
        computers[i].load_program(program)

    queues[0].put(0)
    for i in range(5):
        computers[i].run()

    return queues[5].get()

