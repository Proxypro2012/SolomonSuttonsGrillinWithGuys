from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import streamlit as st

# Define the layout
r1col1, r1col2, r1col3 = st.columns([1, 2, 1])
r2col1, r2col2, r2col3 = st.columns([1, 2, 0.5])
r3col1, r3col2, r3col3 = st.columns([1, 2, 0.5])
r4col1, r4col2, r4col3 = st.columns([1, 2, 0.5])

# Sidebar navigation
nav_pages = ["Home", "My Cart"]
selected_page = st.sidebar.radio("Navigation", nav_pages)

if 'cart' not in st.session_state:
    st.session_state.cart = []


def get_price(item):
    prices = {
        "SkibidiSlicers": 14.99,
        "Fatty Fries": 6.99,
        "Skibidi Cake": 8.99
    }
    
    return prices.get(item, 0)  # Default to 0 if not found







Items = {
    'SkibidiSlicers': "slicers.JPG",
    "Fatty Fries": "fries.JPG",
    "Skibidi Cake:" "skibidi_cake.JPEG"
}





# Content based on the selected navigation option
with r1col2:
    st.title("Solomon Suttons")

# Display content based on the selected page
if selected_page == "Home":
    with r2col2:
        st.subheader("Welcome to Solomon Suttons Home!")
        st.write("Explore our menu and enjoy some delicious dishes.")
    with r2col3:
        st.image("logo.WEBP")
    
    with r3col1:
        st.image(Items["SkibidiSlicers"], caption="Skibidi Slicers. Price: $14.99", width=250)
    with r4col1:
        if st.button("Add to Cart", key="ATCPT1"):
            st.session_state.cart.append("SkibidiSlicers")

    
    with r3col2:
        st.image(Items["Fatty Fries"], caption="Fatty Fries. Price: $6.99", width = 200)
    with r4col2:
        if st.button("Add to Cart", key="ATCPT2"):
                    st.session_state.cart.append("Fatty Fries")
            
    with r3col2:
        st.image(Items["Skibidi Cake"], caption="Skibidi Cake. Price: $8.99", width = 200)
    with r4col2:
        if st.button("Add to Cart", key="ATCPT3"):
                    st.session_state.cart.append("Skibidi Cake")






elif selected_page == "My Cart":
        st.subheader("Your Cart")
        st.write("Check out the items in your cart here.")
        st.header("Items:")
        
        total_price = 0  # Variable to keep track of the total price
        cart_content = []  # To store the cart items for email body

        # Display each item from the cart with a remove button
        for item in st.session_state.cart:
            if item in Items:  # Ensure item exists in the dictionary
                price = get_price(item)  # Get the price
                total_price += price
                total_price = total_price * 0.0625 + total_price  # Add price to total
                
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.image(Items[item], caption=f"{item}. Price: ${price:.2f}", width=200)
                with col2:
                    # Generate unique key for each button
                    unique_key = f"remove_{item}_{st.session_state.cart.index(item)}_{hash(item)}"
                    
                    # Remove from cart button with a unique key for each item
                    if st.button(f"Remove {item} from Cart", key=unique_key):
                        st.session_state.cart.remove(item)
                        
                # Add the item to the cart content list for email
                cart_content.append(f"{item}: ${price:.2f}")

        # Display total price
        st.subheader(f"Total Price: ${total_price:.2f}")

    # Checkout button should only appear when cart is not empty
if st.session_state.cart:
    if selected_page == "My Cart":
        recipient_email = st.text_input("Enter email to verify order:")
        if recipient_email:  # When email is entered
            if st.button("Checkout"):  # Checkout button appears after entering email
                # Create the body of the email
                cart_body = "DO NOT REPLY! This is an automated message. Inquire here: https://shopromanclothing.streamlit.app/n"
                cart_body = "You ordered:\n"
                cart_body += "\n".join(cart_content)
                cart_body += f"\n\nTotal Pretium (including tax): ${total_price:.2f}"

                # Send email
                def send_email(recipient, subject, body):
                    sender_email = "iamtheskibidisigma420@gmail.com"  # Your email address
                    sender_password = "hqqd yfbq ccdr hlyy"  # Your email password (or app-specific password)
                
                    msg = MIMEMultipart()
                    msg['From'] = sender_email
                    msg['To'] = recipient
                    msg['Subject'] = "Your order at solomon-suttons.streamlit.app is arriving soon!"  # Fixed subject
                
                    # Attach the body with the email
                    msg.attach(MIMEText(body, 'plain'))
                
                    try:
                        # Set up the server (for Gmail in this case)
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()
                        server.login(sender_email, sender_password)
                        text = msg.as_string()
                        server.sendmail(sender_email, recipient, text)
                        server.quit()
                        st.success("Email sent successfully!")
                    except Exception as e:
                        st.error(f"Failed to send email: {e}")
                
                send_email(recipient_email, "Your order at solomon-suttons.streamlit.app is arriving soon!", cart_body)
        else:
            st.error("Please enter an email address. (example-email@your-domain.com)")


