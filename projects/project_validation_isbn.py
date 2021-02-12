'''
Validity: 10 (old) or 13 (new) numbers
10 digit:
number position from left to right, backwards
multiply number by its position
sum all products
divide by 11, find out remainder
if remainder is 0, it's valid

13 digit:
number position left to right, backwards
multiply each number by 1 and 3 alternating (odd - 1, even - 3)
divide sum by 10, find out remainder
if remainder is 0, it's valid

remove anything that's not a number

'''
def removespace(string):
    return string.replace(" ", "")

def removedash(string):
    return string.replace("-", "")

def reverse(string):
  return string[::-1]

def isbn13(onethree):
    oddlist = []
    evenlist = []
    multipliedlist = []
    multiplied = 0
    for i in range(13):
        if (i + 1) % 2 == 1:
            multiplied = 1 * int(onethree[i])
            oddlist.append(multiplied)
        if (i + 1) % 2 == 0:
            multiplied = 3 * int(onethree[i])
            evenlist.append(multiplied)
    isbn13summing = 0
    isbn13total = 0
    multipliedlist = oddlist + evenlist
    while isbn13summing < len(multipliedlist):
        isbn13total += multipliedlist[isbn13summing]
        isbn13summing += 1
    print (multipliedlist)
    return (isbn13total % 10) == 0
def isbn10(onezero):
    multipliedlist = []
    multiplied = 0
    for i in range(10):
        multiplied = int(i + 1) * int(onezero[i])
        multipliedlist.append(multiplied)
        isbn10summing = 0
        isbn10total = 0
        while isbn10summing < len(multipliedlist):
            isbn10total += multipliedlist[isbn10summing]
            isbn10summing += 1
    return (isbn10total % 11) == 0
def checkisbn(isbn):
    """
    >>> 978-1-56619-909-4
    True
    >>> 1-56619-909-3
    True
    >>> 1029304901
    False
    >>> 1019294069482
    False
    """
    isbn = removespace(isbn)
    isbn = removedash(isbn)
    isbn = reverse(isbn)
    print(isbn)
    if len(isbn) == 10:
        return isbn10(isbn)
    if len(isbn) == 13:
        return isbn13(isbn)
    else:
        return 'input is not a 10 digit or 13 digit ISBN number'





    pass


if __name__ == '__main__':
    print(checkisbn(input('please give an isbn number: ')))
