import streamlit as st
import openai
openai.api_key =  st.secrets["mykey"]

# Title and Heading
st.title("Smart FAQ Assistant (Health Monitoring)")
st.header("This is a header")
st.write("This is some text.")

# Input and Output
name = st.text_input("Ask your question:", value="Type here")
if st.button("Submit"):
    st.write(f"Here you go!!")
