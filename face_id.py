import cv2
import numpy as np
from scipy.spatial import distance


class FaceID:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.NUM_CLUSTERS = 1
        self.NUM_COLORS = 6
        self.colors_list = []
        self.names = ['white', 'yellow', 'blue', 'green', 'red', 'orange']
        self.grid_size = 180
        self.grid_rows = 3
        self.grid_cols = 3
        self.line_thickness = 1

    def __del__(self):
        self.cap.release()
        cv2.destroyAllWindows()

    def perform_clustering(self, image):
        pixels = np.float32(image.reshape(-1, 3))
        _, labels, centers = cv2.kmeans(pixels, self.NUM_CLUSTERS, None,
                                        criteria=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0),
                                        attempts=10, flags=cv2.KMEANS_RANDOM_CENTERS)
        center_colors = np.round(centers).astype(np.uint8)
        return center_colors[0]

    def find_closest_color(self, target_color):
        target_color_2d = target_color.reshape(1, -1)
        reference_colors_2d = self.colors_list.reshape(len(self.colors_list), -1)
        distances = distance.cdist(target_color_2d, reference_colors_2d)
        closest_color_index = np.argmin(distances)
        closest_color = self.names[closest_color_index]
        return closest_color

    def get_face(self, color):
        while True:
            ret, frame = self.cap.read()
            height, width, _ = frame.shape
            grid_x = int((width - self.grid_size) / 2)
            grid_y = int((height - self.grid_size) / 2)

            for i in range(1, self.grid_rows):
                y = grid_y + int((i / self.grid_rows) * self.grid_size)
                cv2.line(frame, (grid_x, y), (grid_x + self.grid_size, y), (0, 0, 0), self.line_thickness)

            for i in range(1, self.grid_cols):
                x = grid_x + int((i / self.grid_cols) * self.grid_size)
                cv2.line(frame, (x, grid_y), (x, grid_y + self.grid_size), (0, 0, 0), self.line_thickness)

            cv2.imshow('Capture Grid', frame)

            key = cv2.waitKey(1)
            if key == ord('q'):
                grid_roi = frame[grid_y:grid_y + self.grid_size, grid_x:grid_x + self.grid_size]
                cv2.imwrite(color + '.png', grid_roi)
                break

    def face_color(self, color):
        self.get_face(color)
        image = cv2.imread(color + '.png')

        row1 = [[(0, 0), (60, 60)], [(60, 0), (120, 60)], [(120, 0), (180, 60)]]
        row2 = [[(0, 60), (60, 120)], [(60, 60), (120, 120)], [(120, 60), (180, 120)]]
        row3 = [[(0, 120), (60, 180)], [(60, 120), (120, 180)], [(120, 120), (180, 180)]]
        rows = [row1, row2, row3]

        face_state = ""
        for row in rows:
            for i in row:
                top_right = i[0]
                bottom_left = i[1]
                roi = image[top_right[1]:bottom_left[1], top_right[0]:bottom_left[0]]
                target_color = self.perform_clustering(roi)
                closest_color = self.find_closest_color(target_color)
                face_state += closest_color[0]

        return face_state

    def get_cube_state(self, color):
        self.colors_list = np.array(self.get_six_colors())
        cube_state = ""
        for c in color:
            cube_state += self.face_color(c)
        return cube_state

    def get_six_colors(self):
        color_identified = 0
        identified_colors = []

        while True:
            _, frame = self.cap.read()
            height, width, _ = frame.shape
            center_x = int(width / 2)
            center_y = int(height / 2)
            square_size = 20
            top_left = (center_x - int(square_size / 2), center_y - int(square_size / 2))
            bottom_right = (center_x + int(square_size / 2), center_y + int(square_size / 2))
            cv2.rectangle(frame, top_left, bottom_right, (0, 0, 0), 1)
            cv2.imshow('Live Webcam', frame)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break
            elif key == ord('c'):
                square_roi = frame[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
                identified_color = self.perform_clustering(square_roi)
                identified_colors.append(identified_color)
                color_identified += 1
                if color_identified == self.NUM_COLORS:
                    identified_colors_squares = np.full((50, 50 * self.NUM_COLORS, 3), 255, dtype=np.uint8)
                    for i, color in enumerate(identified_colors):
                        identified_color_square = np.full((50, 50, 3), color, dtype=np.uint8)
                        identified_colors_squares[:, i * 50:(i + 1) * 50, :] = identified_color_square
                    cv2.imshow('Identified Colors', identified_colors_squares)
                    cv2.waitKey(0)

                    return identified_colors


face_id = FaceID()
cube_state = face_id.get_cube_state(['white'])
print(cube_state)
