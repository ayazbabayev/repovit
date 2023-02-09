# If　a = 1, b = 2, c = 3 ... z = 26
# Then l + o + v + e = 54
# and f + r + i + e + n + d + s + h + i + p = 108
# So friendship is twice as strong as love :-)
# Your task is to write a function which calculates the value of a word based off the sum of the alphabet positions of its characters.
# The input will always be made of only lowercase letters and will never be empty.

def calculate_value_of_letters(word):
    alphabet = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6,
                'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
                'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18,
                's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,
                'y': 25, 'z': 26}

    word = word.lower()

    letter_list = []
    if word == '':
        return False
    else:
        for l in str(word):
            letter_list.append(alphabet[l]) # by dictionary value
            print(alphabet[l])

        print(f'{word} numerized:', letter_list)
    return sum(letter_list)


word = 'love'
result = calculate_value_of_letters(word)
print(result)

#OR:

# def words_to_marks(s):
#    return sum('_abcdefghijklmnopqrstuvwxyz'.index(e) for e in s)
#
# s = 'love'
# print(words_to_marks(s))
