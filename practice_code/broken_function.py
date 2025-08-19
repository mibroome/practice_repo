import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from practice_code.another_function import wrapper_for_yet_another_function

ax = plt.figure().add_subplot(projection='3d')
X_start, Y_start, Z_start = axes3d.get_test_data(0.05)

X, Y, Z = wrapper_for_yet_another_function(X_start, Y_start, Z_start)

# Plot the 3D surface
ax.plot_surface(X, Y, Z, edgecolor='royalblue', lw=0.5, rstride=8, cstride=8,
                alpha=0.3)

# Plot projections of the contours for each dimension.  By choosing offsets
# that match the appropriate axes limits, the projected contours will sit on
# the 'walls' of the graph
ax.contourf(X, Y, Z, zdir='z', offset=-100, cmap='coolwarm')
ax.contourf(X, Y, Z, zdir='x', offset=-40, cmap='coolwarm')
ax.contourf(X, Y, Z, zdir='y', offset=40, cmap='coolwarm')

ax.set(xlim=(-40, 40), ylim=(-40, 40), zlim=(-100, 100),
       xlabel='X', ylabel='Y', zlabel='Z')

plt.show()