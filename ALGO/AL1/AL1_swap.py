#SWAP THE VALUES BETWEEN TWO; a to b  &  b to a:
a=12
b=9

print(f'1-BEFORE: a: {a}, b: {b}')
#or
print('2-BEFORE: a: '+str(a),'b: '+str(b))
############################################
#SOLUTION 1: Temporary variable:
# temp=a
# a=b
# b=temp

#SOLUTION 2: Python built-in function:
#a,b = b,a

#SOLUTION 3: arithmetics:
a= a+b #12+9=21
b= a-b #21-9=12 (a+b)- 
a= a-b #21-12=9

############################################
print(f'1-AFTER: a: {a}, b: {b}')
print('2-AFTER: a: '+str(a),'b: '+str(b))
