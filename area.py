import math
def triangle():
     b = float(input("Enter the base: "))
     h = float(input("Enter the height: "))
     print(f"the area of triangle is {0.5*b*h} unit")
def rectangle():
    w = float(input("Enter the width: "))
    h = float(input("enter the height: "))
    print(f"The area of the rectangle is: {w*h} unit")
def trapezium():
     a = float(input("Enter the upper base: "))
     b = float(input("Enter the lower base: "))
     h = float(input("Enter the height: "))
     print(f"the area of the triangle is {((a+b)/2)*h} unit")
def ellipse():
    a = float(input("Enter the first axis: "))
    b = float(input("Enter the another axis: "))
    print(f"The area of the ellipse is {math.pi*a*b} unit")
def square():
    a = float(input("Enter the length of hand: "))
    print(f"The area of the square is: {a*a} unit")
def parallelogram():
    a = float(input("Enter the base: "))
    b = float(input("Enter the vertical height: "))
    print(f"The area of the parallelogram is: {a*b} unit")
def circle():
    r = float(input("Enter the radius: "))
    print(f"The area of the circle is: {math.pi*r*r} unit")
def equilitriangle():
    a = float(input("Enter the value of one side: "))
    print(f"The area of equilateral triangle is {((math.sqrt(3)/4)*(a**2))}")
print("Welcome to basic area calculator!!")
print('''for triangle press 1, for rectangle press 2, for  trapezium press 3,for ellipse 
press 4,for square press 5,for parallelogram press 6,for circle press 7,
for equilateral triangle press 8''')
n = int(input("press the suitable icon and press enter:  "))
if (n == 1):
    triangle()
elif (n ==2):
    rectangle()
elif (n==3):
    trapezium()
elif(n==4):
    ellipse()
elif(n==5):
    square()
elif(n==6):
    parallelogram()
elif(n==7):
    circle()
elif(n==8):
    equilitriangle()
else:
    print("please enter the correct keyword!!")


