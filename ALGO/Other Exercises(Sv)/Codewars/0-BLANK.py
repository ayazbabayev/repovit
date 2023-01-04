def multiplyList(myList):
    # Multiply elements one by one
    result = 1
    for x in myList:
        result *= x
    return result


# Driver code
list1 = [1, 2, 4]
print(multiplyList(list1))

