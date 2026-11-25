def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    n = len(vectors[0])

    centered = []

    for vector in vectors:
        mean = sum(vector) / n
        centered.append([x - mean for x in vector])

    result = []

    for x in centered:
        row = []

        for y in centered:
            cov = sum(a * b for a, b in zip(x, y)) / (n - 1)
            row.append(cov)

        result.append(row)

    return result