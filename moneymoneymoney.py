import math
def calculate_years(principal, interest, tax, desired):
    return math.ceil(math.log(desired/principal) / math.log(1+interest-tax*interest))
