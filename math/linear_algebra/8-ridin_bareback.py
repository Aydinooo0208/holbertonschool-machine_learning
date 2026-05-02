#!/usr/bin/env python3
"""Function that performs matrix multiplication"""


def mat_mul(mat1, mat2):
    """Returns the product of two 2D matrices, or None if incompatible"""
    if len(mat1[0]) != len(mat2):
        return None
    return [[sum(mat1[i][k] * mat2[k][j] for k in range(len(mat2)))
             for j in range(len(mat2[0]))]
            for i in range(len(mat1))]
