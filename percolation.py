import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
sys.setrecursionlimit(10000)
sns.set()

def newgrid(p,N=100):
    """create new grid of N by N with probability of p

    Args:
        p (float): probability
        N (int): number of grid to 100.

    Returns:
        2d_array: 0 or 1 with probability p
    """
    return np.random.choice(2 ,p=[1-p, p], size=(N,N))

def walk(m, n, grid, nwalk):
    """walk for percolation

    Args:
        m (int): mth column
        n (int): nth row
        grid (2d_array): 
        nwalk (int): number of component
    """
    
    N = len(grid)
    # fill grid 
    grid[n][m] = nwalk
    
    #check right
    if m < N - 1 and grid[n][m + 1] == 1:
        walk(m+1, n, grid, nwalk)

    #check left
    if m and grid[n][m - 1] == 1:
        walk(m-1, n, grid, nwalk)

    #check down
    if n < N - 1 and grid[n+1][m] == 1:
        walk(m, n+1, grid, nwalk)
    
    #check up
    if n and grid[n-1][m] == 1:
        walk(m, n-1, grid, nwalk)

    elif n == N - 1:
        return print("percolated")

def check(grid):
    """check the grid for percolation from top

    Args:
        grid (2d_array):

    Returns:
        2d_array: percolated grid
    """
    M = len(grid)
    nwalk = 1
    for m in range(M):
        if grid[0,m] == 1:
            nwalk +=1
            walk(m,0, grid, nwalk)
    return grid

def CountFrequency(my_list):
    """count frequency of the list

    Args:
        my_list (list): list of data

    Returns:
        dictinary: a dictionary that keys are items in list and its values are frequency of items
    """

    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
    return freq


if __name__ == "__main__":
    p = 0.57
    grid = newgrid(p)
    grid = check(grid)
    size = CountFrequency(grid.flatten())
    size.pop(0)
    size.pop(1)
    maxsize = max(size.values())
    plt.figure(figsize=(10,10))
    sns.heatmap(grid, cbar=False, cmap="viridis", yticklabels=False, xticklabels=False)
    plt.title(f"Percolation Simulation for p = {p}, size of giant component : {maxsize}")
    plt.savefig("percolation")