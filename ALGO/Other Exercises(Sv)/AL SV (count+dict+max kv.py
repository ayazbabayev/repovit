# Find 1st unique letter in a string

# For example:
# str = "Google", it should return “l”
# str = "Amazon", it should return "m"

def unique(str1):
    str1 = str1.lower()
    for char in str1:
        str1.count(char)
        if str1.count(char) == 1:
            return char

str1 = 'Amazon'
print(unique(str1))

##################################################


def unique(str1):
    str1 = str1.lower()
    dict1 = {}
    for char in str1:
        if char not in dict1:
            dict1[char] = 1
        else:
            dict1[char] += 1

    # {'a': 2, 'm': 1, 'z': 1, 'o': 1, 'n': 1}
    max_v = 0
    max_k = ''
    for k, v in dict1.items():
        if v > max_v:
            max_v = v
            max_k = k
    return print('max key & max value:', max_k, max_v)


str1 = 'Google'
print(unique(str1))

##################################################

def unique(str1):
    str1 = str1.lower()
    dict1 = {}
    for char in str1:
        if char not in dict1:
            dict1[char] = 1
        else:
            dict1[char] += 1

    # {'a': 2, 'm': 1, 'z': 1, 'o': 1, 'n': 1}
    for k, v in dict1.items():
        if v == 1:
            return k


str1 = 'Google'
print(unique(str1))



########################################################################################################################

# Find 1st unique letter in a string

# For example:
# str = "Google", it should return “l”
# str = "Amazon", it should return "m"

def unique4(string4):
    str4 = string4.lower()
    dict4 = {}
    for char in str4:
        # if str4.count(char) == 1:
        #     return char
        if char not in dict4:
            dict4[char] = 1
        else:
            dict4[char] += 1
    print(dict4)
    max_value = 0
    max_key = ''
    for key,value in dict4.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key, max_value


string4 = 'Penelope'
print(unique4(string4))


########################################################################################################################

# Find 1st unique letter in a string

# For example:
# str = "Google", it should return “l”
# str = "Amazon", it should return "m"

def uniq(x):
    string=x.lower()
    dct={}
    for lett in string:
        if lett not in dct:
            dct[lett] =1
        else:
            dct[lett]+=1
    kmax=''
    vmax=0
    for k,v in dct.items():
        if v>vmax:
            vmax=v
            kmax=k
    return kmax, vmax




x='ALABALA'
print(uniq(x))

