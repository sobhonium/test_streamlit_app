import pandas as pd
import numpy as np
import streamlit as st


nz_cities = {
    "Dunedin":[-45.894738, 170.554005],
    "Christchurch":[-43.519493, 172.647741]
             }

lon_lat = np.array([nz_cities["Dunedin"],nz_cities["Christchurch"]])
df = pd.DataFrame(lon_lat, columns=['lat', 'lon'])
st.map(df)