# Create a program that reads in a plain text file and reverses 
# all the letters of the words but keeps the words in the 
# correct order and writes this back to a new file. For example:
#    The quick brown fox
# would be converted to
#    ehT kciuq nworb xof
# Running the program twice should return to the original text.

def reverse_str(s):
    return s[::-1]

newlist = []
newlist2 = []
f = open("task_wordreverse_text.txt", 'r')
for line in f:
  newlist = line.split(" ")
  newlist = line.strip()
  newlist2.append(newlist)
  #reverseline = reverse_str(newlist)a
f.close()
print (newlist2)
# for item in line:

#for each line in file 
#create a list
#words = line.split on spaces
#for each word run reverse_str and add it to another list called output