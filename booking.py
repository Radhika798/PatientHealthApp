import streamlit as st

def main():
    st.header("📅 Book a Consultation")
    with st.form("booking_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        date = st.date_input("Preferred Date")
        submitted = st.form_submit_button("Book Now")
        if submitted:
            st.success(f"Appointment booked for {name} on {date}")

if __name__ == "__main__":
    main()
