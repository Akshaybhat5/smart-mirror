import os
import streamlit as st
from api_key import API_KEY
from langchain.llms import OpenAI
from text_to_speech import text_to_speech
from voice_to_text import speech_to_text

# print('Ran Successfully!')
os.environ['OPENAI_API_KEY'] = API_KEY

llms = OpenAI(temperature = 0.9)
def main():
    # print('🦜🔗 GPT Assistant Test')

    # print("Welcome!, speak 'bye' to end the conversation")

    while True:
        prompt = speech_to_text()
        if "bye" in prompt.lower():
        # if prompt.lower() == "bye":
            break
        open_ai_response = llms(prompt)
        print("OpenAI: ", open_ai_response)
        text_to_speech(open_ai_response)

if __name__ == "__main__":
    main()