import io

from google.cloud import vision

vision_client = vision.Client()

file_name = '220px-President_Barack_Obama.jpg'

with io.open(file_name, 'rb') as image_file:

    content = image_file.read()

    image = vision_client.image(content = content)

labels = image.detect_labels()

for label in labels:

    print(label.description)
"""
faces = image.detect_faces()

for face in faces:

    print(face.description)
"""
text = image.detect_text()

for txt in text:

    print(txt.description, txt.score)
