def validade_values(favorable_cases, possible_cases):
    if type(favorable_cases) != int or type(possible_cases) != int:
        raise TypeError("Parameters must have integer values.")
        
    if favorable_cases < 0:
        raise ValueError("Quantity of favorable cases must be at least zero.")
    
    if possible_cases <= 0:
        raise ValueError("Quantity of possible cases must be greater than zero.")
    
    if favorable_cases > possible_cases:
        raise ValueError("Quantity of favorable cases must be smaller of or equal to possible cases.")


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
