import streamlit as st
import asyncio
from truecallerpy import search_phonenumber


async def NormalSearch(phone_number):
    country_code = "US"
    installation_id = "a1i03--lJA-YoFKkPpJkYKoe42mQpRdgh-w22OoFRX4KAAa22vubbc3zA7APDTwT"

    response = await search_phonenumber(phone_number, country_code, installation_id)

    name = response["data"]["data"][0]["name"]
    return name


# Streamlit App
def main():
    with open("styles.css", "r") as f:
        css = f.read()

    # Your Streamlit app content here

    # Inject custom CSS
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    st.title("Phone Number Details")

    phone_number = st.text_input("Enter Phone Number:")

    if st.button("Submit"):
        if phone_number:
            name = asyncio.run(NormalSearch(phone_number))

            st.success(
                f"The name associated with the phone number {phone_number} is: {name}"
            )

            st.markdown(
                """
                <style>
                    .main.st-emotion-cache-uf99v8.ea3mdgi8{
                        
                        background:rgb(116, 143, 44);
                        transition: 1s ease-in;
                    }
                </style>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.warning("Please enter a valid phone number.")


if __name__ == "__main__":
    main()
