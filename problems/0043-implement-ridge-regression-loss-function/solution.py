import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
	y_predict = X @ w # (m, n) * (n)
	mse = np.mean((y_predict - y_true) ** 2)
	ridge = alpha * np.sum(w ** 2)
	return np.round(mse + ridge, 3)