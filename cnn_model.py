from keras import layers
from keras.models import Sequential
from keras.optimizers import Adam
from keras.applications.densenet import DenseNet201

def build_model(backbone, lr=1e-4):
    model = Sequential()
    model.add(backbone)
    model.add(layers.GlobalAveragePooling2D())
    model.add(layers.Dropout(0.5))
    model.add(layers.BatchNormalization())
    model.add(layers.Dense(2, activation='softmax'))
    
    model.compile(
        loss='binary_crossentropy',
        optimizer=Adam(learning_rate=lr),
        metrics=['accuracy']
    )
    return model



#model = build_model(resnet ,lr = 1e-4)
#model.summary()