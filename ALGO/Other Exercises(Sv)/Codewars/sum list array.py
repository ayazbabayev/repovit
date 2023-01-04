# SUM LIST
# SUM ARRAY
# SUM ELEMENTS IN LIST
# SUM ELE IN LIST

a = [1, 2]

def sum_array(a):
    sum = 0
    if a == []:
        return 0
    else:
        for ele in a:
            sum += ele
        return sum


print(sum_array(a))