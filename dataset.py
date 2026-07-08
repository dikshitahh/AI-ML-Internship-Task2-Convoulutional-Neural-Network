from tensorflow.keras.datasets import mnist
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def load_dataset():
    # Load dataset
    (train_images, train_labels), (test_images, test_labels) = mnist.load_data()

    # Normalize images
    train_images = train_images / 255.0
    test_images = test_images / 255.0

    # Reshape images
    train_images = train_images.reshape((60000, 28, 28, 1))
    test_images = test_images.reshape((10000, 28, 28, 1))

    # Data augmentation
    datagen = ImageDataGenerator(
        rotation_range=10,
        width_shift_range=0.1,
        height_shift_range=0.1,
        zoom_range=0.1
    )
    datagen.fit(train_images)
    return train_images, train_labels, test_images, test_labels, datagen
