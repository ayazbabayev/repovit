# CONTAINS DUPLICATE:
# Return true if contains duplicate
# Return false if numbers are unique

def detect_duplicate(arr):
    set_for_arr = set(arr)
    if len(arr) == len(set_for_arr):
        return (False,'No duplicates')
    return (True,'Contains duplicates!')

pos_list = [1,2,3,1]
neg_list = [1,2,3,4]
pos_result = detect_duplicate(pos_list)
neg_result = detect_duplicate(neg_list)
print(pos_result)
print(neg_result)