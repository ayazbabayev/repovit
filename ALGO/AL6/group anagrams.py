# GROUP ANAGRAMS:
# example:
# strs = ['eat','tea','tan','ate','nat','bat']
# [['bat'],['nat','tan'],['ate','eat','tea']

def group_anagrams(strs):
    anagram_dict = {}
    for word in strs:
        key = "".join(sorted(word))
        if key in anagram_dict:
            anagram_dict[key].append(word)
        else:
            anagram_dict[key] = []
            anagram_dict[key].append(word)

    return list(anagram_dict.values())

test_list = ['eat','tea','tan','ate','nat','bat']
result = group_anagrams(test_list)
print(result)