import streamlit as st
from streamlit_timeline import timeline


# use full page width
st.set_page_config(page_title="Timeline Example", layout="wide")

# load data
with open('base.json', "r") as f:
    timeline(f.read(), height=800)
