# implement an algorithm to determine if a string has all unique characters


def all_unique_chars(string):
    if len(string) > 128:
        return False

    elif len(string) == 0:
        return None

    chars = set()

    for char in string:
        if char not in chars:
            chars.add(char)
        else:
            return False
    return True
