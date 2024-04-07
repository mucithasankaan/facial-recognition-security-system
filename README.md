
# FACIAL-RECOGNITION-SECURITY-SYSTEM

#### This project is a simple example of a facial recognition system that scans the face of the person in front of the computer every second and prevents anyone other than the owner of the computer from using it. This system is basic and highly open to development.

## Prerequisites:
1: Python 3.x <br>
2: Compatible with Windows, MacOS, Linux <br>
3: Webcam

## Installation Instructions:

#### 1: To download the face_recognition library, enter these commands in the command window one by one:

1: pip install cmake <br>
2: git clone https://github.com/davisking/dlib.git <br>
3: cd dlib <br>
4: python setup.py install <br>
5: pip install face_recognition

#### 2: To download cv2, write this command:

pip install opencv-python

## Included Codes:

### face_recognition_core.py:
This code contains the fundamentals of a facial recognition system that works with the face recognition library. It processes a given image with artificial intelligence, compares it with other photos in memory, and returns the name of a similar photo.

### sample_security_system.py:
This code uses the basic facial recognition system from face_recognition_core.py to scan the face of the person in front of the computer every second. If the name returned by the face_recognition_core.py code does not contain the predefined host variable, or if no face is detected for a period, it locks the mouse. This is a sample code.

### data_generation_system:
This code takes a large number of photos every second in a designated folder after the code is executed. It saves each photo with a name combining the name entered on the console and the photo number. These photos can later be used to train the artificial intelligence.

#### To better understand how to use and operate these codes, you can read the User Guide.py file.
