import os
import json
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

BASE_DIR = os.path.dirname(__file__)

load_dotenv()

st.set_page_config("AI Assistant - Open AI")
st.title("AI Assistant - Open AI")
api_key = os.getenv("OPEN_AI_KEY")

if not api_key:
    st.error("Open AI Key was not found")
    st.stop()

client = OpenAI(api_key=api_key) #create an object from the open 
#AI class and initialize it with the API Key

def load_orders_data(filepath: str):
    from pathlib import Path
    import json

    json_path = Path(filepath)
    if json_path.exists():
        with open(json_path,"r") as f:
            return json.load(f)
    else:
        return []
    
orders = load_orders_data(os.path.join(BASE_DIR, "orders.json"))

def load_logs(filepath):
    json_path = Path(filepath)
    if json_path.exists():
        with open(json_path, "r") as f:
            return json.load(f)
    else:
        return []
        
def save_logs(filepath, logs):
    json_path = Path(filepath)
    with open(json_path, "w") as f:
        json.dump(logs,f)

if "messages" not in st.session_state:
    st.session_state['messages'] = []

logs = load_logs(os.path.join(BASE_DIR, "ai_logs.json"))

for log in logs:
    st.session_state['messages'].append(
        {
            'role': log['role'],
            'content': log['context']
        }
    )

user_input = st.chat_input("Ask me a question...")

if user_input:
    st.session_state['messages'].append(
        {
            "role":"user",
            "content":user_input
        }
    )
    with st.chat_message('user'):
        st.markdown(user_input)

    with st.chat_message("ai-assistant"):
        with st.spinner("Thinking..."):
            import time
            time.sleep(2)
            ai_response = get_ai_response(client,st.session_state['messages'])
            pass

        st.session_state['messages'].append(
            {
                'role':'ai-assistant',
                'content':ai_response
            }
        )

    log_filepath = os.path.join(BASE_DIR, "ai_logs.json")
    logs = load_logs(log_filepath)
    logs.append({
        'user_message': user_input,
        'ai_response': ai_response
    })
    save_logs(log_filepath, logs)

def build_ai_prompt():
    return "" \
    " You are a helpful company assistant. " \
    "Answer user questions based on some sample data that you create" \
    "and return the response to the user, include some data in the response" \
    "these are the guardrailes: " \
    "- do not use negative words"

def get_ai_response(client: OpenAI, chat_history: list):
    #build the prompt
    ai_prompt = build_ai_prompt()
    ai_prompt_message = [
        {
            "role":"system",
            "content": ai_prompt
        }
    ]
    message = chat_history + ai_prompt_message
        #call the open ai agent, get the response
    ai_response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=message,
        temperature=0.2
    )

    return ai_response.choices[0].message.content


