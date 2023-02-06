# Rasa Tutorial Practice
My practice repo. It follows RASA tutorials.

# Setup
## Rasa Install
1. [Rasa Installation](https://rasa.com/docs/rasa/2.x/installation/#:~:text=Install%20Rasa%20Open%20Source%20using,Python%203.7%2C%20or%203.8)
2. [Rasa command line interface](https://rasa.com/docs/rasa/2.x/command-line-interface)
3. [Rasa CI/CD](https://rasa.com/docs/rasa/2.x/setting-up-ci-cd/)
Note: This setup doesn't use pyenv, but system shell. 
```commandline
brew install python@3.8
python3.8 -m venv ./venv
source ./venv/bin/activate
pip install rasa[full]
pip install --upgrade rasa
rasa init
python -m spacy download en_core_web_md
```
Project location: ROOT/proj

# RASA Concepts Note
[Click me](README_concept_notes.md)

# APIs
1. [HTTP API](https://rasa.com/docs/rasa/2.x/http-api)
Besides basic functions (training, sending messages, running tests, ...), it offers authentication methods (Token Based Auth, JWT Based Auth)
2. [NLU-Only Server](https://rasa.com/docs/rasa/2.x/nlu-only-server)



