from pathlib import Path
script_path = Path(__file__)
record_search_data = script_path.with_name("project_recordsearch_data.csv")

#from mergesort import *
# https://www.geeksforgeeks.org/python-program-for-binary-search/
# https://www.bbc.co.uk/bitesize/guides/zjdkw6f/revision/3
listofdicts = []
f = open(record_search_data, 'r')
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

def bubbleSort(data, key_to_sort_by):
#    print('bubbleSort')
    has_changed = True
    while has_changed == True:
#      print (data)
      has_changed = False
      for i in range((len(data) -1)):
        a = data[i][key_to_sort_by]
        b = data[i+1][key_to_sort_by]
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

def binarysearch(query, data, key_to_search):
    key_to_search = int(key_to_search)
    justonecategory = []
    for i in data:
        dicttolist = list(i.values())
        justonecategory.append(dicttolist[key_to_search])
    found = False
    low = 0
    high = len(justonecategory)
    # need to fix this so that it doesn't infinitely loop if it can't find the search term
    while found == False:
    #while low < high:
        mid = int(((high + low) // 2))
        if justonecategory[mid] == query:
            found = True
            return data[mid]
            #return(f'Found at index {mid}')
        elif mid < high:
            if justonecategory[mid] > query:
                high = (mid - 1)
            else:
                low = (mid + 1)
    if found == False:
        return ('Not Found')



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


def do_menu(menu_items):
    key = None
    while not key:
        print('Please choose an option: ')
        for (k, v) in menu_items.items():
            print(f'    {k}: {v}')
        print("Please enter a number:")
        key = input()
        if key not in menu_items.keys():
            print ('Invalid choice')
            key = None
    return (key, menu_items[key])



if __name__ == '__main__':

    #search_query = 'Squarepants'

    main_menu_items = {
        '1': 'View Records',
        '2': 'Sort Records',
        '3': 'Search Records',
    }   

    search_menu_items = {
        '1': 'First Name',
        '2': 'Surname',
        '3': 'Date of Birth',
        '4': 'Address',
    }

    (main_menu_choice, _) = do_menu(main_menu_items)
    
    if main_menu_choice == '1':
      for i in listofdicts:
        print(i)
      pass
    elif main_menu_choice == '2':
      # Create an option menu to say 'would you like to save the results to a csv'
      (menu_choice, menu_value) = do_menu(search_menu_items)
      print(menu_choice)
      print(menu_value)
      listofdicts = bubbleSort(listofdicts, menu_value)
      write_to_sorted_file(listofdicts)
      print(f'A CSV file containing data sorted by {menu_value} has been created.')
    elif main_menu_choice == '3':
      (menu_choice, menu_value) = do_menu(search_menu_items)
      search_query = input('Please enter your search term: ')
      listofdicts = bubbleSort(listofdicts, menu_value)
      searchresult = binarysearch(search_query, listofdicts, menu_choice)
      finalsearchresult = []
      for i in searchresult.values():
        finalsearchresult.append(i)
        print('Found the following result: ' + str(finalsearchresult))
      # Create an option menu to say 'would you like to save the results to a csv'
      write_to_search_results(finalsearchresult)

    #menu_items_strings = ''.join(
    #    f'    {key}: {value}\n'
    #    for key, value in menu_items.items()
    #)

    #print(menu_choice)
    #print(menu_value)
    exit()


 
