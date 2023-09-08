import re
def is_valid(isbn):
    # Extract the digits.
    digits = ''.join(re.findall(r'\w', isbn))
    # Check for invalid formats.
    if len(digits) != 10:
        return False
    if not digits[-1].isnumeric():
        if digits[-1] != 'X':
            return False
    # Check for invalid check digit.
    digits = [*digits]    
    if digits[-1] == 'X':
        digits[-1] = '10'
    # Initialize variables.
    total = int()
    count = 10
    # Process the digits.
    for digit in digits:
        print(digit)
        if digit.isalpha():
            return False
        total += int(digit) * count
        count -= 1
    return total % 11 == 0