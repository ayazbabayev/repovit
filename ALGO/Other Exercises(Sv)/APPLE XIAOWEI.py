# def say_hello():
#     print('Hello, World')

# for i in range(5):
#     say_hello()

# Your previous Plain Text content is preserved below:
# 1. Sort a linked list of integers to be with ascending order.
# Input : 3, 5, 1, 4
# Output: 1, 3, 4, 5

def sortthelist(x):
    for i in range(len(x)):
        for cur in range(len(x) - 1 - i):
            if x[cur] > x[cur + 1]:
                x[cur], x[cur + 1] = x[cur + 1], x[cur]
    return x


x = [3, 5, 1, 4, -1, 100, 200, 9]
print(sortthelist(x))


# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
#  
# Example 1:
# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:
# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:
# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

def function2(x):
    x = x.lower()
    listx = []
    listy = []
    splitted = x.split(' ')
    print(splitted)
    for val in range(len(splitted) - 1, -1, -1):
        listx.append(splitted[val])

    for i in range(len(listx)):
        listy.append(listx[i])
        joined=' '.join(listy)

    return joined


x = 'the sky is blue'
x2 = 'hello world'
print(function2(x))
print(function2(x2))