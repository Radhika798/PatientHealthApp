import streamlit as st

def show_booking_page():
    st.header("Book a Consultation")

    name = st.text_input("Your Name")
    doctor = st.selectbox("Choose Doctor", ["Dr. Smith", "Dr. Khan"])
    date = st.date_input("Pick a date")

    if st.button("Book Appointment"):
        st.success(f"Appointment booked for {name} with {doctor} on {date}")
