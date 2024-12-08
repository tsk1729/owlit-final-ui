from webhooks.dto import MediaType
from webhooks.webhooks_utils import get_all_posts, subscribe_post_to_webhook
import streamlit as st
import os

os.environ['PYDEVD_USE_FRAME_EVAL'] = 'NO'


def display(session):
    user_id = session["user"]["id"]
    if 'posts' not in st.session_state:
        st.session_state.posts = get_all_posts(user_id)
    posts = st.session_state.posts
    st.title("Instagram Posts")
    posts_per_page = 5
    total_posts = len(posts)
    total_pages = (total_posts // posts_per_page) + (1 if total_posts % posts_per_page > 0 else 0)

    # Initialize session state variables
    if 'page_num' not in st.session_state:
        st.session_state.page_num = 1

    # Callback to update page number
    def change_page(delta):
        st.session_state.page_num += delta

    # Get the current page's posts
    start_idx = (st.session_state.page_num - 1) * posts_per_page
    end_idx = start_idx + posts_per_page
    posts_to_display = posts[start_idx:end_idx]

    # Display posts
    for post in posts_to_display:
        st.markdown("---")
        with st.form(key=f"form_{post['id']}"):  # Use a unique key for each form
            col1, col2 = st.columns([3, 2])  # Create two columns with ratio 3:2

            # Left column (details)
            with col1:
                sub_string = st.text_area(label=f"Bot Substring for Post ", value=post['sub_string'],
                                          key=f"sub_string_{post['id']}", height=70)
                bot_message = st.text_area(label=f"Bot Message for Post ", value=post['bot_message'],
                                           key=f"bot_message_{post['id']}", height=70)
                bot_comment = st.text_area(label=f"Bot Comment for Post ", value=post['bot_comment'],
                                           key=f"bot_comment_{post['id']}", height=70)

            # Right column (media - image or video)
            with col2:
                media_type = post['media_type']
                if media_type == MediaType.VIDEO.value:
                    st.video(post['media_url'])  # Display video
                else:
                    st.image(post['media_url'], width=400)  # Display image

            # Submit button inside the form
            submitted = st.form_submit_button(f"subscribe {post['id']}")
            if submitted:
                response = subscribe_post_to_webhook(user_id, post['id'], sub_string, bot_message, bot_comment)
                if response.status_code == 200:
                    st.balloons()
                    st.success("Subscribed to webhook successfully!")
                else:
                    st.warning("Something went wrong")

    # Navigation buttons
    col1, col2, col3 = st.columns([1, 4, 1])

    with col1:
        if st.session_state.page_num > 1:
            st.button("Previous", on_click=change_page, args=(-1,))

    with col3:
        if st.session_state.page_num < total_pages:
            st.button("Next", on_click=change_page, args=(1,))

    # Display the current page number
    st.write(f"Page {st.session_state.page_num} of {total_pages}")
