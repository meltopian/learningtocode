aa = [12,13,14,15]
print(aa)

# total = 0
# for item in aa:
#     print(f'the item is {item}')
#     print(f'the total is {total}')
#     total = total + item
#     print(f'After I added item the total is now {total}')
# print('the final total is')
# print(total)

data = []
with open('test.txt', 'r') as filehandle:
    for line in filehandle:
        line = line.strip()
        data.append(line)

print(f'i have read in {data}')

data = [
    'file',
    'to',
    'write yeah',    
]
with open('out.txt', 'w') as filehandle:
    for item in data:
            filehandle.write(item + '\n')


for x in range(5):
    if x == 3:
        break
    else
    print(x)

