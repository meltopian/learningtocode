

line_count = 0
d = []
with open("project_recordsearch_data.csv", 'r') as f:
  for line in f:
#    (fname, sname, dob, address) = line.split("|")
    #line = line.replace(" ", "")
    worklist = line.split("|")
    index = 0
    while index < len(worklist):
      worklist[index] = worklist[index].strip()
      index += 1
    d.append(worklist)

    # d[fname] = worklist[0]
    # d[sname] = worklist[1]
    # d[dob] = worklist[2]
    # d[address] = worklist[3]
#    d[key] = val 
#    print("Line " + str(line_count) + ": " + line)
    print (worklist)
    line_count += 1

print (d)
print (d[0][1])








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