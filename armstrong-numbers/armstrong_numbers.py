def is_armstrong_number(number):
    digits = [int(digit) for digit in str(number)]
    total = sum(digit ** len(digits) for digit in digits)
    return total == number