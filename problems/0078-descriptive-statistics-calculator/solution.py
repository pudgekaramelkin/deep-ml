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
    
