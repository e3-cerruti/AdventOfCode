def add(intcode_program, args):
    intcode_program[args[2]] = intcode_program[args[0]] + intcode_program[args[1]]


def multiply(intcode_program, args):
    intcode_program[args[2]] = intcode_program[args[0]] * intcode_program[args[1]]


def read(intcode_program, args):
    system = int(input("What system should be tested?"))
    intcode_program[args[0]] = system


def write(intcode_program, args):
    print(args)
    print("Diagnostic code: "+str(intcode_program[args[0]]))


def jump_if_true(intcode_program, args):
    global instruction_pointer
    if intcode_program[args[0]]:
        instruction_pointer = intcode_program[args[1]]


def jump_if_false(intcode_program, args):
    global instruction_pointer
    if not intcode_program[args[0]]:
        instruction_pointer = intcode_program[args[1]]


def less_than(intcode_program, args):
    if intcode_program[args[0]] < intcode_program[args[1]]:
        intcode_program[args[2]] = 1
    else:
        intcode_program[args[2]] = 0


def equals(intcode_program, args):
    if intcode_program[args[0]] == intcode_program[args[1]]:
        intcode_program[args[2]] = 1
    else:
        intcode_program[args[2]] = 0


halted = True


def halt(_1, _2):
    global halted
    halted = True


instruction_set = {
    1: [add, 3],
    2: [multiply, 3],
    3: [read, 1],
    4: [write, 1],
    5: [jump_if_true, 2],
    6: [jump_if_false, 2],
    7: [less_than, 3],
    8: [equals, 3],
    99: [halt, 0],
}
instruction_pointer = 0


def decode(opcode):
    global instruction_pointer
    code = opcode % 100
    modes = opcode // 100
    parameter_modes = []

    for i in range(instruction_set[code][1]):
        parameter_modes.append(modes % 10)
        modes //= 10

    return code, parameter_modes


def intcode_computer(intcode_program):
    global instruction_pointer
    global halted

    instruction_pointer = 0
    halted = False
    while not halted:
        opcode, parameter_modes = decode(intcode_program[instruction_pointer])
        parameters = []
        for mode in parameter_modes:
            instruction_pointer += 1
            if mode:
                parameters.append(instruction_pointer)
            else:
                parameters.append(intcode_program[instruction_pointer])

        instruction_pointer += 1
        instruction_set[opcode][0](intcode_program, parameters)

    return intcode_program[0]


def main():
    print(intcode_computer([1002, 4, 3, 4, 33]))
    print(intcode_computer([1101, 100, -1, 4, 0]))
    intcode_computer(
        [3, 225, 1, 225, 6, 6, 1100, 1, 238, 225, 104, 0, 1102, 27, 28, 225, 1, 113, 14, 224, 1001, 224, -34, 224, 4,
         224, 102, 8, 223, 223, 101, 7, 224, 224, 1, 224, 223, 223, 1102, 52, 34, 224, 101, -1768, 224, 224, 4, 224,
         1002, 223, 8, 223, 101, 6, 224, 224, 1, 223, 224, 223, 1002, 187, 14, 224, 1001, 224, -126, 224, 4, 224, 102,
         8, 223, 223, 101, 2, 224, 224, 1, 224, 223, 223, 1102, 54, 74, 225, 1101, 75, 66, 225, 101, 20, 161, 224, 101,
         -54, 224, 224, 4, 224, 1002, 223, 8, 223, 1001, 224, 7, 224, 1, 224, 223, 223, 1101, 6, 30, 225, 2, 88, 84,
         224, 101, -4884, 224, 224, 4, 224, 1002, 223, 8, 223, 101, 2, 224, 224, 1, 224, 223, 223, 1001, 214, 55, 224,
         1001, 224, -89, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 4, 224, 1, 224, 223, 223, 1101, 34, 69, 225, 1101,
         45, 67, 224, 101, -112, 224, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 2, 224, 1, 223, 224, 223, 1102, 9, 81,
         225, 102, 81, 218, 224, 101, -7290, 224, 224, 4, 224, 1002, 223, 8, 223, 101, 5, 224, 224, 1, 223, 224, 223,
         1101, 84, 34, 225, 1102, 94, 90, 225, 4, 223, 99, 0, 0, 0, 677, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1105, 0,
         99999, 1105, 227, 247, 1105, 1, 99999, 1005, 227, 99999, 1005, 0, 256, 1105, 1, 99999, 1106, 227, 99999, 1106,
         0, 265, 1105, 1, 99999, 1006, 0, 99999, 1006, 227, 274, 1105, 1, 99999, 1105, 1, 280, 1105, 1, 99999, 1, 225,
         225, 225, 1101, 294, 0, 0, 105, 1, 0, 1105, 1, 99999, 1106, 0, 300, 1105, 1, 99999, 1, 225, 225, 225, 1101,
         314, 0, 0, 106, 0, 0, 1105, 1, 99999, 1007, 677, 677, 224, 102, 2, 223, 223, 1005, 224, 329, 101, 1, 223, 223,
         1108, 226, 677, 224, 1002, 223, 2, 223, 1005, 224, 344, 101, 1, 223, 223, 1008, 677, 677, 224, 102, 2, 223,
         223, 1005, 224, 359, 101, 1, 223, 223, 8, 226, 677, 224, 1002, 223, 2, 223, 1006, 224, 374, 101, 1, 223, 223,
         108, 226, 677, 224, 1002, 223, 2, 223, 1006, 224, 389, 1001, 223, 1, 223, 1107, 226, 677, 224, 102, 2, 223,
         223, 1005, 224, 404, 1001, 223, 1, 223, 7, 226, 677, 224, 1002, 223, 2, 223, 1005, 224, 419, 101, 1, 223, 223,
         1107, 677, 226, 224, 102, 2, 223, 223, 1006, 224, 434, 1001, 223, 1, 223, 1107, 226, 226, 224, 1002, 223, 2,
         223, 1006, 224, 449, 101, 1, 223, 223, 1108, 226, 226, 224, 1002, 223, 2, 223, 1005, 224, 464, 101, 1, 223,
         223, 8, 677, 226, 224, 102, 2, 223, 223, 1005, 224, 479, 101, 1, 223, 223, 8, 226, 226, 224, 1002, 223, 2, 223,
         1006, 224, 494, 1001, 223, 1, 223, 1007, 226, 677, 224, 1002, 223, 2, 223, 1006, 224, 509, 1001, 223, 1, 223,
         108, 226, 226, 224, 1002, 223, 2, 223, 1006, 224, 524, 1001, 223, 1, 223, 1108, 677, 226, 224, 102, 2, 223,
         223, 1006, 224, 539, 101, 1, 223, 223, 1008, 677, 226, 224, 102, 2, 223, 223, 1006, 224, 554, 101, 1, 223, 223,
         107, 226, 677, 224, 1002, 223, 2, 223, 1006, 224, 569, 101, 1, 223, 223, 107, 677, 677, 224, 102, 2, 223, 223,
         1006, 224, 584, 101, 1, 223, 223, 7, 677, 226, 224, 102, 2, 223, 223, 1005, 224, 599, 101, 1, 223, 223, 1008,
         226, 226, 224, 1002, 223, 2, 223, 1005, 224, 614, 1001, 223, 1, 223, 107, 226, 226, 224, 1002, 223, 2, 223,
         1005, 224, 629, 101, 1, 223, 223, 7, 226, 226, 224, 102, 2, 223, 223, 1006, 224, 644, 1001, 223, 1, 223, 1007,
         226, 226, 224, 102, 2, 223, 223, 1006, 224, 659, 101, 1, 223, 223, 108, 677, 677, 224, 102, 2, 223, 223, 1005,
         224, 674, 1001, 223, 1, 223, 4, 223, 99, 226])


if __name__ == '__main__':
    main()
