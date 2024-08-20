
import tensorflow as tf


##
# 
#  First Proper Neural Network That i got to ``train and save``
# 
##


mnist = tf.keras.datasets.mnist

(xTrain, yTrain), (xTest, yTest) = mnist.load_data()
xTrain, xTest = xTrain / 255.0, xTest / 255.0
yTrain = tf.keras.utils.to_categorical(yTrain)
yTest = tf.keras.utils.to_categorical(yTest)
xTrain = xTrain.reshape(
    xTrain.shape[0], xTrain.shape[1], xTrain.shape[2], 1
)

xTest = xTest.reshape(
    xTest.shape[0], xTest.shape[1], xTest.shape[2], 1
)

model = tf.keras.models.Sequential([

    tf.keras.layers.Conv2D(
        32, # numbr of filters
        (3,3), # filter kerel 
        activation='relu', # activation func rectify linear unit 
        input_shape=(28, 28, 1) # 28by28 Pixel,, and 1 answer
    ), 

    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)), # get the max val 

    tf.keras.layers.Flatten(),

    tf.keras.layers.Dense(128, activation='relu'), # 128 neurons 
    tf.keras.layers.Dropout(0.5), # dropout rate

    tf.keras.layers.Dense(10, activation='softmax')


])

model.compile(
    optimizer='adam',
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

model.fit(xTrain, yTrain, epochs=2)

model.evaluate(xTest, yTest)

fileNm = 'trainedModel.h5'
model.save(fileNm)
print('+'*10)
print(f"Train model Save to --> {fileNm} ")
print('+'*10)