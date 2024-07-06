import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

### TO DO: Code to generate test dataset
def generate_initial_points(num_points):
    initial_points = np.random.rand(num_points, 3) * 100 # Points in a 100 x 100 x 100 cube
    return initial_points

def generate_transformed_points(initial_points, rotation_matrix, translation_vector):
    transformed_points = np.dot(initial_points, rotation_matrix.T) + translation_vector
    return transformed_points

def generate_rotation_matrix(angle):
    cos_angle = np.cos(angle)
    sin_angle = np.sin(angle)
    rotation_matrix = np.array([
        [cos_angle, -sin_angle, 0],
        [sin_angle, cos_angle, 0],
        [0, 0, 1]])
    
    return rotation_matrix

def plot_points(points, color):
    fig = plt.figure(figsize = (10, 7))
    ax = plt.axes(projection ="3d")

    x = points[:, 0]
    y = points[:, 1]
    z = points[:, 2]
    
    ax.scatter3D(x, y, z,  color = color)
    plt.title("3D Scatter Plot")
    
    plt.show() 

num_points = 100
initial_points = generate_initial_points(num_points)
angle = np.pi/4
rotation_matrix = generate_rotation_matrix(angle)
translation_vector = np.array([12, 10, 5])
transformed_points = generate_transformed_points(initial_points, rotation_matrix, translation_vector)

x_n = initial_points
y_n = transformed_points

plot_points(x_n, "green")
plot_points(y_n, "blue")

y_0 = np.mean(y_n , axis = 0)
x_0 = np.mean(x_n, axis = 0)

a = y_n - y_0
print(a.shape)

H = (y_n - y_0).T @ (x_n - x_0)
print((y_n - y_0).shape)

U, S, V_T = np.linalg.svd(H)

D = np.diag(S)

R = V_T.T @ U.T
t = y_0 - np.dot(R , x_0)

print(rotation_matrix)
print(f'The rotation matrix is {R} ; translation vector is {t}')

predicted_points = generate_transformed_points(x_n, R, t)
plot_points(predicted_points, "red")