# Your task, is to create NxN multiplication table,
# of size provided in parameter.
# for example, when given size is 3:

# 1 2 3
# 2 4 6
# 3 6 9

# for given example, the return value should be: [[1,2,3],[2,4,6],[3,6,9]]

# def multiplication_table(size):
#
#     list = [1, 2, 3]
#     for i in range(len(list)):
#         list[i] = int(list[i])
#         # print('int(list[i])', list[i])  # int values of each i
#
#     n_list = []
#     n = 1
#     n_list.append(n)
#     while n <= size:
#         n += 1
#         n_list.append(n)
#         # print('n', n)
#         print('n_list', n_list)
#         if n == size:
#             break
#     print('loop stops') # reaches size 3 here
#
#     mult_list =[]
#     n_list[i] = int(n_list[i])
#     for i in list:
#         while 0 < n_list[i] < 4:
#             mult_list.append(n_list * list[i])
#             print(mult_list)
#     return ('mult_list: ', mult_list)
#
# size = 3
# result = multiplication_table(size)
# print(result)

def multiplication_table(size):
    table = []
    for i in range(1, size + 1):    #(index 1 till index 3)
        aux = []
        for j in range(1, size + 1):
            aux.append(i * j)

        table.append(aux)

    return table

print(multiplication_table(5))



