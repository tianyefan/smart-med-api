from CNN.cnn_model import build_model
from CNN.image_utils import transform_image
from keras.applications.densenet import DenseNet201


resnet = DenseNet201(
    weights='imagenet',
    include_top=False,
    input_shape=(224,224,3)
)


weights = './CNN/weights_best.hdf5'

def predict(url):
    img = transform_image(url)
    model = build_model(resnet, lr=1e-4)
    model.load_weights(weights)
    predction = model.predict(img)
    return predction

#url='https://firebasestorage.googleapis.com/v0/b/smart-med-aba54.appspot.com/o/images%2F16555_idx5_x951_y851_class1.png?alt=media&token=9500f46f-5657-4a41-9cc6-60a2a273d804'
#print(predict(url))