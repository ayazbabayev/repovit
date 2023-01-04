# SEPARATE A STRING / INT INTO LIST.

def separatestringtolist(word):
    word_list = [w for w in str(word)]
    print(type(word_list))
    return word_list

word = 'alaku'
print(separatestringtolist(word))

##################################

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

###################################
