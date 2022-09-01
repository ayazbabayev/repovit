# SELECTION Sort:
# Gathers to beginning
# DEFINITION: an algo that selects the smallest ele from unsorted list in ea iteration
# and places that ele at the beginning of the unsorted list.

# In an unsorted list: it finds the smallest ELE by comparing, and at the end of comparison
# smallest ele goes to beginning of the list.

# Checks/compares ea ELE by next ELE (till end of list).
# If 2nd ELE is smaller than 1st ELE, they swap places: if not then ELE remains its index.
# 2nd ELE replaces index ELE1, ELE moves to ELE2 place.
# list=[2, 1, 4, 7, 9, 3]
# is 2 < 1 ? no, so swap places.
# compare 1 to all rest. no smaller so keep it.
# move to 4. at 4 compared to 3. 4>3 so move to 3. compare to 5.
# move 3 to beginning after 1,2 .

#o(n2)
def selection_sort(list):
    for i in range(0, len(list)):   # for each i in range from 0 till the end of list
        min_index = i                                           # we take i as min_index
        for smaller_n in range(i + 1, len(list)):              # for 'smaller_n' in range from i +1 (from next ele after i) till end of list
            if list[smaller_n] < list[min_index]:              # if ele in index 'smaller_n' in list ... is smaller than ele in index 'min_index' in list
                min_index = smaller_n                          # min_index becomes that smaller_n
        list[i], list[min_index] = list[min_index], list[i]    # SWAP: ele at index i & ele at index min_index ...........................

    return list

list_2b_sorted = [1, 6, 4, 8, 9, 2, 3]
print('original:        ', list_2b_sorted)
print('selection sorted:', selection_sort(list_2b_sorted))
