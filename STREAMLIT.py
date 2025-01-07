from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

nvidia_api_key = os.getenv("NVIDIA_API_KEY")

st.title("Maheroo")

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=nvidia_api_key,
)


def chatter(user_input):
    completion = client.chat.completions.create(
        model="meta/llama3-70b-instruct",
        messages=[
            {
                "role": "user",
                "content": user_input,
            }
        ],
        temperature=1,
        top_p=1,
        max_tokens=1024,
        stream=False,
    )

    return completion.choices[0].message.content


query = st.text_input("Ask a Question from Alina Baaji")

if st.button("Submit"):
    if query:
        output = chatter(query)
        st.write(output)