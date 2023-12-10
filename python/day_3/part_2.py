# with open("day_3/test.txt") as file:
with open("day_3/input.txt") as file:
    lines = [line.rstrip() for line in file]
T = []
for index, line in enumerate(lines):
    T.insert(index, line)


def is_asterisk(s):
    if s == "*":
        return True
    else:
        return False


def lefparttofnumber(lines: list, index: int, value: int, currentnumber: str) -> str:
    if value + 1 < len(lines[index]) and value - 1 >= 0:
        if not lines[index][value - 1].isdigit():
            return currentnumber

        else:
            return (
                lefparttofnumber(lines, index, value - 1, lines[index][value - 1])
                + currentnumber
            )
    else:
        print(
            "left check out of bounds at index: ",
            index,
            " : ",
            value,
            " : ",
            currentnumber,
        )
        return currentnumber


def rightpartofnumber(lines: list, index: int, value: int, currentnumber: str) -> str:
    if value + 1 < len(lines[index]) and value - 1 >= 0:
        if not lines[index][value + 1].isdigit():
            return currentnumber
        else:
            return rightpartofnumber(
                lines, index, value + 1, currentnumber + lines[index][value + 1]
            )
    else:
        print(
            "right check out of bounds at index: ",
            index,
            " : ",
            value,
            " : ",
            currentnumber,
        )
        return currentnumber


def middleofnumber(lines: list, index: int, value: int, currentnumber: str) -> str:
    if not lines[index][value - 1].isdigit() and not lines[index][value + 1].isdigit():
        return currentnumber

    if lines[index][value - 1].isdigit() and lines[index][value + 1].isdigit():
        return (
            lefparttofnumber(lines, index, value - 1, lines[index][value - 1])
            + currentnumber
            + rightpartofnumber(lines, index, value + 1, lines[index][value + 1])
        )
    elif lines[index][value - 1].isdigit():
        return (
            lefparttofnumber(lines, index, value - 1, lines[index][value - 1])
            + currentnumber
        )
    elif lines[index][value + 1].isdigit():
        return rightpartofnumber(
            lines, index, value + 1, currentnumber + lines[index][value + 1]
        )
    else:
        return currentnumber


def check_for_adjacents(lines: list, index: int, value: int) -> int:
    print("adjacents: ")
    if index >= 0 and value <= len(lines[index]) and value >= 0:
        print(
            lines[index - 1][value - 1],
            lines[index - 1][value],
            lines[index - 1][value + 1],
        )
    if value <= len(lines[index]) and value >= 0:
        print(lines[index][value - 1], lines[index][value], lines[index][value + 1])
    if index <= len(lines) and value <= len(lines[index]) and value >= 0:
        print(
            lines[index + 1][value - 1],
            lines[index + 1][value],
            lines[index + 1][value + 1],
        )

    power = 1
    count = 0
    # check above asterisk
    if lines[index - 1][value].isdigit():
        print("digit above")
        count = count + 1
        mid = int(middleofnumber(lines, index - 1, value, lines[index - 1][value]))
        print("power * mid: ", power, " * ", mid)
        power *= mid
    else:
        # check top left of asterisk
        if lines[index - 1][value - 1].isdigit():
            print("digit top left")
            count = count + 1
            topleft = int(
                lefparttofnumber(
                    lines, index - 1, value - 1, lines[index - 1][value - 1]
                )
            )
            print("power * topleft: ", power, " * ", topleft)
            power *= topleft
        # check top left of asterisk
        if lines[index - 1][value + 1].isdigit():
            print("digit top right")
            count = count + 1
            topright = int(
                rightpartofnumber(
                    lines, index - 1, value + 1, lines[index - 1][value + 1]
                )
            )
            print("power * topright: ", power, " * ", topright)
            power *= topright
    # check below asterisk
    if lines[index + 1][value].isdigit():
        print("digit below")
        count = count + 1
        below = int(middleofnumber(lines, index + 1, value, lines[index + 1][value]))
        print("power * below: ", power, " * ", below)
        power *= below
    else:
        # check bottom left of asterisk
        if lines[index + 1][value - 1].isdigit():
            print("digit bottom left")
            count = count + 1
            belowleft = int(
                lefparttofnumber(
                    lines, index + 1, value - 1, lines[index + 1][value - 1]
                )
            )
            print("power * belowleft: ", power, " * ", belowleft)
            power *= belowleft
        # check bottom right of asterisk
        if lines[index + 1][value + 1].isdigit():
            print("digit bottom right")
            count = count + 1
            belowright = int(
                rightpartofnumber(
                    lines, index + 1, value + 1, lines[index + 1][value + 1]
                )
            )
            print("power * belowright: ", power, " * ", belowright)
            power *= belowright
    # check left of asterisk
    if lines[index][value - 1].isdigit():
        print("digit on left")
        count = count + 1
        left = int(lefparttofnumber(lines, index, value - 1, lines[index][value - 1]))
        print("power * left: ", power, " * ", left)
        power *= left
    # check right of asterisk
    if lines[index][value + 1].isdigit():
        print("digit on right")
        right = int(rightpartofnumber(lines, index, value + 1, lines[index][value + 1]))
        count = count + 1
        print("power * right: ", power, " * ", right)
        power *= right
    if count < 2:
        return 0
    else:
        return power


part_number_total = 0
activenumber = False
for index, row in enumerate(T):
    for jndex, value in enumerate(row):
        # print("current: ", T[index][jndex])
        if is_asterisk(T[index][jndex]):
            print("line: ", index)
            part_number_total = part_number_total + check_for_adjacents(
                lines, index, jndex
            )


print(part_number_total)
