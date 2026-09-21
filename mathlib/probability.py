from function import validate_values


def validate_probability(*values):
    for value in values:
        if not 0 <= value <= 1:
            raise ValueError("Probability must be between zero and one.")
            

def probability(favorable_cases, possible_cases):
    if type(favorable_cases) != int or type(possible_cases) != int:
        raise TypeError("Parameters must have integer values.")
    
    if favorable_cases < 0:
        raise ValueError("Quantity of favorable cases must be at least zero.")

    if possible_cases <= 0:
        raise ValueError("Quantity of possible cases must be greater than zero.")

    if favorable_cases > possible_cases:
        raise ValueError("Quantity of favorable cases must be smaller than or equal to possible cases.")

    return favorable_cases / possible_cases


def complement_probability(probability):
    validate_values(probability)
    validate_probability(probability)
    
    return 1 - probability


def conditional_probability(joint_probability, condition_probability):
    validate_values(joint_probability, condition_probability)
    validate_probability(joint_probability, condition_probability)

    if condition_probability <= 0:
        raise ValueError("Condition probability must be greater than zero.")

    if joint_probability > condition_probability:
        raise ValueError("Joint probability must be smaller of or equal to condition probability.")

    return joint_probability / condition_probability
