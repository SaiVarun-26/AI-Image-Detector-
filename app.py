import streamlit as st
from transformers import pipeline
from PIL import Image

# Load model
detector = pipeline(
    "image-classification",
    model="umm-maybe/AI-image-detector"
)

# animated background + glass UI
st.markdown("""
<style>
.stApp {
    background: linear-gradient(-45deg, #3b000f, #6b001a, #400012, #1a0006);
    background-size: 400% 400%;
    animation: waveMove 10s ease infinite;
}

@keyframes waveMove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Glass card */
.block-container {
    background: rgba(255, 255, 255, 0.05);
    padding: 2rem;
    border-radius: 20px;
    backdrop-filter: blur(20px);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
    max-width: 800px;
    margin: auto;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("""
<h1 style='
    text-align: center;
    color: white;
    font-size: 3rem;
    text-shadow: 0 0 20px rgba(255, 100, 120, 0.8);
'>
AI Image Detector
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p style='text-align:center; color:#f8d7da; font-size:18px;'>
Advanced AI-generated image detection using pretrained deep learning models
</p>
""", unsafe_allow_html=True)

# File uploader
uploaded_file = st.file_uploader(
    "Upload Image",
    type=["jpg", "png"],
    key="main_uploader"
)

# main code
if uploaded_file is not None:
    image = Image.open(uploaded_file)

    with st.spinner("Analyzing image..."):
        result = detector(image)

    label = result[0]["label"]
    score = result[0]["score"]

    # Rename label for UI
    if label.lower() in ["human", "real"]:
        display_label = "Real Image"
        bar_color = "#00cc88"
        text_color = "#b3ffe0"
    elif label.lower() in ["artificial", "ai", "fake"]:
        display_label = "AI Generated"
        bar_color = "#ff4d6d"
        text_color = "#ffb3c1"
    else:
        display_label = label
        bar_color = "#ffffff"
        text_color = "#ffffff"

    # Show prediction ABOVE image
    st.markdown(f"""
    <h2 style="color:white; margin-top:20px;">
        Prediction: <span style="color:{text_color};">{display_label}</span>
    </h2>
    """, unsafe_allow_html=True)

    # Confidence bar
    st.markdown(f"""
    <div style="
        background: rgba(255,255,255,0.1);
        border-radius: 10px;
        padding: 10px;
        margin-top:10px;
        margin-bottom:20px;
    ">
        <div style="
            width:{score*100}%;
            background: {bar_color};
            height: 15px;
            border-radius: 10px;
            transition: width 1s ease-in-out;
        "></div>
    </div>
    <p style="color:white;">
        Confidence: {score:.2f}
    </p>
    """, unsafe_allow_html=True)

    # Show image AFTER result
    st.image(image, caption="Uploaded Image", use_container_width=True)