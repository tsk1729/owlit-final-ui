from constants import IS_USER_PAID_SUBSCRIBER_URL, RequestType, IS_USER_AUTHORIZED_SUBSCRIBER_URL, \
    SYNC_INSTAGRAM_POSTS_URL, DEAUTHORIZE_URL
from utils import make_request


def is_paid_subscriber(id):
    url = IS_USER_PAID_SUBSCRIBER_URL
    return make_request(RequestType.POST, url, payload=id)


def is_authorized_subscriber(id):
    url = IS_USER_AUTHORIZED_SUBSCRIBER_URL
    return make_request(RequestType.POST, url, payload=id)


def sync_instagram_posts(id):
    url = SYNC_INSTAGRAM_POSTS_URL
    return make_request(RequestType.POST, url, payload=id)


def instagram_deauthorze(id):
    url = DEAUTHORIZE_URL
    return make_request(RequestType.POST, url, payload=id)