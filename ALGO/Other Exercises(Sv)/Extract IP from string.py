# Extract ip from a string:
# x = 'a 12.9.1986 Babayev 123.456.7890'

def ipextracter(x):
    splitted = x.split(' ')      # You split to separate Nos from letters.
    list1=[]
    for v in splitted:
        if not v.isalpha():
            list1.append(v)
            print('v1',v)
    return list1

x = 'a 12.9.1986 Babayev 123.456.7890'
print(ipextracter(x))


# TURN string x = 'a b c  d  e   f' into  string 'abcdef'
def samplejoin(x):
    ls=[]
    for char in x:
        if char.isalpha():
            ls.append(char)
    joined=''.join(ls)
    return joined

x='a b c  d   e     f'
print(samplejoin(x))


# x = 'a 12.9.1986 Babayev 123.456.7890'



