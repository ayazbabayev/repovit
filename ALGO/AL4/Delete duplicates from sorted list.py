# Write a program that takes as input a sorted list and updates it
# so that all duplicates have been removed and the remaining elements have been shifted left
# to fill the emptied indices.
#
# Fill the remaining indices with zeros.
# Return the number of valid elements.
# You cant use sets for this coding challenge.

def delete_duplicates(list):
    write_index = 1                                 # Q: Why not zero? is it because we check duplication with prev? 0?

    for i in range(1, len(list)):                   # start from 1 and go till the end of list
        print(f'\nIteration # {i}')
        print(list)
        print(write_index)
        if list[write_index - 1] != list[i]:        # Q: 1:32:17 ??  checking if current element is the same as previous element: 1 != 4
            list[write_index] = list[i]             # after != HE SKIPS THIS PART at video. overwrite index write_index and set it to current element
            write_index += 1                        # increment the right index
                                                    # Q: i = i+1 is this simply adding to list?
    for i in range(write_index, len(list)):
        list[i] = 0                                  # Q: ?

    print(list,'<-- elements have shifted left')

test_list = [1, 4, 6, 6, 8, 9, 11, 11, 12]
delete_duplicates(test_list)
