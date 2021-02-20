

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
