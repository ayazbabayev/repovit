# ALMOST PALINDROME:
# Ex: radar & radkar : almost palindrome
# but radar & radario: is not.

def is_almost_palindrome(s):
    for v in range(len(s)):
        temp_string = s[:v] + s[v+1:]   # goes from beginning from the string till "v"
                                        # then + concatenates /w:
                                        # other slice or the word from next character
        if temp_string == temp_string[::-1]:
            return "Almost a palindrome"
    return False
word1 = "radapr"   #eliminates "p" in rada(p)r  # tum harflerin ustunden carpi X vur bax if zerkalniy = almost pal.
word2 = "radaroo"

print(is_almost_palindrome(word1))
print(is_almost_palindrome(word2))