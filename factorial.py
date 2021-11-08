def factorial(n):
# an ITERATIVE example of the factorial def
    total = 1
    for i in range (0, n):
    # i < n ensures that i will never reach n... (n will never == i)
        total = total * (n - i)
    # ... and therefore we never multiply it by 0
        print("Current i is: " + str(i))
        print("Current value of total is: " + str(total))
    return total

userstring = input("Number please... ")
usernum = int(userstring)

print(str(usernum) + "! is " + str(factorial(usernum)))
