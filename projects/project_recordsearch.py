
listofdicts = []
f = open("project_recordsearch_data.csv", 'r')
for line in f:
    d = {}
    worklist = [item.strip() for item in line.split("|")]
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
    
print (listofdicts)


