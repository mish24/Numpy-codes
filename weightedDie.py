#this program is the description of how cumulative probabilites work in numpy
import numpy as np
from collections import Counter


def find_interval(x, partition):
    """ find_interval -> i
        partition is a sequence of numerical values
        x is a numerical value
        The return value "i" will be the index for which applies
        partition[i] < x < partition[i+1], if such an index exists.
        -1 otherwise
    """
    
    for i in range(0, len(partition)):
        if x < partition[i]:
            return i-1
    return -1

def weighted_choice(sequence, weights):
 """
 weighted_choice selects a random element of the sequence according to the list of weights
 """
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


