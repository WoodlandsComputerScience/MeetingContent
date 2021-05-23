import math


def pythagorean(a, b):
    return math.sqrt(a**2 + b**2)


sides = open("sides.txt", mode='r', encoding='utf-8')
answers = open("answers.txt", mode='w', encoding='utf-8')
for line in sides:
    line_input = list(map(int, line.split()))
    answers.write(str(pythagorean(line_input[0], line_input[1])))
    answers.write('\n')
sides.close()
answers.close()
