import tensorflow as tf
import numpy as np

orLogic = np.array([[0, 0], # output 0
                    [0, 1], # output = 1
                    [1, 0], # output = 1
                    [1, 1]], dtype=float) # output = 1

output = np.array([[0], [1], [1], [1]], dtype=float)

# init model.. 
model =  tf.keras.models.Sequential([    
     tf.keras.layers.Dense(1, input_dim=2, activation='sigmoid')
])

# compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(orLogic, output, epochs=1000, verbose=0)

loss, accuracy = model.evaluate(orLogic, output)
print(f'Accuracy: {accuracy*100:.2f}%')

predictions = model.predict(orLogic)
print("Predictions:")
print(np.round(predictions))

###########################################
# 
# 1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 84ms/step - accuracy: 0.7500 - loss: 0.2984
# Accuracy: 75.00%
# 1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 32ms/step
# Predictions:
# [[1.]
#  [1.]
#  [1.]
#  [1.]]
#
###########################################

#// if epochs > the better the output