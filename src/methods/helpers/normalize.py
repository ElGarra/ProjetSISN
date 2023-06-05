import numpy as np

def normalize_columns(array):
    min_vals = np.min(array, axis=0)
    max_vals = np.max(array, axis=0)
    normalized_array = (array - min_vals) / (max_vals - min_vals)
    return normalized_array