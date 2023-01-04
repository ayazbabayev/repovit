def remove_every_other(my_list):
    kept = []
    for n in range(len(my_list)):  # range goes through every INDEX not value

        # my_list = [1,2,3,4,5,6,7,8,9,10]
        #    index=  0,1,2,3,4,5,6,7,8,9

        if n % 2 == 0:
#           my_list.pop(n)
            kept.append(my_list[n])
    return kept

# OR:
#     return my_list[::2]


test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test_list2 = ['Hello', 'Goodbye', 'Hello Again', 'Hello', 'Hello Againnn']
result = remove_every_other(test_list2)
print(result)
