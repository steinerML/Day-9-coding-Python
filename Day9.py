# University examination calculator tool
#Suppose you just attended a University examination and these are your marks. Based on these marks, you have the following brackets for each grade.

#Grade A >= 80%
#Grade B >= 60
#Grade C >= 50%
#Grade F <50%

#Function to define average

def find_average (marks):
    sum_of_marks = sum(marks)
    number_of_subjects = len(marks)
    average = sum_of_marks/number_of_subjects
    return average

#Calculate the grade and return

def compute_grade(average):
    if average >= 80:
        grade = 'A'
    elif average >= 60:
        grade = 'B'
    elif average >= 50:
        grade = 'C'
    else:
        grade = 'F'
    return grade
    
marks = [55,67,88,92,54]
average = find_average(marks)
print("Your average is:", average)
grade = compute_grade(average)
print("Your grade is:", grade)


    
