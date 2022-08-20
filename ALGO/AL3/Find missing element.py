# CONSIDER AN ARRAY OF NON-NEGATIVE INTEGERS.
# A 2ND ARRAY IS FORMED BY SHUFFLING THE ELEMENTS OF THE 1ST ARRAY AND DELETING A RANDOM ELEMENT.
# GIVEN THESE 2 ARRAYS, FIND WHICH ELEMENT IS MISSING IN 2ND ARRAY.
# HERE IS AN EXAMPLE INPUT:
# 1ST ARRAY SHUFFLED & NO5 IS MISSING IN 2ND ARRAY.

# Input = [1,2,3,4,5,6,7]
# Output = [3,7,2,1,4,6]

########################################################################################################################
# SOLUTION 1:
def find_missing(input, output):
    input.sort()
    output.sort()

    for n in range(len(output)):    # n is in range of output length?
        if input[n] != output[n]:   # if n in input's list doesnt match n in output's list
            return input[n]         # bring that n

    return input[-1]      # if we gone till last n in output & still not found missing n, then return 'last n in input'.


test_input = [1, 2, 3, 4, 5, 6, 7]
test_output = [3, 7, 2, 1, 4, 6]

print(find_missing(test_input, test_output))


########################################################################################################################
# SOLUTION 2: zip

def find_missing(input, output):
    input.sort()
    output.sort()

    for no1, no2 in zip(input, output):
        if no1 != no2:
            return no1
    return input[-1]

test_input = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
test_output = ['d', 'a', 'b', 'f', 'e', 'c']

print(find_missing(test_input, test_output))

