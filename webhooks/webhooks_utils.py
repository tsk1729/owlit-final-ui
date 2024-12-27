from constants import GET_ALL_POSTS_URL, RequestType, SUBSCRIBE_POST_TO_WEBHOOK, UNSUBSCRIBE_POST_TO_WEBHOOK
from utils import make_request
import os
import streamlit as st

os.environ['PYDEVD_USE_FRAME_EVAL'] = 'NO'


def get_all_posts(id):
    url = GET_ALL_POSTS_URL
    response = make_request(RequestType.POST, url, payload=id)
    return response.json()


def subscribe_post_to_webhook(id, post_id, sub_string, bot_message, bot_comment):
    url = SUBSCRIBE_POST_TO_WEBHOOK
    pay_load = {"user_id": id, "post_id": post_id, "sub_string": sub_string, "bot_message": bot_message,
                "bot_comment": bot_comment}
    response = make_request(method=RequestType.POST, url=url, payload=pay_load)
    return response


def unsubscribe_post_to_webhook(id, post_id):
    url = UNSUBSCRIBE_POST_TO_WEBHOOK
    pay_load = {"user_id": id, "post_id": post_id}
    response = make_request(method=RequestType.POST, url=url, payload=pay_load)
    return response


def clear_text_areas(post):
    st.session_state[f"sub_string_{post['id']}"] = ""
    st.session_state[f"bot_message_{post['id']}"] = ""
    st.session_state[f"bot_comment_{post['id']}"] = ""


def validate_fields(sub_string, bot_message, bot_comment):
    errors = []
    if " " in sub_string:
        errors.append("Substring shouldn't have any empty spaces")
    if bot_message.strip() == "" and bot_comment.strip() == "":
        errors.append("Both bot_comment and bot message should be set")
    return errors
