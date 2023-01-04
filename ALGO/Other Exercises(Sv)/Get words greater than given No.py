# GET WORDS THAT ARE GREATER THAN GIVEN NUMBER:

number = 6
list = ['Apple', 'Amazon', 'Tesla', 'Google', 'Internet', 'Selenium', 'Automation', 'Victory']
greater_than_6_list = []

def word_vs_number_measurer(list, number):
    for word in list:
        if len(word) > number:
            greater_than_6_list.append(word)
    return greater_than_6_list

print(word_vs_number_measurer(list, number))