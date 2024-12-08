import streamlit as st
from home.home_utils import fetch_user_details, submit_user_details, validate_user_details


def display(session):
    # Streamlit UI to fetch user details
    st.title("User Details")
    # st.write(session["user"]["id"])
    # Check if user_id exists in session state
    if "user_id" not in st.session_state:
        st.session_state.user_id = session["user"]["id"]

    for key in ["country_code", "mobile", "email", "address"]:
        if key not in st.session_state:
            st.session_state[key] = ""

    # Button to fetch user details
    if st.button("Fetch User Details"):
        if st.session_state.get("user_id"):
            try:
                response = fetch_user_details(st.session_state.user_id)
                if response.status_code == 200:
                    details = response.json()
                    st.session_state["country_code"] = details.get("country_code", "")
                    st.session_state["mobile"] = details.get("mobile", "")
                    st.session_state["email"] = details.get("email", "")
                    st.session_state["address"] = details.get("address", "")
                    st.success("User found. You can update details.")
                else:
                    st.warning("No user found. You can register new details.")
            except Exception as e:
                st.warning(str(e))
        else:
            st.warning("Please signin.")

    # Form for updating user details
    st.subheader("User Details")

    with st.form(key="user_details_form"):
        country_code = st.text_input("Country Code", value=st.session_state.get("country_code", ""))
        mobile = st.text_input("Mobile", value=st.session_state.get("mobile", ""), max_chars=15)
        email = st.text_input("Email", value=st.session_state.get("email", ""))
        address = st.text_area("Address", value=st.session_state.get("address", ""))

        # Submit button for the form
        submitted = st.form_submit_button("Update User Details")
    # Validation logic after submission
    if submitted:
        errors = validate_user_details(country_code, mobile, email,address)
        # Display errors or proceed with update
        if errors:
            for error in errors:
                st.error(error)
        else:
            updated_details = {
                "user_id": st.session_state.get("user_id"),
                "country_code": country_code,
                "mobile": mobile,
                "email": email,
                "address": address,
            }
            try:
                response = submit_user_details(payload=updated_details)
                if response.status_code == 200:
                    st.success("User details updated successfully.")
                    # Optionally update session state
                    st.session_state["country_code"] = country_code
                    st.session_state["mobile"] = mobile
                    st.session_state["email"] = email
                    st.session_state["address"] = address
                else:
                    st.error("Failed to update user details.")
            except Exception as e:
                st.error(str(e))
