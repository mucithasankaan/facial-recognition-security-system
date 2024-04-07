import pickle
import face_recognition
import cv2  # write this command to download cv2: pip install opencv-python
import os
import glob
import numpy as np
from pynput.mouse import Controller, Button

"""
This script serves as the core
of our facial recognition-based locking system,
utilizing the capabilities of the face_recognition library.
"""


class SimpleFacerec:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []

        # Resize frame for faster processing
        self.frame_resizing = 0.8

    def load_model(self, file_path):
        """
        Load face encodings and names from a file.
        :param file_path: Path to the model file.
        """
        with open(file_path, "rb") as f:
            data = pickle.load(f)
            self.known_face_encodings = data["encodings"]
            self.known_face_names = data["names"]

    def save_model(self, file_path):
        """
        Save face encodings and names to a file.
        :param file_path: Path to save the model.
        """

        data = {
            "encodings": self.known_face_encodings,
            "names": self.known_face_names
        }
        with open(file_path, "wb") as f:
            pickle.dump(data, f)

    def load_encoding_images(self, images_path):
        """
        Load images from a given path and encode faces.
        :param images_path: Directory path containing images.
        """
        # Load Images
        images_path = glob.glob(os.path.join(images_path, "*.*"))

        print("{} encoding images found.".format(len(images_path)))

        # Store image encoding and names
        for img_path in images_path:
            img = cv2.imread(img_path)
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Extract the filename without the extension
            basename = os.path.basename(img_path)
            (filename, ext) = os.path.splitext(basename)
            # Get face encoding
            try:
                img_encoding = face_recognition.face_encodings(rgb_img)[0]
                self.known_face_encodings.append(img_encoding)
                self.known_face_names.append(filename)
            except Exception as e:
                print("Error: " + str(e))

        print("Encoding images loaded")

    def detect_known_faces(self, frame):
        # Resize frame for faster face detection
        small_frame = cv2.resize(frame, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)
        # Convert the image to RGB color space
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_small_frame)

        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            # Check if the face matches any known faces
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"

            # Use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]
            face_names.append(name)
        # Scale back up face locations to match the original frame
        face_locations = np.array(face_locations) / self.frame_resizing
        return face_locations.astype(int), face_names
