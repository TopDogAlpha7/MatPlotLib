import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.transforms import Bbox
from numpy import size

plt.style.use('ggplot')

x_values = range(1, 50001)
y_values = [x**3 for x in x_values ]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=x_values, cmap=plt.cm.Reds, s=5)

ax.set_title("Coloured cubes", fontsize=15)
ax.set_xlabel("Number of squares", fontsize=15)
ax.set_ylabel("Squares", fontsize=15)

ax.tick_params(axis='both', which='major', labelsize=15)
ax.axis([0, 5500, 0, 166375000000])

plt.show()
plt.savefig('Coloured_Cubes.png', Bbox_inches= 'tight')