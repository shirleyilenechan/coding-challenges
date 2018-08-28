# You have been given a string s, which is supposed to be a sentence.
# However, someone forgot to put spaces between the different words, and for some reason they capitalized the first letter of every word.
# Return the sentence after making the following amendments:

# Put a single space between the words.
# Convert the uppercase letters to lowercase.


def amend_the_sentence(s):
    new_sentence = ""

    for char in s:
        if char == char.upper():
            new_sentence = new_sentence + " " + char.lower()
        else:
            new_sentence = new_sentence + char

    return new_sentence.strip()
