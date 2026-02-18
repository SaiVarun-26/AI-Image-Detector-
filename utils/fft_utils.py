import numpy as np
import cv2

def compute_fft(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    f = np.fft.fft2(gray)
    fshift = np.fft.fftshift(f)
    magnitude = 20 * np.log(np.abs(fshift) + 1)
    return cv2.normalize(magnitude, None, 0, 1, cv2.NORM_MINMAX)
