
string = 'ABC123'

print('for i in string:')
for i in string:
    print(i)                # ABC123 (values)

print('for i in range(3): print(i)')
for i in range(3):
    print(i)                # 012 (INDEX till range3)

print('for i in range(3): print(string[i])')
for i in range(3):
    print(string[i])        # ABC (values till range(3)


########################################################################################################################


list = [6,7,8,'x','y','z']

print('for i in list:')
for i in list:
    print(i)                # 012345 (INDEXES)

print('for i in range(len(list)):')
for i in range(len(list)):
    print(list[i])          # 012345 (values)


########################################################################################################################
# TEST THEM IN def functions:

