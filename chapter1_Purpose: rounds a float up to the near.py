# Purpose: rounds a float up to the nearest integer
# Example:
#   Call:    round_up(4.5)
#   Returns: 5
import math
def round_up(float) :
    return math.ceil(float)
print (round_up(4.5))