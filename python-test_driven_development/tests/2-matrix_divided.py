#!/usr/bin/python3
"""
This module contains the function matrix_divided for dividing all elements of a matrix.

>>> matrix_divided([[1, 2], [3, 4]], 2)
[[0.5, 1.0], [1.5, 2.0]]

>>> matrix_divided([[10, 20], [30, 40]], 10)
[[1.0, 2.0], [3.0, 4.0]]
"""

def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div and returns a new matrix."""
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
Faylı yadda saxla və çıx:
ESC → :wq → Enter

✅ 2. doctest-i işlət:
İndi terminalda bu əmr ilə faylı test et:

bash
Copy
Edit
python3 -m doctest 2-matrix_divided.py -v
✅ 3. Nəticəyə bax:
Əgər hər şey düzgündürsə, bu kimi bir nəticə alacaqsan:

bash
Copy
Edit
Trying:
    matrix_divided([[1, 2], [3, 4]], 2)
Expecting:
    [[0.5, 1.0], [1.5, 2.0]]
ok
Trying:
    matrix_divided([[10, 20], [30, 40]], 10)
Expecting:
    [[1.0, 2.0], [3.0, 4.0]]
ok
2 tests in 1 items.
2 passed and 0 failed.
Test passed.
