# Write a program that prints numbers from 1 to 100.
# For multiples of 3 print "Fizz" instead of number.
# For multiples of 5 print "Buzz" instead of number.
# For numbers which are multiples of BOTH 3 & 5 print "FizzBuzz"
# 1
# 2
# Fizz
# 4
# Buzz
# ...
# 14
# FizzBuzz
# 16
# ...
# 100

#O(n):
# we have to go through each element in the list & we execute one of those operations for each n.
# so we'll execute n operations.

def fizzbuzz(n): #n is highest number, 100.
    for v in range(1, n+1):   #n is 99 here, we need 100 so +1
#for Fizz we need number divisible to 3 and remainder 0:
#for Buzz we need number divisible to 5 and remainder 0:
#for FizzBuzz we need number divisible to 3 & 5 (3*5=15) and remainder 0:
        if v % (3 * 5) == 0:  # YOU CAN USE 15 TOO #if v is divisible by 5 and remainder =equals to 0
                print('FizzBuzz')
        #If line "if" above doesn't work, then moves down to elif options.

        elif v % 3 == 0:      #if v is divisible by 3 and remainder =equals to 0
            print('Fizz')

        elif v % 5 == 0:      #if v is divisible by 5 and remainder =equals to 0
            print('Buzz')

        else:
            print(v)          #if all 3 above are not true then just print number.

fizzbuzz(100)