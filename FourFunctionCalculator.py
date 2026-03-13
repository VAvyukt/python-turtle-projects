from turtle import *

def checkNumber(num):
    if str(num).isdigit():
        return(1)
    else:
        return(0)
        
def checkSymbol(symbol):
    if symbol in "+-x/":
        return(1)
    else:
        return(0)

def performOp(first, second, op):
    if op == "+":
        return(first+second)
    elif op == "-":
        return(first-second)
    elif op == "x":
        return(first*second)
    else:
        return(first/second)

firstNum = int(input("Enter a number: "))
if checkNumber(firstNum) == 0:
    print("Not a valid number! 1 will be used.")
    firstNum = 1

secondNum = int(input("Enter another number: "))
if checkNumber(secondNum) == 0:
    print("Not a valid number! 1 will be used.")
    secondNum = 1

operator = input("Choose the mathematical expression to perform (+, -, x, or /): ")
if checkSymbol(operator) == 0:
    print("Not a valid operator. \"+\" will be used.")
    operator = "+"

answer = performOp(firstNum, secondNum, operator)

opMsg = "{} {} {} = {}"

print(opMsg.format(firstNum, operator, secondNum, answer))