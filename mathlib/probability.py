def probability(favorable_cases, possible_cases):
    if type(favorable_cases) != int or type(possible_cases) != int:
        raise TypeError("Parameters must have integer values.")
    
    if favorable_cases < 0:
        raise ValueError("Quantity of favorable cases must be at least zero.")

    if possible_cases <= 0:
        raise ValueError("Quantity of possible cases must be greater than zero.")

    if favorable_cases > possible_cases:
        raise ValueError("Quantity of favorable cases must be smaller of or equal to possible cases.")

    return favorable_cases / possible_cases


def complement_probability(probability):
    if type(probability) not in (int, float):
        raise TypeError("Probability must have a numeric value.")
    
    if not 0 <= probability <= 1:
        raise ValueError("Probability must be between zero and one.")

    return 1 - probability


def conditional_probability(joint_probability, condition_probability):
    if type(joint_probability) not in 
