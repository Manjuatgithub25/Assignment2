import random_word


def random():
    lists_of_words = []
    total_num_of_words = int(input("Enter the number of words you would like to generate: "))
    for i in range(total_num_of_words):
        random_words = random_word.RandomWords().get_random_word()
        lists_of_words.append(random_words)

    return lists_of_words


print(random())
