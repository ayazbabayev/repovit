# Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).
# For example,
# The correct answer would be 17.
# Hint: Don't forget to check for bad values like null/undefined

# [True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]

array1 = [True, True, True, False,
          True, True, True, True,
          True, False, True, False,
          True, False, False, True,
          True, True, True, True,
          False, False, True, True]

def count_sheep(array1):
    return array1.count(True)
# OR
#     return sum(array1)

print(count_sheep(array1))