
num = int(input("enter a number: "))
factorial = 1

if num < 0:
    print("factorial does not exist for negative numbers")
elif num == 0 or num == 1:
    print("factorial is 1")
else:
    for i in range(1,num+1):
        factorial *= i
        print("factorial of",num,"is",factorial)
