sum = 0
def add(a,b):
    sum = a+b
    print(sum)
def min(a,b):
    sum = a-b
    print(sum)
def inn(a,b):
    sum = a*b
    print(sum)
def di(a,b):
    sum = a/b
    print(sum)
def simcal():
        a = float(input("Enter a number: "))
        print("Enter operation to perform: you can you can use + for addition,- ,* and /,=")

        op = str(input("Enter the operator: "))
        if (op == "+"):
            b = float(input())
            add(a, b)
        elif (op == "-"):
            b = float(input())
            min(a, b)
        elif (op == "*"):
            b = float(input())
            inn(a, b)
        elif (op == "/"):
            b = float(input())
            di(a, b)
        elif (op == "="):
            print("Total = ", sum)
        else:
            print("Please enter correct notations")
n = int(input("How many time do you wanna use this??"))
for i in range(1,n+1):
    simcal()



