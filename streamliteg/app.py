import streamlit as st

st.title("Basic Textbox Example")

# 1. Single-line textbox
name = st.text_input("Enter your name:", placeholder="Type your name here...")

# 2. Password textbox (hides characters)
password = st.text_input("Enter a password:", type="password")

# 3. Multi-line textbox (Text Area)
bio = st.text_area("Tell us about yourself:", placeholder="Write a few lines...")

# Button to display the entered values
if st.button("Submit"):
    if name:
        st.success(f"Hello, {name}!")
        st.write("**Your Bio:**", bio)
    else:
        st.warning("Please enter your name first.")