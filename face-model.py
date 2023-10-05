from PIL import Image, ImageDraw
import face_recognition
import pickle

# Name and image path
known_faces = [
    ('Lisa', 'lisa.jpg'),
    ('Jennie', 'jennie.jpg'),
    ('Rose', 'rose.jpg'),
    ('Jisoo', 'jisoo.jpg')
]
# Encode faces from images
# known_face_names = []
# known_face_encodings = []
# for face in known_faces:
#     known_face_names.append(face[0])
#     face_image = face_recognition.load_image_file(face[1])
#     face_encoding = face_recognition.face_encodings(face_image)[0]
#     known_face_encodings.append(face_encoding)

# # Dump face names and encoding to pickle
# pickle.dump((known_face_names, known_face_encodings), open('faces.p', 'wb'))


known_faces_names = []
known_faces_encoding = []
for face in known_faces:
    # print(face[1])
    known_faces_names.append(face[1])
    face_image = face_recognition.load_image_file(face[1])
    face_encoding = face_recognition.face_encoding = (face_image)[0]
    known_faces_encoding.append(face_encoding)

pickle.dump((known_faces_names, known_faces_encoding), open('faces.p', 'wb'))