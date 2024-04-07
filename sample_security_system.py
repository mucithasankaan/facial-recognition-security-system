import Face_Recognition_Core as frc  # 'Face_Recognition_Core' is a custom module for face recognition
import cv2 # write this command to download cv2: pip install opencv-python
import threading
from pynput.mouse import Controller, Button

"""
This is a sample code
of a security system working
using a face recognition system.
"""

# name of authorized person
host = ""

# Create a mouse controller instance
m = Controller()
# Initialize the lock state and counters
lock_state = False
counter_i = 0
counter_j = 0
# Initial position of the mouse
position = (0, 0)

images_path = "images"


# Function to lock the mouse position
def lock_mouse():
    while True:
        if lock_state:
            m.position = position


# Creating a thread to run the lock_mouse function
thread_lock_mouse = threading.Thread(target=lock_mouse)
thread_lock_mouse.start()

# Initialize the face recognition module
sfr = frc.SimpleFacerec()
# Train model
sfr.load_encoding_images(images_path)

# Save model (assuming 'model.pkl')
sfr.save_model("model.pkl")

# Start the camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    # Detect faces in the frame
    face_locations, face_names = sfr.detect_known_faces(frame)

    for face_loc, name in zip(face_locations, face_names):
        # If "kaan" is detected, unlock the mouse
        if host in name:
            print("Face recognized")
            counter_i = 0
            counter_j = 0
            lock_state = False
        else:
            # If a different face is detected, initiate the locking process
            counter_i += 1
            if counter_i > 5:
                if counter_i == 6:
                    position = m.position
                    lock_state = True
                else:
                    lock_state = True

    # If no faces are detected, start a different locking process
    if len(face_names) == 0:
        print("No face detected")
        counter_j += 1
        if counter_j > 100:
            if counter_j == 101:
                position = m.position
                lock_state = True
            else:
                lock_state = True
