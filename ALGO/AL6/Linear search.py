# LINEAR SEARCH

# 1. start from 1st element, compare k with ea element.
# 2. if x == k, return index of ele
# 3. Else, return None

def linear_search(arr, x):          # we need to pass not only list but also the value we're looking for
    for i in range(len(arr)):
        if x == arr[i]:             # if that x = to ele at arr's index i
            return i                # return the index of this ele
    return None                          # otherwise return None.

test_list = [1, 4, 2, 7, 9, 12, 5, 2]
test_pos_x = 7
test_neg_x = 3
result_pos = linear_search(test_list, test_pos_x)
result_neg = linear_search(test_list, test_neg_x)
print(result_pos)
print(result_neg)