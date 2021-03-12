'''
>>> mergesort(873430971362)
012333467789
'''

def everycharalist(query):
    newlist = []
    for i in query:
        newlist += i
    return newlist

# def joinlists(list1, list2):
#     newlist = list1 + list2

# startlist = [8], [7], [3], [4], [3], [0], [9], [7], [1], [3], [6], [2]

def merge(left, right):
    output = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else: 
            output.append(right[j])
            j += 1
    output.extend(left[i:])
    output.extend(right[j:])
    return output

def mergesort(query):
    list_len = len(query)
    if list_len == 1:
        return query
    mid = (len(query) // 2)
    leftlist = mergesort(query[:mid])
    rightlist = mergesort(query[mid:])
    return merge(leftlist, rightlist)

def backtostring(query):
    output = ''
    for i in query:
        output += i
    return output
if __name__ == '__main__':
    startlist = everycharalist(input('please enter the string you would like to sort: '))
    sortedlist = mergesort(startlist)
    finallist = backtostring(sortedlist)
    print (startlist)
    print (sortedlist)
    print (finallist)

