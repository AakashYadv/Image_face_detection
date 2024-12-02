opencv-python



#upload  an images
import streamlit as st

# Streamlit file uploader
uploaded_file = st.file_uploader("Choose a file", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Read the file into an image or other data format
    # Example: to display the image
    import PIL.Image
    image = PIL.Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


import cv2

#Load Haar cascade for face detection
cascade_file=cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
cascade = cv2.CascadeClassifier(cascade_file)

#LOAD th uploaded image
image_path=list(uploaded.keys())[0]
image=cv2.imread(image_path)

#Convert image to grayscale
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#DETECT FACE
faces=cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30)) # Using cascade instead of face_cascade

#DRAW eectangles around detected faces
for(x,y,w,h) in faces:
  cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

#Display the result
cv2.imshow(image)

#!pip install opencv-python-headless # To install opencv-python-headless library using pip
import cv2 # Import the necessary library
from google.colab.patches import cv2_imshow # Import the required function for displaying images in Colab

#LOAD th uploaded image
# ... (rest of your code) ...

#Display the result
cv2_imshow(image)  # Use cv2_imshow instead of cv2.imshow
