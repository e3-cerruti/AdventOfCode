from collections import Counter

WIDTH = 25
HEIGHT = 6
FILE_NAME = 'password_image.dat'

# WIDTH = 2
# HEIGHT = 2
# FILE_NAME = 'test_image.dat'

LAYER_SIZE = WIDTH*HEIGHT


def print_password(password):
    password = ''.join(password)
    password = password.replace('0', ' ')
    password = password.replace('1', 'X')
    for i in range(HEIGHT):
        print(password[i*WIDTH: i*WIDTH + WIDTH])


count_of_zero = LAYER_SIZE + 1
product_of_nonzero = 0
final_image = '2' * LAYER_SIZE
with open(FILE_NAME) as image:
    for layer in iter(lambda: image.read(LAYER_SIZE), ''):
        final_image = [pixel if pixel != '2' else layer[index] for index, pixel in enumerate(final_image)]

print_password(final_image)
