import time
import webbrowser

import streamlit as st

from constants import DEAUTHORIZE_URL
from instagram.instagram_utils import is_paid_subscriber, is_authorized_subscriber, sync_instagram_posts, \
    instagram_deauthorze


def handle_instagram_login():
    id = st.session_state.get("user_id", "")
    # instagram_url = (
    #     f"https://www.instagram.com/oauth/authorize?enable_fb_login=0&force_authentication=1&client_id=581334411142953&redirect_uri=https://owlit-backend.vercel.app/instagram_redirect"
    #     f"&response_type=code&scope=instagram_business_basic%2Cinstagram_business_manage_messages%2Cinstagram_business_manage_comments%2Cinstagram_business_content_publish&state=id%3D{id}"
    # )
    instagram_url = (f"https://www.instagram.com/oauth/authorize?enable_fb_login=0&force_authentication=1&client_id"
                     f"=581334411142953&redirect_uri=https://api.owlit.in/instagram_redirect&response_type=code&scope"
                     f"=instagram_business_basic%2Cinstagram_business_manage_messages"
                     f"%2Cinstagram_business_manage_comments&state=id%3D{id}")

    # Display a clickable button-like link
    st.markdown(
        f"""
        <a href="{instagram_url}" target="_blank" style="display: inline-block; padding: 10px 20px; font-size: 16px; background-color: #4CAF50; color: white; text-align: center; text-decoration: none; border-radius: 5px;">
            Authorize Instagram
        </a>
        """,
        unsafe_allow_html=True,
    )


def handle_instagram_deauthorize():
    id = st.session_state.get("user_id", "")
    if st.button("Deauthorize Instagram"):
        try:
            response = instagram_deauthorze(id)
            if response.status_code ==200:
                st.success("Deauthorized Instagram successfully")
            else:
                st.error("Deauthorized Instagram unsuccessfull")
        except:
            st.error("Deauthorized Instagram unsuccessfull")



def display():
    # if st.session_state.get("paid") is True:
    #     st.success("You are a paid subscriber")
    # else:
    #     st.warning("You are not a paid subscriber")

    if st.session_state.get("auth") is True:
        st.success("You are a authorized subscriber. You need not  authorize again")
    else:
        st.error("You are not a authorized subscriber")
        st.write("Instagram Business Login")
        # if st.button("Authorize Instagram", type="primary"):
        handle_instagram_login()
    handle_instagram_deauthorize()

    st.write("Sync Instagram Posts")
    if st.button("Sync Instagram Posts",type="primary"):
        id = st.session_state.get("user_id", "")
        # Show a progress bar and spinner while syncing
        progress_bar = st.progress(0)
        with st.spinner('Syncing Instagram posts...'):
            # Simulate syncing task with a progress update
            response = sync_instagram_posts(id)  # Use the appropriate ID
            for i in range(1, 101):
                time.sleep(0.05)  # Simulate work being done
                progress_bar.progress(i)  # Update progress

        # After syncing is complete, show the success message
        if response.status_code == 200:
            st.success('Syncing Complete!')

        else:
            st.error('Error during syncing.')

