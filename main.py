from sympy import symbols, limit, oo, sympify
from sympy.core.sympify import SympifyError


def calculate_limit(func, var, point):
    """
    Calculate the limit of a function as the variable approaches a point.
    :param func: The function f(x).
    :param var: The variable x.
    :param point: The point to approach, can be a real number or ±oo (infinity).
    :return: The limit of the function.
    """
    try:
        # Calculate the limit
        limit_value = limit(func, var, point)
        return limit_value
    except Exception as e:
        return str(e)


def main():
    print("Limit Calculator")
    print("Enter the function in terms of x. Example: sin(x)/x")
    print("For infinity, use 'oo' (positive infinity) or '-oo' (negative infinity).")

    try:
        # User input for the function
        user_function = input("Enter f(x): ")
        # Convert the input string into a SymPy expression
        func = sympify(user_function)

        # Define the symbol
        x = symbols('x')

        # User input for the limit value
        limit_value = input("Enter the limit value (x approaches to): ")
        # Convert the limit value to the appropriate type
        if limit_value == 'oo':
            limit_point = oo
        elif limit_value == '-oo':
            limit_point = -oo
        else:
            limit_point = float(limit_value)

        # Calculate and print the limit
        result = calculate_limit(func, x, limit_point)
        print(f"The limit of f(x) as x approaches {limit_point} is: {result}")

    except SympifyError:
        print("Invalid function entered.")
    except ValueError:
        print("Invalid limit value entered.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
