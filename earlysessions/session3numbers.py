# #Reading a file
# line_count = 0
# with open("in.txt", 'r') as f:
#   for line in f:
#     print("Line " + str(line_count) + ": " + line)
#     line_count += 1

# #Alternate way of reading file
# f = open("in.txt", 'r')
# for line in f:
#   print("Line " + str(line_count) + ": " + line)
#   line_count += 1
# f.close()

# Variable array fixed length
# names = []
# names.insert(0,"Bob")
# names.insert(1,"Foo")
# names.insert(2,"Rah")
# for name in names:
#   print(name)
# print ("array size is %s" % len(names))

total = 0

data = [0]
with open('session3numlist.txt', 'r') as filehandle:
    for line in filehandle:
        line = line.strip()
        data.append(line)


for item in data:
     print(f'the item is {item}')
     print(f'the total is {total}')
     total = total + int(item)
     print(f'After I added item the total is now {total}')
print('the final total is')
print(total)



# total = 0
# aa = 0
# with open('session3numlist.txt', 'r') as filehandle:
#     for item in filehandle:
#             aa
# print(aa)
# for item in aa:
# add    

# print (total)