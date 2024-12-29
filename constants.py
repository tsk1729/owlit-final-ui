class RequestType:
    GET = "GET"
    POST = "POST"
    DELETE = "DELETE"
    PUT = "PUT"


class SUPERBASE:
    URL = "https://ikygxetagzzrdajalxwl.supabase.co"
    API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlreWd4ZXRhZ3p6cmRhamFseHdsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzI4MjA0NTcsImV4cCI6MjA0ODM5NjQ1N30.rG4mpQx8LRQCtxP9ERsaS5YPl2QTEi6xq6vvx4KJUQk"
    PROVIDERS = ["google"]


# fatapi_url = "localhost:8000"
# base_url = "http://"
fatapi_url = "api.owlit.in"  # Remote production URL
base_url = "https://"

# Define the URLs
FETCH_USER_URL = f"{base_url}{fatapi_url}/v1/fetch_user_details/"
UPDATE_USER_URL = f"{base_url}{fatapi_url}/v1/update_details/"
IS_USER_PAID_SUBSCRIBER_URL = f"{base_url}{fatapi_url}/v1/paid_subscriber/"
IS_USER_AUTHORIZED_SUBSCRIBER_URL = f"{base_url}{fatapi_url}/v1/authorized_subscriber/"
SYNC_INSTAGRAM_POSTS_URL = f"{base_url}{fatapi_url}/v1/sync_instagram_media/"
GET_ALL_POSTS_URL = f"{base_url}{fatapi_url}/v1/get_all_posts/"
SUBSCRIBE_POST_TO_WEBHOOK = f"{base_url}{fatapi_url}/v1/subscribe_post_to_webhook/"
UNSUBSCRIBE_POST_TO_WEBHOOK = f"{base_url}{fatapi_url}/v1/unsubscribe_post_to_webhook/"
DEAUTHORIZE_URL = f"{base_url}{fatapi_url}/v1/manual_deauthorize/"
temporary_session = {
    "provider_token": "ya29.a0ARW5m77_dQbCSVqhRG4QX7LfimPqoiNgjyXBfsBHYq2XIDcET1LkgrDqO1TKlO6RfKQdgftCf2DNN9bE2nbVc0X3fUnNGSzG6Ev2jSf_JeA6l5jMMEVUCF-iIZoqzPOru9k8AIM523fPjO3F39tsmzsfoGzQG_MDr2UaCgYKAcASARMSFQHGX2MibZJ2YxznZRcSTau_akrEFg0170",
    "access_token": "eyJhbGciOiJIUzI1NiIsImtpZCI6InFYelg2b2hxMnNiZHQ4ME4iLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2lreWd4ZXRhZ3p6cmRhamFseHdsLnN1cGFiYXNlLmNvL2F1dGgvdjEiLCJzdWIiOiJjMzY2Yjc5NS1jMWJjLTRhN2YtYTU4MS1hZGU0MmI3NjBkYTIiLCJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzM1NDYzNzI4LCJpYXQiOjE3MzU0NjAxMjgsImVtYWlsIjoib3dsaXQuMTk5OUBnbWFpbC5jb20iLCJwaG9uZSI6IiIsImFwcF9tZXRhZGF0YSI6eyJwcm92aWRlciI6Imdvb2dsZSIsInByb3ZpZGVycyI6WyJnb29nbGUiXX0sInVzZXJfbWV0YWRhdGEiOnsiYXZhdGFyX3VybCI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FDZzhvY0p2NDNheldxSFhaNHVEZE9qN1hPdWFIUDRFY1kxaFdWbG1NRkRsZS1FWjhNaDIzUT1zOTYtYyIsImVtYWlsIjoib3dsaXQuMTk5OUBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZnVsbF9uYW1lIjoib3dsaXQiLCJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJuYW1lIjoib3dsaXQiLCJwaG9uZV92ZXJpZmllZCI6ZmFsc2UsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQ2c4b2NKdjQzYXpXcUhYWjR1RGRPajdYT3VhSFA0RWNZMWhXVmxtTUZEbGUtRVo4TWgyM1E9czk2LWMiLCJwcm92aWRlcl9pZCI6IjEwMTMwNzcwMjg3MDQ0MDg5MTQ1MSIsInN1YiI6IjEwMTMwNzcwMjg3MDQ0MDg5MTQ1MSJ9LCJyb2xlIjoiYXV0aGVudGljYXRlZCIsImFhbCI6ImFhbDEiLCJhbXIiOlt7Im1ldGhvZCI6Im9hdXRoIiwidGltZXN0YW1wIjoxNzM1NDYwMTI4fV0sInNlc3Npb25faWQiOiI5ODEyOWFkYS00YmE3LTQzMzItYTZmYS0xODM3YWZhNjJhOTUiLCJpc19hbm9ueW1vdXMiOmZhbHNlfQ.ig8VfP2XmtDvy-q50rCSMznjTe2jLMt1E-yr8DT-2ro",
    "expires_in": 3600, "expires_at": 1735463730, "refresh_token": "yTQtDmA5tKpdFiGnKjIKfg", "token_type": "bearer",
    "user": {"id": "c366b795-c1bc-4a7f-a581-ade42b760da2", "aud": "authenticated", "role": "authenticated",
             "email": "owlit.1999@gmail.com", "email_confirmed_at": "2024-12-28T21:22:20.034651Z", "phone": "",
             "confirmed_at": "2024-12-28T21:22:20.034651Z", "last_sign_in_at": "2024-12-29T08:15:28.062511Z",
             "app_metadata": {"provider": "google", "providers": ["google"]}, "user_metadata": {
            "avatar_url": "https://lh3.googleusercontent.com/a/ACg8ocJv43azWqHXZ4uDdOj7XOuaHP4EcY1hWVlmMFDle-EZ8Mh23Q=s96-c",
            "email": "owlit.1999@gmail.com", "email_verified": True, "full_name": "owlit",
            "iss": "https://accounts.google.com", "name": "owlit", "phone_verified": False,
            "picture": "https://lh3.googleusercontent.com/a/ACg8ocJv43azWqHXZ4uDdOj7XOuaHP4EcY1hWVlmMFDle-EZ8Mh23Q=s96-c",
            "provider_id": "101307702870440891451", "sub": "101307702870440891451"}, "identities": [
            {"identity_id": "76b1f290-f783-4542-a062-e89cd15abcf6", "id": "101307702870440891451",
             "user_id": "c366b795-c1bc-4a7f-a581-ade42b760da2", "identity_data": {
                "avatar_url": "https://lh3.googleusercontent.com/a/ACg8ocJv43azWqHXZ4uDdOj7XOuaHP4EcY1hWVlmMFDle-EZ8Mh23Q=s96-c",
                "email": "owlit.1999@gmail.com", "email_verified": True, "full_name": "owlit",
                "iss": "https://accounts.google.com", "name": "owlit", "phone_verified": False,
                "picture": "https://lh3.googleusercontent.com/a/ACg8ocJv43azWqHXZ4uDdOj7XOuaHP4EcY1hWVlmMFDle-EZ8Mh23Q=s96-c",
                "provider_id": "101307702870440891451", "sub": "101307702870440891451"}, "provider": "google",
             "last_sign_in_at": "2024-12-28T21:22:20.025161Z", "created_at": "2024-12-28T21:22:20.025253Z",
             "updated_at": "2024-12-29T08:15:28.055968Z", "email": "owlit.1999@gmail.com"}],
             "created_at": "2024-12-28T21:22:20.005377Z", "updated_at": "2024-12-29T08:15:28.06491Z",
             "is_anonymous": False}}
