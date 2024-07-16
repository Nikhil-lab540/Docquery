import requests
import streamlit as st

def get_lamma_response(input_text):
    response= requests.post('http://localhost:8000/essay/invoke',json={"input":{'topic':input_text}})
    return response.json()['output']

st.title("Langchain Demo with llama3 api")
input_text =st.text_input("Top 10 books on")

if input_text:
    st.write(get_lamma_response(input_text=input_text))


def about_book(input_text1):
        response= requests.post('http://localhost:8000/essay/info/invoke',json={"input":{'topic':input_text1}})
        return response.json()['output']



st.subheader("Select the book you want")
input_text1 =st.text_input("Book Name")
if input_text1:
    st.write(get_lamma_response(input_text=input_text1))