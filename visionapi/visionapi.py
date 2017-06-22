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
text = image.detect_text() #Detcts text that happens to be in an image

#NOTES
"""

detect_text():
Detects text that happens to be in an image

detect_full_text()
Used when text in an image that is text

"""

for txt in text:

    print(txt.description, txt.score)#Score is the confidence level (0-1)
