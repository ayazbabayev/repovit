# ANAGRAM
# ABCD & BACD are anagrams of each other.

# measure len() & inside sorted()
# if len(x) != len(y): return "Not anagrams"
# if sorted(str1) == sorted(str2): return "Are anagrams"
# else: False

def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return "Not anagrams"

    if sorted(str1) == sorted(str2):    # Here we will put all characters into an ascending order
        return "Are anagrams"

    else:
        return False


test_st1 = "abcd"
test_st2 = "bacd"

result = is_anagram(test_st1, test_st2)
print(result)

########################################################################################################################
# REQ: LENGTH AND SORTED
def anagramma(s1,s2):
    if len(s1) == len(s2):
        if sorted(s1) == sorted(s2):
            return 'YES! THEY ARE ANAGRAMS'
    return 'NOT ANAGRAMS. NO.'

s1 = 'wxya'
s2 = 'xwzy'
print(anagramma(s1,s2))

print('\n#############################################################################################################')

def anagramcheck(s1,s2):
    if len(s1)==len(s2):
        if sorted(s1)==sorted(s2):
            return 'yes s1 & s2 are anagrams.'

    return 'no, s1 & s2 are not anagrams'

s1='xyz'
s2='yxz'
print(anagramcheck(s1,s2))

##################################################




















