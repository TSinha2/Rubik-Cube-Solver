import cv2

# Function to draw a square in the center of the frame
def draw_square(frame):
    height, width, _ = frame.shape
    square_size = min(height, width) // 4  # Modify this value to adjust the square size
    square_thickness = 2
    square_color = (0, 0, 0)  # Green color

    # Calculate the top-left corner of the square
    top_left_x = (width // 2) - (square_size // 2)
    top_left_y = (height // 2) - (square_size // 2)

    # Draw the square
    cv2.rectangle(frame, (top_left_x, top_left_y), (top_left_x + square_size, top_left_y + square_size),
                  square_color, square_thickness)

    # Return the square region
    return frame[top_left_y:top_left_y + square_size, top_left_x:top_left_x + square_size]

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Check if the frame was successfully captured
    if not ret:
        break

    # Draw the square on the frame
    square_frame = draw_square(frame)

    # Display the frame with the square
    cv2.imshow("Webcam", frame)

    # Check for the 'q' key to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Check if the square frame is not empty
    if square_frame.size != 0:
        # Display the cropped square frame
        cv2.imshow("Cropped Frame", square_frame)

        # Save the cropped square frame
        cv2.imwrite("cropped_frame.png", square_frame)

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
