# ALMOST PALINDROME:
# Ex: radar & radkar : almost
# palindrome
# but radar & radario: is not.

def almost_pal(string):
    string = string.lower()
    for char in range(len(string)):
        temp = string[:char] + string[char+1:]
        print(temp)

        if temp == temp[::-1]:
            return 'ALMOST PALINDROMES!'
    return 'FALSE: NOT EVEN "ALMOST" PALINDROMES'

word = 'Rapdar'
print(almost_pal(word))

#######################################################################################################################


def is_almost_palindrome(s):
    for v in range(len(s)):
        temp_string = s[:v] + s[v+1:]               # goes from beginning from the string till "v"
                                                    # then + concatenates /w:
                                                    # other slice or the word from next character
        # print(s[:v])
        #         # print(s[v+1:])
        if temp_string == temp_string[::-1]:        # Mirroring straight and reverse
            return temp_string,"Almost a palindrome"
    return False
word1 = "radapr"   #eliminates "p" in rada(p)r  # tum harflerin ustunden carpi X vur bax if zerkalniy = almost pal.
word2 = "radaroo"

print(is_almost_palindrome(word1))
# print(is_almost_palindrome(word2))

######################################################################################################################

print('string:')
string = '+alpha-'

for char in range(len(string)):
# print EA CHAR ONE-BY-ONE:
    print(string[char])       # a / l / p / h / a
for chr in range(len(string)):
# print from blank to whole by ea CHAR
    print(string[:chr])      # '' / + / +a / +al / +alp / +alph / +alpha
for chr in range(len(string)):
# print from whole to blank by ea CHAR
    print(string[chr+1:])  # alpha- / lpha- / pha- / ha- / a- / - / ''
print('stop')

#######################################################################################################################

# ALMOST PALINDROME:
# Ex: radar & radkar : almost
# palindrome
# but radar & radario: is not.

print('\n###########################################################################################################\n')

















