# VALID PARENTHESES:

# Given a string "s", containing '(' , ')', '[', ']'.
# The input string is valid if:
# Open brackets will be closed by close brackets.
# All in correct order.
# Example:
# Input:    s = "()[]"
# Output:   True
# Input:    s = "])[("
# # Output: False

def is_valid_parenthesis(s):
    parenthesis = {'(':')','[':']'}     # We create a dictionary, and use key vs value: key= open bracket, value=close bracket.
    control = []                        # create 'control', if finds opening, adds closing into control
                                        # iterates to key and returns related value.
    for i in s:
        if i in parenthesis:
            control.append(parenthesis[i])      # ???
            # print(parenthesis[i])
        elif control.pop() != i:                # ???
            return False

    if len(control) == 0:
        return True

    return False

test_pos = '()[]'    # True
test_neg = '(][)'    # False
result_pos = is_valid_parenthesis(test_pos)
result_neg = is_valid_parenthesis(test_neg)
print(result_pos)
print(result_neg)

# Q: General explanation. especially control part.
# Q: How it goes with sequence here. are we following key:value sequence?
# Q: Can we visually see how it appends & pops in printed lists?
