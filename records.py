import streamlit as st

def main():
    st.header("📋 Patient Records")
    st.write("You can view or upload patient records here.")
    uploaded_file = st.file_uploader("Upload Patient File", type=["pdf", "txt"])
    if uploaded_file:
        st.success("File uploaded successfully!")
        st.write(f"Filename: {uploaded_file.name}")

if __name__ == "__main__":
    main()
