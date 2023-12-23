import random

def monte_carlo_pi(num_samples):
    """
    Calculate an approximation of PI using the Monte Carlo method.
    
    :param num_samples: Number of random points to generate
    :return: An approximation of PI
    """
    inside_circle = 0

    for _ in range(num_samples):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            inside_circle += 1

    return 4 * inside_circle / num_samples

# Example usage
approx_pi = monte_carlo_pi(100000000)  # Using 100,000,000 samples for demonstration
print (approx_pi)


