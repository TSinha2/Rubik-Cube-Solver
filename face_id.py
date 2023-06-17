import cv2
import numpy as np
from scipy.spatial import distance


# Set up the webcam
cap = cv2.VideoCapture(0)

# Constants for k-means clustering
NUM_CLUSTERS = 1
NUM_COLORS = 6

# Initialize variables for color identification
# color_identified = 0
# identified_colors = []

# Function to perform k-means clustering
def perform_clustering(image):
    # Convert image to float32 for k-means clustering
    pixels = np.float32(image.reshape(-1, 3))

    # Perform k-means clustering
    _, labels, centers = cv2.kmeans(pixels, NUM_CLUSTERS, None, criteria=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0), attempts=10, flags=cv2.KMEANS_RANDOM_CENTERS)

    # Get the RGB values of the cluster centers
    center_colors = np.round(centers).astype(np.uint8)

    return center_colors[0]

def get_six_colors():
    color_identified = 0
    identified_colors = []

    while True:
        # Capture frame from the webcam
        _, frame = cap.read()

        # Get the dimensions of the frame
        height, width, _ = frame.shape

        # Calculate the center coordinates for the color region
        center_x = int(width / 2)
        center_y = int(height / 2)

        # Draw unfilled black square at the center
        square_size = 20
        top_left = (center_x - int(square_size / 2), center_y - int(square_size / 2))
        bottom_right = (center_x + int(square_size / 2), center_y + int(square_size / 2))
        cv2.rectangle(frame, top_left, bottom_right, (0, 0, 0), 1)

        # Display the frame
        cv2.imshow('Live Webcam', frame)

        # Check for key press
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('c'):
            # Extract the square region and perform k-means clustering
            square_roi = frame[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
            identified_color = perform_clustering(square_roi)

            # Add the identified color to the list
            identified_colors.append(identified_color)
            color_identified += 1

            # Check if all colors have been identified
            if color_identified == NUM_COLORS:
                return identified_colors



identified_colors = get_six_colors()

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
    print("THE COLOR IS " + names[closest_color_index])
    return names[closest_color_index]
    #return closest_color


# Display the identified colors
identified_colors_squares = np.full((50, 50 * NUM_COLORS, 3), 255, dtype=np.uint8)
for i, color in enumerate(identified_colors):
    identified_color_square = np.full((50, 50, 3), color, dtype=np.uint8)
    identified_colors_squares[:, i * 50:(i + 1) * 50, :] = identified_color_square
cv2.imshow('Identified Colors', identified_colors_squares)
cv2.waitKey(0)

# Store the identified colors as a list of RGB values
colors_list = np.array(identified_colors)
names = ['white', 'yellow', 'blue', 'green', 'red', 'orange']

# print(colors_list)
for i in range(6):
    print(names[i] + ': ' + str(colors_list[i]))

# Release the webcam and destroy the windows
cap.release()
cv2.destroyAllWindows()



# def display_color(color):
#     color_image = np.zeros((100, 100, 3), np.uint8)
#     color_image[:] = color
#     cv2.imshow("Target Color", color_image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# Perform color extraction using k-means clustering
# display_color(target_color)

def get_face(color):
    # Set up the webcam
    cap = cv2.VideoCapture(0)

    # Constants for grid dimensions
    grid_size = 180
    grid_rows = 3
    grid_cols = 3
    line_thickness = 1

    while True:
        # Capture frame from the webcam
        ret, frame = cap.read()

        # Get the dimensions of the frame
        height, width, _ = frame.shape

        # Calculate the top-left corner coordinates of the grid
        grid_x = int((width - grid_size) / 2)
        grid_y = int((height - grid_size) / 2)

        # Draw the grid lines within the grid region
        for i in range(1, grid_rows):
            # Draw horizontal lines
            y = grid_y + int((i / grid_rows) * grid_size)
            cv2.line(frame, (grid_x, y), (grid_x + grid_size, y), (0, 0, 0), line_thickness)

        for i in range(1, grid_cols):
            # Draw vertical lines
            x = grid_x + int((i / grid_cols) * grid_size)
            cv2.line(frame, (x, grid_y), (x, grid_y + grid_size), (0, 0, 0), line_thickness)

        # Display the frame
        cv2.imshow('Capture Grid', frame)

        # Check for key press
        key = cv2.waitKey(1)
        if key == ord('q'):
            # Extract the grid region from the frame
            grid_roi = frame[grid_y:grid_y + grid_size, grid_x:grid_x + grid_size]

            # Save the grid image as color.png
            cv2.imwrite(color + '.png', grid_roi)

            break

    # Release the webcam and destroy the window
    cap.release()
    cv2.destroyAllWindows()


def face_color(color):
    get_face(color)
    image = cv2.imread(color+'.png')

    row1 = [ [(0,0), (60,60)],   [(60, 0), (120,60)],  [(120, 0), (180, 60)]   ]
    row2 = [ [(0,60), (60,120)],   [(60, 60), (120,120)],  [(120, 60), (180, 120)]   ]
    row3 = [ [(0,120), (60,180)],   [(60, 120), (120,180)],  [(120, 120), (180, 180)]   ]
    rows = [row1, row2, row3]

    colors = ""
    for row in rows:
        for i in row:
            top_right = i[0]
            bottom_left = i[1]
            roi = image[top_right[1]:bottom_left[1], top_right[0]:bottom_left[0]]
            target_color = perform_clustering(roi)
            closest_color = find_closest_color(target_color, colors_list)
            colors += closest_color[0]
    
    return colors



# closest_color = find_closest_color(target_color, colors_list)
# print(f"Closest color: {closest_color}")

cube_state = ""
for color in names:
    cube_state += face_color(color)

print(cube_state)