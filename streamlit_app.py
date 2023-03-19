import csv
import streamlit as st
import pandas as pd
import numpy as np
import plost
from PIL import Image
import sys
import os
import time
import threading
sys.path.append(os.getcwd())

# Page setting
st.set_page_config(layout="wide")

with open('/home/ollie/dashboard/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


a1, a2 = st.columns(2)
a1.image(Image.open('/home/ollie/dashboard/kfc.png'))
st.title("KFC Barker Street")



live_data_widget = st.empty()
file_path = '/home/ollie/dashboard/data/HourlySalesByTradingDay-OKL5380.csv'

while True:
    if not os.path.exists(file_path):
        # Wait for 1 second before checking again
        time.sleep(1)
        continue

    with open(file_path, newline='') as csvfile:
        # Create a CSV reader object
        reader = csv.reader(csvfile)

        # Skip the first 24 rows (header rows)
        for i in range(24):
            next(reader)

        # Get the value in row 25 and column N
        row25 = next(reader)
        columnN = row25[13]  # Note that the column index is zero-based, so column N is at index 13

        # Update the live data widget with the latest value
        live_data_widget.metric("Sales", f"£{columnN}")

    # Wait for 2 seconds before updating again
    time.sleep(2)
