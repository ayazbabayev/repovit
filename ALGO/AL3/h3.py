# 1. Below The Arithmetical Mean
# When given a list, the program should return a list of all the elements below the original list’s arithmetical mean.
# The arithmetical mean is the sum of all elements divided by the number of elements.
# Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25)
# Return [1, 3, 4, 2, 3]


def below_ari_mean(nums):
    ari_mean = sum(nums) / len(nums)
    blank_list = []
    i = 0                               # 1st Iteration : i = 0.   2nd Interation: i = 1
    while i < len(nums):
        if nums[i] < ari_mean:
            blank_list.append(nums[i])
        i += 1

    return blank_list


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
