def removespace(string):
    return string.replace(" ", "") 

def getsum(n):
    summing = 0
    for digit in str(n):
        summing += int(digit)
    return summing

def checkccnumber(ccnumber):       
# remove spaces
# separate even and odd indexes
# double the numbers in first set
# for any that end up as 2 digit numbers, add the digits together
# Add all doubled digits in first set to non-doubled digits in second set
# If the final result is divisible by ten, it's valid #
#    ccnumber = input('Please enter a credit card number to validate: ')
# ADD A DOCTEST
    """
    >>> checkccnumber('3400 0000 0000 009')
    True
    >>> checkccnumber('4111 1111 1111 1111')
    True
    >>> checkccnumber('5500 0000 0000 0004')
    True
    >>> checkccnumber('12345678')
    False
    >>> checkccnumber('3000 0000 0000 04')
    True
    >>> checkccnumber('3000 0000 0000 04')
    True
    >>> checkccnumber('6011 0000 0000 0004')
    True
    >>> checkccnumber('2014 0000 0000 009')
    True
    >>> checkccnumber('3088 0000 0000 0009')
    True
    """
    nospace = removespace(ccnumber)
    ccindex = 0
    oddsetindexes = list(range(0, len(nospace), 2))
    evensetindexes = list(range(1, len(nospace), 2))
#    breakpoint()
    while ccindex < len(nospace):
        pass
    # while ccindex < len(nospace):
    #     oddset += nospace[ccindex]
    #     ccindex += 1
    # ccindex = 1
    # while ccindex < len(nospace):
    #     evenset += nospace[ccindex]
    #     ccindex += 1

    # FIX THIS COMMENTED OUT SECTION - 
    # it won't work on odd numbers if it's 
    # adding 2 to the index each time
    # tuple(range(0, len(nospace), 2))

    oddset = [int(i) for i in oddset]
    evenset = [int(i) for i in evenset]
    doubledindex = 0
    while doubledindex < len(oddset):
        oddset[doubledindex] = oddset[doubledindex] * 2
        doubledindex += 1
    getsumindex = 0
    while getsumindex < len(oddset):
        oddset[getsumindex] = getsum(oddset[getsumindex])
        getsumindex += 1
    # print(oddset)
    # print(evenset)
    part1 = 0
    part2 = 0
    finalresult = 0
    for i in oddset:
        part1 += i
    # print(part1)
    for i in evenset:
        part2 += i
    # print(part2)
    finalresult = part1 + part2
    return (finalresult % 10) == 0
   
# aa = ['1', '2', '3', '55']
# bb = [int(i) for i in aa]
# or do:
# aa = [int(i) for i in aa]

if __name__ == '__main__':
    print(checkccnumber(input('please give a credit card number: ')))




# Example numbers:
# Visa  	4111 1111 1111 1111 
# MasterCard  	5500 0000 0000 0004 
# American Express  	3400 0000 0000 009 
# Diner's Club  	3000 0000 0000 04 
# Carte Blanche  	3000 0000 0000 04 
# Discover  	6011 0000 0000 0004 
# en Route  	2014 0000 0000 009 
# JCB  	3088 0000 0000 0009 
