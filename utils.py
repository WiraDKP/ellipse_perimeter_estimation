import numpy as np
from scipy.special import binom
from math import factorial, tau


def perimeter_hm(a, b=1):
    return tau * (1/a + 1/b) / 2 

def perimeter_am(a, b=1):
    return tau * (a + b) / 2

def perimeter_gm(a, b=1):
    return tau * np.sqrt(a*b)

def perimeter_rms(a, b=1):
    return tau * np.sqrt((a**2 + b**2) / 2)

def perimeter_bessel(a, b=1, k=10):
    h = (a-b)**2 / (a+b)**2
    return np.pi * (a + b) * [(binom(0.5, range(k)) ** 2 * v**np.arange(k)).sum() for v in h]

def perimeter_parker(a, b=1):
    return 3 * tau * (a / 5 + b / 8)

def find_fractional_approx(target, max_error=0.0005):
    a = 1
    b = 1
    error = 1
    while error > max_error:
        if (a/b) > target:
            b += 1
        else:
            a += 1
        error = np.abs(target - a/b)
    return a, b