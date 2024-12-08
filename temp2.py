import streamlit as st
@st.dialog("Title")
def show_dialog(msg):
    st.write(msg)
show_dialog("Erripuka")