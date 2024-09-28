import easyocr as ocr  #OCR
import streamlit as st  #Web App
from PIL import Image #Image Processing
import numpy as np #Image Processing 

#title
st.title("      Extract Text from Images")

#subtitle
st.markdown("## OPTICAL CHARACTER RECOGNITION")

st.markdown("")

#image uploader
image = st.file_uploader(label = "Upload your image here",type=['png','jpg','jpeg'])

@st.cache
def load_model():
    # Specify the URL of the EasyOCR model for English language
    model_url = 'https://github.com/jaidedai/easyocr/releases/download/pre-v1.3.2/transformer-lite.pth'
    # Load the model using the specified URL
    reader = ocr.Reader(['en'], model_storage_directory='.', download_enabled=False, model_url=model_url)
    return reader

@st.cache
def load_model(): 
    reader = ocr.Reader(['en'],model_storage_directory='.')
    return reader 

reader = load_model() #load model

if image is not None:

    input_image = Image.open(image) #read image
    st.image(input_image) #display image

    with st.spinner("🤖 AI is at Work! "):
        

        result = reader.readtext(np.array(input_image))

        result_text = [] #empty list for results


        for text in result:
            result_text.append(text[1])

        st.write(result_text)
    #st.success("Here you go!")
    st.balloons()
else:
    st.write("Upload an Image")

st.caption("Made with ❤️ by @1littlecoder")





