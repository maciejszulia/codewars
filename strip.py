def alphabet_position(text):
    get_letters = [str(ord(str(char))-96) for char in text.lower() if str(char).isalpha()]
    return " ".join(get_letters)

print(alphabet_position("The sunset sets at twelve o' clock."))