from decimal import Decimal, getcontext
from math import factorial

def chudnovsky_pi(num_terms):
    """
    Calculate an approximation of PI using the Chudnovsky Algorithm.
    
    :param num_terms: Number of terms in the series to achieve high precision
    :return: An approximation of PI
    """
    getcontext().prec = 110  # Setting precision higher than 100 to ensure accuracy in the first 100 digits
    C = 426880 * Decimal(10005).sqrt()
    M = 1
    L = 13591409
    X = 1
    K = 6
    S = L

    for i in range(1, num_terms):
        M = (K**3 - 16 * K) * M // i**3
        L += 545140134
        X *= -262537412640768000
        S += Decimal(M * L) / X
        K += 12

    pi = Decimal(C) / S
    return str(pi)[:101]  # Return the first 101 characters (including the '3' before the decimal point)

# Compute an approximation of pi using the Chudnovsky algorithm
approx_pi = chudnovsky_pi(10)  # The number of terms is set to 10 for demonstration
print (approx_pi)



