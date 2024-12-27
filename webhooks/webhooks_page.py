from webhooks.dto import MediaType
from webhooks.webhooks_utils import get_all_posts, subscribe_post_to_webhook, unsubscribe_post_to_webhook, \
    clear_text_areas, validate_fields
import streamlit as st
import os

os.environ['PYDEVD_USE_FRAME_EVAL'] = 'NO'


def display(session):
    if st.session_state["paid"] is False:
        st.warning("Please pay for subscription")
        st.stop()
    if st.session_state["auth"] is False:
        st.warning("Please Complete Authorzation")
        st.stop()

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
        col1, col2 = st.columns([3, 2])  # Create two columns with ratio 3:2
        # Right column (media - image or video)
        with col1:
            media_type = post['media_type']
            if media_type == MediaType.VIDEO.value:
                st.video(post['media_url'])  # Display video
            else:
                st.image(post['media_url'], width=400)  # Display image

        # Left column (details)
        with col2:
            sub_string = st.text_area(
                label=":orange[Bot Substring]",
                value=st.session_state.get(f"sub_string_{post['id']}", post['sub_string']),
                key=f"sub_string_{post['id']}",
                height=70,
            )
            bot_message = st.text_area(
                label=f":orange[Bot Message] ",
                value=st.session_state.get(f"bot_message_{post['id']}", post['bot_message']),
                key=f"bot_message_{post['id']}",
                height=70,
            )
            bot_comment = st.text_area(
                label=f":orange[Bot Comment]",
                value=st.session_state.get(f"bot_comment_{post['id']}", post['bot_comment']),
                key=f"bot_comment_{post['id']}",
                height=70,
            )


            # Subscribe form
            with st.form(key=f"subscribe_form_{post['id']}"):
                subscribe_button = st.form_submit_button(f"Subscribe",type="primary")
                if subscribe_button:
                    errors = validate_fields(sub_string,bot_message,bot_comment)
                    if errors:
                        for error in errors:
                             st.error(error)
                    else:
                        response = subscribe_post_to_webhook(user_id, post['id'], sub_string.strip(), bot_message, bot_comment)
                        if response.status_code == 200:
                            st.balloons()
                            st.success(f"Subscribed to webhook successfully with fields sub_stirng:[{sub_string}] \n bot_message: [{bot_message}] \n bot_comment: [{bot_comment}]")
                        else:
                            st.warning("Something went wrong")

            # Unsubscribe form
            with st.form(key=f"unsubscribe_form_{post['id']}"):
                unsubscribe_button = st.form_submit_button(f"Unsubscribe",type="primary", on_click=clear_text_areas, args=[post])
                if unsubscribe_button:
                    response = unsubscribe_post_to_webhook(user_id, post['id'])
                    if response.status_code == 200:
                        st.balloons()
                        st.success("Unsubscribed from webhook successfully!")
                    else:
                        st.error("Something went wrong")

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
