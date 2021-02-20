# Write a program that converts strings from one number format to another.

#     Binary to Denary (and vice versa)
#     HEX to Denary (and vice versa)
#     3Bit Grey Code (and vice versa) http://en.wikipedia.org/wiki/Grey_code

# Techniques

#     This project will assess Grey Codes, Suitable Test data and Algorithm design
#         To convert to and from grey codes I suggest a lookup table and the use of a Linear Search.

import math as m


def dentohex(numbertoconv):
    """
    >>> dentohex(0)
    '0'
    >>> dentohex(9)
    '9'
    >>> dentohex(10)
    'a'
    >>> dentohex(16)
    '10'
    """
    # hex numbers - 0-9 = 0-9, 10-15 = A-F
    hexnums = "0123456789abcdef" 
    numbertoconv = int(numbertoconv)
    output = ''
    workingnum = 0
    while numbertoconv > 0:
#        print (f'intial num {numbertoconv}')
        newhex = numbertoconv % 16
        newhex = hexnums[newhex]
        output += str(newhex)
#        print (output)
        workingnum = numbertoconv / 16
        numbertoconv = m.floor(workingnum)
    if not output:
        output = '0'
    return output[::-1]

def hextoden(numbertoconv):
    numbertoconv = str(numbertoconv)
    dennums = {"0": "0", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9", "a": "10", "b": "11", "c": "12", "d": "13", "e": "14", "f": "15"} 
    conv2 = ''
    for i in numbertoconv:
#        if i in dennums:
            #breakpoint()
            conv1 = dennums[i]
            conv2 += str(dentobin(conv1))
            output = bintoden(conv2)
    return output

def dentogrey(numbertoconv):
    pass

def greytoden(numbertoconv):
    pass

def bintoden(numbertoconv):
    reversednum = numbertoconv[::-1]
#    print (reversednum)
    binstep = 1
    p = 0
    convertednum = 0
    while p < len(reversednum):
        # print(f'index {reversednum[p]}')
        if reversednum[p] == '1':
            convertednum += binstep
        binstep = binstep * 2
        # print (f'binstep {binstep}')
        # print (f'convnum {convertednum}')
        p += 1
    return convertednum
    
def dentobin(numbertoconv):
    """
    >>> dentobin(240)
    '11110000'
    >>> dentobin(101)
    '1100101'
    >>> dentobin(23)
    '10111'
    """
    numbertoconv = int(numbertoconv)
    output = ''
    workingnum = 0
    while numbertoconv > 0:
#        print (f'intial num {numbertoconv}')
        output += str(numbertoconv % 2)
#        print (output)
        workingnum = numbertoconv / 2
        numbertoconv = m.floor(workingnum)
    return output[::-1]


if __name__ == '__main__':
    print(hextoden(input('please type a number to convert: ')))

    # choice = input('please type 1 for denary to binary, 2 for binary to denary: ')

    # if choice == 1:
    #     print(dentobin(input('please type a number to convert: ')))

    # if choice == 2:
    #     print(bintoden(input('please type a number to convert: ')))
