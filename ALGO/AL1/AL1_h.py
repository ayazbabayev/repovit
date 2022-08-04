# 1. COMPUTE THE SUM OF DIGITS IN ALL NUMBERS FROM 1 to N.
# When a user enters a number n, find the sum of digits in all numbers from 1 to n.
# Example: n = 5. Result = 1+2+3+4+5 = 15.

def sum_of_numbers(n):
    result = 0
    if n != 0:
        for d in range(1, n+1):
            result = result + d
    return result

print('1.Compute the sum of digits in all numbers from 1 to n:')

n = int(input('Enter your number here: '))

print(f'Sum of numbers from 1 to {n}:', sum_of_numbers(n))
##############################################################################

# 2. Find max number from values, entered manually from keyboard.
# Example, 124, 21, 32. Result = 124.

# 2 Solutions were given:
# Solution 1:
print('2. Find max number from values, entered manually from keyboard.')

def max_number(n):
    list = [a, b, c]
    return max(list)

a=int(input('Enter your 1st No here: '))
b=int(input('Enter your 2nd No here: '))
c=int(input('Enter your 3rd No here: '))

print(f'Your max number among 3 is', max_number(n))

# Solution2:
def max_no(list):
    max = list[0]
    for n in list:
        if n > max:
            max = n
    return max

x=int(input('Enter your 1st No here: '))
y=int(input('Enter your 2nd No here: '))
z=int(input('Enter your 3rd No here: '))

list=[x,y,z]

print('Max number among 3 is', max_no(list))

##############################################################################
# 3. Count odd and even numbers. Count odd and even digits of the whole number.
# Example: entered number is 34560, then 3 digits will be even (4,6,0) and 2 odd digits (3,5).

n = int(input('Enter a number to count the odd & even digits: '))

#Breaking down the digits in "n" into the list:
digit_list = [int(d) for d in str(n)]

even_count = 0
odd_count = 0

for x in digit_list:
    if x % 2 == 0:
        even_count +=1
    else:
        odd_count +=1

print("Count of the even digits: ", even_count)
print("Count of the odd digits : ", odd_count)

