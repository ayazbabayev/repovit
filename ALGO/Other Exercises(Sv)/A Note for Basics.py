
lista = ['a', 'b', 'c', 'd']        # len 4.
# PRINT LIST VALUES:
print(lista[0])                     # FIRST VALUE: a
print(lista[-1])                    # LAST VALUE: 1

# PRINT LIST INDEXES:
for i in range(len(lista)):          # outputs indexes
    print('print(i) is index:', i)   # indexes in list
    print('lista[i]:', lista[i])     # values in list

# FIND INDEX by VALUE:
countries = ('USA', 'Canada', 'Mexico')
ulke = 'Canada'


def find_index_by_value(value, tuple1):
    if value not in tuple1:
        return -1
    else:
        return tuple1.index(value)


print(find_index_by_value(ulke, countries))


print('_______________________________________________________')

for i in lista:                     # outputs values
    print('print (i):', i)

print('___')

# x + 1 : next ele than i
# x - 1 : prev ele than i

x = 1
x += 1
print(x)
x -= 1
print(x)

print('___')

# EXAMPLE:
# def sample(list):
#     i = 500                     # INDEX. index 500
#     while i < len(list):        # if len(list) = [3,5] = 2
                                # i is index here. not value. so this while wont be executed
# ###########################################################################################

# INDEXES   ###############################################################

str = "America"
print(str[::])              # America (straight)
print(str[::-1])            # aciremA (reverse)
print(str[len(str)//2])     # r       (MIDDLE)
print(str[1::])             # merica  (from 2nd value)
print(str[:2])             # Am      (1st 2 letters)
print(str[1::-1])           # mA      (1st 2 letters but reverse)

test_list = [1,2,3,4,5,6]
print(test_list[::3])       # jumps to every 2nd number
# test_list[starting_index:end index: step]


# STEP included - By default its "1":
s = 'HELLO'
print(s)
print(s[0:3])       # HEL : 0:3:1...This will include 0,1,2, till 3 (excluding)
print(s[0:4:2])     # HL :from H to L AND SKIP every 2nd
print(s[4:1:-1])    # OLL: from O to first L & go reverse

# RANGES    ###############################################################
range(0, 10)     # again: excludes 2nd value (10) so 0 to 9.

range(3)         # 0,1,2
range(0, 3)       # 0,1,2 SAME AS ABOVE
range(0, 3, 1)     # 0,1,2 SAME AS ABOVE

print('for n in range(0,3):')
for n in range(0, 3):
    print(n)


print('for n in range(2,7,2):')
range(2, 7, 2)     # 2,4,6
for n in range(2, 7, 2):
    print(n)


# WHILE LOOP: basic example:
print('WHILE LOOP')
x = 10
while x > 0:
    print(x)
    x -= 1
    if x==5:
        break

print('loop stopped: out of loop ')

def countdown(a):
    x = a
    while x >= 1:
        # print(x)
        x -=1
        if x == 10:
            print('LAST 10 REMAINING:')
            for i in range(x, 0, -1):   #from x till index 0 (*1*) by -1 step
                print('i',i)

countdown(50)


# result = countdown(10) # result: only if you have return statement
# print(result)


# CONTINUE function:
print('CONTINUE function: skipping "l"')
for char in 'hello world':
    if char == 'l':
        continue    # STOPS when sees Ls, SKIPS them and goes back to the top of the loop.
    print(char)

### Reversing (in separate py file)
# for idx in range(len(s)-1,-1,-1):    # start at max index len(s)-1, stop at 0 so use -1, do reverse/countdown -1
#     print('idx',idx,s[idx])

########################################################################################################################
name = 'ben'
result = ''         # (blank intentionally)
for x in range(3):  # loop 3 times
    result += name
print(result)


#######################################################################################################################
# Taxi fare
def taxi_fare(distance): # in km
    basefare = 4.0
    while distance >= 0.14:
        distance -= 0.14
        basefare += 0.25
    return basefare

print(taxi_fare(10))



#############################
print('for n in range(0, 3):')
for n in range(0, 3):
    print('n:', n)
########################################################################################################################
# EXTRACT VALUE FROM LIST:
lista = ['w', 'x', 'y', 'z']

for i in range(len(lista)):         # outputs INDEXES
    print('index:i:', i)            # INDEXES 0/1/2/3 : print(i)
    print('values: ', lista[i])     # VALUES  w/x/y/z : list[i]

print('for i in lista:  ')
for v in lista:                     # outputs VALUES
    print('i:', v)                  # VALUES w/x/y/z : print(i)
########################################################################################################################
# EXTRACT VALUE FROM STRING:
string = 'abc'
print('string', string)
for val in string:                    # outputs VALUES
    print(val)                        # VALUES a/b/c
########################################################################################################################





#############################
print('string:')
string = '+alpha-'

for char in range(len(string)):
# print EA CHAR ONE-BY-ONE:
    print(string[char])       # a / l / p / h / a
for chr in range(len(string)):
# print from blank to whole by ea CHAR
    print(string[:chr])      # '' / + / +a / +al / +alp / +alph / +alpha
for chr in range(len(string)):
# print from whole to blank by ea CHAR
    print(string[chr+1:])  # alpha- / lpha- / pha- / ha- / a- / - / ''
print('stop')


########################################################################

# SORT STRINGS : sorted(STRING)
# SORT LISTS: list.sort()

soz = 'axyczdb123'
print(sorted(soz))

x = sorted(soz)
rev = x[::-1]
rev.sort()


############ ???
# EXTRACT VALUE FROM INT: ???
# integ = 123
# print('integer', integ)
# while integ != 0:
#     i = integ // 100
#     print('i',i)
#     rem = integ % 100
#     print('rem', rem)
#     integ = rem // 10