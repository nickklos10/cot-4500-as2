import numpy as np

# Given data points
x = np.array([7.2, 7.4, 7.5, 7.6])
y = np.array([23.5492, 25.3913, 26.8224, 27.4589])

# Function to calculate the divided differences
def divided_differences(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    coef[:,0] = y
    
    for j in range(1,n):
        for i in range(n-j):
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j]-x[i])
    
    return coef

# Calculate the difference table
a = divided_differences(x, y)

# Function to calculate the first, second and third divided differences
def calculate_divided_differences(x, y):
    n = len(y)
    # Initialize the differences matrix
    div_diffs = np.zeros((n, n))
    # The first column is the y values
    div_diffs[:,0] = y
    
    # Calculate the divided differences
    for i in range(1, n):
        for j in range(n - i):
            div_diffs[j][i] = (div_diffs[j+1][i-1] - div_diffs[j][i-1]) / (x[j+i] - x[j])
    
    # We are interested in the first three values from the top row
    # These will be the coefficients for the polynomials of degree 1, 2, and 3
    first = div_diffs[0, 1]  # Δ1
    second = div_diffs[0, 2] # Δ2
    third = div_diffs[0, 3]  # Δ3
    
    return first, second, third

# Calculate the required differences
first_diff, second_diff, third_diff = calculate_divided_differences(x, y)

# We calculate the first order differences (which is Δ1 for all pairs)
first_order_diffs = np.diff(y) / np.diff(x)

# Then, calculate the second order differences (Δ2)
second_order_diffs = np.diff(first_order_diffs) / np.diff(x[:-1])

# Finally, calculate the third order differences (Δ3)
third_order_diffs = np.diff(second_order_diffs) / np.diff(x[:-2])

# The first values of each of these differences will be our required coefficients
required_diffs = first_order_diffs[0], second_order_diffs[0], third_order_diffs[0]

print("(Δ1)", first_diff)
print("(Δ2):", second_diff)
print("(Δ3):", third_diff)


# Coefficients provided for the polynomial interpolations
f_x0 = 23.5492
delta_f_x0 = 1.8421
delta2_f_x0 = -0.411
delta3_f_x0 = -0.3832

# Calculate the coefficients for the polynomial interpolations
# For degree 1 (linear)
P1_coefficient = delta_f_x0

# For degree 2 (quadratic)
P2_coefficient = delta_f_x0 + delta2_f_x0 * (7.4 - 7.2)

# For degree 3 (cubic)
P3_coefficient = delta_f_x0 + delta2_f_x0 * (7.4 - 7.2) + delta3_f_x0 * (7.4 - 7.2) * (7.5 - 7.2)

# Given the coefficients and the polynomials, we can approximate f(7.3) using the polynomials of degree 1, 2, and 3.

# Polynomial functions using the calculated coefficients
def P1(x):
    return f_x0 + P1_coefficient * (x - 7.2)


# Approximate f(7.3) using the polynomials
approximation_P1 = P1(7.3)


print(approximation_P1)


# Given data for Hermite polynomial approximation
x = np.array([3.6, 3.8, 3.9])
f_x = np.array([1.675, 1.436, 1.318])
f_prime_x = np.array([-1.195, -1.188, -1.182])

# Constructing the Hermite Divided Difference Table
# For Hermite interpolation, we need to consider each x twice for the f(x) and f'(x)
x_hermite = np.repeat(x, 2)
n = len(x_hermite)

# The first column will be f(x), f(x), f'(x), f'(x), ...
# The second column is the first divided difference but for repeated x, it is f'(x)
divided_diffs = np.zeros((n, n))
divided_diffs[::2, 0] = f_x
divided_diffs[1::2, 0] = f_x
divided_diffs[::2, 1] = f_prime_x
divided_diffs[1:-1:2, 1] = (f_x[1:] - f_x[:-1]) / (x[1:] - x[:-1])

# Computing the rest of the divided difference table
for i in range(2, n):
    for j in range(n - i):
        divided_diffs[j, i] = (divided_diffs[j + 1, i - 1] - divided_diffs[j, i - 1]) / (x_hermite[j + i] - x_hermite[j])

# Function to print the table
def print_hermite_table(x, f_x, f_prime_x, divided_diffs):
    # Here we replace the backslash with double quotes
    print(f"{'x':^10}{'f(x)':^10}{'f''(x)':^15}{'Δ1':^20}{'Δ2':^20}")
    for i in range(len(x)):
        # Print x, f(x), and f'(x) for the original points
        print(f"{x[i]:^10}{f_x[i]:^10}{f_prime_x[i]:^15}", end="")
        # Print the divided differences. We take the first element from each column for the ith row
        for j in range(2, 4):
            if j - 1 < len(x) * 2:
                print(f"{divided_diffs[i, j]:^20}", end="")
            else:
                print(f"{'':^20}", end="")
        print()

# Print the Hermite Divided Difference Table
print_hermite_table(x_hermite, divided_diffs[:, 0], divided_diffs[:, 1], divided_diffs)

#Cubic Spline Interpolation

def cubic_spline_coefficients(x_vals, y_vals):
    n = len(x_vals) - 1  # Number of splines
    h = [x_vals[i+1] - x_vals[i] for i in range(n)]

    # Coefficients matrix A initialization
    A = np.zeros((n+1, n+1))
    # Result vector b initialization
    b = np.zeros(n+1)

    # Setting up the equations for the coefficients
    # Natural spline boundary conditions
    A[0][0], A[n][n] = 1, 1

    for i in range(1, n):
        A[i][i-1] = h[i-1]
        A[i][i] = 2 * (h[i-1] + h[i])
        A[i][i+1] = h[i]
        b[i] = 3 * ((y_vals[i+1] - y_vals[i]) / h[i] - (y_vals[i] - y_vals[i-1]) / h[i-1])

    # Solving the system of linear equations for coefficients
    c = np.linalg.solve(A, b)

    return A, b, c

# Example usage (to be uncommented when running the actual script):
# Given values
x_points = [2, 5, 8, 10]
y_points = [3, 5, 7, 9]
A_matrix, b_vector, c_vector = cubic_spline_coefficients(x_points, y_points)

#Printing the results
print("Matrix A:")
print(A_matrix)
print("\nVector b:")
print(b_vector)
print("\nVector c:")
print(c_vector)
