# To Do: 

    # Write a calculator program that
    #     Takes text input and calculates the answer
    #     The input will be in the format
    #         <NUMBER><SPACE><OPERATOR><SPACE><NUMBER>
    #         Support the following mathematical operators +-*/%
    #     The output should never be longer than 3 decimal places
    #       Extension - 
    #    If the first number is not inputted, use the answer from 
    #    the previous step automatically
    #       Extension 2 -   
    #    In VB.NET, create a GUI calculator with buttons for each 
    #    digit/operation. Each digit will append to a display textbox/string


# This project is designed to get you to understand
#     String splitting
#     Parsing strings
#     Float/Double/Real data-types,
#     Rounding, 
#     Mathematical Operators

print ('Please enter a calculation in the form x + x. You can use +, -, *, / and %')

def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def remainder(a, b):
    return a % b

userinput = input()

calcthis = userinput.split(" ")

calcthis[0] = float(calcthis[0])
calcthis[2] = float(calcthis[2])

#for calcthis[0] in calcthis:

if calcthis[1] == '+':
#    finalanswer = calcthis[0] + calcthis[2]
    finalanswer = add(calcthis[0],calcthis[2])
elif calcthis[1] == '-':
    finalanswer = minus(calcthis[0],calcthis[2])
elif calcthis[1] == '*':
    finalanswer = multiply(calcthis[0],calcthis[2])
elif calcthis[1] == '/':
    finalanswer = divide(calcthis[0],calcthis[2])
elif calcthis[1] == '%':
    finalanswer = remainder(calcthis[0],calcthis[2])
# elif calcthis[0] or calcthis[2] != float:
#     print('please enter a calculation I can understand')
else: 
    print('You need to use a defined operator')

finalanswer = round(finalanswer, 3)
print(finalanswer)

# sum = 5 + int('5')
# print(str(sum))  # should print 10
