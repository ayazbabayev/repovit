# SORTING: straight & reverse:

# LIST w/ Integers:
list = [1, 5, 3, 7, 9, 2, 12]
print('ORIGINAL:', list)

list.sort()
print('SORTED:  ', list)    # SORTED:   [1, 2, 3, 5, 7, 9, 12]

list.sort(reverse=True)     # REVERSED: [12, 9, 7, 5, 3, 2, 1]
print('REVERSED:', list)


# LIST w/ Strings (SORTED BY LENGTH AND REVERSED):
wordlist = ['apple', 'orange', 'kiwi', 'banana']
print('ORIGINAL:                ', wordlist)    # ORIGINAL: ['apple', 'orange', 'kiwi', 'banana']
#
wordlist.sort(key=len, reverse=True)
print('S by LENGTH & Reversed:  ', wordlist)    # S by LENGTH & Reversed: ['orange', 'banana', 'apple', 'kiwi']


########################################################################################################################

# SORT for LIST. SORTED for STRING:

# X.SORT is for LIST: [1,3,3,2,4]-->[1,2,3,3,4]
x=[1,3,3,2,4]
print(x)
x.sort()
print('sort x:',x)              # sort x: [1, 2, 3, 3, 4]

# SORTED(x) works for string. Sorts & converts string to list:
y='acdbd'
print('sorted y:',sorted(y))    # sorted y: ['a', 'b', 'c', 'd', 'd']
joined = ''.join(sorted(y))
print('joined y:',joined)

# Set eliminates dupicates!
setted=set(joined)
print('setted:',setted)         # setted: {'d', 'c', 'b', 'a'}