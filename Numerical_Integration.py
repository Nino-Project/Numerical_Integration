import sympy as sy  # Using sympy library to display entered information to user and for substitution

x = sy.symbols("x")  # Defining Symbol. Assume all problems are f(x)
global_list = []  # Global list to be used for both Trapezoidal and Simpson's rule


def main():
    user_verify = 'y'
    while user_verify != 'n':  # Loop to verify user entry

        f = sy.sympify(input("Enter f(x): "))
        n = int(input("Enter the number of subdivision: "))
        a = float(input("Enter lower limit: "))
        b = float(input("Enter upper limit: "))
        print("------------------------ \n")
        sy.pprint(sy.Integral(f, (x, a, b)))  # Display User Entry
        user_verify = input("\nRe-enter Information: (Y|N) ").lower()

    delta_x = (b - a) / n   # Calculate delta x

    populate_global_list(a, f, n, delta_x)
    print("\nTrapezoidal Approximation: ", (trapezoidal_approximation(delta_x)))

    isEven = n % 2  # If 0 it is Even. If 1 it is odd
    if isEven == 1:  # Dont run Simpson's Rule if n is odd
        return "Unable to approximate using Simpson's Rule. The number Subdivisions must be even"
    else:
        print("Simpson's Approximation: ", (simpson_approximation(delta_x)))


def populate_global_list(lower, function, subdivision, d_x):
    for i in range(0, subdivision + 1):
        Xi = lower + i * d_x  # Find Xi
        global_list.append(function.subs(x, Xi))  # Find f(Xi) then append to global list


def trapezoidal_approximation(d_x):
    for i in range(1, len(global_list) - 1):  # For loop that ignores first and last index
        global_list[i] = 2 * global_list[i]  # Multiply each index by 2
    return (d_x / 2) * sum(global_list)  # Return Trapezoidal Approximation


def simpson_approximation(d_x):
    for i in range(1, len(global_list) - 1, 2):  # For loop that ignores first and last index, then increments odd index
        global_list[i] = 2 * global_list[i]  # Multiply each odd index by 2
    return (d_x / 3) * sum(global_list)


main()
