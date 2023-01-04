def smallest(x):
    if len(x) == 0:
        return 'list2 is blank. No function to process here.'
    else:
        smallest_value = x[0]
        for item in x:
            if item < smallest_value:
                smallest_value = item
        return smallest_value

test = [1,2,-1,3,-77,4,5]
result = smallest(test)
print(result)