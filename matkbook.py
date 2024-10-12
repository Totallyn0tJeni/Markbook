fObj = open("marks.txt")

with open("marks.txt", 'r') as file:
    Students = file.readlines()

#print(Students)
studentNames = []
'''FirstName LastName- 66 - 2003.12.12 - 1 - Grade 4 - 405 - 18
Thor OdinSon- 10 - 2001.02.14 - 2 - Grade 2 - 201 - 11
Tony Stark- 20 - 1970.05.27 - 3 - Grade 9 - 901 - 9
Loki OdinSon- 98 - 2007.01.13 - 4 - Grade 7 - 701 -10
Serverou Snape- 79 - 1960.01.09 - 5 - Grade 11 - 1101 - 14
Lily Evans-100- 1960.01.20 - 6 - Grade 11 - 1102 -40
James Potter- 89 - 1960.03.27 - 7 - Grade 11 - 1102 -23
Harry Potter-90- 1980.07.31 - 8 - Grade 9 - 908 -3
Lyra Malfoy- 96 - 1998.06.20 - 9 - Grade 6 - 603 - 19'''

for student in Students:
    grades = (student.strip().split('-'))
    studentNames.append(grades[0])
print(studentNames)

class StudentXo:
    def __init__(self, name, mark, DOB, studentNumber, grade, classNum, attendance):
        self.name = name
        self.mark = mark
        self.DOB = DOB
        self.studentNumber = studentNumber
        self.grade = grade
        self.classNum = classNum
        self.attendance = attendance
        pass

pogramFunction = int(input("""Would you like to know:
1) Information about a specifc Student
2) The average grade
3) Top 3 performing students
4) List of students failing
5) Add student and grade
6) Update score
7) Change Attendance
8) Exit
"""))

while pogramFunction != 8:
    if pogramFunction == 1:
        print("1) Get Information about an specifc student")
        studentNames = []
        studentMarks = []
        studentDOB = []
        studentNum = []
        studentGrades = []
        studentClass = []
        attendance = []

        for student in Students:
            grades = (student.strip().split('-'))
            studentNames.append(grades[0])
        print(studentNames)

        for student in Students:
            grades = (student.strip().split('-'))
            studentMarks.append(int(grades[1]))
        #print(studentMarks)

        for student in Students:
            list = (student.strip().split('-'))
            studentDOB.append(list[2])
        #print(studentDOB)

        for student in Students:
            liste = (student.strip().split('-'))
            studentNum.append(liste[3])
        #print(studentNum)

        for student in Students:
            liste = (student.strip().split('-'))
            studentGrades.append(liste[4])
        #print(studentGrades)

        for student in Students:
            liste = (student.strip().split('-'))
            studentClass.append(liste[5])
        #print(studentClass)

        for student in Students:
            list1 = (student.strip().split('-'))
            attendance.append(list1[6])
        #print(attendance)

        nuM = len(Students) - 1
        print("Choose an index which corresponds to the students attendance number. Make sure that the index is within 0 and", nuM)

        dex = int(input("Enter your number:"))

        if dex > nuM:
            print("Index is greated than value please choose a lower number if you want to continue.")
        else:
            continuation = "n"
            if continuation != "y":
                stutent = StudentXo(studentNames[dex], studentMarks[dex] , studentDOB[dex], studentNum[dex], studentGrades[dex], studentClass[dex], attendance[dex])
                print("Student Name:" , stutent.name)
                print("Student Mark:" , stutent.mark)
                print("Student Date of Birth:" , stutent.DOB)
                print("Student Number:" , stutent.studentNumber)
                print("Student Grade:" , stutent.grade)
                print("Student Class:" , stutent.classNum)
                print("Students Attendnace:" , stutent.attendance)

        continuation = input("Would you like to continue: y or n ? ")
        if continuation == "n":
            print("Thank You! BYE BYE :D")
            fObj.close()
            exit()

    if pogramFunction == 2:
        print("2) The average grade")
        listOfGrades = []
        continuation = "n"
        if continuation != "y":
            for student in Students:
                grades = (student.strip().split('-'))
                #print(grades[1])
                listOfGrades.append(int(grades[1]))
                #print(listOfGrades)
                average = sum(listOfGrades)/len(listOfGrades)
            print(average)

        continuation = input("Would you like to continue: y or n ? ")
        if continuation == "n":
            print("Thank You! BYE BYE :D")
            fObj.close()
            exit()
       
    if pogramFunction == 3:
        print("3) Top 3 performing students")
        listOfGrades = []
        studentGrade = []
        continuation = "n"
        if continuation != "y":
            for student in Students:
                grades = (student.strip().split('-'))
                #print(grades[1])
                listOfGrades.append(int(grades[1]))
                #print(listOfGrades)
                #print(student)
                studentGrade.append(student.strip().split('-'))
            listOfGrades.sort(reverse=True)
            #print(listOfGrades)
            #print(studentGrade)
           
            for i in range(3): # 92, 90
                for a in studentGrade: # ['FirstName LastName', '92']
                    if listOfGrades[i] == int(a[1]):
                        #print(listOfGrades[i])
                        print(a[0])

        continuation = input("Would you like to continue: y or n ? ")
        if continuation == "n":
            print("Thank You! BYE BYE :D")
            fObj.close()
            exit()
           
    if pogramFunction == 4:
        print("4) List of students failing")
        listOfGrades = []
        studentGrade = []
        continuation = "n"
        if continuation != "y":
            for student in Students:
                grades = (student.strip().split('-'))
                #print(grades[1])
                listOfGrades.append(int(grades[1]))
                #print(listOfGrades)
                studentGrade.append(student.strip().split('-'))
            listOfGrades.sort(reverse=False)
            #print(listOfGrades)
            #print(studentGrade)
           
            for i in range(len(listOfGrades)): # 92, 90
                for a in studentGrade: # ['FirstName LastName', '92']
                    if listOfGrades[i] == int(a[1]):
                        if listOfGrades[i] < 50:
                            print(a[0])

        continuation = input("Would you like to continue: y or n ? ")
        if continuation == "n":
            print("Thank You! BYE BYE :D")
            fObj.close()
            exit()

    if pogramFunction == 5:
        print("5) Add student and grade")
        print(Students)
       
        newStudent = input("Add student name, grade, date of birth, student num, grade, class num & attendance all separated by '-': ")
        Students.append(newStudent + '\n')
        name, mark , dob , studentNum , grade, classNum, attendance = newStudent.split('-')
       
        with open("marks.txt", 'a') as file:
            file.write(newStudent + '\n')

        print("Student added successfully.")

    if pogramFunction == 6:
        print("6) Update score/grades") #update students grade
        print(Students)

        name_to_update = input("Enter student name to update (FirstName LastName): ")
        new_grade = int(input("Enter new grade: "))
        updated = False
        for i in range(len(Students)):
            student = Students[i].strip().split('-')
            if student[0] == name_to_update:
                Students[i] = f"{name_to_update}-{new_grade}-{student[2]}-{student[3]}-{student[4]}-{student[5]}-{student[6]},'\n"
                updated = True
                break
        if updated:
            with open("marks.txt", 'w') as file:
                file.writelines(Students)
            print("Grade updated.")
        else:
            print("Student not found.")

    if pogramFunction == 7:
        print("7) Change Attendance")
        print(Students)

        name_to_update = input("Enter student name to update (FirstName LastName): ")
        new_grade = int(input("Enter new attendnace: "))

        updated = False
        for i in range(len(Students)):
            student = Students[i].strip().split('-')
            if student[0] == name_to_update:
                Students[i] = f"{name_to_update}-{student[1]}-{student[2]}-{student[3]}-{student[4]}-{student[5]}-{new_grade},'\n"
                updated = True
                break
        if updated:
            with open("marks.txt", 'w') as file:
                file.writelines(Students)
            print("Atendance updated.")
        else:
            print("Student not found.")
       
    pogramFunction = int(input("""
What else would you like to know:
1) Information about a specifc Student
2) The average grade
3) Top 3 performing students
4) List of students failing
5) Add student and grade
6) Update score
7) Change Attendance
8) Exit
"""))
   
if pogramFunction == 8:
        print("Thank You! BYE BYE :D")
        print("Your Marks Have Been Updated in the File")
        fObj.close()
        exit()
