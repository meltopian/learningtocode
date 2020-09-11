# Create a program that takes user input 
# and converts a 12h time (e.g. 4:53pm, 6:00am)
# into into a 24h time (e.g. 16:53, 06:00)

print('please enter an am or pm time, for example 4:00pm, and i will convert it to 24hr time')

time = input()
split_time = time.split(":")

if 'p' in split_time[1]:
    split_time[0] = int(split_time[0])+12
    split_time[1] = split_time[1].replace('pm', '')

if 'a' in split_time[1]:
    split_time[0] = split_time[0]
    split_time[1] = split_time[1].replace('am', '')

#split_time[1].replace('am', '').replace('pm, '')
#(commented out as line has been split into above)

final_output = str(split_time[0]) + ':' + str(split_time[1])

#[:-2]
#(commented out as this was originally how I removed am/pm from the final result)

print('input was') 
print(time)
print('output is')
print(final_output)

# Potential improvements:
# Prevent impossible times (e.g. 25:00)
# As user if they want to covert 12->24 or 24->12
# Make input uniform