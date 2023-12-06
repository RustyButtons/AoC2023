from array import *

"""
Using a Matrix (rows, columns / 2d array)
if [row][value] is a digit need to check if:
    horizontals
    [row][value+1] != symbol or digit
    [row][value-1] != symbol or digit
    above
    [row-1][value] != symbol
    [row-1][value+1] != symbol
    [row-1][value-1] != symbol
    below
    [row-1][value] != symbol
    [row-1][value+1] != symbol
    [row-1][value-1] != symbol
"""
# with open("day_3/test.txt") as file:
with open("day_3/input.txt") as file:
    lines = [line.rstrip() for line in file]
T = []
for index, line in enumerate(lines):
    T.insert(index, line)

# for r in T:
#     for c in r:
#         print(c, end=" ")
#     print()


def is_symbol(s):
    if s != "." and not s.isdigit():
        # print(s, " is  a symbol")
        return True
    else:
        return False


def is_dot(s):
    if s == ".":
        return True
    else:
        return False


def check_adjacents(lines: list, index: int, value: int) -> bool:
    # print(lines[index][value], "   -------------- ")
    print("adjacents: ")
    if index - 1 > 0 and value + 1 < len(lines[index]) and value - 1 > 0:
        print(
            lines[index - 1][value - 1],
            lines[index - 1][value],
            lines[index - 1][value + 1],
        )
    if value + 1 < len(lines[index]) and value - 1 > 0:
        print(lines[index][value - 1], lines[index][value], lines[index][value + 1])
    if index + 1 < len(lines) and value + 1 < len(lines[index]) and value - 0 > 0:
        print(
            lines[index + 1][value - 1],
            lines[index + 1][value],
            lines[index + 1][value + 1],
        )

    return (
        index + 1 < len(lines)
        and is_symbol(lines[index + 1][value])
        or index - 1 > 0
        and is_symbol(lines[index - 1][value])
        or index + 1 < len(lines)
        and value + 1 < len(lines[index])
        and is_symbol(lines[index + 1][value + 1])
        or index + 1 < len(lines)
        and value - 1 > 0
        and is_symbol(lines[index + 1][value - 1])
        or index - 1 > 0
        and value + 1 < len(lines[index])
        and is_symbol(lines[index - 1][value + 1])
        or index - 1 > 0
        and value - 1 > 0
        and is_symbol(lines[index - 1][value - 1])
        or value + 1 < len(lines[index])
        and is_symbol(lines[index][value + 1])
        or value - 1 > 0
        and is_symbol(lines[index][value - 1])
    )


part_number_total = 0
number = ""
activenumber = False
for index, row in enumerate(T):
    for jndex, value in enumerate(row):
        print("current: ", T[index][jndex])
        if T[index][jndex].isdigit():
            number = number + T[index][jndex]
            print("current number: ", number)
            if check_adjacents(T, index, jndex):
                activenumber = True
        else:
            if activenumber and number != "":
                print("adding: ", part_number_total, " + ", int(number))
                part_number_total = part_number_total + int(number)

            activenumber = False
            number = ""
    if activenumber and number != "":
        part_number_total = part_number_total + int(number)

    activenumber = False

print(part_number_total)
