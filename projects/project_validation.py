# Data that is entered can be incorrect. E.g “Monkey” is not a valid postcode, “Smith53” is not a valid surname.

# You must write functions that can validate the following

#     Surname (E Grade)
#     Parity Bit (D Grade)
#     Credit Card Number - with or without spaces (D Grade)
#     Postcode (D Grade) (Optional B Grade - full http://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom)
#     ISBN 10 code (http://en.wikipedia.org/wiki/Check_digit) (C Grade)
#         The ISBN code should work with either dashes and spaces in the number or not

# Techniques

# This project is designed to get you to

#     Use "Modula Arithmetic"
#     Consider careful test data





# def surnamevalidate(text):
#     if "text".isalpha() == True and "text[0]".isupper() == True:
#         return "yes"
#     else: 
#         return "no"




# if __name__ == '__main__':
#     while True:
#         surnamevalidate(input)

def checksurname(): 
    surname = input('please enter a surname to check: ')
    if (surname.isalpha()) and (surname[0].isupper()) and (surname[1:].islower()):
        return "valid surname"
    else:
        return "invalid surname"

def checkparity():
    parity = input('enter an 8-digit binary number representing a byte with parity included: ')
    addbits = int(int(parity[0]) + int(parity[1]) + int(parity[2]) + int(parity[3]) + int(parity[4]) + int(parity[5]) + int(parity[6]))
    # if (parity.isalpha) == True or len(parity) > 8:
    #     return('invalid input')
    if addbits % 2 == 0 and int(parity[7]) == 0:
        return('valid parity')
    elif addbits % 2 == 1 and int(parity[7]) == 1:
        return('valid parity')

    else:
        return('invalid parity')

#def checkccnumber():       

# def checkpostcode():

# def checkisbn():


if __name__ == '__main__':
    while True:

        whattocheck = input('Enter a digit to choose what you want to validate - 1 - surname, 2 - parity, 3 - ccnumber, 4 - postcode or 5 - isbn: ')
        if whattocheck == "1":
            print(checksurname())
        if whattocheck == "2":
            print(checkparity())
        # if whattocheck == "3":
        #     print(checkccnumber())
        # if whattocheck == "4":
        #     print(checkpostcode())
        # if whattocheck == "5":
        #     print(checkisbn())
        else: 
            print('try again')
        