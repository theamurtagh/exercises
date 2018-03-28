#Thea M Factorial of a positive no        
def func_factorial(n):
    # factorial is n * by all the '+' no less than it
    #n= 7
    #if n == 1:
        # if n is 1 return 1
        #return n
    #else:
        #return n * (n-1)
        # 

# Python program to find the factorial of a number provided by the user.

# change the value for a different result
#n= 7
# uncomment to take input from the user
#num = int(input("Enter a number: "))

    factorial = 1

# check if the number is negative, positive or zero
    if n < 0:
        print("not doing factorial for zero")
    elif n == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,n + 1):
            factorial = factorial*i
            print("The factorial of",n,"is",factorial)   

func_factorial (7)
