# Find a sum of elements between min and max elements
# min and max elements are NOT INCLUDED.
# ALL numbers are unique.

# list = [2, 1, 3, 5, 4, 11, 9]
# min is 1 here, max is 11. sum will be 3+5+4

# But list can start with max and end with min like: [2,11,3,5,4,1,9]
# The list could be also only [2,11]
# Then what? scenario below:

# o(n)
def sum_btw_min_and_max(list):
    if len(list) < 2:                       # The list could be also only [2,11]
        return "-1 (Error)"


    min_index = list[0]                     # Q: is list[0] here for index and ele INDEX or VALUE?
    max_index = list[0]
# Or just min_index = max_index = 0
    min_ele = list[0]
    max_ele = list[0]
# Or just min_ele = max_ele = list[0]
    i = 0
    while i < len(list):
        if list[i] < min_ele:   # if ELEMENT in the list at INDEX i < min_ele
            min_ele = list[i]
            min_index = i
        if list[i] > max_ele:   # if ELEMENT at index i > max_ele
            max_ele = list[i]
            max_index = i
        i += 1                  # Q: Meaning? add that index into the list? print(i)= 1,2,3,4,5,6,7
        print(i)                # Q: Why there's no 0 because i was 0 in beginning?

    return sum(list[min(min_index, max_index) + 1:max(min_index, max_index)])
    # Or use below: the breakdown of single line:
    # list[start : stop]
    # start = min(min_index, max_index)
    # stop = (min_index, max_index)
    # result_list = list[start + 1:stop]    # +1 because we can't include minimum ele in here...
    # return sum(result_list)

test_list = [5, 2, 11, 23, 4, 51, 9]        # (11+23+4) = 38
result = sum_btw_min_and_max(test_list)
print(result)