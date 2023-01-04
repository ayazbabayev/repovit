# An isogram is a word that has no repeating letters,
# consecutive or non-consecutive.
# Implement a function that determines whether a string that contains only letters is an isogram.
# Assume the empty string is an isogram.
# Ignore letter case.
#
# Example: (Input --> Output)
#
# "Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)


# def is_isogram(string):
#     string = string.lower()
#     for l in string:
#         if string.count(l) >1:
#             return False
#         else:
#             return True
#
# print('Dermatoglyphics is', is_isogram('Dermatoglyphics'))
# print('isogram is', is_isogram('isogram'))
# print('aba is', is_isogram('aba'))
# print('moOse is', is_isogram('moOse'))            # ? NOOO
# print('isIsogram is', is_isogram('isIsogram'))
# print('"" is', is_isogram())

word = 'Texas'
def if_iso(word):
    if len(set(word)) == len(word):
        return True
    else:
        return False

print(if_iso(word))


# YAZ STICKER!
# print(range(len(string))) # range(0,4)
# print(len(string))        # 4
# stri = 123
# print(range(stri))


