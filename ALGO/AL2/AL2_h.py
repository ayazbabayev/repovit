# 1. Split in Half:
# Given a string. Split it into two equal parts. Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the second part.
# Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.

def split_equally_into_two_and_swap_both(s):

    first_half = s[:len(s) // 2:]
    second_half = s[:len(s) // 2:-1]
    middle_part = s[len(s) // 2]

    print(f'1st half of the string: ', first_half)
    print(f'2nd half of the string: ', second_half)
    print(f'Middle part of the string: ', middle_part)

    return second_half+first_half


string = 'bbbbbcaaaaa'

result = split_equally_into_two_and_swap_both(string)
print(f'String split equally into two and swapped:', result)


# 2. Unique Characters in String
# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.
# Hint: https://www.w3schools.com/python/python_sets.asp

def unique_characters_check(s):
    for char in s:
        if s.count(char) > 1:
            return "FALSE. The string contains duplicate characters."

    return "TRUE. All characters in the string are unique characters."
    # When you end the whole loop & didn't refer to prev return.


string1 = 'aabcde'
string2 = 'abcde'
string3 = 'abbdc'

result = unique_characters_check(string1)
print(f'for string1 ({string1}): ', result)

result = unique_characters_check(string2)
print(f'for string2 ({string2}) : ', result)

result = unique_characters_check(string3)
print(f'for string3 ({string3}) : ', result)
