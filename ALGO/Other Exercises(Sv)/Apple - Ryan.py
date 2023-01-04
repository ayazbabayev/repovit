def say_hello():
    print('Hello, World')

for i in range(5):
    say_hello()

# ################################################################################

candidates = [
    # Valid
    "racecar",
    "Kayak",
    "never odd or even",
    "rats live on no evil star",
    "A Toyota! Race fast... safe car: a Toyota",
    "Some men interpret nine memos",

    # Invalid
    "wombat",
    "No lemons, one melon",  # lemons, one->lemon, no
    "Too bad – I hid a book",  # book->boot
    "No trace; not one cartoon",  # cartoon->carton
    "Ma'am, I'm Adam",  # Ma'am->Madam
    "Del was a sled",  # was->saw
    "Flee to Em, remote elf",  # Em->me
    "Ma? Ha! A sham!"  # Ha! A sham->Has a ham
]


def is_palindrome(candidate: str) -> bool:
    candidate = candidate.lower()
    candidate = candidate.replace(' ', '')
    alphalist = []
    for char in candidate:
        if char.isalpha():
            alphalist.append(char)
    # print(alphalist)

    candidate_reversed = alphalist[::-1]
    if alphalist == candidate_reversed:
        return True
    else:
        return False


for candidate in candidates:
    print(f'{candidate}: {is_palindrome(candidate)}')
