import cv2
import time
import os
import streamlit as st

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'keys.json'
import google.cloud.vision as vision
import re

vision_client = vision.ImageAnnotatorClient()
image = vision.Image()

url = st.text_input('Enter the url of the image')
time.sleep(5)

image.source.image_uri = url

response1 = vision_client.text_detection(image=image)

text = response1.text_annotations[0].description
st.write(text)
time.sleep(3)

picture = st.camera_input("First, take a picture...")
path = 'test.jpg'
if picture:
    with open(path, 'wb') as file:
        file.write(picture.getbuffer())

time.sleep(3)
with open(path, 'rb') as image_file:
    content = image_file.read()

vision_image = vision.Image(content=content)
client = vision.ImageAnnotatorClient()
response2 = client.text_detection(image=vision_image)
st.write('We have our picture')
text2 = response2.text_annotations[0].description
st.write(text2)

if text != text2:
    st.write('The products are different, wanna raise a concern')
