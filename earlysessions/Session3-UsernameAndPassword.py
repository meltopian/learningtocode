
print ('Welcome to the Mainframe.')
print ('Please choose a username: ')
username = input()
print (username)
print ('Please choose a password: ')
password = input()
print (password)
print ('We are now setting up your account. Please wait.')
import time
time.sleep(2)
print ('Your account is ready. Please login.')



for attempt_number in range(3):
    print(attempt_number)
    print("please enter your username: ") 
    usernameinput = input()
    print("please enter your password: ")
    passwordinput = input()
    if usernameinput == username and passwordinput == password:
        print('approved')
        exit
    elif usernameinput != username and passwordinput != password:
        time.sleep(2)
        print ('incorrect username or password')

print ('denied')
exit
    # if attempt_number == 1 or 2 or 3 and usernameinput == username:
    #     print('success!')
    # elif attempt_number == 1 or 2 or 3 and usernameinput != username: 
    #     print("try again")
    # elif attempt_number != 1 or 2 or 3 and usernameinput != username:
    #     print('denied')
    #     break

# input1 = input('username: ')
# for input1 == username
#     if input1 == username:
#     print ('success!')
# else: 
#     print ('failed')
#     exit

# input2 = input('password: ')
# if input2 == password:
#     print ('success!')
# else:
#     print ('fail!')
#     exit

# for 