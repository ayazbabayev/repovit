# Complete the method/function so that it converts dash/underscore
# delimited words into camel casing.
# The first word within the output will be capitalized only if the original word was capitalized
# (known as Upper Camel Case,
# also often referred to as Pascal case).
#
# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"
#

# def cc_converter(string):
#     x = 0
#     word = ""
#     while x < len(string):
#         if string[x] == 'a':
#             word = word + 'x'
#         x+=1
#         return word
#
# test_string = "the-stealth-warrior"
# result = cc_converter(test_string)
# print(result)

# def DNA_strand(dna):
#     i = 0
#     dna2 = ""
#     while len(dna) > i:
#         if dna[i] == "A":
#             dna2 = dna2 + "T"
#     return dna2
#
# dna = 'TAAT'
# result = DNA_strand(dna)
# print(result)

# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

sentence = "the-stealth-warrior"
print(sentence.split('-'))

sentence = 'the-stealth-warrior'
words = sentence.split('-')
result = words[0]
print('words[0]', words[0])

# for word in words[1:]:
#     result += word.title()
#     print(result)

for word in words[1:]:
        result += word[0].upper() + word[1:]

print(result)



# def cc_converter(word):
#     i = ''
#     # while i != '':
#     for i in range(len(word)):    # any difference if I'll add word) + 1) ?
#             prev = word[i-1]
#             print('prev:',word[i-1])  # r,t,h,e,-
#             dash = '-'
#             underscore = '_'
#             if prev == dash or prev == underscore:
#                 return word[i].upper()
#             i+=1
#     return word
#
#
#         # # list.append(list[i])
#         # print(word[i])
#         # print('string', word)
#
# test_string = "the-stealth-warrior"
# result = cc_converter(test_string)
# print(result)

# # arr = [1,2,4]
# # print(range(len(arr)))  # range(0,3)
# # print(len(arr))         # 3