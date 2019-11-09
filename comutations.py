from array import *
from math import *
from tkinter import *
from matplotlib import pyplot as plt
import numpy as np

def run(par1_var, par2_var, par3_var):










    def globalError(gi, f):
        glob = [0]*(gi-2)
        for ji in range(2, gi):
            xi, hi = get_x_h(ji)
            glob[ji-2] = abs(f(ji)[-1] - exactSol(xi)[-1])
        return glob

    def plot(xi, yi, line='r-', label="euler", x_axis='x'):
        plt.plot(np.array(xi), np.array(yi), line, alpha=0.7, label=label, ms=1)
        plt.xlabel(x_axis)
        plt.ylabel('y')
        plt.grid(True)

    y = exactSol(x)
    ye = euler(i)
    ye2 = impEuler(i)
    yr = rungeKutta(i)


    figure = plt.figure(figsize=(11, 4))

    plt.subplot(131)
    plt.title('Approximation')
    plot(x, y, 'ks', 'exact solution')
    plot(x, ye, 'g-', 'euler')
    plot(x, ye2, 'r-', 'improved euler')
    plot(x, yr, 'b--', 'rk')
    plt.legend()

    plt.subplot(132)
    plt.title('Local errors')

    leu = localErrorEuler(x, y)
    leu2 = localErrorImpEuler(x, y)
    lrk = localErrorRungeKutta(x, y)

    plot(x, leu, 'g-', 'euler')
    plot(x, leu2, 'r-', 'improved euler')
    plot(x, lrk, 'b--', 'rk')
    plt.legend()
    plt.subplot(133)

    globeu = globalError(i, euler)
    globeu2 = globalError(i, impEuler)
    globeu3 = globalError(i, rungeKutta)

    plt.title('Global errors')
    plot(list(range(2, i)), globeu, 'g-', 'euler', 'n')
    plot(list(range(2, i)), globeu2, 'r-', 'improved euler', 'n')
    plot(list(range(2, i)), globeu3, 'b--', 'rk', 'n')
    plt.legend()
    #plt.show()
    figure.tight_layout()
    return figure
