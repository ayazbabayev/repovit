# SORTING: straight & reverse:
# Integers & Strings:
list = [1, 5, 3, 7, 9, 2, 12]
print('ORIGINAL:', list)

list.sort()
print('SORTED:  ', list)

list.sort(reverse=True)
print('REVERSED:', list)


# Strings (SORTED BY LENGTH AND REVERSED):
wordlist = ['apple', 'orange', 'kiwi', 'banana']
print('ORIGINAL:                ', wordlist)
#
wordlist.sort(key=len, reverse=True)
print('S by LENGTH & Reversed:  ', wordlist)

# Q: SORT AND SORTED DIFFERENCE LOOKUP.