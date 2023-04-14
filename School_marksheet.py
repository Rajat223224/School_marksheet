students = ['raju','geeta','suneeta']
subjects = ['Maths', 'Science', 'English','Art']
marks = [[80, 85, 90,50], [75,40, 80, 85], [80,90, 95, 100]]
print("School Marsheet Result")
print("Student\tMaths\tScience\tEnglish\tArt\tTotal")
for i in range(len(students)):
    total_marks = sum(marks[i])
    print(students[i], end='\t')
    for j in range(len(subjects)):
        print(marks[i][j], end='\t')
    print(total_marks)
