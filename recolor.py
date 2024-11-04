import random
from PIL import Image
import sys
import numpy as np

def load_image(image_path):
    """Load the image and convert it to a list of RGB pixels."""
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = list(img.getdata())  # Get pixel data as a list
    return pixels

def initialize_centroids(k, pixels):
    """Randomly select k unique pixels as initial centroids."""
    return random.sample(pixels, k)

def assign_clusters(pixels, centroids):
    """Assign each pixel to the closest centroid."""
    clusters = []
    for pixel in pixels:
        distances = [np.linalg.norm(np.array(pixel) - np.array(centroid)) for centroid in centroids]
        closest_centroid = distances.index(min(distances))
        clusters.append(closest_centroid)
    return clusters

def update_centroids(pixels, clusters, k):
    """Update centroids based on the assigned clusters."""
    new_centroids = []
    for i in range(k):
        cluster_pixels = [pixels[j] for j in range(len(pixels)) if clusters[j] == i]
        if cluster_pixels:
            new_centroid = np.mean(cluster_pixels, axis=0).astype(int)  # Calculate mean as new centroid
            new_centroids.append(tuple(new_centroid))
        else:
            new_centroids.append(random.choice(pixels))  # If a cluster has no pixels, randomly select a pixel
    return new_centroids

def k_means(pixels, k, max_iterations=100):
    """Run the k-means algorithm."""
    centroids = initialize_centroids(k, pixels)
    for _ in range(max_iterations):
        clusters = assign_clusters(pixels, centroids)
        new_centroids = update_centroids(pixels, clusters, k)

        # Check for convergence (if centroids don't change)
        if np.array_equal(new_centroids, centroids):
            break
        centroids = new_centroids

    return clusters, centroids

def recolor_image(input_image_path, output_image_path, k):
    """Recolor the image using k-means clustering."""
    pixels = load_image(input_image_path)
    clusters, centroids = k_means(pixels, k)

    # Create a new image with reduced colors
    new_pixels = [centroids[cluster] for cluster in clusters]
    new_image = Image.new("RGB", Image.open(input_image_path).size)
    new_image.putdata(new_pixels)
    new_image.save(output_image_path)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 recolor.py <input_image> <output_image> <k>")
        sys.exit(1)

    input_image_path = sys.argv[1]
    output_image_path = sys.argv[2]
    k = int(sys.argv[3])

    recolor_image(input_image_path, output_image_path, k)
    print(f"Recolored image saved as '{output_image_path}' with {k} colors.")
