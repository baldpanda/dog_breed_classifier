#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tensorflow.keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf


if  __name__ == "__main__":
    train_data_generator = ImageDataGenerator(rescale = 1/255)

    train_generator = train_data_generator.flow_from_directory(
        LABELS_PATH,
        target_size=(300,300),
        batch_size=269,
        class_mode='sparse'
    )

    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(16, (3,3), activation='relu', input_shape=(300, 300, 3)),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(512, activation='relu'),
        tf.keras.layers.Dense(120, activation='softmax')
    ])

