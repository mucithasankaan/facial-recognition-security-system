# Face Recognition User Guide

"""
code to import core of the face recognition
import Face_Recognition_Core
"""

"""
code to Initialize the face recognition module
sfr = Face_Recognition_Core.SimpleFacerec()
"""

"""
code to train the model 
sfr.load_encoding_images(images_path)
"""

"""
code to save model
sfr.save_model("model.pkl")
"""

"""
code to Load model
sfr.load_model("model.pkl")
"""

"""
code to Detect faces in the frame
face_locations, face_names = sfr.detect_known_faces(frame)
"""