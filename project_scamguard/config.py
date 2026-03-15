import os
from pathlib import Path
import streamlit as st

# API KEY
gemini_api_key = st.secrets["GEMINI_API_KEY"]

# Models
DEFAULT_MODEL = "gemini-2.5-flash"
temp = 0

# Path 
OUTDIR = "\data"