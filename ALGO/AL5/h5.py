def selection_sort(list):
    for i in range(0, len(list)):
        max_index = i
        for greater_n in range(i + 1, len(list)):
            if list[greater_n] > list[max_index]:
                max_index = greater_n
        list[i], list[max_index] = list[max_index], list[i]
    return list


list_2b_sorted = [1, 6, 4, 8, 9, 2, 3]
print('original:        ', list_2b_sorted)
print('selection sorted:', selection_sort(list_2b_sorted))


print('_______________________________________________________________________________________________________________')


def bubble_sort(list):
    for i in range(len(list)):
        for c in range(len(list) - 1 - i):
            if list[c] < list[c + 1]:
                list[c], list[c + 1] = list[c + 1], list[c]

        return list


list_to_sort = [1, 5, 6, 3, 4, 8, 2]
print('original list: ', list_to_sort)
print('bubble sorted:', bubble_sort(list_to_sort))


print('_______________________________________________________________________________________________________________')


def insertion_sort(list):
    for i in range(1, len(list)):                   # first card - index 0 - was sorted: "2". So we begin with 2nd card -index 1- which is "1".
        key = list[i]                               # key = "1".             any element in list ? all elements in list?
        prev = i - 1                                   # "2"

        while prev >= 0 and key > list[prev]:             # while 2 >= 0 and 1 < 2's index (value 2)
            list[prev + 1] = list[prev]                   # 2 = 1's place
            prev -= 1                           # Q: ??? HOW PREV EQUALS TO -1??? 1:29:56 WHAT IS -1...REMOVAL?
                                             # BECAUSE -1 AND >=0 RULE HE GETS OUT OF LOOP. WAS 0 INDEX? OR VALUE?
        list[prev + 1] = key                    # PREV # HOW TO KNOW IF indentation is True or False WITHOUT else?

    return list

list_sort = [2, 1, 4]
print('original list:   ',list_sort)
result=insertion_sort(list_sort)
print('insertion sorted:',result)


print('_______________________________________________________________________________________________________________')


def merge_sort(list):
    if len(list) <= 1:
        return list
    # print(list)
    middle = len(list) // 2
    first = merge_sort(list[:middle])
    second = merge_sort(list[middle:])
    return merge_arrays(first, second)


def merge_arrays(leftlist, rightlist):
    merged_array = []
    l = r = 0
    while l < len(leftlist) or r < len(rightlist):

        if l == len(leftlist):
            merged_array.append(rightlist[r])
            r += 1
            continue

        if r == len(rightlist):
            merged_array.append(leftlist[l])
            l += 1
            continue


        if leftlist[l] >= rightlist[r]:
            merged_array.append(leftlist[l])
            l += 1

        else:
            merged_array.append(rightlist[r])
            r += 1

    return merged_array


test_list = [1, 4, 3, 5, 2, 6, 7, 8]
print('original list:', test_list)
result_tl = merge_sort(test_list)
print('merge_sort:',result_tl)