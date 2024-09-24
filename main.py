import streamlit as st

# 1. Name and logo of your company
st.image("ApplySmartLogo.png", width=400)  # Adjust width as needed

# 2. Description of your product
st.subheader("Product Description")
st.write("Apply Smart is a startup aimed at putting your best foot forward by leveraging AI to tailor your resume to any job posting with just a couple clicks.")

# 3. Link to your survey
st.subheader("Survey Link")
survey_url = "https://docs.google.com/forms/d/e/1FAIpQLScWqWsH5jpArTVwhszWKjjyEscC0tkj4U-COBoV2aPk0zxiyw/viewform?usp=sf_link"
st.markdown(f"[Click here to take the survey]({survey_url})")

# 4. A form to collect contact information from visitors
st.subheader("Contact Information Form")
with st.form("contact_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    submitted = st.form_submit_button("Submit")

    if submitted:
        st.write(f"Thank you for submitting your details, {name}!")
        st.write(f"We will reach out to you at {email} or {phone}.")

