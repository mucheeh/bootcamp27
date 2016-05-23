#!/bin/python
def calculate_growth_cycle(height,cycle,max_cycle):

    if cycle > max_cycle or max_cycle == 0:
        return height
    else:
        if cycle % 2 == 1:
            height = 2*height
            return calculate_growth_cycle(height,cycle+1,max_cycle)
        else:
            height = height+1
            return calculate_growth_cycle(height,cycle+1,max_cycle)

for _ in xrange(input()):
    print calculate_growth_cycle(1,1,input())