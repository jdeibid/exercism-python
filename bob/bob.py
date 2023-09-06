def response(hey_bob):
    hey_bob = hey_bob.strip()
    
    yelling = hey_bob.isupper()
    question = hey_bob.endswith("?")
    
    if question and not yelling:
        return "Sure."
    if question and yelling:
        return "Calm down, I know what I'm doing!"
    if yelling:
        return "Whoa, chill out!"
    if not hey_bob:
        return "Fine. Be that way!"
    return "Whatever."