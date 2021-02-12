from project_validation_pc import checkpostcode

from project_validation_cc import checkccnumber

import project_validation_isbn

print(checkpostcode(input('please give a postcode: ')))
# print(checkccnumber(input('please give a credit card number: ')))
print(project_validation_isbn.checkisbn(input('please give an isbn number: ')))
