from collections import Counter

WIDTH = 25
HEIGHT = 6
LAYER_SIZE = WIDTH*HEIGHT

count_of_zero = LAYER_SIZE + 1
product_of_nonzero = 0
with open('password_image.dat') as image:
    for layer in iter(lambda: image.read(LAYER_SIZE), ''):
        frequency = Counter(layer)
        # print(frequency)
        layer_count = frequency.get('0')
        print(layer_count)
        if layer_count < count_of_zero:
            count_of_zero = layer_count
            product_of_nonzero = frequency.get('1') * frequency.get('2')
            print(product_of_nonzero)

print(product_of_nonzero)