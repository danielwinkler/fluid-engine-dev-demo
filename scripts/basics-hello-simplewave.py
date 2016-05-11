import matplotlib.pyplot as plt
import numpy as np

height0 = np.load('manual_tests_output/HelloFluidSim/Run/data.#line2,0000,y.npy')
height1 = np.load('manual_tests_output/HelloFluidSim/Run/data.#line2,0150,y.npy')
height2 = np.load('manual_tests_output/HelloFluidSim/Run/data.#line2,0300,y.npy')
data_x = [x / float(len(height0)) for x in range(len(height0))]

fig, ax = plt.subplots()
plt.ylim([0, 1.0])
ax.set_xticks(())
ax.set_xticklabels(())
ax.set_yticks(())
ax.set_yticklabels(())
plt.plot(data_x, height0, color='k')
plt.savefig('basics-hello-simplewave0.pdf')
plt.close(fig)

fig, ax = plt.subplots()
plt.ylim([0, 1.0])
ax.set_xticks(())
ax.set_xticklabels(())
ax.set_yticks(())
ax.set_yticklabels(())
plt.plot(data_x, height1, color='k')
plt.savefig('basics-hello-simplewave1.pdf')
plt.close(fig)

fig, ax = plt.subplots()
plt.ylim([0, 1.0])
ax.set_xticks(())
ax.set_xticklabels(())
ax.set_yticks(())
ax.set_yticklabels(())
plt.plot(data_x, height2, color='k')
plt.savefig('basics-hello-simplewave2.pdf')
plt.close(fig)


height3 = np.load('manual_tests_output/HelloFluidSim/Run/data.#line2,0370,y.npy')
fig, ax = plt.subplots()
plt.ylim([0, 1.0])
ax.set_xticks(())
ax.set_xticklabels(())
ax.set_yticks(())
ax.set_yticklabels(())
plt.plot(data_x, height3, color='k')
plt.savefig('basics-hello-simplewave-properties0.pdf')
plt.close(fig)

height4 = np.load('manual_tests_output/HelloFluidSim/Run/data.#line2,0024,y.npy')
height5 = np.load('manual_tests_output/HelloFluidSim/Run/data.#line2,0028,y.npy')

fig, ax = plt.subplots()
plt.ylim([0, 1.0])
ax.set_xticks(())
ax.set_xticklabels(())
ax.set_yticks(())
ax.set_yticklabels(())
plt.plot(data_x, height4, color='k')
plt.plot(data_x, height5, '--', color='k')
plt.savefig('basics-hello-simplewave-move0.pdf')
plt.close(fig)

fig, ax = plt.subplots()
plt.ylim([0, 1.0])
ax.set_yticks(())
ax.set_yticklabels(())
plt.plot(data_x, height4, color='k')
plt.plot(data_x, height5, '--', color='k')
plt.savefig('basics-hello-simplewave-heightf0.pdf')
plt.close(fig)
