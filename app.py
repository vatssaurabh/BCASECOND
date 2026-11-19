import streamlit as st

# Page configuration
st.set_page_config(page_title="Simple Login", page_icon="🔒", layout="centered")

# Hardcoded credentials for demonstration (replace with a database or st.secrets in production)
USERS = {
    "admin": "password123",
    "user": "welcome2026"
}

# Initialize session state for login tracking
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""


def login_page():
    st.title("🔒 Login")
    st.write("Please enter your credentials to continue.")

    # Using a form so the page only reruns when the Submit button is clicked
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login", use_container_width=True)

        if submit:
            if username in USERS and USERS[username] == password:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid username or password")


def dashboard_page():
    st.title(f"👋 Welcome, {st.session_state.username}!")
    st.write("You are now logged into the main application.")

    st.divider()
    st.subheader("Dashboard Content")
    st.info("Put your protected app content, charts, or tools here.")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()


# Route between Login and Dashboard based on session state
if st.session_state.logged_in:
    dashboard_page()
else:
    login_page()