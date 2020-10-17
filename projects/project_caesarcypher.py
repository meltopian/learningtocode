# This is a stub - the doctest gets nothing back because we haven't written the code yet

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def getindex(letter):
    """
    >>> getindex('a')
    0
    >>> getindex('z')
    25
    """
    for i in range(26):
        newletter = alphabet[i]
        if newletter == letter:
            return i

#getindex('z')

def caesar_cypher(offset, word):
    """
    >>> caesar_cypher(1, 'abc')
    'bcd'
    >>> caesar_cypher(1, 'hello')
    'ifmmp'
    >>> caesar_cypher(-1, 'ifmmp')
    'hello'
    >>> caesar_cypher(1, 'xyz')
    'yza'
    #>>> caesar_cypher(1, 'z a b')
    #'a b c'
    """
    outputlist = []
    convertedtostring = ''
    for letter in word:
        letter_number = getindex(letter)
        letter_number = int(letter_number) + int(offset)
        letter_number = (letter_number % len(alphabet))
        finalletter = alphabet[letter_number]
        outputlist.append(finalletter)
        convertedtostring = ''.join(outputlist)
    return convertedtostring

if __name__ == "__main__":
    result = caesar_cypher(input('offset: '), input('word: '))
    print(result)