import numpy as np

def kl_divergence_normal(mu_p, sigma_p, mu_q, sigma_q):
    log_term = np.log(sigma_q / sigma_p)

    fraction = (
        sigma_p ** 2 + (mu_p - mu_q) ** 2
    ) / (2 * sigma_q ** 2)

    return log_term + fraction - 0.5