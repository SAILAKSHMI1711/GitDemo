import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, LSTM, Embedding
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import matplotlib.pyplot as plt

# Load the VGG16 model pretrained on ImageNet dataset
vgg_model = VGG16(weights='imagenet')
vgg_model = Model(inputs=vgg_model.input, outputs=vgg_model.layers[-2].output)

# Function to preprocess and extract features from an image
def extract_features(image_path):
    img = load_img(image_path, target_size=(224, 224))
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    features = vgg_model.predict(img)
    return features

# Define the RNN model for caption generation
def define_caption_model(vocab_size, max_length):
    inputs1 = Input(shape=(4096,))
    fe1 = Dropout(0.5)(inputs1)
    fe2 = Dense(256, activation='relu')(fe1)

    inputs2 = Input(shape=(max_length,))
    se1 = Embedding(vocab_size, 256, mask_zero=True)(inputs2)
    se2 = Dropout(0.5)(se1)
    se3 = LSTM(256)(se2)

    decoder1 = add([fe2, se3])
    decoder2 = Dense(256, activation='relu')(decoder1)
    outputs = Dense(vocab_size, activation='softmax')(decoder2)

    model = Model(inputs=[inputs1, inputs2], outputs=outputs)
    model.compile(loss='categorical_crossentropy', optimizer='adam')
    return model

# Generate captions for an image
def generate_caption(model, photo, max_length, tokenizer):
    in_text = 'startseq'
    for i in range(max_length):
        sequence = tokenizer.texts_to_sequences([in_text])[0]
        sequence = pad_sequences([sequence], maxlen=max_length)
        yhat = model.predict([photo, sequence], verbose=0)
        yhat = np.argmax(yhat)
        word = word_for_id(yhat, tokenizer)
        if word is None:
            break
        in_text += ' ' + word
        if word == 'endseq':
            break
    return in_text

# Load and preprocess the image
image_path = 'example.jpg'  # Replace with your image path
photo = extract_features(image_path)

# Load the tokenizer and define max sequence length
tokenizer = load(open('tokenizer.pkl', 'rb'))
max_length = 34

# Load the caption generation model
model = define_caption_model(len(tokenizer.word_index) + 1, max_length)
model.load_weights('model_weights.h5')

# Generate and print the caption
caption = generate_caption(model, photo, max_length, tokenizer)
print(caption)
