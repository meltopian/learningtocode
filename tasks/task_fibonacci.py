#Fibonacci Sequence: Generate the following sequence under 200. 1,1,2,3,5,8,13,21,etc
#   Add the previous 2 numbers, e.g. 2+3=5 3+5=8

numbers = [0, 1]


count = 0
while count < 11:
    count = count + 1
    numbers.append(numbers[-1]+numbers[-2])

print (numbers)

# if numbers[-1 ] > 200:
#     exit