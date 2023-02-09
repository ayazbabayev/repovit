def movetoend(x, n): # n burda 2 mesela, ama dynamic olsun diye n dedik.
    final = []
    for val in range(len(x)):

        if x[val] == n:
            final.append(x[val])
        else:
            final.insert(0, x[val])
    return final


x = [0, 2, 1, 4, 3, 2, 5]
n = int(input('Enter your number here: '))
print(movetoend(x, n))

# x = [0, 2, 1, 4, 3, 2, 5]
# # move 2 to the end
# expect = [5, 3, 4, 1, 0, 2, 2]
#
# # move 4 to the end
# expect = [5, 3, 1, 0, 2, 2, 4]