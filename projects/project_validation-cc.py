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
    nospace = removespace(ccnumber)
    ccindex = 0
    evenset = []
    oddset = []
    while ccindex < len(nospace):
        oddset += nospace[ccindex]
        ccindex += 1
        evenset += nospace[ccindex]
        ccindex += 1
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
    if (finalresult % 10) == 0:
        isitvalid = 'This credit card number is valid'
    else: 
        isitvalid = 'This credit card number is not valid'
    return isitvalid

# aa = ['1', '2', '3', '55']
# bb = [int(i) for i in aa]
# or do:
# aa = [int(i) for i in aa]

if __name__ == '__main__':
    print(checkccnumber(input('please give a credit card number: ')))
