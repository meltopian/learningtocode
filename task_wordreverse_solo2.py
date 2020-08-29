def reverse_str(s):
    return s[::-1]

f = open("task_wordreverse_text.txt", 'r')
for line in f:
    line = line.split(" ")
    linereverse = [reverse_str(i) for i in line]
    linereverse_string = ' '.join(linereverse)

with open("task_wordreversed.text.txt", 'a') as f:
      f.write(linereverse_string + "\n")

#     linereverse.append

# str.linereverse

# with open("task_wordreversed.text.txt", 'a') as f:
#     f.write(linereverse)

