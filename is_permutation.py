# given two strings, write a method to decide if one is a permutation of the other


def is_permutation(str_a, str_b):
    if str_a == str_b:
        return True

    elif len(str_a) != len(str_b):
        return False

    seen = set()

    for char in str_a:
        if char not in seen:
            seen.add(char)
            if str_a.count(char) != str_b.count(char):
                return False
    return True
