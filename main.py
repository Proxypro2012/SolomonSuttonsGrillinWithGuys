import streamlit as st

# Define the layout
r1col1, r1col2, r1col3 = st.columns([1, 2, 1])
r2col1, r2col2, r2col3 = st.columns([1, 2, 0.5])
r3col1, r3col2, r3col3 = st.columns([1, 2, 0.5])

# Sidebar navigation
nav_pages = ["Home", "My Cart"]
selected_page = st.sidebar.radio("Navigation", nav_pages)

if 'cart' not in st.session_state:
    st.session_state.cart = []


def get_price(item):
    prices = {
        "Skibidi Slicers": 14.99
    }
    
    return prices.get(item, 0)  # Default to 0 if not found







Items = {
    'SkibidiSlicers': "slicers.JPG"
}





# Content based on the selected navigation option
with r1col2:
    st.title("Solomon Suttons")

# Display content based on the selected page
if selected_page == "Home":
    with r2col2:
        st.subheader("Welcome to Solomon Suttons Home!")
        st.write("Explore our menu and enjoy some delicious dishes.")
    with r3col1:
        st.image(Items["SkibidiSlicers"], caption="Skibidi Slicers. Price: $14.99", width=250)
elif selected_page == "My Cart":
    st.subheader("Your Cart")
    st.write("Check out the items in your cart here.")


