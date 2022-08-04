# GET A RANDOM NUMBER & CALCULATE SUM OF THREE DIGITS:

# Here we use MODULUS DIVISION: We divide the number by 10. We get the remainder:
# For example: 123 % 10 = 123/10 = 12."3" we get our first remainder!

# 1- LONG METHOD: 

def sum_of_3digits(n):                  # n will be 123

    result = 0                          # because you will need result down in res = res + cur_no
    current_number = n % 10             # 123 / 10 = 12."3"
    result = result + current_number    # 0+"3"= '3'
    n = n // 10                         # Floor division: getting rid of remainder. 12."3" --> 12
    current_number = n % 10             # 12 / 10 = 1."2"
    result = result + current_number    # '3'+"2" = '5'
    n = n // 10                         # 1."2" --> 1
    result = result + n                 # '5'+1 = 6

    return(result)

result = sum_of_3digits(123)
print(result) # 1 + 2 + 3 = 6


# 2- SHORT METHOD - WITH LOOP:
def sum_of_3digits(n):                      # n will be 456

    result = 0
    while n != 0:                           # While number is NOT EQUAL to 0, I'll execute three steps below.
        current_number = n % 10                 # Current number is n/10 remainder.
        result = result + current_number        # new result = result + remainder taken from above.
        n = n // 10                             # get rid of remainder
    return result

result = sum_of_3digits(456)
print(result) # 4 + 5 + 6

