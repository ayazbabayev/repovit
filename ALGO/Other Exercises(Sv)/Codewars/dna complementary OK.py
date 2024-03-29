# In DNA strings, symbols
# "A" and "T" are complements of each other,
# as "C" and "G".
# Your function receives one side of the DNA
# (string, except for Haskell);
# you need to return the other complementary side.
# DNA strand is never empty or there is no DNA at all
# (again, except for Haskell).
# More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

# Example: (input --> output)
# "ATTGC" --> "TAACG"
# "GTAT" --> "CATA"

def dna_changer(dna_code):
    dict = {'A':'T',
           'T':'A',
           'C':'G',
           'G':'C'}

    return "".join(dict[x] for x in dna_code)


dna_code = 'TAACAGAAT'
result = dna_changer(dna_code)    # result should be
print(result)