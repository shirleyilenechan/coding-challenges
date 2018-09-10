# Given an input string, reverse the string word by word.


def reverseWords(s):
    s_string = s.split()
    reverse_s = s_string[::-1]
    return " ".join(reverse_s)
