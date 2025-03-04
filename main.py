import streamlit as st

r1col1, r1col2, r1col3 = st.columns([1, 2, 1])
r2col1, r2col2, r2col3 = st.columns([1, 2, 0.5])

nav_pages = ["Home", "My Cart",]

with r1col2:
  st.title("Solomon Suttons")
with r2col2:
  st.header("Grillin with Guys")


navbar = st.sidebar.title("Navigation")

navbar.radio(nav_pages[0])




