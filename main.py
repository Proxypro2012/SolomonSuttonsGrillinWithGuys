import streamlit as st

# Define the layout
r1col1, r1col2, r1col3 = st.columns([1, 2, 1])
r2col1, r2col2, r2col3 = st.columns([1, 2, 0.5])

# Sidebar navigation
nav_pages = ["Home", "My Cart"]
selected_page = st.sidebar.radio("Navigation", nav_pages)



Items = {
    'SkibidiSlicers': "slicers.JPG"
}





# Content based on the selected navigation option
with r1col2:
    st.title("Solomon Suttons")

# Display content based on the selected page
if selected_page == "Home":
    st.subheader("Welcome to Solomon Suttons Home!")
    st.write("Explore our menu and enjoy some delicious dishes.")
elif selected_page == "My Cart":
    st.subheader("Your Cart")
    st.write("Check out the items in your cart here.")


