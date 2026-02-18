import cv2
import numpy as np

def extract_noise(image):
    denoised = cv2.GaussianBlur(image, (5, 5), 0)
    residual = cv2.absdiff(image, denoised)
    return (residual / 255.0).astype(np.float32)
