
#from mergesort import *
# https://www.geeksforgeeks.org/python-program-for-binary-search/
# https://www.bbc.co.uk/bitesize/guides/zjdkw6f/revision/3
listofdicts = []
f = open("project_recordsearch_data.csv", 'r')
for line in f:
    d = {}
    worklist = [item.strip() for item in line.split("|")]
    #worklist = list(map(lambda ss: ss.strip() , worklist))
    #def strip(string):
    #    return string.strip
    #worklist = map(strip, worklist)
    # another way of doing the above in a less pythonic way
    # worklist2 = []
    # for item in worklist:
    #     worklist2.append(item.strip)
    # worklist = worklist2
    listofdicts.append({
        "First Name": worklist[0],
        "Surname": worklist[1],
        "Date of Birth": worklist[2],
        "Address": worklist[3],
    })
    #print (listofdicts)

def bubbleSort(data, datatype):
#    print('bubbleSort')
    has_changed = True
    while has_changed == True:
#      print (data)
      has_changed = False
      for i in range((len(data) -1)):
        a = data[i][datatype]
        b = data[i+1][datatype]
        if a > b:
#          print("swap")
          data[i], data [i+1] = data [i+1], data [i]
          has_changed = True
    return data

def linearsearch(query):
    present = 'false'
    for i in listofdicts:
            if query in i.values():
                present = 'true'
                break
    if present == 'true':
        print (query + ' was found')
    else:
        print (query + ' not found') 

def binarysearch(query, data, datatype):
    justonedatatype = []
    for i in data:
        dicttolist = list(i.values())
        justonedatatype.append(dicttolist[datatype])
    found = False
    low = 0
    high = len(justonedatatype)
    # need to fix this so that it doesn't infinitely loop if it can't find the search term
    while found == False:
    #while low < high:
        mid = int(((high + low) // 2))
        if justonedatatype[mid] == query:
            found = True
            return data[mid]
            #return(f'Found at index {mid}')
        elif mid < high:
            if justonedatatype[mid] > query:
                high = (mid - 1)
            else:
                low = (mid + 1)
    if found == False:
        return ('Not Found')

def translateuserchoice(query):
    if query == 0:
        return 'First Name'
    if query == 1: 
        return 'Surname'
    if query == 2:
        return 'Date of Birth'
    if query == 3:
        return 'Address'

def write_to_sorted_file(data):
    datatowrite = ''
    for i in data:
        for i in list(i.values()):
            datatowrite += i
            datatowrite += ' | '
        datatowrite = datatowrite[:-3]
        datatowrite += '\n'
    with open("project_recordsearch_sorted.csv", 'w') as f:
        f.write(datatowrite)

def write_to_search_results(query):
    with open("project_recordsearch_results.csv", 'w') as f:
        f.write(str(query) + "\n")

if __name__ == '__main__':
    whattosearch = input('Please enter your search term: ')
    searchparam = input('What field do you wish to search? \n    1: First Name \n    2: Surname \n    3: Date of Birth \n    4: Address \nPlease enter a number: ')
    # whattosearch = 'Squarepants'
    # userchoice = 'Surname'
    if searchparam == '1' or '2' or '3' or '4':
        searchparam = int(searchparam)
        searchparam = searchparam - 1
        userchoice = translateuserchoice(searchparam)
    else:
         print ('Invalid choice')
    #searchparam = str(searchparam)
    listofdicts = bubbleSort(listofdicts, userchoice)
    write_to_sorted_file(listofdicts)
    # print(binarysearch(whattosearch, listofdicts, searchparam))
    searchresult = binarysearch(whattosearch, listofdicts, searchparam)
    finalsearchresult = []
    for i in searchresult.values():
        finalsearchresult.append(i)
    print('Found the following result: ' + str(finalsearchresult))
    write_to_search_results(finalsearchresult)