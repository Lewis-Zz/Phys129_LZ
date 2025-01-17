import numpy as np
import matplotlib.pyplot as plt

# Graham Scan Implementation
def graham_scan(points):
    def ccw(p, q, r):
        return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])

    points = sorted(points, key=lambda p: (p[0], p[1]))
    hull = []

    # Lower hull
    for p in points:
        while len(hull) >= 2 and ccw(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(tuple(p))

    # Upper hull
    for p in reversed(points):
        while len(hull) >= 2 and ccw(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(tuple(p))

    return np.array(hull[:-1])  # Remove the duplicate end point

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
    plt.plot(hull[:, 0], hull[:, 1], color="purple", label="Convex Hull")

    # Customize plot
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Convex Hull Using Graham Scan")
    plt.legend()
    plt.grid(True)

    # Save the plot as a file
    plt.savefig(filename, dpi=300)
    plt.close()  # Close the plot to free resources

# Main function to test Graham Scan
if __name__ == "__main__":
    file_path = "mesh.dat"  # Update the path to your mesh.dat file
    points = load_data(file_path)

    hull = graham_scan(points)
    print("Convex Hull Coordinates (Graham Scan):")
    print(hull)

    # Save the output plot
    save_hull_plot(points, hull, "graham_scan_hull.png")
    print("Convex hull plot saved as 'graham_scan_hull.png'.")
