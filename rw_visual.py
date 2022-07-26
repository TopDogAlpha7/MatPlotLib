import matplotlib.pyplot as plt 

from randomwalks import RandomWalk

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10,6), dpi=128)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none',  s=1)
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',  s=100)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.plot(rw.x_values, rw.y_values, linewidth=1)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    keep_running.lower()
    if keep_running == 'n':
        break

