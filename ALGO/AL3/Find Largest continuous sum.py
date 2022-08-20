#

def calculate_largest_cont_sum(list_of_nums):
    if len(list_of_nums) == 0:
        return 0

    max_sum = list_of_nums[0]       # SETS TO THE FIRST ELEMENT OF THE LIST : since 0 is 1st ele
    current_sum = list_of_nums[0]   # ^-- Assuming that the biggest ele in list is 1st ele

    for n in list_of_nums[1:]:      # starts from 2nd ele in list and goes till the end [x:] for i in list
        # print(f'start: {n}: current_sum{n}, max_sum={max_sum} ')
        current_sum = max(n, current_sum+n)
        max_sum = max(max_sum, current_sum)
        # print(f'finish {n}: current_sum{n}, max_sum={max_sum} ')
    return max_sum


#1st Iteration n =2, current_sum = max(2, 3), max_sum = max(1, 3) >>>>> n =2, current_sum =3, max_sum=3
#2ndIteration: n=-1,  current_sum = max(-1, 3-1), max_sum = max(3, 2) >>>>>> n =-1, current_sum = 2, max_sum = 3
#3rdIteration: n=3, current_sum= max(3, 2+3), max_sum = max(3, 5)> >>>>>>. n =3, current_sum =5, max_sum =5

test_list = [1,2,-1,3,4,10,10,-10,-1]
test_result = calculate_largest_cont_sum(test_list)
print(test_result)
