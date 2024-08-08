fObj = open("marks.txt")

with open("marks.txt", 'r') as file:
    Students = file.readlines()

print(Students)

pogramFunction = int(input("""Would you like to know:
1) The average grade
2) Top 3 performing students
3) List of students failing
4) Add student and grade
5) Update score
6) Exit 
"""))

while pogramFunction != 6:
    if pogramFunction == 1:
        print("1) The average grade")
        listOfGrades = []
        for student in Students:
            grades = (student.strip().split('-'))
            #print(grades[1])
            listOfGrades.append(int(grades[1]))
            #print(listOfGrades)
            average = sum(listOfGrades)/len(listOfGrades)
        print(average)
        
    if pogramFunction == 2:
        print("2) Top 3 performing students")
        listOfGrades = []
        studentGrade = []
        for student in Students:
            grades = (student.strip().split('-'))
            #print(grades[1])
            listOfGrades.append(int(grades[1]))
            #print(listOfGrades)
            studentGrade.append(student.strip().split('-'))
        listOfGrades.sort(reverse=True)
        #print(listOfGrades)
        #print(studentGrade)
        
        for i in range(3): # 92, 90 
            for a in studentGrade: # ['FirstName LastName', '92']
                if listOfGrades[i] == int(a[1]):
                    print(a[0])
            
    
    if pogramFunction == 3:
        print("3) List of students failing")
        listOfGrades = []
        studentGrade = []
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

    if pogramFunction == 4:
        print("4) Add student and grade")
        print(Students)
        
        newStudent = input("Add student first and last name & Grade all separated by '-': ")
        Students.append(newStudent + '\n')
        name, grade = newStudent.split('-')
        
        with open("marks.txt", 'a') as file:
            file.write(newStudent + '\n')

        print("Student added successfully.")

    if pogramFunction == 5:
        print("5) Update score/grades") #update students grade
        print(Students)

        name_to_update = input("Enter student name to update (FirstName LastName): ")
        new_grade = int(input("Enter new grade: "))
        updated = False
        for i in range(len(Students)):
            student = Students[i].strip().split('-')
            if student[0] == name_to_update:
                Students[i] = f"{name_to_update}-{new_grade}\n"
                updated = True
                break
        if updated:
            with open("marks.txt", 'w') as file:
                file.writelines(Students)
            print("Grade updated.")
        else:
            print("Student not found.")
        

    pogramFunction = int(input("""What else would you like to know:
1) The average grade
2) Top 3 performing students
3) List of students failing
4) Add student and grade
5) Update score
6) Exit 
""")) 
    

if pogramFunction == 6:
        print("Thank You! BYE BYE :D")
        exit()