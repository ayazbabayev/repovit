# list = [1, 2, 3, 4, 5, 1111]
lista = ['a', 'b', 'c', 'd']        # len 4.

for i in range(len(lista)):         # outputs indexes
    print(i)                        # indexes
    print('&')
    print(lista[i])                 # values
    print('----')

print('___')

for i in lista:                     # outputs values
    print('print i',i)

print('___')

print(lista[2])

print('___')

# x + 1 : next ele than i
# x - 1 : prev ele than i

x = 1
x += 1
print(x)
x -= 1
print(x)


#if we do
# def sample(list):
#     i = 500                     # INDEX. index 500
#     while i < len(list):        # if len(list) = [3,5] = 2
                                # i is index here. not value. so this while wont be executed