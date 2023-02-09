

string = [1,None,14,"two"]

def reverser(string):
    empty_list = list()
    for i in range(len(string)-1,-1,-1):
    # for i in string[::-1]:
        empty_list.append(string[i])
    return empty_list

print(reverser(string))

# print('i', i)
# print('string[i]: value:',string[i])
# print('empty_list', empty_list)


string = [12, 'twelve', None]
for i in range(len(string)-1,-1,-1):    # -1 start: last ele # -1 stop: 0 # reverse -1
    print('string[i]', string[i])
    print('i:',i)

#######################################################################################################################

def revstring(s):
    print(s[::-1])
    for char in range(len(s)-1,-1,-1):
        return s[char]

s= 'hello world'
print(revstring(s))


######################################

def revlist(x):
    listx=[]
    for val in range(len(x)-1,-1,-1):
        listx.append(x[val])
    return listx

x = [50, 'FIFTY', '5x10', None]
print(revlist(x))

############################################
