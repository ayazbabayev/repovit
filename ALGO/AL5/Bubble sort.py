# BUBBLE Sort:
# Gathers to the end.
# DEFINITION: an algo that compares the adjacent (komsu/bitisik) elements and swaps their positions
# If they are not in the intended order. The order can be ascending and descending.

# always bubbles up smallest/biggest element to the end of list.
# list = [1, 7, 9, 4, 5, 3]
# 1 to 7: 1<7...keep same
# 7 to 9: 7<9...keep same
# 9 to 8: 9>8...so swap places.
# 9 to 4: 9>4...so swap places.
# 9 gets bubbled to the end of the list.
# then it restarts cycle again with 1 from very beginning.
# till [1 3 4 5 7 8 9]
# o(n2)
def bubble_sort(list):
    for i in range(len(list)):                              # for each i/ele in range of length of list
        for cur in range(len(list) - 1 - i):                  # -1 (exclude the last/sorted ele)  &  -i (exclude all sorted eles too)
            if list[cur] > list[cur + 1]:                       # if curr_ele in list is > than "curr_ele + 1" (ele at next index)
                list[cur], list[cur+1] = list[cur+1], list[cur]

    return list

list_to_sort = [1, 5, 6, 3, 4, 8, 2]
print('original list: ', list_to_sort)
print('bubble sorted:', bubble_sort(list_to_sort))