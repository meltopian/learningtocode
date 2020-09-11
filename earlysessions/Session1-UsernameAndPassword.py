
print ('Welcome to Mainframe. You have been pre-selected to enter a world of unknown potential.')
print ('Please choose a username: ')
username = input()
print (username)
print ('Please choose a password: ')
password = input()
print (password)
print ('We are now setting up your account. Please wait.')
import time
time.sleep(2)
print ('Your account is ready. Welcome to Mainframe. Please login.')

input1 = input('username: ')
if input1 == username:
    print ('success!')
else: 
    print ('failed')
    exit

input2 = input('password: ')
if input2 == password:
    print ('success!')
else:
    print ('fail!')
    exit