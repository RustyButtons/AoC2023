import re

with open("day_1/input.txt") as file:
    lines = [line.rstrip() for line in file]

part_1_answer = 0
for line in lines:
    firstdigit = re.search('\d', line).group(0)
    enil = line[::-1]
    lastdigit = re.search('\d', enil).group(0)
    number = firstdigit + lastdigit
    number = int(number)
    part_1_answer = part_1_answer + number

print(part_1_answer)
