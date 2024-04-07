import cv2  # write this command to download cv2: pip install opencv-python
import time

"""
This code is designed to collect facial data
for training a facial recognition system. 
It captures numerous photos every second 
with a camera and saves them according to the name initially entered.
"""

# Get a name input from the user
name = input("Enter a name: ")
# Get the number of photos to be taken
number_of_photos = int(input("Enter the number of photos to be taken: "))
# Specify the folder path where photos will be saved
folder_path = "images"
time.sleep(3)
# Initialize the camera
cap = cv2.VideoCapture(0)

for i in range(number_of_photos):
    print("Photo was taken")
    # Capture the frame
    ret, frame = cap.read()

    if not ret:
        break

    # Save the captured frame
    cv2.imwrite(f"{folder_path}/{name}_{str(i)}.jpg", frame)

    # Wait for 0.1 seconds
    time.sleep(0.1)

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
