from google.cloud import vision

import os
import io
import difflib

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="gvapitest-ed1b08406094.json"

client = vision.ImageAnnotatorClient()

for fname in os.listdir('images'):
    print (fname)

    print ('-----------------------------')
    with io.open('images/%s' %fname, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    text_response = client.text_detection(image=image)
    
    texts = [text.description for text in text_response.text_annotations]
    
    print(texts[0])






