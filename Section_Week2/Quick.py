import numpy as np
import matplotlib.pyplot as plt

# QuickHull Implementation
def quickhull(points):
    def distance(p1, p2, p):
        # Perpendicular distance from point `p` to line formed by `p1` and `p2`
        return abs((p[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p[0] - p1[0]))

    def find_hull(points, p1, p2):
        if not points:
            return []
        # Find the farthest point
        farthest = max(points, key=lambda p: distance(p1, p2, p))
        points_left = [p for p in points if ccw(p1, farthest, p) > 0]
        points_right = [p for p in points if ccw(farthest, p2, p) > 0]
        return find_hull(points_left, p1, farthest) + [farthest] + find_hull(points_right, farthest, p2)

    def ccw(p, q, r):
        return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])

    points = sorted(points, key=lambda p: (p[0], p[1]))
    leftmost, rightmost = points[0], points[-1]

    upper = find_hull([p for p in points if ccw(leftmost, rightmost, p) > 0], leftmost, rightmost)
    lower = find_hull([p for p in points if ccw(rightmost, leftmost, p) > 0], rightmost, leftmost)

    return np.array([leftmost] + upper + [rightmost] + lower)

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
    plt.plot(hull[:, 0], hull[:, 1], color="yellow", label="Convex Hull")

    # Customize plot
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Convex Hull Using QuickHull")
    plt.legend()
    plt.grid(True)

    # Save the plot as a file
    plt.savefig(filename, dpi=300)
    plt.close()  # Close the plot to free resources

# Main function to test QuickHull
if __name__ == "__main__":
    file_path = "mesh.dat"  # Update the path to your mesh.dat file
    points = load_data(file_path)

    hull = quickhull(points)
    print("Convex Hull Coordinates (QuickHull):")
    print(hull)

    # Save the output plot
    save_hull_plot(points, hull, "quickhull_hull.png")
    print("Convex hull plot saved as 'quickhull_hull.png'.")
