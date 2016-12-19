#using numpy and explaining the use of gauss/random
import numpy as np
from random import gauss

n=1000
values = []
freq={}
while len(values) < n:
 value = gauss(550,30)
 if(130<value<230):
  freq[int(value)]= freq.get(int(value),0) + 1
  values.append(value)

print(valuea[:10])

