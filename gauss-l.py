from decimal import Decimal, getcontext

def gauss_legendre_pi(iterations, precision):
    """
    Calculate an approximation of PI using the Gauss-Legendre Algorithm.
    
    :param iterations: Number of iterations for the algorithm
    :param precision: The number of decimal places to calculate to
    :return: An approximation of PI
    """
    getcontext().prec = precision + 2  # Set the precision of decimal number calculations to be higher than what we need
    
    a = Decimal(1)
    b = 1 / Decimal(2).sqrt()
    t = Decimal(0.25)
    p = Decimal(1)  # Changed from float to Decimal

    for _ in range(iterations):
        a_next = (a + b) / 2
        b = Decimal(a * b).sqrt()
        t -= p * (a - a_next)**2
        a = a_next
        p *= 2

    approx_pi = (a + b)**2 / (4 * t)
    getcontext().prec -= 2  # Reduce the precision back down

    return approx_pi

# Example usage
approx_pi = gauss_legendre_pi(100, 100)  # Using 100 iterations for demonstration, and 100 decimal places
print (approx_pi)


