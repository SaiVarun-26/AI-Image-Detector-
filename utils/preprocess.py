import cv2
import numpy as np

def load_image(file):
    image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), 1)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def resize_image(image, size=(224, 224)):
    return cv2.resize(image, size)

def normalize(image):
    return (image / 255.0).astype(np.float32)
