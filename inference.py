import tensorflow as tf
import numpy as np

SIZE=128

def get_prediction(image_path):
    image = tf.keras.preprocessing.image.load_img(
        image_path,
        target_size=(SIZE,SIZE)
    )