print("Welcome to the GPA calculator Using Grade")
print("Please Enter the Grade as standard")
print("AT last double click on enter")

points = {'A+':4.0,'A':3.75,'A-':3.5,'B+':3.25,'B':3.00,'B-':2.75,'C+':2.5,'C':2.25,'C-':2.0,'D+':1.75,'D':1.5,'D':1.0,'F':0.0}
num_courses = 0
total_points = 0
done = False
while not done:
    grade = input()
    if grade == '':
        done = True
    elif grade not in points:
        print("Uknown grade '{0} being ignored".format(grade))
    else:
        num_courses+=1
        total_points+=points[grade]
    if num_courses>0:
        total_gpa = total_points/num_courses
print("Your GPA is {0:.3}".format(total_points/num_courses))