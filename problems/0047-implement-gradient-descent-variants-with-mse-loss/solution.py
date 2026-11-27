import numpy as np

def gradient_descent(X, y, weights, learning_rate, n_epochs,
                     batch_size=1, method='batch'):

    if method == 'batch':
        batch_size = len(y)
    elif method == 'stochastic':
        batch_size = 1

    for epoch in range(n_epochs):
        for i in range(0, len(y), batch_size):
            X_selected = X[i:i + batch_size]
            y_selected = y[i:i + batch_size]

            predictions = X_selected @ weights
            errors = predictions - y_selected

            gradient = 2 / len(y_selected) * (X_selected.T @ errors)

            weights = weights - learning_rate * gradient

    return weights