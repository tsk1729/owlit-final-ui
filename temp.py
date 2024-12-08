import streamlit as st

# Sample data: Replace with your actual data
posts = [
    {
        "thumbnail": "https://via.placeholder.com/100",  # Replace with actual image URL
        "comment": f"Comment for post {i}",
        "reply": f"Reply to post {i}",
        "link": f"https://example.com/post{i}",
    }
    for i in range(1, 31)
]

# Parameters for pagination
posts_per_page = 5
total_pages = -(-len(posts) // posts_per_page)  # Calculate total pages

# Session state to store the current page and inputs
if 'current_page' not in st.session_state:
    st.session_state.current_page = 1

if 'user_inputs' not in st.session_state:
    st.session_state.user_inputs = {i: {"comment": post["comment"], "reply": post["reply"]} for i, post in
                                    enumerate(posts)}


# Functions to navigate between pages
def next_page():
    if st.session_state.current_page < total_pages:
        st.session_state.current_page += 1


def prev_page():
    if st.session_state.current_page > 1:
        st.session_state.current_page -= 1


# Display posts for the current page
start_idx = (st.session_state.current_page - 1) * posts_per_page
end_idx = start_idx + posts_per_page
current_posts = posts[start_idx:end_idx]

st.write(f"### Page {st.session_state.current_page} of {total_pages}")

# Table Header
header_cols = st.columns([1, 3, 3, 2, 2])  # Adjust widths for better space
with header_cols[0]:
    st.write("**Thumbnail**")
with header_cols[1]:
    st.write("**Comment Subword**")
with header_cols[2]:
    st.write("**Reply Message**")
with header_cols[3]:
    st.write("**Post Link**")
with header_cols[4]:
    st.write("**Submit**")

# Editable Table Rows
for idx, post in enumerate(current_posts, start=start_idx):
    row_cols = st.columns([1, 3, 3, 2, 2])

    with row_cols[0]:
        st.image(post["thumbnail"], width=80)

    with row_cols[1]:
        # Use text_area for larger input fields (like a text box)
        st.session_state.user_inputs[idx]["comment"] = st.text_area(
            f"Comment {idx}",
            value=st.session_state.user_inputs[idx]["comment"],
            height=100,  # Adjust height to make the box bigger
            key=f"comment_{idx}"
        )

    with row_cols[2]:
        # Use text_area for the reply message
        st.session_state.user_inputs[idx]["reply"] = st.text_area(
            f"Reply {idx}",
            value=st.session_state.user_inputs[idx]["reply"],
            height=100,  # Adjust height to make the box bigger
            key=f"reply_{idx}"
        )

    with row_cols[3]:
        st.markdown(f"[View Post]({post['link']})", unsafe_allow_html=True)

    with row_cols[4]:
        # Submit button for each row
        if st.button(f"Submit {idx}", key=f"submit_{idx}"):
            # Process the data when the button is clicked
            comment = st.session_state.user_inputs[idx]["comment"]
            reply = st.session_state.user_inputs[idx]["reply"]
            st.success(f"Submitted for Post {idx}:\nComment: {comment}\nReply: {reply}")

# Navigation buttons
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("Previous"):
        prev_page()
with col2:
    if st.button("Next"):
        next_page()

# Debugging: Display all inputs
st.write("### User Inputs")
st.json(st.session_state.user_inputs)
