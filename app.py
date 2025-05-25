import streamlit as st
from api import show_booking_page
from utils import show_upload_page

# Title and welcome
st.title("🎉 Patient Health Records App")
st.write("Welcome to your Streamlit app! 👋")

# Sidebar navigation
page = st.sidebar.selectbox("Navigate", ["🏥 Upload Records", "📅 Book Appointment"])

# Conditional rendering
if page == "🏥 Upload Records":
    show_upload_page()
elif page == "📅 Book Appointment":
    show_booking_page()
