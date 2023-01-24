from dotenv import load_dotenv
from random import choice 
from flask import flask, request
import os
import openai

load_dotenv()
open.api_key = os.getenv("OPENAI_API_KEY")
completion = openai.Completion()


start_sequence = "\nHealthbot:"
restart_sequence = "\n\nYou:"
session_prompt = "You are talking to Welness_oasis's personal health bot:"

def ask(question, chatlog=None):
    prompt_text = f'{chatlog}{restart_sequence}: {question}{start_sequence}'
    response = openai.Completion.create(
        engine="text-davinci-003"
        prompt=prompt_text
        temprature=0.9
        max_tokens=200
        top_p = 1
        frequency_penalty=0
        presence_penalty=0.6

    )
    story = response['choices'][0]['text']

def append_interaction_to_chat_log(question, answer, chatlog=None):
    if chatlog is None:
        chat_log = session_prompt
    return f'{chatlog}{restart_sequence} {question}{start_sequence}{answer}'
