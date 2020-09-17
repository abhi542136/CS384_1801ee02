# Function to add two numbers
def add(num1, num2):
    addition = num1 + num2
    return addition

# Function to subtract two numbers


def subtract(num1, num2):
    subtraction = num1 - num2
    return subtraction

# Function to multiply two numbers


def multiply(num1, num2):
    # Multiplication Logic
    multiplication = num1*num2
    return multiplication

# Function to divide two numbers


def divide(num1, num2):
    # DivisionLogic
    division = num1/num2
    return division


def power(num1, num2):  # num1 ^ num2
    # DivisionLogic
    # if((isinstance(num1, int) or isinstance(num1, float)) and (isinstance(num2, int) or isinstance(num2, float)):
    x = 1
    if(num2 < 0):
        num1 = 1/num1
        y = -(num2)
    else:
        y = num2
    for num in range(y):
        x = x*num1

    power = round(x, 3)
    # else:
   # power=0

    return power

# Python 3 program to print GP.  geometric Progression
# You cant use the inbuilt python function. Write your own function


def printGP(a, r, n):
    gp = []
    for num in range(n):
        x = pow(r, num)
        y = a*x
        ans = round(y, 3)
        gp.append(ans)

    return gp

# Python 3 program to print AP.  arithmetic Progression
# You cant use the inbuilt python function. Write your own function


def printAP(a, d, n):
    ap = []
    return ap

# Python 3 program to print HP.   Harmonic Progression
# You cant use the inbuilt python function. Write your own function


def printHP(a, d, n):
    hp = []
    return hp
