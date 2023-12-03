import re
from word2number import w2n

with open("day_1/input.txt") as file:
    lines = [line.rstrip() for line in file]

number_words = ["one","two","three","four","five","six","seven","eight","nine",]
numbers = ["1","2","3","4","5","6","7","8","9"]
reverse_number_words = [num[::-1] for num in number_words]

numbers_and_words = numbers + number_words
numbers_and_reverse = numbers + reverse_number_words
numbers_regex = re.compile("|".join(numbers_and_words))
reverse_regex = re.compile("|".join(numbers_and_reverse))

part_2_answer = 0
for line in lines:
    firstdigit = re.search(numbers_regex, line).group(0)
    enil = line[::-1]
    lastdigit = re.search(reverse_regex, enil).group(0)    
    first = w2n.word_to_num(firstdigit)
    last = w2n.word_to_num(lastdigit[::-1])
    number = str(w2n.word_to_num(firstdigit)) + str(w2n.word_to_num(lastdigit[::-1]))
    number = int(number)
    part_2_answer = part_2_answer + number

print(part_2_answer)



