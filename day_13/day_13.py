import queue
from threading import Thread
from time import sleep

from graphics import *
from intcode_machine.intcode_machine import IntcodeMachine


class Board():
    BLOCK_SIZE = 10
    TILE_COLORS = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']

    def __init__(self, width, height, computer_thread, input_queue, output_queue):
        self.width = width
        self.height = height
        self.screen = {}
        self.ball_x = 0
        self.paddle_x = 0

        self.count_moves = 0
        self.count_balls = 0

        self.computer_thread = computer_thread
        self.input_queue = input_queue
        self.output_queue = output_queue

        self.win = GraphWin("Breakout", width, height)

    def read_output_queue(self):
        while self.computer_thread.is_alive():
            x = self.output_queue.get()
            y = self.output_queue.get()
            if (x, y) == (-1, 0):
                print("Score: " + str(self.output_queue.get()))
            else:
                if (x, y) in self.screen.keys():
                    self.screen[(x, y)].undraw()
                    del self.screen[(x, y)]

                tile = self.output_queue.get()
                if tile in [1, 2]:
                    p1 = Point(x * self.BLOCK_SIZE, y * self.BLOCK_SIZE)
                    p2 = Point(p1.x + self.BLOCK_SIZE, p1.y + self.BLOCK_SIZE)

                    r = Rectangle(p1, p2)
                    r.setFill(self.TILE_COLORS[tile])
                    r.draw(self.win)
                    self.screen[(x, y)] = r

                elif tile == 3:
                    p1 = Point(x * self.BLOCK_SIZE, y * self.BLOCK_SIZE + self.BLOCK_SIZE/4)
                    p2 = Point(p1.x + self.BLOCK_SIZE, p1.y + self.BLOCK_SIZE - self.BLOCK_SIZE/4)

                    r = Rectangle(p1, p2)
                    r.setFill(self.TILE_COLORS[tile])
                    r.draw(self.win)
                    self.screen[(x, y)] = r
                    self.paddle_x = x

                elif tile == 4:
                    p1 = Point(x * self.BLOCK_SIZE + self.BLOCK_SIZE / 2, y * self.BLOCK_SIZE + self.BLOCK_SIZE/2)
                    c = Circle(p1, self.BLOCK_SIZE/2)
                    c.setFill(self.TILE_COLORS[tile])
                    c.draw(self.win)
                    self.screen[(x, y)] = c
                    self.ball_x = x



                    if self.ball_x < self.paddle_x:
                        self.input_queue.put(-1)
                    elif self.ball_x > self.paddle_x:
                        self.input_queue.put(1)
                    else:
                        self.input_queue.put(0)


def main():
    input_queue = queue.Queue()
    output_queue = queue.Queue()
    computer = IntcodeMachine(input_queue, output_queue)
    computer.load_program_from_file('game.dat')

    computer_thread = Thread(target=computer.run)
    computer_thread.start()

    board = Board(430, 210, computer_thread, input_queue, output_queue)
    board.read_output_queue()


if __name__ == '__main__':
    main()
