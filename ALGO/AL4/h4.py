# Your input is a list of integers,
# and you have to reorder its entries so that the even entries appear first.
# You are required to solve it without allocating additional storage
# (operate with the input list).
# Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]

def reorder_list_evens_first(list):
    print(f'start :', list)

    for i in list:
        if i % 2 != 0:
            list.remove(i)
            list.insert(len(list), i)   # Insert i to the end of the list.
            # print('loop  :', list)    # #############
    return list


test_list = [7, 3, 5, 6, 4, 10, 3, 2]
result = reorder_list_evens_first(test_list)
print('result:', result)

# Q: WHY MY LIST IS NOT MATCHING WITH EXPECTED RESULT ORDER?
# Q: WHAT IS THE LOGIC OF LOOP'S SEQUENCE HERE?
# My test_list = [6, 4, 10, 2, 5, 7, 3, 3]
# Vitalys list = [6, 4, 10, 2, 7, 3, 5, 3]

print('------------------------------------------------------------------------------------------------')

# Write a program that takes as input a list of digits encoding a nonnegative decimal integer D
# and updates the list to represent the integer D + 1.
# For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].

# list = [1,2,9]
# concatenate values in list 1+2+9= 129
# add +1 make 130
# take result 130 and break into list.


def d1_transformation(list):
    print(f'original list:   ', list)
    concat = ''
    final_list = []

    for d in list:
        concat += str(d)            # +'1' +'2' +'9'

    d1 = int(concat)+1              # 129 + 1 = 130

    for v in str(d1):
        final_list.append(int(v))   # +1 +3 +0
    return final_list


test_list = [1, 2, 9]
result = d1_transformation(test_list)
print('transformed list:', result)
