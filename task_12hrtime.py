# task_12hrtime

# Create a program that takes user input 
# and converts a 12h time (e.g. 4:53pm, 6:00am)
# into into a 24h time (e.g. 16:53, 06:00)
print('please enter an am or pm time, for example 4:00pm, and i will convert it to 24hr time')

time = input()
split_time = time.split(":")

#if 'p' in split_time:
if 'p' in split_time[1]:
    split_time[0] = int(split_time[0])+12

if 'a' in split_time[1]:
    split_time[0] = split_time[0]

final_output = split_time[0] + ':' + split_time[1][:-2]

print('input was') 
print(time)
print('output is')
print(final_output)