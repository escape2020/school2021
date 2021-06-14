# flake8: noqa
kdtree = spatial.cKDTree(points)

target_point = [0.5, 0.5, 0.5]
indices = kdtree.query_ball_point(target_point, r=0.1)
points[indices]
