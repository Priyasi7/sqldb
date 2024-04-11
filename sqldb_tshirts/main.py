import streamlit as st

# Function to add custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load CSS file
local_css("styles.css")

from langchain_helper import get_few_shot_db_chain

st.title("Shirts::Database Q&A 👕")

question = st.text_input("Query: ")

if question:
    chain = get_few_shot_db_chain()
    response = chain.run(question)

    st.header("Answer")
    st.write(response)
