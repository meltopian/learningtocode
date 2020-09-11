
count = 0
for attempt_number in range(31):
    if (
        attempt_number == 4 or 
        attempt_number == 8 or 
        attempt_number == 12 or 
        attempt_number == 16 or 
        attempt_number == 20 or 
        attempt_number == 24 or
        attempt_number == 28
    ):
        print('')
    else:
        print (attempt_number)

#Matt's solution
# numberlist = list(range(0, 30))

# print('The numbers between 0 and 30 not divisible by 4 are: ')
# for item in numberlist:
#     if item % 4 != 0:
#         print(item)