# Worksheet 1.3: Task 3

# Your code for the overall grade classification

# ask for filename of the student file
filename = input("What is the filename for the student file? ")
# open the file
raw_student_data = {}
with open(filename, "r") as file:
    for line in file.read().split("\n")[1:-1]:
        filtered_line = line.split(",")
        raw_student_data[filtered_line[0]] = filtered_line[1:]

# read in the data, and for each student calculate their average grade and classification
#print(raw_student_data)
classification = {"1":[70,101],
                  "2:1":[60, 70],
                  "2:2":[50, 60],
                  "3":[40,50],
                  "F":[-1,40]}

student_data = {"student:id":["average_grade","classification"]}
for entry in raw_student_data:
    student_data[entry] = 0
    for score in raw_student_data[entry]:
        if score:
            student_data[entry] += int(score)
    student_data[entry] /= len(raw_student_data[entry])
    classed_grade = ""
    for classname in classification:
        if classification[classname][0] <= student_data[entry] < classification[classname][1]:
            classed_grade = classname 
    student_data[entry] = [f"{student_data[entry]:.2f}",classed_grade]

file2 = open(f"{filename}_out.csv", "w")
file2.truncate()
for entry in student_data:
    file2.write(f"{entry}, {student_data[entry][0]}, {student_data[entry][1]}\n")



# write out this calculated data in the format without a header:
#      student_id,average_grade,classification - replace this with actual value
#      The average grade should be given to 2 decimal places
#      this can be achieved by using the following in an fstring: {variable_name:.2f}


# write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'raw_student_data.csv' -> 'raw_student_data.csv_out.csv'

# You can compare your output files with the 4 example files in example_outfiles folder