# CONVERT LIST INTO TO STRING

def list_stringer(x):
    final = ""
    for chars in x:
        final += chars
    return final

word = ['I',' ','l','i','k','e',' ','Algo!',' ', ':)']
result = list_stringer(word)
print(result)
# OR solution 2:
print(''.join(word))

