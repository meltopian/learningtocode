# convert filesize in bytes to something human readable

# TODO Know the names, symbols and corresponding powers
# of 2 for the binary prefixes: bi=2

#     kibi, Ki - 2^10
#     mebi, Mi - 2^20
#     gibi, Gi - 2^30
#     tebi, Ti - 2^40 
# 
# Know the names, symbols and corresponding powers of 10 for the decimal prefixes:
#     kilo, k - 10^3
#     mega, M - 10^6
#     giga, G - 10^9
#     tera, T - 10^12

# kibi = 1024
# kilo = 1000

# doctest

print ('please input the filesize in bytes')
userinput = input()
print ('type d to use decimal or b to use binary')
userinput2 = input()

#userinput = userinput.strip()

def passthrough(x):
    return x

def kibi(x):
    return x / 1024

def mibi(x):
    return x / 1048576

def gibi(x):
    return x / 1073741824

def tebi(x):
    return x / 1099511627776

def kilo(x):
    return x / 1000

def mega(x):
    return x / 1000000

def giga(x):
    return x / 1000000000

def tera(x):
    return x / 1000000000000

userinput = int(userinput)

finalanswer = None

if userinput <= 999 and userinput2 == 'd':
    finalanswer = passthrough(userinput)
    finalanswer = str(finalanswer) + ' bytes'
elif userinput <= 1023 and userinput2 == 'b':
    finalanswer = passthrough(userinput)
    finalanswer = str(finalanswer) + ' bytes'
elif userinput <= 9999999 and userinput2 == 'd':
    finalanswer = kilo(userinput)
    finalanswer = round(finalanswer, 2)
    finalanswer = str(finalanswer) + ' KB'
elif userinput <= 9999999999 and userinput2 == 'd':
    finalanswer = mega(userinput)
    finalanswer = round(finalanswer, 2)
    finalanswer = str(finalanswer) + ' MB'
elif userinput <= 9999999999999 and userinput2 == 'd':
    finalanswer = giga(userinput)
    finalanswer = round(finalanswer, 2)
    finalanswer = str(finalanswer) + ' GB'
elif userinput <= 9999999999999999 and userinput2 == 'd':
    finalanswer = tera(userinput)
    finalanswer = round(finalanswer, 2)
    finalanswer = str(finalanswer) + ' TB'
elif userinput <= 1048575 and userinput2 == 'b':
    finalanswer = kibi(userinput)
    finalanswer = round(finalanswer, 2)
    finalanswer = str(finalanswer) + ' KiB'
elif userinput <= 1073741823 and userinput2 == 'b':
    finalanswer = mibi(userinput)
    finalanswer = round(finalanswer, 2)
    finalanswer = str(finalanswer) + ' MiB'
elif userinput <= 1099511627775 and userinput2 == 'b':
    finalanswer = gibi(userinput)
    finalanswer = round(finalanswer, 2)
    finalanswer = str(finalanswer) + ' GiB'
elif userinput <= 1125899906842623 and userinput2 == 'b':
    finalanswer = tebi(userinput)
    finalanswer = round(finalanswer, 2)
    finalanswer = str(finalanswer) + ' TiB'
else:
    print('something went wrong')

print (f'your file is: {finalanswer}')

#830642644
# test number - 830,642,644 (792MB)

if thing != 