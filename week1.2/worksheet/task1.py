# Worksheet 1.2: Task 1 Solution
from sys import exit
score = -1

#While loop to continuously prompt user until they're inpoutted the right grade
while score < 0 or score > 100:
    score = input("Please enter your integer grade: ")
    if not score.isdecimal():
        exit("Error: Grade must be an integer between 0 and 100")
    else:
        score = int(score)
        if score < 0 or score > 100:
            exit("Error: Grade must be an integer between 0 and 100")

# LUT to map grade to score ranges
score_grades = {"Fail":range(40),
                "Pass":range(40, 70),
                "Distinction":range(70,101)}

#Iterate thorough each grade to print correct message
for key in score_grades:
    if score in score_grades[key]:
        print(f"{score} is a {key}")
        break
