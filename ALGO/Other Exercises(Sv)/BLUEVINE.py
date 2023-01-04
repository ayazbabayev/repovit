# Given an array containing None values, fill in the None values with the most recent non None value in the array.
# For example, for array1= [1, None, 2, 3, None, None, 5, None]
# Output should be: [1, 1, 2, 3, 3, 3, 5, 5]


def prevreplacement(x):
    print('original',x)

    final_list = []
    for v in range(len(x)):                 # v in x demistim. hata vermisti. ozum sonra range(len(x)) dedim.
        if x[v] == None:                    # Ben burda 'None' string diye vermistim.
            x[v]=x[v-1]                     # Bu kismi yazmayi unutmastum.
            final_list.append(x[v])
        else:
            final_list.append(x[v])
    return final_list

x = [1, None, 2, 3, None, None, 5, None]
print('final:  ',prevreplacement(x))

########################################################################################################################

def find_ort(s):
    allwords= s.split()
    l = min(allwords,key=len)
    print('l',l)
    print(len(l))
    # for word in allwords:
    #     print(len(word))

s='wanna travel the world shall we'
print(find_ort(s))

######################################

def DNA_strand(dna):
    list=[]

    for letter in dna:

        if letter=='A':
            list.append('T')
        if letter=='T':
            list.append('A')
        if letter=='G':
            list.append('C')
        if letter=='C':
            list.append('G')

    joined = ''.join(list)
    return joined


print(DNA_strand(dna='ATTGC'))


########################################################################################################################

def vowelremover(string):
    list=[]
    final=[]
    for let in string:
        list.append(let)

    for v in list:
        if v!='a' and v!='e' and v!='i' and v!='o' and v!='u':
            final.append(v)

    joined= ''.join(final)

    return joined

print(vowelremover(string='good night'))


########################################################################################################################

def removesmallest(list):

    new=[]
    for v in range(len(list)):
        print('v',v)
        if list[v] != min(list):
            new.append(list[v])
    return new

print(removesmallest(list=[1,2,3,4,5]))


########################################################################################################################

