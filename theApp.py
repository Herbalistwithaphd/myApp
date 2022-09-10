import streamlit as st
st.title("Welcome to Preston Hotel Lagos")
st.header("Dishes Survey App")
st.subheader("Discover Different Dishes")
st.text("Enter the Items of Choice")
st.success("Done")
st.info("Information")
st.warning("Warning")
st.error("Error")
from PIL import Image
img = Image.open("universe.jpg")
st.image(img, width=150)
st.checkbox("Select/Unselect")
st.text("Selection Ready") 
status = st.radio("Select Dish: ", ('Africana', 'Asia'))
if (status == 'Africana'):
    st.success("Africana")
else:
    st.success("Asia")