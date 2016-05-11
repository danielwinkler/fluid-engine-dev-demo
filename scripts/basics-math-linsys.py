import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

import render

a = np.array([[2, -1], [-1, 2]])
b = np.array([3, 6])

def f(x):
    r = a.dot(x) - b
    return r.dot(r)

delta = 0.2
x = np.arange(-10.0, 20.0, delta)
y = np.arange(-10.0, 20.0, delta)
X, Y = np.meshgrid(x, y)

Z = np.zeros(X.shape)
for i in range(len(x)):
    for j in range(len(y)):
        Z[j][i] = f(np.array([x[i], y[j]]))

output_filename = 'basics-math-linsys-gd.pdf'
fig, ax = plt.subplots()
ax.set_xticks(())
ax.set_xticklabels(())
ax.set_yticks(())
ax.set_yticklabels(())
plt.contour(Z, 50, colors='k')
plt.savefig(output_filename)
plt.close(fig)
