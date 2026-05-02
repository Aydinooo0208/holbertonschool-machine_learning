#!/usr/bin/env python3
"""Function that concatenates two numpy arrays along a specific axis"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Returns a new numpy ndarray of mat1 and mat2 concatenated"""
    return np.concatenate((mat1, mat2), axis=axis)
