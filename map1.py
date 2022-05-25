import streamlit as st
from streamlit_observable import observable

@st.cache
def get_trader_joes():
    # a lot of code...
    return df

#df = get_trader_joes()

observable("Colorado Precinct Map", 
    notebook="@marilynwaldman/colorado-precincts-map-with-tooltips", 
    targets=["map"]
    
)