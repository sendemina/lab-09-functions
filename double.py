def double(n):
# n is a PARAMETER that is used within the function DEFINITION
# a PARAMETER is a placeholder for input data that gets processed by our functions
    return n * 2


userstring = input("Number please...")
usernum = int(userstring)

print(double(usernum))
# usernum is passed as an ARGUMENT as the double() function CALL
# an ARGUMENT is a placeholder for a real value that gets PASSED into a function call
# 1. usernum is evaluated; 2. double() is evaluated; 3. console.log() evaluated
