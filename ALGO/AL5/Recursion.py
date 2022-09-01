def recursion(number):
    if number == 0:     # if our no = 0, then we just return...
        return          # exits the function
    print(number)
    recursion(number-1)

result = recursion(5)
print(result)