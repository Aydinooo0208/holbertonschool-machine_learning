#!/usr/bin/env python3
"""Module for Binomial distribution"""


class Binomial:
    """Represents a Binomial distribution"""

    def __init__(self, data=None, n=1, p=0.5):
        """
        Initializes Binomial distribution

        Args:
            data: list of data to estimate the distribution
            n: number of Bernoulli trials
            p: probability of a success
        """
        if data is not None:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            mean = sum(data) / len(data)
            variance = sum((x - mean) ** 2 for x in data) / len(data)
            p = 1 - (variance / mean)
            self.n = round(mean / p)
            self.p = float(mean / self.n)
        else:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)

    def pmf(self, k):
        """
        Calculates the value of the PMF for a given number of successes

        Args:
            k: number of successes

        Returns:
            PMF value for k, or 0 if k is out of range
        """
        k = int(k)

        if k < 0 or k > self.n:
            return 0

        k_factorial = 1
        for i in range(1, k + 1):
            k_factorial *= i

        n_factorial = 1
        for i in range(1, self.n + 1):
            n_factorial *= i

        nk_factorial = 1
        for i in range(1, self.n - k + 1):
            nk_factorial *= i

        combination = n_factorial / (k_factorial * nk_factorial)

        return combination * (self.p ** k) * ((1 - self.p) ** (self.n - k))

    def cdf(self, k):
        """
        Calculates the value of the CDF for a given number of successes

        Args:
            k: number of successes

        Returns:
            CDF value for k, or 0 if k is out of range
        """
        k = int(k)

        if k < 0 or k > self.n:
            return 0

        return sum(self.pmf(i) for i in range(0, k + 1))
