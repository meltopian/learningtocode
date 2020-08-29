# Read in a phrase from a user. If the phrase exists in a file,
# print "Phrase exists"
# This should ignore case

#what it needs to do:
#take user input
#open file
#convert input to lowercase
#for line in file, if input phrase == line
#print "phrase exists"

# use str.lower()
# converts to lower case
# capitalize does opposite

phrase_input = input()

phrase_input = phrase_input.lower()


new_number = 0

f = open("task_phraselookup_phrasefile.txt", 'r')
for line in f:
    line = line.lower()
    line = line.strip()
    if phrase_input == line:
        new_number = 1
f.close()

if new_number == 1:
  print ('phrase exists')
if new_number == 0:
  print ('phrase does not exist')

