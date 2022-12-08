import numpy
import os


# are you proud sir i named it after your function

def matVecMult(n):
    try:
        print("\n=== Matrix Data Entry ===")
        print("Enter", n, "values per row.")
        matrix = []

        for i in range(n):
            print("Row", i, "value:")
            row = list(map(int, input().split()))
            matrix.append(row)

        print("\n === Vector Data Input ===")
        vector = []

        for j in range(n):
            print("Enter a single integer for row", j, ":")
            row = list(map(int, input().split()))
            vector.append(row)
        print("\n")

        print("=== Your Entered Values ===")
        print("Matrix:", matrix)
        print("Vector:", vector)
        print("\n")

        print("Matrix Multiplication: ")

        result = numpy.dot(matrix, vector)
        for row in result:
            print(row)
        print("\nIs this in line with the code written in C?")

    except ValueError:
        print("There was an error in your value. Please try again.")
        return matVecMult(n)


os.system('cls')
""" Matrix and Vector Multiplication Test Case """

print("A matrix and vector multiplication calculator\n"
      "following the formula NxN * Nx1\n")

n = int(input("Enter the value of N: "))

matVecMult(n)
