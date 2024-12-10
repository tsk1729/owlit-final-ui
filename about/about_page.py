import json
from streamlit_lottie import st_lottie
import streamlit as st

def display():
    # st.set_page_config(page_title="About Us - Owlit", layout="wide")
    def load_lottie_local(file_path: str):
        with open(file_path, "r") as f:
            return json.load(f)

    lottie_json = load_lottie_local("owl.json")
    # Page layout with columns
    col1, col2 = st.columns([1, 1])  # Adjust column widths

    with col1:
        if lottie_json:
            st_lottie(lottie_json, speed=1, width=400, height=400, key="animation")

    with col2:
        # Add a title with color
        st.markdown(
            "<h1 style='color: #4B9CD3;'>Welcome to Owlit's Web App for Content Creators!</h1>",
            unsafe_allow_html=True,
        )

        # Add a subheading with another color
        st.markdown(
            "<h3 style='color: #FF6F61;'>Boost Your Reach and Engagement</h3>",
            unsafe_allow_html=True,
        )

        # Add bullet points with styled text
        st.markdown(
            """
            <p style='font-size: 18px;'>📧 <b>Email:</b> <a href='mailto:tsk1729@yahoo.com' style='color: #2ECC71;'>tsk1729@yahoo.com</a></p>
            <p style='font-size: 18px;'>🌐 <b>Website:</b> <a href='https://www.owlit.in' target='_blank' style='color: #2ECC71;'>www.owlit.in</a></p>
            <p style='font-size: 18px;'>📞 <b>Mobile:</b> <a href='tel:+918688765697' style='color: #2ECC71;'>+91 8688765697</a></p>
            """,
            unsafe_allow_html=True,
        )

        # Call to action
        st.markdown(
            "<p style='font-size: 18px; color: #2ECC71;'>Subscribe to our webhook and let Owlit do the rest!</p>",
            unsafe_allow_html=True,
        )
