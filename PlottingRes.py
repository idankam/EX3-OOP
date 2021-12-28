import matplotlib.pyplot as plt
import numpy as np


labels = ['Load', 'Save', 'Center', 'Tsp','shortestPath']
python_means = [0.001, 0.003, 0.0009, 0.00099]
java_means = [0.069, 0.0295, 0.003, 0.0010]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, python_means, width, label='Python')
rects2 = ax.bar(x + width/2, java_means, width, label='Java')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('seconds')
ax.set_title('A1 Graph')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()



