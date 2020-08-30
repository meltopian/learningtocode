# Read a multiline CSV file. Print the highest number 

thelist = []


with open("task_readcsv-file.csv", 'r') as f:
  for line in f:
    line = line.strip()
    line = line.split(",") 
    for i in line:
        thelist.append(i)

#convert list to integers
thelist = [int(i) for i in thelist]

# first way I did the above before simplifying:
# intlist = map(int, thelist)
# intlist = list(map(int, intlist))   

#sort list
thelist.sort()

#print the list number in the list

print('the highest number in the csv file is:')
print(thelist[-1])