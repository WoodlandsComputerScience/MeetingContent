lines = int(input())
student_answers = []
points = 0
for i in range(0, lines):
    student_answers.append(input())
for i in range(0, lines):
    if(input() == student_answers[i]):
        points += 1
print(points)