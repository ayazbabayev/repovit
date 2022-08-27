# Given an array of integers, calculate sum & multiplications of the elements.
# Return the list that includes sum & mutiplication.
# Ex: [1, 7, 3] return [11, 21]

#o(n)
def cs_sum_and_multiply_list(list):
    sum_list = 0
    mult_list = 1   # Because if 0 then all multiplications = 0

    for num in list:
        sum_list += num
        mult_list *= num
    return [sum_list, mult_list]

mylist = [1,7,3]
print(cs_sum_and_multiply_list(mylist))