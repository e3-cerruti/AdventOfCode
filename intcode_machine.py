class IntcodeMachine:
    def __init__(self, input_queue=None, output_queue=None):
        self.halted = False
        self.instruction_set = {
            1: [self.add, 3],
            2: [self.multiply, 3],
            3: [self.read, 1],
            4: [self.write, 1],
            5: [self.jump_if_true, 2],
            6: [self.jump_if_false, 2],
            7: [self.less_than, 3],
            8: [self.equals, 3],
            99: [self.halt, 0],
        }
        self.instruction_pointer = 0
        self.program = None
        self.set_queues(input_queue, output_queue)

    def set_queues(self, input_queue, output_queue):
        self.input_queue = input_queue
        self.output_queue = output_queue

    def load_program(self, program):
        self.program = program

    def load_program_from_file(self, fileName):
        program = []
        with open(fileName) as program_file:
            for line in program_file:
                program.extend([int(i) for i in line.strip().split(',')])
        self.load_program(program)

    def add(self, args):
        self.program[args[2]] = self.program[args[0]] + self.program[args[1]]

    def multiply(self, args):
        self.program[args[2]] = self.program[args[0]] * self.program[args[1]]

    def read(self, args):
        self.program[args[0]] = self.input_queue.get()

    def write(self, args):
        self.output_queue.put(self.program[args[0]])

    def jump_if_true(self, args):
        if self.program[args[0]]:
            self.instruction_pointer = self.program[args[1]]

    def jump_if_false(self, args):
        if not self.program[args[0]]:
            self.instruction_pointer = self.program[args[1]]

    def less_than(self, args):
        if self.program[args[0]] < self.program[args[1]]:
            self.program[args[2]] = 1
        else:
            self.program[args[2]] = 0

    def equals(self, args):
        if self.program[args[0]] == self.program[args[1]]:
            self.program[args[2]] = 1
        else:
            self.program[args[2]] = 0

    def halt(self, _1):
        self.halted = True

    def decode(self, opcode):
        code = opcode % 100
        modes = opcode // 100
        parameter_modes = []

        for i in range(self.instruction_set[code][1]):
            parameter_modes.append(modes % 10)
            modes //= 10

        return code, parameter_modes

    def run(self):
        self.halted = False
        self.instruction_pointer = 0
        while not self.halted:
            opcode, parameter_modes = self.decode(self.program[self.instruction_pointer])
            parameters = []
            for mode in parameter_modes:
                self.instruction_pointer += 1
                if mode:
                    parameters.append(self.instruction_pointer)
                else:
                    parameters.append(self.program[self.instruction_pointer])

            self.instruction_pointer += 1
            self.instruction_set[opcode][0](parameters)

        return self.program[0]

    def run_program(self, program):
        self.load_program(program)
        return self.run()
