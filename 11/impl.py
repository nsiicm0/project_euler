#!/bin/python3

import sys
from functools import reduce

def get_horizontal_four(subgrid, x=0):
    _h = subgrid[x]
    return _h

def get_vertical_four(subgrid, y=0):
    _v = []
    for row in subgrid:
        _v.append(row[y])
    return _v

def get_positive_diagonal_four(subgrid):
    _d = []
    for i, row in enumerate(subgrid):
        _d.append(row[len(row)-1 - i])
    return _d

def get_negative_diagonal_four(subgrid):
    _d = []
    for i, row in enumerate(subgrid):
        _d.append(row[i])
    return _d

def get_max_product(grid):
    combinations = []
    subgrid_dim = 4
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if len(grid[y])-x >= subgrid_dim and len(grid)-y >= subgrid_dim:
                subgrid = [el[x:x+subgrid_dim] for el in grid[y:y+subgrid_dim]]
                combinations.append(get_horizontal_four(subgrid))
                combinations.append(get_vertical_four(subgrid))
                combinations.append(get_positive_diagonal_four(subgrid))
                combinations.append(get_negative_diagonal_four(subgrid))
            elif len(grid[y])-x >= subgrid_dim:
                # no full matrix anymore but we can still grab horizontal
                combinations.append(get_horizontal_four(subgrid, y % subgrid_dim))
            elif len(grid)-y >= subgrid_dim:
                # no full matrix anymore but we can still grab vertical
                combinations.append(get_vertical_four(subgrid, x % subgrid_dim))
    combinations = filter(lambda c: 0 not in c and len(c) == 4, combinations)
    max_prod = 0
    for combination in combinations:
        _product = reduce(lambda x,y: x*y, combination)
        max_prod = _product if _product > max_prod else max_prod
    return max_prod
            

grid = []
for grid_i in range(20):
	grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
	grid.append(grid_t)
print(get_max_product(grid))
