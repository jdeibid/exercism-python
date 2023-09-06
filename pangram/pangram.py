def is_pangram(sentence):
    # Create a dictionary of letters.
    letters = dict()
    # Check each letter in the sentence.
    for letter in sentence:
        # Check if the letter is in the dictionary.
        if letter.isalpha():
            # Add the letter to the dictionary.
            letters[letter.lower()] = letters.get(letter.lower(), 0) + 1
    # Check if the dictionary contains 26 letters.
    return len(letters.keys()) == 26