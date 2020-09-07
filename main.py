import numpy as np
from math import tau
from scipy.special import binom

import matplotlib.pyplot as plt


def perimeter_bessel(a, b=1, k=10):
    h = (a-b)**2 / (a+b)**2
    return np.pi * (a + b) * [(binom(0.5, range(k)) ** 2 * v**np.arange(k)).sum() for v in h]
    
def perimeter_parker(a, b=1):
    return 3 * tau * (a / 5 + b / 8)    
    
def perimeter_jcop(a, b=1):
    return tau * (7/45 * a + 27/41 * np.sqrt((a**2 + b**2)/2) + 7/37 * b)

def main():
    space = np.linspace(1, 75, 500)

    parker = perimeter_parker(space)
    bessel = perimeter_bessel(space)
    jcop = perimeter_jcop(space)

    err_parker = np.abs(1 - parker / bessel) * 100
    err_jcop = np.abs(1 - jcop / bessel) * 100
    
    plt.figure(figsize=(12, 4))
    plt.subplot(121)
    plt.plot(space[:40], err_parker[:40], "k-", label="parker")
    plt.plot(space[:40], err_jcop[:40], "m-", label="jcop")
    plt.legend()
    
    plt.subplot(122)
    plt.plot(space, err_parker, "k-", label="parker")
    plt.plot(space, err_jcop, "m-", label="jcop")
    plt.legend()
    
    plt.tight_layout()
    plt.show()

    
if __name__ == "__main__":
    main()