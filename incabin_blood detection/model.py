import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models
import cv2

# Dataset paths and parameters
data_dir = "dataset"  # Update with your dataset path
batch_size = 32
img_height = 128
img_width = 128

# Set up data generators for training and validation
train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)
train_data = train_datagen.flow_from_directory(
    data_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical',
    subset='training'
)
val_data = train_datagen.flow_from_directory(
    data_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical',
    subset='validation'
)

# Build a CNN model for blood classification
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(img_height, img_width, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(3, activation='softmax')  # 3 classes for minor, moderate, and severe
])

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(
    train_data,
    validation_data=val_data,
    epochs=10
)

# Save the trained model
model.save("blood_detection_model.h5")

# Load the trained model if you want to use it directly
# model = load_model("blood_detection_model.h5")

# Define a function for combined blood detection
def combined_blood_detection(image_path):
    # Step 1: Classify image severity using CNN
    image = cv2.imread(image_path)
    image_resized = cv2.resize(image, (img_height, img_width))
    image_array = np.expand_dims(image_resized / 255.0, axis=0)
    
    # Predict the class using the CNN model
    predictions = model.predict(image_array)
    class_labels = ['Minor injury', 'Moderate injury', 'Severe injury']
    severity = class_labels[np.argmax(predictions)]
    print(f"Predicted Severity (CNN): {severity}")

    # Step 2: Use color-based blood detection if blood is detected by CNN
    if severity != "No injury":
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
        # Define HSV range for red color
        lower_red = np.array([0, 50, 50])
        upper_red = np.array([10, 255, 255])
        mask = cv2.inRange(hsv_image, lower_red, upper_red)
        
        # Calculate blood area percentage
        blood_area = np.sum(mask > 0)
        total_area = mask.shape[0] * mask.shape[1]
        blood_percentage = (blood_area / total_area) * 100
        
        # Further refine severity based on blood area
        if blood_percentage < 1:
            refined_severity = "No visible blood"
        elif blood_percentage < 5:
            refined_severity = "Minor injury"
        elif blood_percentage < 15:
            refined_severity = "Moderate injury"
        else:
            refined_severity = "Severe injury"

        print(f"Refined Severity (Color-based): {refined_severity}")
        print(f"Blood Percentage: {blood_percentage:.2f}%")

        # Show the mask and original image
        cv2.imshow("Original Image", image)
        cv2.imshow("Blood Mask", mask)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("No blood detected in image based on CNN model.")

# Test the function on an image
combined_blood_detection("018.jpg")
