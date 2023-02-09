
STRING = 'ABC123'

print('for i in string:')
for i in STRING:
    print(i)                # ABC123 (values)

print('for i in range(3): print(i)')
for i in range(3):
    print(i)                # 012 (INDEX till range(3))

print('for i in range(3): print(string[i])')
for i in range(3):
    print(STRING[i])        # ABC (values till range(3))


########################################################################################################################


LIST = [6,7,8,'x','y','z']

print('for i in list:')
for i in LIST:
    print(i)          # 6,7,8,x,y,z (values)


print('for i in range(len(list)): \nprint(i)')
for i in range(len(LIST)):
    print(i)          # 012345 (INDEXES)


print('for i in range(len(list)): \nprint(LIST[i])')
for i in range(len(LIST)):
    print(LIST[i])    # 6,7,8,x,y,z (values)


########################################################################################################################
# TEST THEM IN def functions:
print('----------------------------')
def listfunction(x):
    ls=[]
    print('start')
    for v in x:

        ls.append(v)        # values ['a', 'b', 'c', 'd', 'e']
    return ls
x=['a','b','c','d','e']
print('listfunction',listfunction(x))


def listfunction(x):
    ls=[]
    print('start')
    for v in range(len(x)):
        ls.append(v)        # indexes [0, 1, 2, 3, 4]
    return ls
x = ['a', 'b', 'c', 'd', 'e']
print('listfunction', listfunction(x))


def listfunction(x):
    ls=[]
    print('start')
    for v in range(len(x)):
        ls.append(x[v])     # values ['a', 'b', 'c', 'd', 'e']
    return ls
x = ['a', 'b', 'c', 'd', 'e']
print('listfunction', listfunction(x))