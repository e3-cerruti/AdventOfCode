import itertools
import queue

from intcode_machine import IntcodeMachine

queues = []
computers = []


def init_amplifiers():
    global queues, computers
    queues = [queue.Queue(), queue.Queue(), queue.Queue(), queue.Queue(), queue.Queue(), queue.Queue()]
    computers = [IntcodeMachine(), IntcodeMachine(), IntcodeMachine(), IntcodeMachine(), IntcodeMachine()]
    for i in range(5):
        computers[i].set_queues(queues[i], queues[i + 1])


def compute_signal_strength(phases, program):
    global queues, computers
    for i in range(5):
        queues[i].put(phases[i])
        computers[i].load_program(program)

    queues[0].put(0)
    for i in range(5):
        computers[i].run()

    return queues[5].get()


def main():
    program = IntcodeMachine.get_program_from_file('day_07.dat')
    init_amplifiers()

    phase_settings = [0, 1, 2, 3, 4]
    phase_permutations = list(itertools.permutations(phase_settings))
    signal = compute_signal_strength(phase_permutations[0], program.copy())

    for phase_array in phase_permutations[1:]:
        signal = max(signal, compute_signal_strength(phase_array, program.copy()))

    print(signal)


if __name__ == '__main__':
    main()
