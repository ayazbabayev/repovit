# PALINDROME
# radar = radar
# radkar != radar

def is_palindrome(s):      # ex: "s" is "radar" here
    s_reversed = s[::-1]   # radar in function gets reversed. :start :stop -1 step
    if s==s_reversed:      # if s = reversed s
        return "Palindrome."
    else:
        return "Not Palindrome."

word1 = "radar"
word2 = "radax"

test_result = is_palindrome(word1)
print(test_result)

test_result = is_palindrome(word2)
print(test_result)


#######################################################################################################################
