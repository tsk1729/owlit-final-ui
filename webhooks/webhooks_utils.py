from constants import GET_ALL_POSTS_URL, RequestType, SUBSCRIBE_POST_TO_WEBHOOK
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
    response = make_request(method=RequestType.POST, url=url,payload=pay_load)
    return response
