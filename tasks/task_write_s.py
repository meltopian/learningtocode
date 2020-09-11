#Create a program that reads a line from the user. If the line starts with S. Append that line to the bottom of a text file.
input1 = input()

if input1.startswith('s'):
    f = open("task_write_s_out.txt", "a")
    f.write(input1)
    f.close()

#open and read the file after the appending:
f = open("task_write_s_out.txt", "r")
print(f.read())

#make it a loop