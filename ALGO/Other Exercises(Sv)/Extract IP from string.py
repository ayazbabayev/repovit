# Extract ip from a string:
# x = 'a 12.9.1986 Babayev 123.456.7890'

def ipextracter(x):
    splitted = x.split(' ')
    list1=[]
    for v in splitted:
        if not v.isalpha():
            list1.append(v)
            print('v',v)
    return list1

x = 'a 12.9.1986 Babayev 123.456.7890'
print(ipextracter(x))