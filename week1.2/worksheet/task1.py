# Worksheet 1.2: Task 1 Solution
from sys import exit
score = -1

while score < 0 or score > 100:
    score = input("Please enter your integer grade: ")
    if not score.isdecimal():
        exit("Error: Grade must be an integer between 0 and 100")
    else:
        score = int(score)
        if score < 0 or score > 100:
            exit("Error: Grade must be an integer between 0 and 100")

score_grades = {"Fail":range(40),
                "Pass":range(40, 70),
                "Distinction":range(70,101)}

for key in score_grades:
    if score in score_grades[key]:
        print(f"{score} is a {key}")
        break
