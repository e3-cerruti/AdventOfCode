import queue
from threading import Thread

from intcode_machine.intcode_machine import IntcodeMachine

x = y = 0
direction = 0
# Start on black
# hull = {(x, y): 0}
# Start on white
hull = {(x, y): 1}


def up():
    global y
    y += 1


def down():
    global y
    y -= 1


def right():
    global x
    x += 1


def left():
    global x
    x -= 1


move = {
    0: up,
    1: right,
    2: down,
    3: left
}

input_queue = queue.Queue()
output_queue = queue.Queue()
computer = IntcodeMachine(input_queue, output_queue)
computer.load_program_from_file('paint.dat')

input_queue.put(hull.get((0, 0)))

computer_thread = Thread(target=computer.run)
computer_thread.start()

while computer_thread.is_alive():
    color = output_queue.get()
    hull[(x, y)] = color

    turn = output_queue.get()
    if turn:
        direction = (direction + 1) % 4
    else:
        direction = (direction + 3) % 4

    func = move.get(direction, "Nothing")
    func()

    if (x, y) in hull.keys():
        input_queue.put(hull[(x, y)])
    else:
        input_queue.put(0)

print(len(hull))

min_x = 0
min_y = 0
max_x = 0
max_y = 0

for x, y in hull.keys():
    min_x = min(min_x, x)
    min_y = min(min_y, y)
    max_x = max(max_x, x)
    max_y = max(max_y, y)

for y in range(max_y, min_y - 1, -1):
    for x in range(min_x, max_x+1):
        if (x, y) in hull.keys() and hull.get((x, y)) == 1:
            print('#', end='')
        else:
            print(' ', end='')
    print()
