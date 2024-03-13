# Numerical Methods for Polynomial Interpolation and Approximation

### Introduction

This Python script demonstrates several numerical methods for polynomial interpolation and approximation, including divided differences for Newton's interpolation, Hermite interpolation, and cubic spline interpolation. The script calculates divided differences for given data points, approximates values using polynomial interpolations, and constructs a cubic spline based on provided data points.

### Key Components

**1. Divided Differences for Newton's Interpolation**

The script calculates the divided differences for a given set of data points (x, y) using the divided_differences function. This table is essential for constructing Newton's interpolating polynomial.

**2. Approximation Using Polynomial Interpolation**

After calculating the divided differences, the script uses them to approximate values for a given x using polynomials of degrees 1, 2, and 3. The coefficients for these polynomials are derived from the divided differences.

**3. Hermite Interpolation**

Hermite interpolation considers not only the function values at certain points but also the values of the function's derivatives. The script creates a Hermite divided difference table and constructs the Hermite interpolating polynomial.

**4. Cubic Spline Interpolation**

Cubic spline interpolation involves constructing a piecewise polynomial function that passes through a series of control points. The script calculates the coefficients of cubic splines using the given data points, ensuring smoothness and continuity at the control points.

### Functions and Their Descriptions

1. divided_differences(x, y): Calculates the divided differences table for the given data points.
2. calculate_divided_differences(x, y): Extracts specific divided differences from the table, which are used as coefficients for the polynomial approximations.
3. print_hermite_table(x, f_x, f_prime_x, divided_diffs): Prints the Hermite divided difference table.
4. cubic_spline_coefficients(x_vals, y_vals): Calculates and returns the coefficients for cubic spline interpolation.

### How to run the script

1. **Install Python:** Ensure that Python is installed on your computer. If it's not installed, you can download and install it from python.org.
2. **Install NumPy:** The code requires NumPy, a popular Python library for numerical computations. If you don't have NumPy installed, you can install it using pip (Python's package installer). Open a terminal or command prompt and run the following command:

pip install numpy


3. **Run the Code:** Open a terminal or command prompt. Navigate to the directory where you saved assignment_2.py. You can run the Python script by executing the following command:

python assignment_2.py

By following these steps, you should be able to run the Python code successfully and view the results of the various interpolation methods.
