from constants import FETCH_USER_URL, RequestType, UPDATE_USER_URL
from utils import make_request


def validate_user_details(country_code, mobile, email, address):
    errors = []

    # Validate country_code
    if not country_code.strip():
        errors.append("Country code cannot be empty.")

    # Validate mobile
    if not mobile.strip() or not mobile.isdigit():
        errors.append("Mobile number must be numeric and cannot be empty.")

    if not 7<=len(mobile)<=15:
        errors.append("Mobile number length must be between 7 and 15.")

    # Validate email
    if not email.strip() or "@" not in email:
        errors.append("Email must be a valid email address.")

    # Validate address
    if len(address.strip()) < 5:
        errors.append("Address must be at least 5 characters long.")

    return errors


def fetch_user_details(uid):
    url = FETCH_USER_URL
    return make_request(RequestType.POST, url, payload=uid)

def submit_user_details(payload):
    url = UPDATE_USER_URL
    return make_request(RequestType.POST, url, payload=payload)
