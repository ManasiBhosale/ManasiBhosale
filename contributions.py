# contributions.py

import requests
import streamlit as st
from datetime import datetime

st.title("GitHub Contributions Tracker")

username = st.text_input("Enter your GitHub username", "octocat")
year = st.selectbox("Select Year", list(range(datetime.now().year, 2012, -1)))

if username:
    url = f"https://github-contributions-api.jogruber.de/v4/{username}?y={year}"
    resp = requests.get(url)

    if resp.status_code == 200:
        data = resp.json()
        total = sum(day['count'] for day in data['contributions'])
        st.success(f"Total contributions in {year}: {total}")
    else:
        st.error("Failed to fetch data. Check the username.")
