# Create a function taking a positive integer as its parameter
# and returning a string containing the Roman Numeral representation of that integer.
# Modern Roman numerals are written by expressing each digit separately
# starting with the left most digit and skipping any digit with a value of zero.
# In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC.
# 2008 is written as 2000=MM, 8=VIII; or MMVIII.
# 1666 uses each Roman symbol in descending order: MDCLXVI.

# Example:
# solution(1000) # should return 'M'

# Symbol    Value
# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000

def roman_no_converter(number):
    dict = {1: 'I', 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    roman_list = []
    if number == 0:
        return False
    else:
        for n in str(number):
            roman_list.append(dict[int(n)])
            print(dict[int(n)])
    return roman_list
# how to add another line after return?
# ex: ''.join(roman_list)

n = 1000
result = roman_no_converter(n)
print(result)

