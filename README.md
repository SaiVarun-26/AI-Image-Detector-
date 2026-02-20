# AI Image Detector

A Streamlit-based web application that detects whether an image is AI-generated or a real photograph using a pretrained deep learning model from Hugging Face.

---

## Overview

With the rapid advancement of generative AI tools like Stable Diffusion, Midjourney, and DALL·E, distinguishing between AI-generated and real images is becoming increasingly challenging.

This project leverages a pretrained vision model to classify images as:

- 🟢 **Real Image**
- 🔴 **AI Generated Image**

The application provides a confidence score and an intuitive UI for seamless interaction.

---

## Features

- ✅ Pretrained AI detection model (Hugging Face)
- 🎨 Animated burgundy glassmorphism UI
- 📊 Confidence visualization with dynamic progress bar
- ⚡ Fast image classification
- 🧩 Clean and modular project structure
- 💻 Built with Streamlit

---

## Tech Stack

- **Python**
- **Streamlit**
- **Hugging Face Transformers**
- **PyTorch**
- **Pillow (PIL)**

---
``ai-image-detector/``
``├── app.py               # Main Streamlit application``
``├── requirements.txt     # Project dependencies``
``└── README.md            # You are here :D``

---

# Clone the repository:


``git clone https://github.com/SaiVarun-26/ai-image-detector.git
cd ai-image-detector``

# To run

``streamlit run app.py``

---
## How It Works

*User uploads an image.
*The image is processed using Pillow.
*The pretrained Hugging Face model performs classification.
*The model outputs:
    *Predicted label
    *Confidence score
*Results are displayed with a visual confidence bar.


## screenshots
home page
<img width="1860" height="843" alt="image" src="https://github.com/user-attachments/assets/aec20689-21ae-43dd-9fd5-29b99f8227d2" />

after uploading
<img width="1858" height="848" alt="image" src="https://github.com/user-attachments/assets/fcd49c60-2326-42cc-b2ad-08b4b3d6a3ef" />

Thank you!



