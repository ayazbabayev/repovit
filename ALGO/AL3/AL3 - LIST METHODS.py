# LIST (Python) = ARRAY (Java)

########################################################################################################################
# 1/11: CONCATENATE LIST:
list_no1 = [1,2,3]
list_no2 = [4,5,6]
string_list = ['A', 'B', 'C']

result_list= list_no1 + list_no2
print(result_list)


########################################################################################################################
# 2/11: INDEX in list starts with 0.
print(result_list[1])   # 1 is second number, "2" in list.
print(result_list[-1])  # -1 is last number, "6" in list.


########################################################################################################################
# 3/11: APPEND into list...to END of the list!
string_list.append('W')
print(string_list)


########################################################################################################################
# 4/11: REMOVE ALL ELEMENTS from list.
list_no1 = [1,2,3]
list_no1.clear()
print(list_no1)

string_list = ['A', 'B', 'C']
string_list.clear()
print(string_list)


########################################################################################################################
# 5/11: COUNT ELEMENTS in list:
list = [1,2,3,4,4,5,6,7]
print('COUNT ELEMENTS in list:', list.count(4))    # Counts how many "4"s in the list.



########################################################################################################################
# 6/11: Returning INDEX of a specific element: (Finds the 1st one!)
list = [9, 12, 0, 1, 12, 6, 7, 8]
print('Returning INDEX of a specific element: ', list.index(12))     # The first "12"s index is 1 in list.


########################################################################################################################
# 7/11: INSERT VALUE by INDEX in the list (index, value):
list = [1, 2, 3, 4, 5, 6, 7]
list.insert(0, 100)     # ADDS "100" into index 0, the beginning.
print('INSERT VALUE by INDEX in the list (index, value): ', list)



########################################################################################################################
# 8/11: REMOVE by INDEX:
list = [1, 2, 3, 4, 5, 6, 7]
list.pop(0)     # Removed index 0 which is "1" from list.
print('REMOVE by INDEX: ', list)


########################################################################################################################
# 9/11: REMOVE by VALUE.
list = [1, 2, 3, 4, 5, 6, 7]
list.remove(2)
print('REMOVE by VALUE: ', list)     # "2" is removed from list.


########################################################################################################################
# 10/11: REVERSE the list:
list = [1, 2, 3, 4, 5, 6, 7]
list.reverse()
print('REVERSE the list: ', list)


########################################################################################################################
# 11/11: SORT the list:
unsorted_list = [1, 3, 6, 2, 4, 7, 5]
unsorted_list.sort()
print('SORT the unsorted list: ', unsorted_list)
