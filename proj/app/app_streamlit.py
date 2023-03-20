'''
Dependency
    1. export AUTH_TOKEN="FILL ME"


To run
    1. local:
        python -m streamlit run app_streamlit.py
    2. server
        python -m streamlit run app_streamlit.py --server.port 5005
        then you can see the streamlit page from your local machine at an external URL
        (e.g., http://xx.xx.xx.xxx:5005)

'''
import streamlit as st
from streamlit_chat import message
from typing import Dict
import requests
import json
import os


def generate_response(data_in: Dict):
    auth_token = os.environ.get('AUTH_TOKEN')
    rasa_api_endpint = "http://localhost:5005/webhooks/rest/webhook?token=" + auth_token
    data_json = json.dumps(data_in)
    res = requests.post(url=rasa_api_endpint, data=data_json)
    res_json = res.json()
    print(res_json)
    res_out = '. '.join([x["text"] for x in res_json])
    return res_out


st.title('Chat AI Demo')

# user
user_name = st.text_input("Enter a unique user name.")  # any string

# Storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

user_message = st.text_input("You: ", "Hello? How can I help?", key="input")

if (st.button('Submit')):
    st.success('Submitted')

    if user_name and user_message:
        data_in = {
            "sender": user_name,    # sender ID
            "message": user_message,
        }
        res_text = generate_response(data_in)
        print(res_text)
        # store the output
        st.session_state.past.append(user_message)
        print(1)
        st.session_state.generated.append(res_text)
        print(2)

if st.session_state['generated']:
    print(3)
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        print("itor {:d}".format(i))
        print(4)
        message(st.session_state["generated"][i], key=str(i))
        print(5)
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        print(6)
