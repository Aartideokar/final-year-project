import pickle
from pathlib import Path

import streamlit_authenticator as stauth

names = ["Aarti Deokar", "Aarti"]
usernames = ["aDeokar", "aarti"]
passwords = ["aDeokar123", "aarti123"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pws.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)
