import streamlit as st
import pandas as pd

st.title("File Upload Example")

df = st.file_uploader("Upload a PDF file", type="pdf")

