#a game similar to german lottery using numPy
import numpy as np
from collections import Counter

def find_interval(x, partition):
 for i in range(0, len(partition)):
  if x< partition[i]:
   return i-1
 return -1

"""I = [0, 3, 5, 7.8, 9, 12, 13.8, 16]
for x in [-1.3, 0, 0.1, 3.2, 5, 6.2, 7.9, 10.8, 13.9, 15, 16, 16.5]:
    print(find_interval(x, I))"""

def weighted_choice(sequence, weights):
 x=np.random.random()
 cum_weights= [0] + list(np.cumsum(weights))
 index= find_interval(x, cum_weights)
 return sequence[index]

faces_of_die = [1, 2, 3, 4, 5, 6]
weights = [1/12, 1/6, 1/6, 1/6, 1/6, 3/12]
outcomes = []
n = 10000
for _ in range(n):
    outcomes.append(weighted_choice(faces_of_die, weights))
c = Counter(outcomes)
for key in c:
    c[key] = c[key] / n
    
print(sorted(c.values()))


