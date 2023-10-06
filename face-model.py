from PIL import Image, ImageDraw
import face_recognition
import numpy as np
import pickle

# Name and image path
known_faces = [
    ['Lisa', 'lisa.jpg'],
    ['Jennie', 'jennie.jpg'],
    ['Rose', 'rose.jpg'],
    ['Jisoo', 'jisoo.jpg']
]


known_faces_names = []
known_faces_encoding = []
for face in known_faces:
    known_faces_names.append(face[0])
    face_image = face_recognition.load_image_file(face[1])
    face_encoding = face_recognition.face_encodings(face_image)[0]
    known_faces_encoding.append(face_encoding)

print(known_faces_names)
print(known_faces_encoding)

# pickle.dump((known_faces_names, known_faces_encoding), open('faces.p', 'wb'))