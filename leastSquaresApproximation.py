# lsa_module.py
import numpy as np

def lsaMethod(data):
    """
    Perform Least Squares Approximation using the X^T X | X^T Y method.

    :param data: List of temperature readings.
    :return: A tuple of (x_min, x_max, c, d) values of the least squares equation.
    """
    n = len(data)
    x = np.arange(1, n + 1)


    X = np.vstack((x, np.ones_like(x))).T

  
    XTX = np.dot(X.T, X)
    XTY = np.dot(X.T, data)

   
    coefficients = np.linalg.solve(XTX, XTY)

    x_min = x[0]
    x_max = x[-1]
    c = coefficients[1]
    d = coefficients[0]

    return (x_min, x_max, c, d)
