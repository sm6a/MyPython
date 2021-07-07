from google.cloud import vision

import os
import io

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="gvapitest-ed1b08406094.json"

client = vision.ImageAnnotatorClient()

for fname in os.listdir('faces'):
    print (fname)
    print ('-----------------------------')
    with io.open('faces/%s' %fname, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    #print('Faces:')

    i=0
    for face in faces:
        #print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
        #print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
        #print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))

        #vertices = (['({},{})'.format(vertex.x, vertex.y)
        #            for vertex in face.bounding_poly.vertices])

        #print('face bounds: {}'.format(','.join(vertices)))
        i=i+1
    
    print('Number of Faces:', i)