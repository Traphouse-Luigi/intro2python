def print_upper_words(uppercase, must_start_with):
    """Change the letters in a list of words to uppercase, then print them
    on separate lines
    For example:
    list = ["nancy", "garvin", "keanon"] will return
    NANCY
    GARVIN
    KEANON
    """
    for words in uppercase:
        if words.startswith('e') or words.startswith('E'):
            words = words.upper()
        print(words)


def print_upper_words_G(uppercase, must_start_with):
    """Change the letters in a list of words to uppercase only if they start with certain letters,
    then print them on separate lines
    For example:
    list = ["nancy", "garvin", "keanon"] will return
    NANCY
    GARVIN
    KEANON
    """
    for words in uppercase:
        for letter in must_start_with:
            if words.startswith(letter):
                print(words.upper())
