import math
def score(x, y):
    # Define the inner, middle, and outer circle.
    INNER_CIRCLE, MIDDLE_CIRCLE, OUTER_CIRCLE = 1, 5, 10

    # Calculate the distance between the two points.
    distance = math.sqrt((x**2) + (y**2))

    # Return the score based on the distance.
    if distance <= INNER_CIRCLE:
        return 10
    elif distance <= MIDDLE_CIRCLE:
        return 5
    elif distance <= OUTER_CIRCLE:
        return 1
    else:
        return 0