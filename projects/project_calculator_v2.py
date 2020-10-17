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

    # define functions  

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

def parsecalc():
    userinput = str(input('please enter a calculation: '))
    calcthis = userinput.split(" ")
    while True:
        if len(calcthis) == 3:
            answer = int(calcthis[0]) (calcthis[1]) int(calcthis[2])
            print(answer)
            return 
        elif len(calcthis) == 2:
            answer = (answer + calcthis[1])
            print(answer)
            return
    print (calcthis)

if __name__ == "__main__":
#    result = caesar_cypher(input('offset: '), input('word: '))
#    print(result)

parsecalc()

