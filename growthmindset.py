import streamlit as st

# App title
st.set_page_config(page_title="User Profile Generator", layout="wide")
st.sidebar.title("User Profile Settings")

# Sidebar input fields
name = st.sidebar.text_input("Enter your name:")
age = st.sidebar.text_input("Enter your age:")
profession = st.sidebar.text_input("Enter your profession:")
bio = st.sidebar.text_area("Write a short bio about yourself:")
email = st.sidebar.text_input("Enter your email:")
phone = st.sidebar.text_input("Enter your phone number:")
address = st.sidebar.text_area("Enter your address:")

# Generate profile card
st.title("User Profile Card Generator")
if st.sidebar.button("Generate Card"):
    st.markdown(f"""
    <div style="border: 2px solid #4CAF50; padding: 20px; border-radius: 10px; background-color: #f9f9f9; text-align: center; width: 50%; margin: auto;">
        <h2 style="color: #4CAF50;">User Profile</h2>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Age:</strong> {age}</p>
        <p><strong>Profession:</strong> {profession}</p>
        <p><strong>Bio:</strong> {bio}</p>
        <p><strong>Email:</strong> {email}</p>
        <p><strong>Phone:</strong> {phone}</p>
        <p><strong>Address:</strong> {address}</p>
    </div>
    """, unsafe_allow_html=True)

