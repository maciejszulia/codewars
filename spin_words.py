sen = "Hey fellow warriors"


def spin_words(sentence):
    list_of_words = sentence.split()
    for word in list_of_words:
        if len(word) > 5:
            list_of_words[list_of_words.index(word)] = word[::-1]
    output = " ".join(list_of_words)
    return output

print(spin_words(sen))
