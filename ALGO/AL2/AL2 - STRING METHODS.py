# AL 2
# STRING METHODS:

# 1. ESCAPING CHARACTERS: String with "quotes"
print('\n1.__________________________________________________')

str1= "This is a string with \"quotes\"."
print(str1)

# 2. "IN" SYNTAX: Find letter in string & give TRUE / FALSE
print('\n2.__________________________________________________')

str2 = "This is a string."
print("i" in str2)
print("z" in str2)

# 3. INDEXING & SLICING STRINGS:
print('\n3.__________________________________________________')
# ([START:END])

str = "This is a string."
print(str[0])      # First character
print(str[0:4])    # First 4 characters
print(str[:4])     # First 4 characters (alternative)
print(str[4:])     # All after 4th character
print(str[-3:])    # Last 3 characters
print(str[-1])     # Last 1st character


# 4. CONCATENATION: a+b = ab
print('\n4.__________________________________________________')

str1= "This is a string"
str2= "!!!"
result = str1+str2
print(result)

# 5. ITERATION: string >>> (vertical) s t r i n g (vertical)
print('\n5.__________________________________________________')

str="string"
for each_character in str:
    print(each_character)

# 6. LEN: Counts LENGTH of a string: "Hello" = 5
print('\n6.__________________________________________________')

str="Hello"
total_character_count = len(str)
print(f'Length of "hello": ', total_character_count)

# 7. UPPER & lower:
print('\n7.__________________________________________________')

str="My String"
print(str.upper())
print(str.lower())

# 8. SPLIT: Splits string into list of items.
print('\n8.__________________________________________________')
str8= "This is a string"
all_words = str8.split()     # empty () will split by spaces!

for word in all_words:
    print(word)

# 9. JOIN: Splits string into list of items.
print('\n9.__________________________________________________')
list_of_words=['This','is','a','string']
joined_str= ''.join(list_of_words)
print(joined_str)

# 10. STRIP: Removes blanks & periods in START & END.
print('\n10._________________________________________________')
str10= '    ...This.is.a.string...    '

strip_func = str10.strip()
print(str10)        #BEFORE
print(strip_func)   #AFTER
#Other example:
strip_func2 = str10.strip().strip(".")
print(strip_func2)

# 11. REPLACE: replacing value or character with another.
print('\n11._________________________________________________')
str11= "This is a string"
replace_func = str11.replace('s', '$')
print(replace_func)

# 12. FIND: Returns the index of the 1st occurence of the string passed as the argument.
print('\n12._________________________________________________')
# If not found, it turns -1.

city_name = "Baku"
print(city_name.find('k'))  # Prints k as 2 > (B:0 A:1 K:2 U:3)

# 13. FORMAT:
print('\n13._________________________________________________')
str13= "This is string {}"
print(str13.format(13))
print(str13.format('Thirteen'))



