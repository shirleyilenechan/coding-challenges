# Given an arbitrary ransom note string and another string containing letters from all the magazines,
# write a function that will return true if the ransom note can be constructed from the magazines;
# otherwise, it will return false.

# Each letter in the magazine string can only be used once in your ransom note.

# Note:
# You may assume that both strings contain only lowercase letters.


def can_construct(self, ransomNote, magazine):
    for char in ransomNote:
        if char not in magazine:
            return False
        else:
            if magazine.count(char) < ransomNote.count(char):
                return False
    return True
