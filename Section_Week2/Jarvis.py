import numpy as np
import matplotlib.pyplot as plt

# Jarvis March Implementation
def jarvis_march(points):
    def ccw(p, q, r):
        return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])

    n = len(points)
    hull = []

    # Find the leftmost point
    leftmost = np.argmin(points[:, 0])
    p = leftmost

    while True:
        hull.append(points[p])
        q = (p + 1) % n
        for r in range(n):
            if ccw(points[p], points[q], points[r]) > 0:
                q = r
        p = q
        if p == leftmost:  # Completed the hull
            break

    return np.array(hull)

# Load the point cloud from mesh.dat
def load_data(file_path):
    points = np.loadtxt(file_path, skiprows=1)  # Adjust skiprows if there's a header
    return points

# Save the point cloud and convex hull plot
def save_hull_plot(points, hull, filename):
    plt.figure(figsize=(8, 6))

    # Plot original points
    plt.scatter(points[:, 0], points[:, 1], color="blue", label="Point Cloud", s=10)

    # Plot convex hull
    hull = np.vstack([hull, hull[0]])  # Close the loop for the hull
    plt.plot(hull[:, 0], hull[:, 1], color="green", label="Convex Hull")

    # Customize plot
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Convex Hull Using Jarvis March")
    plt.legend()
    plt.grid(True)

    # Save the plot as a file
    plt.savefig(filename, dpi=300)
    plt.close()  # Close the plot to free resources

# Main function to test Jarvis March
if __name__ == "__main__":
    file_path = "mesh.dat"  # Update the path to your mesh.dat file
    points = load_data(file_path)

    hull = jarvis_march(points)
    print("Convex Hull Coordinates (Jarvis March):")
    print(hull)

    # Save the output plot
    save_hull_plot(points, hull, "jarvis_march_hull.png")
    print("Convex hull plot saved as 'jarvis_march_hull.png'.")
