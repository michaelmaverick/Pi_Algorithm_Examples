import decimal

def archimedes_pi(iterations):
    """
    Calculate an approximation of PI using Archimedes' method.
    
    :param iterations: Number of iterations (more iterations mean more sides in the polygon, thus more accuracy)
    :return: An approximation of PI
    """
    D = decimal.Decimal
    with decimal.localcontext() as context:
        context.prec = 100  # Set a large enough precision

        polygon_edge_length_squared = D(2)
        polygon_sides = D(4)

        for _ in range(iterations):
            polygon_edge_length_squared = 2 - 2 * (1 - polygon_edge_length_squared / 4).sqrt()
            polygon_sides *= 2

        return polygon_sides * ((polygon_edge_length_squared / 4).sqrt())

# Example usage
approx_pi = archimedes_pi(100)  # Using 100 iterations for demonstration
print(approx_pi)




