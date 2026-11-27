import numpy as np

def sgd_update(X, y, weights, learning_rate, n_iter):
    for i in range(n_iter):
        idx = i % len(y)

        x_selected = X[idx]
        y_selected = y[idx]

        prediction = x_selected @ weights
        error = prediction - y_selected

        gradient = 2 * error * x_selected

        weights = weights - learning_rate * gradient

    return weights.tolist()