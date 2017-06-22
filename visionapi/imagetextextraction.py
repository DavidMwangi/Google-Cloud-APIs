import io

from google.cloud import vision

vision_client = vision.Client()

file_name = 'block-of-text.png'

with io.open(file_name, 'rb') as image_file:

    content = image_file.read()

    image = vision_client.image(content = content)

print(image.detect_full_text().text)

#NOTES
"""
detect_full_text()
Detects text in an image that is text

"""
