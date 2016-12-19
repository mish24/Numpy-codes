import random
import numpy as np
import matplotlib.pyplot as plt
 
print("\nCoin Flip Simulator by AKP")
 
def prob_heads(coin_heads,k):
        prob = float(coin_heads)/float(k)
        return prob
 
target = open("coinsim.txt", 'w+')
 
k = int(input("\n\n\nHow many times you want to flip the coin? > "))
 
l = int(input("\n\n\nHow many times you want to conduct this experiment? > "))
 
experimentdone = 1
 
while experimentdone < l+1:
 
        coin_heads, coin_tails, times_flipped = 0, 0, 0
 
        timesflipped = 0  
        while timesflipped < k:
                coin_flips = random.randrange( 2 )
                if coin_flips == 0:
                        coin_heads += 1
                else:
                        coin_tails += 1
                timesflipped += 1
        print("\n" + "Out of %d flips, "%k + str(coin_heads) + " were heads and " + str(coin_tails) + " were tails.")
        target.write("\n%d %f" %(experimentdone,prob_heads(coin_heads,k)))
        experimentdone += 1
target.close()
 
content = [line.rstrip('\n') for line in open("coinsim.txt",'r')]
m = len(content)
 
x = []
y = []
     
for i in range(1,m):
         k = content[i].split()
         x.append(k[0])
         y.append(k[1])
 
plt.scatter(x, y)
plt.xlabel('Experiments')
plt.ylabel('Probability of getting head')
plt.title('Coin Simulation Graph')
plt.show()
