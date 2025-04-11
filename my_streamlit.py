import streamlit as st

st.title("CHƯƠNG TRÌNH CỦA TÔI")
st.subheader("Demo Streamlit")

menu = ["Home", "About"]
choice = st.sidebar.selectbox('Menu', menu)
if choice == 'Home': 
    st.subheader("Streamlit From Windows")
elif choice == 'About': 
    st.subheader("[Trung Tam Tin Hoc](https://csc.edu.vn)")