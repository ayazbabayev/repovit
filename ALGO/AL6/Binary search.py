# BINARY SEARCH:
# This can be implemented only on sorted list of items.
# If not sorted, we'll need to sort them first.

# To search sorted array, you repeatedly divide in the search interval in half.
# Begin with an interval covering whole array.
# (actual middle of array).
# If value of search key < middle, narrow the interval to lower half.
# If value of search key > middle, narrow to higher half.
# repeatedly check until value is found or interval is empty.
# [0,14,19,21,*99*,210,512,1028,4443,5110]
# 99 is middle.

def binary_search(arr, x):
    low_end = 0                             # First INDEX of array
    high_end = len(arr)-1                   # Q: Last INDEX of array / V:  "We don't want to get out of array."
    # print(high_end)                         # Q: What does it show us below? Index 9=983. What's 2nd 9?
    while low_end <= high_end:
        mid = (low_end + high_end) // 2
        guess = arr[mid]                    # Q: Meaning? Guess = to a/any value in arr?
        # print('guess value:',guess)
        if x == guess:
            return mid
        if x < guess:
            high_end = mid - 1
            # print('high_end index', high_end)
        if x > guess:
            low_end = mid + 1
            # print('low_end index', low_end)
    return None

test_list = [1,5,7,9,14,35,65,98,109,983]
test_pos_x = 5 # ^^^ Will find it at INDEX 1
test_neg_x = 3 # Will turn None

pos_result = binary_search(test_list, test_pos_x)
neg_result = binary_search(test_list, test_neg_x)

print(pos_result)
print(neg_result)