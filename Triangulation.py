import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
import matplotlib.path as mpath

square = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])
polygon = np.array([[0.4, 0.4], [0.6, 0.4], [0.6, 0.6], [0.4, 0.6]])  # 例子中的内部多边形

points = np.vstack([square, polygon])
delaunay_tri = Delaunay(points)

path = mpath.Path(polygon)
include = np.zeros(len(delaunay_tri.simplices), dtype=bool)

for i, tri in enumerate(delaunay_tri.simplices):
    triangle_points = points[tri]
    centroid = np.mean(triangle_points, axis=0)
    include[i] = not path.contains_point(centroid)

plt.triplot(points[:, 0], points[:, 1], delaunay_tri.simplices[include], 'go-')
plt.plot(square[:, 0], square[:, 1], 'b-')
plt.plot(polygon[:, 0], polygon[:, 1], 'r-')
plt.show()
