def is_isogram(string):
    letters = dict()
    # Check each letter in the string
    for letter in string:
        if letter.isalpha():
            letters[letter.lower()] = letters.get(letter.lower(), 0) + 1
    # Check if there is one copy of each letter.
    for count in letters.values():
        if count > 1:
            return False
    return True