#write functions here, don't add input('') statements here!
def multiplication_table(rows=5, cols=10):
    """Create a multiplication table using lists"""
    table = [[i * j for j in range(1, cols + 1)] for i in range(1, rows + 1)]
    return table


def print_multiplication_table(rows=5, cols=10):
    """Print a formatted multiplication table"""
    table = multiplication_table(rows, cols)
    for row in table:
        print(' '.join(f'{num:>2}' for num in row))


def test_config():
    return True