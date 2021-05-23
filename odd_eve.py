def singnum():
    n = int(input("Enter a number to  check it's odd or even:"))
    if (n % 2 == 0):
        print("EveN")
    else:
        print("Odd")
def listprinteve():
    f = int(input("Enter the range : "))
    s = int(input("Enter the initial value : "))
    lst_eve = []
    lst_odd = []
    for i in range (s,f+1):
        if(i%2==0):
            lst_eve.append(i)
        else:
            lst_odd.append(i)

    print(lst_eve)

def listprintodd():
    f = int(input("Enter the range : "))
    s = int(input("Enter the initial value : "))
    lst_eve = []
    lst_odd = []
    for i in range (s,f+1):
        if(i%2==0):
            lst_eve.append(i)
        else:
            lst_odd.append(i)


    print(lst_odd)

def user():
    print("Here you can check even or odd!")
    print("If you just check a single number please press 1")
    print("If you just wanna print a list of even numbers, please press 2")
    print("If you just wanna print a list of odd numbers, please press 3")
    n = int(input("Enter the number: "))
    if (n == 1):
        singnum()
    elif (n == 2):
        listprinteve()
    elif (n == 3):
        listprintodd()
    else:
        print("please Enter the correct keyword!!")


print("How many times you want to use this??")
a = int(input("Enter the times: "))
for i in range (0,a):
    user()
