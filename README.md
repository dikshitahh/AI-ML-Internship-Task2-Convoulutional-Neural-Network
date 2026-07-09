# AI-ML-Internship-Task2-Convoulutional-Neural-Network

# Image Classification using Convolutional Neural Network (CNN)

## Project Overview

This project implements a Convolutional Neural Network (CNN) for handwritten digit classification using the MNIST dataset. The model was developed using TensorFlow and Keras and demonstrates the complete deep learning pipeline, including data preprocessing, data augmentation, CNN model construction, training, evaluation, and performance visualization.

## Objective

The objective of this project is to understand and implement Convolutional Neural Networks (CNNs) for image classification. The model learns to recognize handwritten digits (0–9) from grayscale images and is evaluated using multiple performance metrics.

## Dataset

Dataset: MNIST Handwritten Digits Dataset

Dataset Details:

- 60,000 training images
- 10,000 testing images
- Image size: 28 × 28 pixels
- Grayscale images
- 10 output classes (Digits 0–9)

## Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Matplotlib
- Scikit-learn
- Seaborn

## Data Preprocessing

The following preprocessing techniques were applied:

- Loaded the MNIST dataset
- Normalized pixel values to the range 0–1
- Reshaped images to (28, 28, 1)
- Applied data augmentation using:
  - Rotation
  - Width Shift
  - Height Shift
  - Zoom
    
## CNN Architecture

The implemented CNN consists of:

- Conv2D (32 filters, ReLU)
- MaxPooling2D
- Conv2D (64 filters, ReLU)
- MaxPooling2D
- Flatten Layer
- Dense Layer (64 neurons, ReLU)
- Dropout Layer (0.5)
- Output Dense Layer (10 neurons, Softmax)

## Hyperparameters

- Optimizer: Adam
- Loss Function: Sparse Categorical Crossentropy
- Epochs: 5
- Batch Size: 32
- Activation Function: ReLU
- Output Activation: Softmax

## Model Evaluation

The trained model was evaluated using:

- Test Accuracy
- Test Loss
- Accuracy Curve
- Loss Curve
- Confusion Matrix
- Classification Report

### Final Results

Replace these values with your own:

- Test Accuracy: 99.07%
- Test Loss: 0.0269%

## Learning Outcomes

Through this project, I learned:

- Image preprocessing techniques
- Data augmentation
- CNN architecture design
- Regularization using Dropout
- Training deep learning models
- Model evaluation using confusion matrix and classification report
- Saving trained models for future use

## Conclusion

A Convolutional Neural Network (CNN) was successfully developed and trained for handwritten digit recognition using the MNIST dataset. The model achieved high classification accuracy and demonstrated the effectiveness of CNNs for image classification tasks. The project provided practical experience in deep learning, image preprocessing, model evaluation, and performance analysis.
