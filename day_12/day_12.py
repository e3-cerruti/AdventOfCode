import math
import re
from copy import deepcopy

DATA_FILE = 'input.dat'


def gravity(moon1, moon2):
    if moon1 < moon2:
        return 1
    elif moon1 == moon2:
        return 0
    else:
        return -1


def compute_velocity(dimension):
    for i, moon in enumerate(dimension):
        for other_moon in dimension[i+1:]:
            g = gravity(moon[0], other_moon[0])
            moon[1] += g
            other_moon[1] -= g
    return dimension


def update_position(dimension):
    for moon in dimension:
        moon[0] = moon[0] + moon[1]
    return dimension


def compute_energy(dims):
    total = 0
    for i in range(len(dims[0])):
        print([dims[d][i][0] for d in range(3)], [dims[d][i][1] for d in range(3)])
        potential = sum(map(abs, [dims[d][i][0] for d in range(3)]))
        kinetic = sum(map(abs, [dims[d][i][1] for d in range(3)]))
        total += potential * kinetic
    return total


def update_sequences():
    for i, moon in enumerate(moons):
        sequences.append([])
        for j in range(3):
            sequences[i][j].append(moon[j])


def pattern(inputv, start):
    for pattern_length in range(start+1, len(inputv)):
        # print(inputv[0:pattern_length])
        number_of_patterns = len(inputv) // pattern_length
        if number_of_patterns == 1:
            return None
        # print('a:', inputv[0:(number_of_patterns - 1) * pattern_length])
        # print('b:', inputv[pattern_length:number_of_patterns*pattern_length])
        if inputv[0:(number_of_patterns - 1) * pattern_length] == inputv[pattern_length:number_of_patterns*pattern_length]:
            return pattern_length
    return None


def find_lcm(x, y):
    gcd = math.gcd(x, y)
    lcm = x * y // gcd
    return lcm


def get_moon_data(file_name):
    moons = []
    with open(file_name) as initial_position:
        for line in initial_position:
            moon = list(map(int, re.findall(r'-?\d+', line)))
            moons.append([moon, [0, 0, 0]])
    return moons


moon_data = get_moon_data(DATA_FILE)
dimensions = [[[moon[0][j], moon[1][j]] for moon in moon_data] for j in range(3)]
for i in range(1000):
    for dimension in dimensions:
        compute_velocity(dimension)
        update_position(dimension)


print(compute_energy(dimensions))

dimensions = [[[moon[0][j], moon[1][j]] for moon in moon_data] for j in range(3)]
dim1 = deepcopy(dimensions)
count = [1, 1, 1]
for i, dimension in enumerate(dimensions):
    dimension = compute_velocity(dimension)
    dimension = update_position(dimension)
    while dimension != dim1[i]:
        count[i] += 1
        dimension = compute_velocity(dimension)
        dimension = update_position(dimension)
        if count[i] % 1000 == 0: print('.', end='')
    print(count[i])

lcm = find_lcm(count[0], count[1])
lcm = find_lcm(lcm, count[2])
print(lcm)

# for i, moon in enumerate(moons):
#     sequences.append([])
#     for j in range(3):
#         sequences[i].append([])
#         sequences[i][j]=[moon[j]]
#
# count = 0
# pattern_lengths = [None]*len(moons)*3
# BLOCK_SIZE = 200000
# start = 0
# end = BLOCK_SIZE
#
# while None in pattern_lengths:
#     for i in range(BLOCK_SIZE):
#         compute_velocity()
#         update_position()
#         update_sequences()
#         count += 1
#
#     pattern_lengths = []
#     for moon in sequences:
#         for dimension in moon:
#             pattern_lengths.append(pattern(dimension,start))
#
#     print(pattern_lengths)
#
#     start += BLOCK_SIZE
#     end += BLOCK_SIZE
#
# lcm = find_lcm(pattern_lengths[0], pattern_lengths[1])
# print(lcm)
#
# for i in range(2, len(pattern_lengths)):
#     lcm = find_lcm(lcm, pattern_lengths[i])
#     print(lcm)
#
#
