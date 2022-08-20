#

def calculate_largest_cont_sum(list_of_nums):
    if len(list_of_nums) == 0:
        return 0

    max_sum = list_of_nums[0]       # SETS TO THE FIRST ELEMENT OF THE LIST : since 0 is 1st ele
    current_sum = list_of_nums[0]   # ^-- Assuming that the biggest ele in list is 1st ele

    for n in list_of_nums[1:]:                            # starts from 2nd ele in list and goes till the end [x:]
        print(f'start: {n}: current_sum{n}, max_sum={max_sum} ')
        current_sum = max(n, current_sum+n)     # which is greater, "n" or  "current_sum + n"? *** HOW TO CALCULATE THIS PART HERE??? WHAT IS N HERE?
        max_sum = max(max_sum, current_sum)     # which is greater, max_sum "0"? or current_sum result above?
        print(f'finish {n}: current_sum{n}, max_sum={max_sum} ')

    return max_sum

test_list = [1,2,-1,3,4,10,10,-10,-1]
test_result = calculate_largest_cont_sum(test_list)
print(test_result)
