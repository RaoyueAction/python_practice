import cmath

def get_float_input(prompt):
    '''
    Get a float input from the user with error handling.
    '''
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print('Invalid input. Please enter a valid number.')

def solve_quadratic(a, b, c):
    '''
    Solve the quadratic equation ax^2 + bx + c = 0.
    Returns the two roots as a tuple.
    '''
    discriminant = b**2 - 4*a*c
    root1 = (-b + cmath.sqrt(discriminant)) / (2* a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    return root1, root2

def main():
    print('Quadratic Equation Solver')
    a = get_float_input('Enter coefficient a (non-zero): ')
    while a == 0:
        print('Coefficient a cannot be zero. Please enter a non-zero value.')
        a = get_float_input('Enter coefficient a(non-zero): ')
    b = get_float_input('Enter coefficient b: ')
    c = get_float_input('Enter coefficient c: ')
    root1, root2 = solve_quadratic(a, b, c)
    print(f'The roots of the equation {a}x^2 + {b}x + {c} = 0 are:')
    print(f'root1: {root1:.3f}')
    print(f'root2: {root2:.3f}')

if __name__ == '__main__':
    main()