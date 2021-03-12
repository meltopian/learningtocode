
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

def bubbleSort(data):
    print('bubbleSort')
    has_changed = True
    while has_changed == True:
#      print (data)
      has_changed = False
      for i in range((len(data) -1)):
        a = data[i]['Surname']
        b = data[i+1]['Surname']
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
    # x = listofdicts[0].values
    # for i in x:
    #         if i == query:
    #           present = 'true'
    #           return query + ' was found'
    #           break
    #         if present == 'false':
    #           return query + ' is not here'

if __name__ == '__main__':
#    data = ['b', 'd', 'c', 'a']
    listofdicts = bubbleSort(listofdicts)
    print(listofdicts)
    print(linearsearch('Squarepants'))
    #print(data)

