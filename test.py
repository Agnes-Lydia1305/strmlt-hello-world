import streamlit as st

# Set the page title
st.title("User Registration Form")
# Add a text input with a caption
name = st.text_input("Enter your name", placeholder="Type your name here")
email = st.text_input("Enter your email", placeholder="Type your email here")
pwd = st.text_input("Enter your password", placeholder="Type your password here")

# Add a button with the caption "Register"
st.button("Register")

  
