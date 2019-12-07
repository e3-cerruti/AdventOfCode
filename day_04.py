minimum = 372037
maximum = 905157


# minimum = 172930
# maximum = 683082


def decompose(number):
    result = [number]
    while result[0] > 10:
        temp = result[0]
        result[0] = temp % 10
        result.insert(0, temp // 10)
    return result


def find_matches(minimum_digits, maximum_digits, repeated, parent_digit=None, grandparent_digit=None, last=False,
                 base=0, repeated_digit=None):
    # print(minimum_digits, maximum_digits, parent_digit)
    qualified = 0
    minimum_children = minimum_digits[1:]
    maximum_children = maximum_digits[1:]

    minimum_digit = minimum_digits[0]
    if parent_digit and parent_digit > minimum_digit:
        minimum_digit = parent_digit

    maximum_digit = 10
    if last:
        maximum_digit = maximum_digits[0] + 1

    for i in range(minimum_digit, maximum_digit):
        if i > minimum_digits[0]:
            minimum_children = [0] * len(minimum_children)

        if repeated:
            my_repeated = True
        elif parent_digit and i == parent_digit:
            my_repeated = True
            repeated_digit = i
        else:
            my_repeated = False

        if parent_digit and grandparent_digit and repeated_digit and \
                grandparent_digit == i and parent_digit == i and repeated_digit == i:
            my_repeated = False
            repeated_digit = None

        if not minimum_children:
            if my_repeated:
                print(base * 10 + i)
                qualified += 1
        else:
            qualified += find_matches(minimum_children, maximum_children, my_repeated, i, parent_digit,
                                      last and i + 1 == maximum_digit, base * 10 + i, repeated_digit)
    return qualified


minimum_digits = decompose(minimum)
maximum_digits = decompose(maximum)

while len(minimum_digits) < len(maximum_digits):
    minimum_digits.insert(0, 0)

count = find_matches(minimum_digits, maximum_digits, False, None, None, True, 0)
print(count)
