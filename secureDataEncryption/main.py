import streamlit as st
import hashlib
from cryptography.fernet import Fernet

# Initialize session state
if 'key' not in st.session_state:
    st.session_state.key = Fernet.generate_key()
    st.session_state.cipher = Fernet(st.session_state.key)

if 'stored_data' not in st.session_state:
    st.session_state.stored_data = {}

if 'failed_attempts' not in st.session_state:
    st.session_state.failed_attempts = {}

# Page title
st.title("🔐 Secure Data Encryption System")

# Navigation menu
menu = st.sidebar.radio("Select Option", ["Encrypt Data", "Decrypt Data"])

# 🔐 Encrypt Section
if menu == "Encrypt Data":
    st.subheader("🧪 Encrypt & Store Data")

    username = st.text_input("Username")
    plain_text = st.text_area("Enter Text to Encrypt")
    passkey = st.text_input("Enter Passkey", type="password")

    if st.button("Encrypt & Save"):
        if username and plain_text and passkey:
            hashed_passkey = hashlib.sha256(passkey.encode()).hexdigest()
            encrypted = st.session_state.cipher.encrypt(plain_text.encode()).decode()

            st.session_state.stored_data[username] = {
                "encrypted_text": encrypted,
                "passKey": hashed_passkey
            }

            st.success("✅ Data Encrypted & Saved!")
            st.code(encrypted, language="text")
        else:
            st.error("⚠️ Please fill all fields.")

# 🔓 Decrypt Section
elif menu == "Decrypt Data":
    st.subheader("🔍 Decrypt Stored Data")

    username = st.text_input("Enter Username")
    passkey = st.text_input("Enter Passkey", type="password")

    if st.button("Decrypt"):
        if username not in st.session_state.stored_data:
            st.error("❌ Username not found.")
        else:
            # initialize failed attempts
            if username not in st.session_state.failed_attempts:
                st.session_state.failed_attempts[username] = 0

            if st.session_state.failed_attempts[username] >= 3:
                st.warning("🚫 Too many failed attempts. Try again later.")
            else:
                hashed_pass = hashlib.sha256(passkey.encode()).hexdigest()
                user_data = st.session_state.stored_data[username]

                if hashed_pass == user_data["passKey"]:
                    decrypted = st.session_state.cipher.decrypt(user_data["encrypted_text"].encode()).decode()
                    st.success("✅ Decryption Successful!")
                    st.text_area("🔓 Decrypted Text", value=decrypted, height=100)
                    st.session_state.failed_attempts[username] = 0
                else:
                    st.session_state.failed_attempts[username] += 1
                    remaining = 3 - st.session_state.failed_attempts[username]
                    st.error(f"❌ Incorrect passkey. Attempts left: {remaining}")
