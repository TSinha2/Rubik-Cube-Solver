import cv2
import numpy as np
from scipy.spatial import distance



# Function to draw a 3x3 grid in the center of the frame
def draw_grid(frame):
    height, width, _ = frame.shape
    grid_size = min(height, width) // 4  # Modify this value to adjust the grid size
    square_size = grid_size // 3
    grid_thickness = 2
    grid_color = (0, 0, 0)  # Green color

    # Calculate the top-left corner of the grid
    top_left_x = (width // 2) - (grid_size // 2)
    top_left_y = (height // 2) - (grid_size // 2)

    # Draw the grid
    for i in range(3):
        for j in range(3):
            start_x = top_left_x + (j * square_size)
            start_y = top_left_y + (i * square_size)
            end_x = start_x + square_size
            end_y = start_y + square_size
            cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), grid_color, grid_thickness)

    # Return the grid region
    return frame[top_left_y:top_left_y + grid_size, top_left_x:top_left_x + grid_size]

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Check if the frame was successfully captured
    if not ret:
        break

    # Draw the grid on the frame
    grid_frame = draw_grid(frame)

    # Display the frame with the grid
    cv2.imshow("Webcam", frame)

    # Check for the 'q' key to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Check if the grid frame is not empty
    if grid_frame.size != 0:
        # Display the cropped grid frame
        cv2.imshow("Cropped Frame", grid_frame)

        # Save the cropped grid frame
        cv2.imwrite("cropped_frame.png", grid_frame)

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()

def most_frequent_color(image):
    pixels = np.float32(image.reshape(-1, 3))
    n_colors = 100  # Number of dominant colors to extract
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, 0.1)
    _, labels, centers = cv2.kmeans(pixels, n_colors, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    counts = np.bincount(labels.flatten())
    most_frequent_label = np.argmax(counts)
    most_frequent_color = centers[most_frequent_label]
    return most_frequent_color

# Function to find the closest color
def find_closest_color(target_color, reference_colors):
    target_color_2d = target_color.reshape(1, -1)
    reference_colors_2d = reference_colors.reshape(len(reference_colors), -1)
    distances = distance.cdist(target_color_2d, reference_colors_2d)
    closest_color_index = np.argmin(distances)
    closest_color = reference_colors[closest_color_index]
    print(closest_color_index)
    return closest_color
# Load the image
image = cv2.imread("cropped_frame.png")

# Specify the top-right and bottom-left coordinates of the ROI
top_right = (80, 80)
bottom_left = (100, 100)

# Display the ROI on the image
# cv2.rectangle(image, top_right, bottom_left, (255, 0, 0), 2)

# Extract the ROI
roi = image[top_right[1]:bottom_left[1], top_right[0]:bottom_left[0]]

# Calculate the most frequently occurring color in the ROI
most_frequent = most_frequent_color(roi)
most_frequent = np.uint8([[most_frequent]])

# Reference colors
reference_colors = np.array([[255, 0, 0],    # Red
                             [0, 255, 0],    # Green
                             [0, 0, 255],    # Blue
                             [255, 255, 0],  # Yellow
                             [255, 255, 255],  # White
                             [255, 165, 0]])  # Orange


# Find the closest color to the most frequent color
closest_color = find_closest_color(most_frequent, reference_colors)

# Create a small image to display the most frequent color and the closest color
# Create a small image to display the most frequent color and the closest color
color_display = np.zeros((100, 200, 3), np.uint8)
color_display[:, :100] = np.tile(most_frequent, (100, 100, 1))
color_display[:, 100:] = np.tile(closest_color, (100, 100, 1))

# Display the original image with ROI, the most frequent color, and the closest color
cv2.imshow("Image", image)
cv2.imshow("ROI", roi)
cv2.imshow("Most Frequent Color and Closest Color", color_display)
cv2.waitKey(0)
cv2.destroyAllWindows()
