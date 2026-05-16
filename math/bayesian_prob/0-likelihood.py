#!/usr/bin/env python3
"""Module for calculating likelihood using Binomial distribution"""
import numpy as np


def likelihood(x, n, P):
    """
    Calculates the likelihood of obtaining data given hypothetical
    probabilities of developing severe side effects

    Args:
        x: number of patients that develop severe side effects
        n: total number of patients observed
        P: 1D numpy.ndarray of hypothetical probabilities

    Returns:
        1D numpy.ndarray of likelihoods for each probability in P
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) or x < 0:
        raise ValueError(
            "x must be an integer that is greater than or equal to 0"
        )
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if np.any((P < 0) | (P > 1)):
        raise ValueError("All values in P must be in the range [0, 1]")

    k_factorial = 1
    for i in range(1, x + 1):
        k_factorial *= i

    n_factorial = 1
    for i in range(1, n + 1):
        n_factorial *= i

    nk_factorial = 1
    for i in range(1, n - x + 1):
        nk_factorial *= i

    combination = n_factorial / (k_factorial * nk_factorial)

    return combination * (P ** x) * ((1 - P) ** (n - x))
