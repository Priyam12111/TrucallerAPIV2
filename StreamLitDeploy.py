import streamlit as st
import asyncio
from truecallerpy import search_phonenumber


# Function to simulate the NormalSearch function

async def NormalSearch(phone_number):
    country_code = "US"
    installation_id = "a1i03--lJA-YoFKkPpJkYKoe42mQpRdgh-w22OoFRX4KAAa22vubbc3zA7APDTwT"

    response = await search_phonenumber(phone_number, country_code, installation_id)

    # Access the result after the awaited coroutine completes
    name = response['data']['data'][0]['name']
    return name

# Streamlit App
def main():
    st.title("Phone Number Name Lookup")
    
    # Input for phone number
    phone_number = st.text_input("Enter Phone Number:")
    
    # Button to trigger the search
    if st.button("Submit"):
        # Check if the phone number is provided
        if phone_number:
            # Call the NormalSearch function asynchronously
            name = asyncio.run(NormalSearch(phone_number))
            
            # Display the result with styling
            st.success(f"The name associated with the phone number {phone_number} is: {name}")

            # Additional styling
            st.markdown(
                """
                <style>
                    .main.st-emotion-cache-uf99v8.ea3mdgi8{
                        
                        background:rgb(116, 143, 44);
                        transition: 1s ease-in;
                    }
                </style>
                """,
                unsafe_allow_html=True
            )
        else:
            st.warning("Please enter a valid phone number.")

if __name__ == "__main__":
    main()