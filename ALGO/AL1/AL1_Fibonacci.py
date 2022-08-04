# Fibonacci:
# The number of sum of two previous numbers.

def fibonacci(n):
    if n<0:
         print(f'{n} is not a valid number.')
    #need to add more edge cases: n = 0, n = 1, n = 2
    fib1= 1
    fib2 =1
    index = 3 # Vitaly: "I putted 3 because we calculate the 3rd element of fibonacci sequence, we know first 2 are 1 & 1."
    result = [fib1, fib2] #1, 1, "2"----vvv (#)
    while index <= n:
            result.append(fib1 + fib2) # adding this fib1+fib2 into the list "result". #we take result list and we add new number, we add fib1+fib2 and have new element. we add them to list.
            fib1, fib2 = fib2, fib1 + fib2 #1, 2
            index = index + 1
    return result

fibs = fibonacci(6) # 1, 1, 2, 3 ,5 ,8
print(fibs)
