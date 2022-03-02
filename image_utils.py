from PIL import Image
import requests
from io import BytesIO
import numpy as np
import cv2

#plt.imshow(IMG, interpolation='nearest')

def transform_image(url): 
    img = Image.open(requests.get(url, stream=True).raw).convert('RGB')
    img = np.array(img)
    img = cv2.resize(img, (224,224))
    img = np.array(img)
    img_data = img[np.newaxis, :, :]
    return img_data

#url='https://firebasestorage.googleapis.com/v0/b/smart-med-aba54.appspot.com/o/images%2F16555_idx5_x951_y851_class1.png?alt=media&token=9500f46f-5657-4a41-9cc6-60a2a273d804'
#print(transform_image(url).shape)