import warnings
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt
import pandas as pd


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

def education_budget(year):
    df = pd.read_csv("national-budget.csv")
    df = df[df['שם רמה 2'] == 'חינוך']
    df = df[df['שנה'] == year]
    return df['הוצאה נטו'].sum()


print(education_budget(1999))
print(education_budget(2004))
print(education_budget(2009))
print(education_budget(2016))


def security_budget_ration(year):
    df = pd.read_csv("national-budget.csv")
    df = df[df['שנה'] == year]
    total = 0
    for office in df['שם רמה 2'].unique():
        tmp = df[df['שם רמה 2'] == office]
        total += tmp['הוצאה נטו'].sum()
    df = df[(df['שם רמה 2'] == 'בטחון') | (df['שם רמה 2'] == 'בטחון פנים') | (df['שם רמה 2'] == 'בטחון-אחר')]
    return df['הוצאה נטו'].sum() / total


print(security_budget_ration(1997))
print(security_budget_ration(2000))
print(security_budget_ration(2003))
print(security_budget_ration(2010))
print(security_budget_ration(2017))


def largest_budget_year(office):
    df = pd.read_csv("national-budget.csv")
    df = df[df['שם רמה 2'] == office]
    budgets = []
    for year in df['שנה'].unique():
        tmp = df[df['שנה'] == year]
        budgets.append([tmp['הוצאה נטו'].sum(), year])
    dfb = pd.DataFrame(budgets, columns=['budget','year'])
    dfb = dfb[dfb['budget'] == dfb['budget'].max()]
    return dfb['year'].max()


print(largest_budget_year('בטחון'))
print(largest_budget_year('חינוך'))
print(largest_budget_year('בריאות'))


def smallest_yearly_budget(office):  # return the smallest budget of the given office
    df = pd.read_csv("national-budget.csv")
    df = df[df['שם רמה 2'] == office]
    budgets = []
    for year in df['שנה'].unique():
        tmp = df[df['שנה'] == year]
        budgets.append(tmp['הוצאה נטו'].sum())
    dfb = pd.DataFrame(budgets, columns=["budget"])
    return dfb["budget"].min()


print(smallest_yearly_budget('בטחון'))
print(smallest_yearly_budget('חינוך'))
print(smallest_yearly_budget('בריאות'))

# 3)
# https://www.codingame.com/training/hard/death-first-search-episode-2
