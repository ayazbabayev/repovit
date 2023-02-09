my_dict = {
    'name' : 'Ayaz', 'surname' : 'Babayev', 'age' : 36, 'ANOTHER_KEY': {'SubKey': 'SubValue'}
}

# PRINT DICTIONARY:
print(my_dict)

# PRINT KEYS & PRINT VALUES:
print('KEYS:',my_dict.keys())
print('VALUES:',my_dict.values())

# PRINT SPECIFIC KEY & SPECIFIC VALUE:
print('name' in my_dict)            # True !
print('Ayaz' in my_dict.values())   # True !
print(my_dict['name'])              # Ayaz (finds value through key)

# ADD NEW KEY:
my_dict['NEW KEYYY'] = 'HELLOOO'
print(my_dict)

#

# FIND SUBVALUE IN DICT WITHIN DICT:
print(my_dict['ANOTHER_KEY']['SubKey'])         # SubValue

# FOR LOOP : LOOKUP KEY & VALUE:
for key in my_dict:
    print(key, my_dict[key])    # name # Ayaz # surname # Babayev...

print('___ for key, value in my_dict.items(): ___')
for key, value in my_dict.items():
    print(key, value)

# GET VALUE OR TURN ERROR (0):
height = my_dict.get('height', 0)   # Height is not there, so "0".
print(height)


# CONCATENATE DICTIONARIES:

dict1 = {'A':'1', 'B':'2', 'C':'3'}
dict2 = {'X':'-1', 'Y':'-2', 'Z':'-3'}
dict_final = {}

def join_dicts(dict1, dict2):
    for key, value in dict1.items():
        dict_final[key] = value
    for key, value in dict2.items():
        dict_final[key] = value
    return dict_final

print(join_dicts(dict1,dict2))

# CREATE Numbers squares in dict:

number_size = 5
def create_squareNos_dict(number1):
    result_dict = {}
    for n in range(1, number_size+1):  # from 1 to 5 (5+1 excluded)
        result_dict[n] = n**2
    return result_dict

print(create_squareNos_dict(number_size))

# SUM VALUES IN DICT:
d = {'key1': 12,'key2': 9,'key3': 1986}
def sum_values(d):
    return sum(d.values())

print(sum_values(d))