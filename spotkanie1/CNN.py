import os
import numpy as np
from PIL import Image
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from tensorflow.keras import datasets, layers, models, optimizers, regularizers


dataset_dir = 'path/to/dataset'

target_size = (50, 50)

images = []
labels = []

class_mapping = {
    'benign': 0,
    'malignant': 1
}

for class_folder, class_label in class_mapping.items():
    class_path = os.path.join(dataset_dir, class_folder)

    for filename in os.listdir(class_path):
        if filename.endswith('.jpg'):
            img = Image.open(os.path.join(class_path, filename))
            img = img.resize(target_size)

            img_array = np.array(img) / 255.0  # scale pixel values to range 0-1

            images.append(img_array)
            labels.append(class_label)

images = np.array(images)
labels = np.array(labels)

print("Shape of images:", images.shape)
print("Shape of labels:", labels.shape)

train_images, test_images, train_labels, test_labels = train_test_split(images, labels, test_size=0.2, random_state=41)

x_train, x_val, y_train, y_val = train_test_split(train_images, train_labels, test_size=0.2, random_state=41)

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(50, 50, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(256, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

model.summary()

model.compile(optimizer=optimizers.Adam(learning_rate=0.0001),
              loss='binary_crossentropy',
              metrics=['accuracy'])

history = model.fit(x_train, y_train, epochs=20,
                    validation_data=(x_val, y_val))

test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f"Test accuracy: {test_acc}")


plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()

plt.tight_layout()
plt.show()
