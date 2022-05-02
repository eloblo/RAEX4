import warnings

import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt


# 1)

def plotIntersection(line_space, f, g):
    plt.plot(line_space, f(line_space))
    plt.plot(line_space, g(line_space))
    h = lambda x: f(x) - g(x)    # the intersections are the roots of h(x)
    roots = set()
    for i in line_space:
        with warnings.catch_warnings(record=True) as w:  # check if there are roots
            res = opt.fsolve(h, i)
            if len(w) == 0:
                roots.add(round(res[0], 10))   # add unique roots
    for i in roots:
        plt.scatter(i, f(i), color="red")
    plt.show()


plotIntersection(np.linspace(-10, 10, 1000), lambda x: x**2, lambda x: x+10)
plotIntersection(np.linspace(-10, 10, 1000), lambda x: np.cos(x), lambda x: 0.1*x)
plotIntersection(np.linspace(-10, 10, 1000), lambda x: (x-1)*(x+2)*(x-5)*(x+7), lambda x: x)
plotIntersection(np.linspace(-10, 10, 1000), lambda x: -x, lambda x: x)
plotIntersection(np.linspace(-10, 10, 1000), lambda x: x+10, lambda x: x)

# 2)


# 3)
# https://www.codingame.com/training/hard/death-first-search-episode-2
