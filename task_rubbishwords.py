# Ask the user for 5 words. Print out a rubbish sentence
# putting between 10 and 20 of these words together
print('Please enter 5 words, one at a time, and I will create some delicious word salad for you: ')
input1 = input()
input2 = input()
input3 = input()
input4 = input()
input5 = input()


# Create a list of the words
list1 = [input1, input2, input3, input4, input5]

print('your words are: ')
print(list1)

# Create something that takes the list and picks 
# a random word 10-20 times and prints the results 

print('Here is a tasty word salad: ')

import random

new_num = random.randint(10, 20)

int(new_num)

list2 = []

for attempt_number in range(new_num):
    wordsaladnum = random.randint(0,4)
    list2.append(list1[wordsaladnum])

# print('this is the list:')
# print(list2)
line = " ".join(list2)
print(line)