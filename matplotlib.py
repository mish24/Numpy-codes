import pandas
import matplotlib.pyplot as plt
"""
fig = plt.figure(figsize=(5,7))
ax = fig.add_subplot(1,1,1)
# ax2 = fig.add_subplot(2,3,1)
ax.set_xlim([0,14])
ax.set_ylim([5,20])
plt.show()
# Print the types
print(type(fig))
print(type(ax))
"""

#######################

import numpy as np
"""
month = [1,1,2,2,4,5,5,7,8,10,10,11,12,12]
temperature = [32,15,40,35,50,55,52,80,85,60,57,45,35,105]
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xlim([np.min(month),np.max(month)])
ax.set_ylim([np.min(temperature), np.max(temperature)])
color = 'darkblue'
marker = "*"
plt.xlabel("aa")
ax.set_ylabel("temp")
# run the .scatter() method, params: color, marker
ax.scatter(month, temperature, color=color, marker=marker)
plt.show()
"""
import numpy as np

month = [1,1,2,2,4,5,5,7,8,10,10,11,12,12]
temperature = [32,15,40,35,50,55,52,80,85,60,57,45,35,105]

fig = plt.figure()
ax = fig.add_subplot(3,3,1)
ax2 = fig.add_subplot(3,3,9)
ax.set_xlim([np.min(month)-1,np.max(month)+1])
ax.set_ylim([np.min(temperature)-5, np.max(temperature)+5])

color = 'darkblue'
marker = 'o'
ax.set_xlabel("Month")
ax.set_ylabel("Temperature")
ax.set_title( "Year Round Temperature" )
ax2.set_title("pagal dara")

# run the .scatter() method, params: color, marker
ax.scatter(month, temperature, color='darkblue', marker='o')
# plt.show()



############

file = pandas.read_csv("avengers.csv")
# print file.head(5)
joined = int()
correct = file[file['Years since joining'] == (2015-file['Year']) ]
print correct
