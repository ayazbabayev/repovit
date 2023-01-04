#When a user enters number, its factorial is displayed:

#o(n)
def factorial(n):
    result = 1
    for i in range(1, n+1): #we go through all elements from i to n+1. for variable in range between 1 and n (we include the last value so +1 to make last value count)
        result = result * i
    print(result)

factorial(5) #its 1*2*3*4*5= 120

# Add two numbers example:
n1=3
n2=4
def add2num(n1, n2):
    result = n1 + n2
    return(result)

print(add2num(n1,n2))
#or without n1= n2= above just input below
print(add2num(3,4))
