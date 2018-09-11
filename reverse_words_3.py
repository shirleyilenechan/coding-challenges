# Given a string, you need to reverse the order of characters in each word
# within a sentence while still preserving whitespace and initial word order.


def reverse_words(s):
    s_split = s.split()
    new_string = ""

    for word in s_split:
        new_string = new_string + " " + word[::-1]

    return new_string.strip()
