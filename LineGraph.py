import matplotlib.pyplot as plt
from matplotlib import style
from numpy import size
plt.style.use('ggplot')


input_values = range(1, 1001)
squares = [x**2 for x in input_values]

fig, ax = plt.subplots()
ax.scatter(input_values, squares, c=input_values, cmap=plt.cm.Reds, s=10)


# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=14)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis= 'both', which= 'major', labelsize=14)

ax.axis([0, 1100, 0, 1100000])

plt.show()
