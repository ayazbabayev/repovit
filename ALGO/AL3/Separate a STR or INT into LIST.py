# SEPARATE A STRING / INT INTO LIST.

n= 'abca'
###
digit_list = []

for d in str(n):
   digit_list.append(d)

###
print(n)
print(digit_list)

##################################

n= 123
###
digit_list = []

for d in str(n):
    digit_list.append(int(d))
###
print(n)
print(digit_list)