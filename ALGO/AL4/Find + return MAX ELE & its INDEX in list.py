# Given a list of random numbers.
# Find and return the max element and its' index
# ex: [1,45,33,76,9,10] return [3,76]

# list=[1,45,33,76,9,10]
# max(list)
# print(max(list))
# list.index(max(list))
# print(list.index(max(list)))

# SOLUTION 1:
def max_and_index(list):
    max_no = max(list)
    max_no_index = list.index(max(list))
    return [max_no_index, max_no]


test_list = [1, 45, 33, 76, 9, 10]
print(max_and_index(test_list))
##################################################################################


# SOLUTION 2:
def max_and_index2(list):
    max_ele_index = 0
    max_ele = list[max_ele_index]

    for i in range(len(list)):
        if list[i] > max_ele:
            max_ele_index = i
            max_ele = list[i]
    return [max_ele_index, max_ele]


test_list2 = [1, 45, 33, 76, 9, 10]
print(max_and_index2(test_list2))

##################################################################################


# SOLUTION 3:
def max_and_index3(list):
    max_ele_index = 0
    max_ele = list[max_ele_index]

    i = 0
    while i < len(list):
        if list[i] > max_ele:
            max_ele_index = i
            max_ele = list[i]
        i += 1
    return[max_ele_index, max_ele]


test_list3 = [1, 45, 33, 76, 9, 10]
print(max_and_index3(test_list2))
