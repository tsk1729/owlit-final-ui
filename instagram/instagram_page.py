import time
import webbrowser

import streamlit as st

from instagram.instagram_utils import is_paid_subscriber, is_authorized_subscriber, sync_instagram_posts


def handle_instagram_login():
    id = st.session_state.get("user_id", "")
    print(id)

    instagram_url = f"https://www.instagram.com/oauth/authorize?enable_fb_login=0&force_authentication=1&client_id=581334411142953&redirect_uri=https://owlit-backend.vercel.app/instagram_redirect&response_type=code&scope=instagram_business_basic%2Cinstagram_business_manage_messages%2Cinstagram_business_manage_comments%2Cinstagram_business_content_publish&state=id%3D{id}"
    # instagram_url = f"https://www.instagram.com/oauth/authorize?enable_fb_login=0&force_authentication=1&client_id=581334411142953&redirect_uri=https://owlit-backend.vercel.app/v1/instagram_redirect&response_type=code&scope=instagram_business_basic%2Cinstagram_business_manage_messages%2Cinstagram_business_manage_comments%2Cinstagram_business_content_publish&state=id%3D{id}"
    print(instagram_url)
    webbrowser.open(instagram_url)


def display():
    try:
        id = st.session_state.get("user_id","")
        response = is_paid_subscriber(id)
        if response.status_code == 200:
            st.success("You are a paid subscriber")
        else:
            st.error("You are not a paid subscriber")
    except Exception as e:
        st.warning("Something went wrong")

    try:
        id = st.session_state.get("user_id", "")
        response = is_authorized_subscriber(id)
        if response.status_code == 200:
            st.session_state["auth"]= True
            st.success("You are a authorized subscriber. You need not  authorize again")
        else:
            st.error("You are not a authorized subscriber")
            st.write("Instagram Business Login")
            st.session_state["auth"]= False
            if st.button("Authorize Instagram",type="primary"):
                handle_instagram_login()

    except Exception as e:
        st.warning("Something went wrong")

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

