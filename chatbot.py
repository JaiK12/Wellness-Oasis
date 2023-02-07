from flask import Flask, request
from dotenv import load_dotenv
import os
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
completion = openai.Completion()

start_sequence = "\nHealthbot"
restart_sequence = "\n\nYou"
session_prompt = "You are talking to your personal health ai assistant"

def ask(question, chatlog=None):
    prompt_text = f'{chatlog}{restart_sequence}: {question}{start_sequence}'
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt_text,
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )
    story  = response['choices'][0]['text']

def append_interaction(question, answer, chatlog=None):
    if chatlog is None:
        chat_log = session_prompt
    return f'{chatlog}{restart_sequence}: {question}{start_sequence}'
