A quick implementation and visualization of the vanilla Iterative Closest Point algorithm which is used in point cloud registration. To learn more about ICP, check out the following link:
https://cs.gmu.edu/~kosecka/cs685/cs685-icp.pdf

## Current Issues
The rotation matrix returned is pretty accurate; however, the translation vector is off. My best guess is that it has something to do with how Numpy handles singular value decomposition
because the code behaves as expected until the SVD function is called.
