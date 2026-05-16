#!/usr/bin/env python3
"""Module for Normal distribution"""


class Normal:
    """Represents a Normal distribution"""

    def __init__(self, data=None, mean=0., stddev=1.):
        """
        Initializes Normal distribution

        Args:
            data: list of data to estimate the distribution
            mean: the mean of the distribution
            stddev: the standard deviation of the distribution
        """
        if data is not None:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = float(sum(data) / len(data))
            variance = sum((x - self.mean) ** 2 for x in data) / len(data)
            self.stddev = float(variance ** 0.5)
        else:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)

    def z_score(self, x):
        """
        Calculates the z-score of a given x-value

        Args:
            x: the x-value

        Returns:
            the z-score of x
        """
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """
        Calculates the x-value of a given z-score

        Args:
            z: the z-score

        Returns:
            the x-value of z
        """
        return self.mean + z * self.stddev
