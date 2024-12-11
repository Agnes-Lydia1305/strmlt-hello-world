import streamlit as st

# Set the page title
st.title("User Registration Form")
# Add a text input with a caption
st.write("Enter your name")
name = st.text_input("Name", placeholder="Type your name here")
  
