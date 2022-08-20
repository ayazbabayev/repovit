# 1. Below The Arithmetical Mean
# When given a list, the program should return a list of all the elements below the original list’s arithmetical mean.
# The arithmetical mean is the sum of all elements divided by the number of elements.
# Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25)
# Return [1, 3, 4, 2, 3]


def below_ari_mean(nums):
    ari_mean = sum(nums) / len(nums)
    blank_list = []
    i = 0                                    # ? is "i=0" as value
    while i < len(nums):                     # ? Why do we need this?
        if nums[i] < ari_mean:               # i is index
            blank_list.append(nums[i])
        i += 1   # ? If we have append above, what is the role of this?

    return blank_list

# 1st Iteration : i =0
# 2nd Interation: i=1

testlist = [1, 3, 5, 6, 4, 10, 2, 3]
blank_list = below_ari_mean(testlist)
print(blank_list)



# 2. Two Lowest Elements
# When given a list of elements, find the two lowest elements.
# They can be equal to each other or different.
# Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3

def lowest_2_elements(elements):
    elements.sort()
    return elements[:2]

lista = [198, 3, 4, 9, 10, 9, 2]
print(lowest_2_elements(lista))


# test_list = [198, 3, 4, 9, 10, 9, 2]
# test_list.sort()
# blank_list = []
# blank_list.append(test_list[:2:])

# Could we sort the list, then create another list and append the lowest two to there?