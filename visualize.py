import matplotlib.pyplot as plt
import numpy as np

# Load point cloud data
data_file = "mesh.dat"  # Adjust the path if needed
data = np.loadtxt(data_file, skiprows=1)

print(data)

# Extract x and y coordinates
x = data[:, 0]
y = data[:, 1]

'''
# Plot the points
plt.figure(figsize=(8, 6))
plt.scatter(x, y, s=10, color="blue", label="Point Cloud")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Point Cloud Visualization")
plt.legend()
plt.grid(True)
plt.show()
'''
