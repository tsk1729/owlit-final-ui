class RequestType:
    GET = "GET"
    POST = "POST"
    DELETE = "DELETE"
    PUT = "PUT"


class SUPERBASE:
    URL = "https://ikygxetagzzrdajalxwl.supabase.co"
    API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlreWd4ZXRhZ3p6cmRhamFseHdsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzI4MjA0NTcsImV4cCI6MjA0ODM5NjQ1N30.rG4mpQx8LRQCtxP9ERsaS5YPl2QTEi6xq6vvx4KJUQk"
    PROVIDERS = ["google"]


fatapi_url = "localhost:8000"
FETCH_USER_URL = f"http://{fatapi_url}/v1/fetch_user_details/"
UPDATE_USER_URL = f"http://{fatapi_url}/v1/update_details/"
IS_USER_PAID_SUBSCRIBER_URL = f"http://{fatapi_url}/v1/paid_subscriber/"
IS_USER_AUTHORIZED_SUBSCRIBER_URL = f"http://{fatapi_url}/v1/authorized_subscriber/"
SYNC_INSTAGRAM_POSTS_URL = f"http://{fatapi_url}/v1/sync_instagram_media/"
GET_ALL_POSTS_URL = f"http://{fatapi_url}/v1/get_all_posts/"
SUBSCRIBE_POST_TO_WEBHOOK = f"http://{fatapi_url}/v1/subscribe_post_to_webhook/"
UNSUBSCRIBE_POST_TO_WEBHOOK = f"http://{fatapi_url}/v1/unsubscribe_post_to_webhook/"