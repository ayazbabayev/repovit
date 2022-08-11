# ANAGRAM
# abcd and bacd are anagrams of each other.

#abcd
#bacd

def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return "Not anagrams"

    if sorted(str1) == sorted(str2):    # Here we will put all characters into an ascending order
        return "Are anagrams"

    else:
        return False
test_st1= "abcd"
test_st2= "bacd"

result= is_anagram(test_st1, test_st2)
print(result)

