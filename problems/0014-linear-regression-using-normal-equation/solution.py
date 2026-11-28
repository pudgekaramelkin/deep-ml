import numpy as np
from sklearn.linear_model import LinearRegression

def linear_regression_normal_equation_numpy(X: list[list[float]], y: list[float]) -> list[float]:
    X_formatted = np.array(X)
    y_formatted = np.array(y)
    theta = np.linalg.inv((X_formatted.T @ X_formatted)) @ X_formatted.T @ y_formatted
    theta = np.round(theta, 4)
    return theta.tolist()

def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    model = LinearRegression(fit_intercept=False)
    model.fit(X, y)

    return np.round(model.coef_, 4).tolist()