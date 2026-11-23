import math

def normal_pdf(x, mean, std_dev):
    if std_dev <= 0:
        raise ValueError("std_dev must be positive")

    height = 1 / (std_dev * math.sqrt(2 * math.pi))
    width = math.exp(-((x - mean) ** 2 / (2 * std_dev ** 2)))

    return round(height * width, 5)