import streamlit as st
from streamlit_supabase_auth import login_form, logout_button

from about import about_page
from constants import SUPERBASE, temporary_session as session
from contact import contact_page
from home import home_page
from instagram import instagram_page
from instagram.instagram_utils import is_authorized_subscriber, is_paid_subscriber
from webhooks import webhooks_page

st.set_page_config(page_title="User Details", layout="wide")

# session = login_form(url=SUPERBASE.URL,apiKey=SUPERBASE.API_KEY,providers=SUPERBASE.PROVIDERS)
for key,value in session.items():
    st.session_state[key] = value
# st.write(session)
# if not session:
#     st.warning("Please log in to access the application.")
#     st.stop()

logout_button(url=SUPERBASE.URL,apiKey=SUPERBASE.API_KEY)
if "user_image" not in st.session_state:
    st.session_state["user_image"] = session["user"]["user_metadata"]["picture"]
if "user_name" not in st.session_state:
    st.session_state["user_name"] = session["user"]["user_metadata"]["name"]
st.sidebar.image(st.session_state["user_image"])
st.sidebar.write(st.session_state["user_name"])
menu = st.sidebar.radio(
    "Menu",
    ["Home", "Instagram", "Subscribe Webhooks", "About", "Contact"],
    index=0  # Default selected index
)
if "auth" not in st.session_state:
    st.session_state["auth"] = False

id = st.session_state.get("user_id", "")
response = is_authorized_subscriber(id)
if response.status_code == 200:
    st.session_state["auth"]= True

if "paid" not in st.session_state:
    st.session_state["paid"] = True
# response = is_paid_subscriber(id)
# if response.status_code == 200:
#     st.session_state["paid"] = True

if menu == "Home":
    home_page.display(session)
elif menu == "Instagram":
    instagram_page.display()
elif menu == "Subscribe Webhooks":
    webhooks_page.display(session)
elif menu == "About":
    about_page.display()
elif menu == "Contact":
    contact_page.display()




