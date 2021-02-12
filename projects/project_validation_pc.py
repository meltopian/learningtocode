validpc = frozenset({
    'a11aa', 
    'aa11aa', 
    'a111aa', 
    'aa111aa',
    })
    # this is a set. It's unordered items in squiggly brackets
    # A list is a list of items, mutable and changable.
    # A tuple is the same but immutable, but still the order matters
    # A set means the program can optimise checking whether something's in it 
    # Sets can't contain duplicates.
    # Intersection (what's in both, use & or .intersection()) 
    # and union (combination of both without dupes, use | or .union())
    # Make a set immutable by processing it with a frozenset function like this:
    # frozenset({'data', 'data2',})
def checkpostcode(postcode):
    """
    >>> checkpostcode('SW15 5PU')
    True
    >>> checkpostcode('GL51 0EX')
    True
    >>> checkpostcode('gl51 0ex')
    True
    >>> checkpostcode('gl510ex')
    True
    >>> checkpostcode('thisisnotapostcode')
    False
    """
    postcode = postcode.replace(" ", "")
    index = 0
    conformedpc = ""
    while index < len(postcode):
        if postcode[index].isalpha():
            conformedpc += 'a'
        if postcode[index].isdigit(): 
            conformedpc += '1'
        index += 1
    return conformedpc in validpc

"""
two sections:
1 - 2-4 characters
        1-2 letters
        1-2 digits
2 - 3 characters
        1 number    
        2 letters

a11aa
aa11aa
a111aa
aa111aa

- strip out spaces
- remove capitals
conform all letters to a and all numbers to 1
check against known list
"""

if __name__ == '__main__':
    print(checkpostcode(input('please give a postcode: ')))
