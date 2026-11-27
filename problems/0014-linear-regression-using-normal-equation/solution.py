import numpy as np

def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    X = np.asarray(X)
    y = np.asarray(y)
    theta = np.linalg.inv((X.T @ X)) @ X.T @ y
    theta = np.round(theta, 4)
    return theta.tolist()