def print_upper_words(words, must_start_with):
    """ Uppercase and print words starting with the letters in must_start_with """ 
    for letter in must_start_with:
        for word in words:
            if word[0] == letter:
                print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with = {"h", "y"})