from PIL import Image, ImageDraw
import face_recognition
known_face_names, known_face_encodings = pickle.load(open('faces.p', 'rb'))

image = Image.open('test/group1.jpg')

face_locations = face_recognition.face_locations(np.array(image))
face_encodings = face_recognition.face_encodings(np.array(image), face_locations)

draw = ImageDraw.Draw(image)

for face_encoding, face_location in zip(face_encodings, face_locations):
    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
    best_match_index = np.argmin(face_distances)
    print(face_distances)