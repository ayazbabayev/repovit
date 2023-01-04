# "abc#d##c"      ==>  "ac"
# "abc##d######"  ==>  ""
# "#######"       ==>  ""
# ""              ==>  ""

# Assume "#" is like a backspace in string.
# This means that string "a#bc#d" actually is "bd"
# Your task is to process a string with "#" symbols.

def backspace(string):
    filtered_list = []
    hash = []
    for char in string:
        filtered_list.append(char)
    print(filtered_list.count('#'))

    return filtered_list

# the count of # is the amount of backspaces.
# this count will be the starting from end and applied to all inside list.


test1 = 'abc#d##c'
result = backspace(test1)
print(result)
