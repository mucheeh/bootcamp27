#!/bin/python
from __future__ import division
import sys

n = int(raw_input().strip())
vec = [0, 0, 0]
for h in map(int,raw_input().strip().split(' ')):
    if h > 0:
        vec[0] += 1
    elif h < 0:
        vec[1] += 1
    else:
        vec[2] += 1

print vec[0]/n
print vec[1]/n
print vec[2]/n
