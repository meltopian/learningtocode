def everycharalist(query):
    newlist = []
    for i in query:
        newlist += i
    return newlist

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

def sorting(query):
    list_len = len(query)
    if list_len == 1:
        return query
    mid = (len(query) // 2)
    leftlist = sorting(query[:mid])
    rightlist = sorting(query[mid:])
    return merge(leftlist, rightlist)

def backtostring(query):
    output = ''
    for i in query:
        output += i
    return output

def mergesort(query):
    '''
    >>> mergesort('873430971362')
    '012333467789'
    '''
    startlist = everycharalist(query)
    sortedlist = sorting(startlist)
    finallist = backtostring(sortedlist)
    return finallist

if __name__ == '__main__':
    print(mergesort(input('what do: ')))