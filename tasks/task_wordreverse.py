f = open("task_wordreverse.text.txt", 'r')
for line in f:
    line = line.split(" ")
    linereverse = [i[::-1] for i in line]
    linereverse_string = ' '.join(linereverse)
with open("task_wordreverse.text.txt", 'a') as f:
    f.truncate(0)
    f.write(linereverse_string)
exit

# import os.path
# from os import path

# if path.exists("c:\code\task_wordreversed.text.txt"):
#     f = open("task.wordreversed_text.txt", 'r')
#     for line in f:
#         line = line.split(" ")
#         linereverse = [i[::-1] for i in line]
#         linereverse_string = ' '.join(linereverse)
    
#     with open("task_wordreverse.text.txt", 'a') as f:
#         f.truncate(0)
#         f.write(linereverse_string + "\n")
#     exit

# else:
#     f = open("task_wordreverse_text.txt", 'r')
#     for line in f:
#         line = line.split(" ")
#         linereverse = [i[::-1] for i in line]
#         linereverse_string = ' '.join(linereverse)

#     with open("task_wordreversed.text.txt", 'a') as f:
#         f.truncate(0)
#         f.write(linereverse_string + "\n")
#     exit