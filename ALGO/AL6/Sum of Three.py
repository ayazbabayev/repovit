# SUM OF THREE:
# Given an integer array, return all the triplets --> [nums[a],nums[b],nums[c]]
# return all triplets such that a!=b, b!=c & a!=c
# and [nums[a] + nums[b] + nums[c]] == 0
# Solution must not contain duplicate triplets.

# Ex: nums = [-1,0,1,2,-1,4]
# Output: [[-1,-1,2],[-1,0,1]]

def sum_of_three(arr):
    arr_set = set()         # here removed duplicates.
    arr.sort()              # here sorted from small to big.

    for x in range(len(arr)):
        y = x + 1           # Next index after x
        z = len(arr) - 1    # Last index of array

        while y < z:
            sum = arr[x] + arr[y] + arr[z]              # sum all indexess
            if sum == 0:
                arr_set.add((arr[x],arr[y],arr[z]))     # adds those indexes into arr_set in ()
                y = y + 1                               # increments next after index y where?
                z = z + 1                               # ^^^

            elif sum > 0:
                z = z - 1                               # what is the logic of removing bigger number here?
                                                        # how it minimizes sum down to 0 ?

    return arr_set

test_list = [-1,0,1,2,-1,4]
result = sum_of_three(test_list)
print(result)




