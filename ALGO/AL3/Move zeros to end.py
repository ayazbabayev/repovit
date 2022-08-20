# WRITE A FUNCTION THAT MOVES ALL ZEROS TO END.
# BUT KEEP THE ORDER OF OTHER ELEMENTS.

# input = [0,4,0,3,1,2]
# output = [4,3,1,2,0,0]

# When we'll see 0 we'll remove it an add it to the end of the list.

# o(n)
def move_zeros_to_end(arr):
    for i in range(0, len(arr)):     # you'll go through ea ele of this list (i) in range from 0 to length of array
        if arr[i] == 0:              # if our element in index i = 0
            arr.pop(i)               # remove that element by index i
            arr.append(0)            # then add it to the end of array

    return arr

input = [0,4,0,3,1,2]
output = move_zeros_to_end(input)
print(output)