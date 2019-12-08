default_opcode_program = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 10, 1, 19, 1, 19, 9, 23, 1, 23, 6, 27, 2,
                          27, 13, 31, 1, 10, 31, 35, 1, 10, 35, 39, 2, 39, 6, 43, 1, 43, 5, 47, 2, 10, 47, 51, 1, 5, 51,
                          55, 1, 55, 13, 59, 1, 59, 9, 63, 2, 9, 63, 67, 1, 6, 67, 71, 1, 71, 13, 75, 1, 75, 10, 79, 1,
                          5, 79, 83, 1, 10, 83, 87, 1, 5, 87, 91, 1, 91, 9, 95, 2, 13, 95, 99, 1, 5, 99, 103, 2, 103, 9,
                          107, 1, 5, 107, 111, 2, 111, 9, 115, 1, 115, 6, 119, 2, 13, 119, 123, 1, 123, 5, 127, 1, 127,
                          9, 131, 1, 131, 10, 135, 1, 13, 135, 139, 2, 9, 139, 143, 1, 5, 143, 147, 1, 13, 147, 151, 1,
                          151, 2, 155, 1, 10, 155, 0, 99, 2, 14, 0, 0]


def add(opcode_program, arg1_position, arg2_position, result_pos):
    opcode_program[result_pos] = opcode_program[arg1_position] + opcode_program[arg2_position]


def multiply(opcode_program, arg1_position, arg2_position, result_pos):
    opcode_program[result_pos] = opcode_program[arg1_position] * opcode_program[arg2_position]


def intcode_computer(noun, verb):
    opcode_program = default_opcode_program.copy()
    opcode_program[1] = noun
    opcode_program[2] = verb

    instruction_pointer = 0
    opcode = opcode_program[instruction_pointer]
    while opcode != 99:
        if opcode == 1:
            add(opcode_program, opcode_program[instruction_pointer + 1], opcode_program[instruction_pointer + 2],
                opcode_program[instruction_pointer + 3])
        elif opcode == 2:
            multiply(opcode_program, opcode_program[instruction_pointer + 1], opcode_program[instruction_pointer + 2],
                     opcode_program[instruction_pointer + 3])
        else:
            # print("Something went wrong.")
            return None
        instruction_pointer += 4
        opcode = opcode_program[instruction_pointer]

    return opcode_program[0]


def main():
    for noun in range(100):
        for verb in range(100):
            result = intcode_computer(noun, verb)
            if result == 19690720:
                print(100 * noun + verb)


if __name__ == '__main__':
    main()
