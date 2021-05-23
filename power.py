def pow():
    n = float(input("Enter a number: "))
    a = int(input("Enter the degree of power: "))
    power = 1
    i = 0
    for i in range (1,a+1):
        power = power * n
    print(power)


print("Welcome to power calculation.")
pow()