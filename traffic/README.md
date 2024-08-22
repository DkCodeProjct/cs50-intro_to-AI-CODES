# experimenting../


### First Train
   * i begin my model init Sequential,,
   and i Add ::
    ---------------------------
           layers.Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
           layers.MaxPooling2D((2, 2)),
           layers.Conv2D(32, (3, 3), activation='relu'),
           layers.MaxPooling2D((2, 2)),
           layers.Flatten(),
           layers.Dense(128, activation='relu'),
           layers.Dropout(0.5),
           layers.Dense(NUM_CATEGORIES, activation='softmax')
   ---------------------------

   * since model had  conv2D and activation func as ReLU, its a great match for the model.
   also maxPooling and 3x3 KERNEL  layers are keep shrink the img and getting neccesary and valuable data as much as possible. and that good for the model performes cos its lower the messines and noise in the img.
   with another conv2D, and maxPooling the model got a chance to focus on more accurate and Neccesary data about the img, enabling model to detect more complex Patterns and Featurs.

   * after that i put Dense or 128 Neurons/Units/Nodes. and with the activation of relu.. 
   The DENS the model, the BETTER it perform and Predictiing. also i think the Droput with a rate of [0.5]
   prevent the overfitting by ensuring the training proccess is distrubuted across all the NODES tather than relying
   too much on Few Nodes.

   * i think the model Training Acuracy and loss Prove my Points above i mentioend..
    -----------------------------
    
    Epoch 1/10
    168/168 ━━━━━━━━━━━━━━━━━━━━ 8s 39ms/step -` accuracy: 0.2690 - loss: 10.0697` - val_accuracy: 0.4574 - val_loss: 1.4328
    Epoch 2/10
    168/168 ━━━━━━━━━━━━━━━━━━━━ 9s 32ms/step - accuracy: 0.4647 - loss: 1.3757 - val_accuracy: 0.6839 - val_loss: 
    .
    .
    .
    .
    Epoch 10/10
    168/168 ━━━━━━━━━━━━━━━━━━━━ 11s 33ms/step -` accuracy: 0.9301 - loss: 0.1958` - val_accuracy: 0.9380 - val_loss 0.
    -----------------------------

  

### BAD MODEL...!
  * since Brain said go around and play with the nn, i just put some parameters to the model,,, 
  and here are they:::
      * first i dropout  filters from 32 to ---> 28, 
      * 2 `sigmoid activation func instead of ReLU
      * drop down Layed `DENS` from 128 to ---> 68
      * also drop down `DROPOUT` rate 0.5 to ---> 0.2
      * and replace the last Layer or `output` Layers Activation func with the `Sigmoid` insted of `Softmax`
  
  * after all those changes the model did horrible at training.
  and thers lot of reason for the,, first the drop down of [filters].
  if theres more filter, the model get to extract data more Precicly.. but i put it into 28 which is low and 
  unefficent.
  
  * and the ReLU func is more suitable for this project. cos its offer `non-linearity` while being computationaly efficent, allowing network to learn complex pattern without cuasing any `vanishing gradient problem`./
  but i choose to put `SIGMOID SQUSIFICATION`, sigmoid is a rather 0|1 binary classifire.
  Sigmoid func squash inputs into a small range between 0 and 1, which can cause `gradients to become `very small `during backpropagation`, leading to slow convergence and difficulty in learning complex patterns.
  
  * and the drop down of [Dropout] rate 0.5 to ==> 0.2,decreases the amount of `regularization,` which may lead to less `underfitting but could increase the risk of overfitting.`
  also with the Dens of 68 Nodes the netwrok may rely more heavily on specific nodes during training,,,
  potentially reducing the model's ability to generalize well to new data.

  * and lastly, and most importantly. 
  replacing `sigmoid` with [softmax],...
    + `SIGMOID:` Outputs a probability for each class independently and is typically used for binary classification or multi-label classification (where each class is treated independently). 
    
    + `SOFTMAX`: Normalizes the output to sum` to 1 across all categories`, providing a probability distribution over multiple classes, `which is ideal for multiclass classification problems like traffic sign recognition.`

  * with all the reason i mentioned above we can see how bad the model trained, compare to the first mode;

  --------------------------------
  Epoch 1/10
    168/168 ━━━━━━━━━━━━━━━━━━━━ 15s 79ms/step - `accuracy: 0.2033 - loss: 2.4362` - val_accuracy: 0.2848 - val_loss: 1.6733
    Epoch 2/10
    .
    .
    .
    Epoch 10/10
    168/168 ━━━━━━━━━━━━━━━━━━━━ 20s 76ms/step - `accuracy: 0.6420 - loss: 0.8630` - val_accuracy: 0.7930 - val_loss: 0.6
  --------------------------------


* since i got intel i3 cpu,, i trained the model on `Google CoLAB`,
and id like to amazing Engineers on Google and Tensorflow cos damn
thats the definition of user experienc,, Thank you so much