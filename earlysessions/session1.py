#A function is a named list of commands

#def life_story(name):
#    print ('I am a banana')
#    print ('Please dont eat me')
#    print ('I like')
#    print (name)

#life_story('potatoes')
#print('Hello World')
#print('Crabbledobs')
#life_story('cucumbers')

print('Hello World')

#x = 'pizza'
#y = 'cheese'
#z = x + y
#print(z)

# when you add 2 strings together it joins them together

def add(a, b):
    return a + b

#answer = add(11, 19)
#print(answer)

def multiply(a, b):
    return a * b

input1 = input('First number: ')
input2 = input2 = input('Second number: ')
operation = input('what do you want to do with your numbers? + or *:')

input1 = int(input1)
input2 = int(input2)

if operation == '+':
    answer = add(input1, input2)
elif operation == '*':
    answer = multiply(input1, input2)
else:
    answer = 'thats not a + or *!!'

print(answer)

