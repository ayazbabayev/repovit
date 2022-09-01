def merge_sort(list):
    if len(list) <= 1:
        return list
    # print(list)
    middle = len(list) // 2
    first = merge_sort(list[:middle])
    second = merge_sort(list[middle:])
    return merge_arrays(first, second)


def merge_arrays(leftlist, rightlist):                  # first = leftlist and second = rightlist
    merged_array = []
    l = r = 0                                           # INDEX for leftlist = lf  and   rightlist = rt
    while l < len(leftlist) or r < len(rightlist):

        if l == len(leftlist):                          # IF LEFT IS NOT THERE, (because l = 0 up there) then add r to rigtlist.
            merged_array.append(rightlist[r])           # we add the value
            r += 1                                      # ADDS +1 to index, and moves to next index.
            continue                                    # continues back to while

        if r == len(rightlist):                         # IF RIGHT IS NOT THERE (because r = 0 up there) then add l to leftlist.
            merged_array.append(leftlist[l])
            l += 1
            continue


        if leftlist[l] <= rightlist[r]:                 # Q: By value; if l in leftlist (smaller than / equal to) r in rightlist
            merged_array.append(leftlist[l])            # add leftlist into merged array
            l += 1

        else:
            merged_array.append(rightlist[r])
            r += 1

    return merged_array


# la = [1, 7]
# ra = [2, 5]
# combined = merge_arrays(la, ra)
# print('merge arrays, combined:', combined)

test_list = [1, 4, 3, 5, 2, 6, 7, 8]
result_tl = merge_sort(test_list)
print('merge_sort:',result_tl)
