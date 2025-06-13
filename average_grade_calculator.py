import math
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

scores = student_marks[query_name]
ave_score = sum(scores) / len(scores)
print(f'{ave_score:.2f}')
