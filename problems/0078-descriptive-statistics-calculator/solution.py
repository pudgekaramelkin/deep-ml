def descriptive_statistics_manual(data: list) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """

    data = sorted(data)

    if not data:
        raise ValueError("Data must not be empty.")

    n = len(data)


    mean = sum(data) / n

    mid = n // 2
    if n % 2 == 0:
        median = (data[mid - 1] + data[mid]) / 2
    else:
        median = data[mid]

    acc = {}
    for i in data:
        acc[i] = acc.get(i, 0) + 1

    mode = max(acc, key=acc.get)

    variance = (sum((x - mean) ** 2 for x in data)) / n
    standard_deviation = variance ** 0.5

    def get_percentile(q=50):
        index = (n - 1) * q / 100
        lower = int(index)
        upper = min(lower + 1, n - 1)

        weight = index - lower

        return data[lower] * (1 - weight) + data[upper] * weight

    q25 = get_percentile(25)
    q50 = get_percentile(50)
    q75 = get_percentile(75)

    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "variance": variance,
        "standard_deviation": standard_deviation,
        "25th_percentile": q25,
        "50th_percentile": q50,
        "75th_percentile": q75,
        "interquartile_range": q75 - q25,
    }
        
import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    data_array = np.asarray(data)
    result = {}

    result["mean"] = np.mean(data_array) # sum(data_array) / len(data_array)
    result["median"] = np.median(data_array)

    values, counts = np.unique(data_array, return_counts=True)
    most_frequent = values[np.argmax(counts)]
    result["mode"] = most_frequent

    result["variance"] = np.var(data_array)
    result["standard_deviation"] = np.std(data_array)

    percentiles = [25, 50, 75]
    result.update({f"{x}th_percentile": np.percentile(data_array, q=x) for x in percentiles})

    result["interquartile_range"] = np.percentile(data_array, q=75) - np.percentile(data_array, q=25)

    return result
