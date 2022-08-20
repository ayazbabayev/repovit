# THE LENGTH OF ARRAY IS BIGGER THAN 3 or EQUAL TO 3
# THERE EXISTS SOME INDEX i SUCH AS:
# a[0] < a[0] < ... < a[i]
# a[i] > a[i+1] > ... > a[a.size-1]

# Basically, find if there is an increasing subarray followed by a decreasing subarray
# [3, 5, 5] -> false
# [3, 4, 5, 2] --> true

# Basically, formula should give you a mountain shape on graph... x: index. y: value.


# o(n)
def is_mountain_array(mountain_list):
    i = 1
    while i < len(mountain_list) and mountain_list[i] > mountain_list[i-1]:
        i = i + 1       # or  i+=1
    if i == len(mountain_list) and i == 1:
        return False
    while i < len(mountain_list) and mountain_list[i] < mountain_list[i-1]:
        i = i + 1

    if i==len(mountain_list):
        return True

    return False

test_neg=[3,5,5]   # FALSE
test_pos=[3,4,5,2] # TRUE

test_neg_result = is_mountain_array(test_neg)
print(test_neg_result)

test_pos_result = is_mountain_array(test_pos)
print(test_pos_result)