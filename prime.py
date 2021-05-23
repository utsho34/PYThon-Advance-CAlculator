num = int(input("Enter the range: "))
#st = int(input("Initial: "))
def prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i == 0):
                return False
                break
        else:
            return True
    else:
        return False

lst = []
#st = int(input("st="))
st  = 0
while st <= num:
    if prime(st):
        lst.append(st)
    st = st + 1
print(f"The list of prime numbers in the range within {num} is ={lst}")
sum = 0
for i in range(0, len(lst)):
    sum = sum + lst[i]
print(f"The sum of all prime numbers in the range of {num}  is {sum}")
a = len(lst)
print(f"There  are total {a} numbers are prime in the range of {num}")
