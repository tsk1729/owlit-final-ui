import json
import streamlit as st
from streamlit_lottie import st_lottie


def display():
    def load_lottie_local(file_path: str):
        with open(file_path, "r") as f:
            return json.load(f)

    lottie_json = load_lottie_local("owl2.json")


    # Page layout with columns
    col1, col2 = st.columns([1, 1])  # Adjust column widths

    with col1:
        if lottie_json:
            st_lottie(lottie_json, speed=1, width=400, height=400, key="animation")

    with col2:
        # Add a title with color
        st.markdown(
            "<h1 style='color: #4B9CD3;'>Contact Us</h1>",
            unsafe_allow_html=True,
        )

        # Add a subheading with another color
        st.markdown(
            "<h3 style='color: #FF6F61;'>We’d Love to Hear From You!</h3>",
            unsafe_allow_html=True,
        )

        # Add contact details with styled text
        st.markdown(
            """
            <p style='font-size: 18px;'>📧 <b>Email:</b> <a href='mailto:tsk1729@yahoo.com' style='color: #2ECC71;'>tsk1729@yahoo.com</a></p>
            <p style='font-size: 18px;'>🌐 <b>Website:</b> <a href='https://www.owlit.in' target='_blank' style='color: #2ECC71;'>www.owlit.in</a></p>
            """,
            unsafe_allow_html=True,
        )

        # Call to action
        st.markdown(
            "<p style='font-size: 18px; color: #2ECC71;'>Feel free to reach out for inquiries, feedback, or collaborations!</p>",
            unsafe_allow_html=True,
        )
