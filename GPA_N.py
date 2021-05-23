n = int(input("Enter the number of courses: "))
lst = []
lst1 = []
lst2=[]
for i in range (1,n+1):
    a = float(input(f"Enter the obtained mark of course {i} :"))
    lst.append(a)
    if(a>=80):
        grade="A+"
        gpa=float(4.00)
        lst1.append(grade)
        lst2.append(gpa)
    elif(a>=75):
        grade = "A"
        gpa=float(3.75)
        lst1.append(grade)
        lst2.append(gpa)
    elif(a>=70):
        grade = "A-"
        gpa = float(3.50)
        lst1.append(grade)
        lst2.append(gpa)
    elif(a>=65):
        grade = "B+"
        gpa = float(3.25)
        lst1.append(grade)
        lst2.append(gpa)
    elif(a>=60):
        grade = "B"
        gpa = float(3.00)
        lst1.append(grade)
        lst2.append(gpa)
    elif(a>=55):
        grade = "B-"
        gpa = float(2.75)
        lst1.append(grade)
        lst2.append(gpa)
    elif(a>=50):
        grade = "C+"
        gpa = float(2.50)
        lst1.append(grade)
        lst2.append(gpa)
    elif(a>=45):
        grade = "C"
        gpa = float(2.25)
        lst1.append(grade)
        lst2.append(gpa)
    elif(a>=40):
        grade = "D"
        gpa = float(2.00)
        lst1.append(grade)
        lst2.append(gpa)
    else:
        grade = "F"
        gpa = float(0.00)
        lst1.append(grade)
        lst2.append(gpa)
print(f"Obtained NUMbers: {lst}")
print(f"Obtained Grade: {lst1}")
print(f"Obtained GPA: {lst2}")
sum = 0
for i in range(0, len(lst2)):
    sum = sum + lst2[i]
total = float(sum/n)
print(f"Total obtained GPA is= {total}")



