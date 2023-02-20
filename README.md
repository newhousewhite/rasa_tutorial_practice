# Rasa Tutorial Practice
My practice repo. It follows RASA tutorials.

# Setup
## Rasa Install
1. [Rasa Installation](https://rasa.com/docs/rasa/2.x/installation/#:~:text=Install%20Rasa%20Open%20Source%20using,Python%203.7%2C%20or%203.8)
2. [Rasa command line interface](https://rasa.com/docs/rasa/2.x/command-line-interface)
3. [Rasa CI/CD](https://rasa.com/docs/rasa/2.x/setting-up-ci-cd/)

Note: This setup doesn't use pyenv, but system shell.

### Option 1: pip
```commandline
brew install python@3.8
python3.8 -m venv ./venv
source ./venv/bin/activate
pip install rasa[full]
pip install --upgrade rasa
rasa init
python -m pip install spacy==2.3    # rasa 2.0 is not fully comparable with spacy 3.0
python -m spacy download en_core_web_md
```
Project location: ROOT/proj


### Option 2: from source
```commandline
curl -sSL https://install.python-poetry.org | python -
export PATH="$HOME/.local/bin:$PATH" >> ~/.bash_profile
source ~/.bash_profile
git clone https://github.com/RasaHQ/rasa.git
cd rasa
poetry install
poetry update   # not included in the instruction, but good to do.
pip install rasa[full]
```

## Others
1. Jupyter notebook
```commandline
brew install jupyter
brew link --overwrite jupyterlab

```
# RASA Tutorial
- [Note for Rasa Udemy Tutorial](README_udemy_rasa_tutorial.md)

# RASA Note
### RASA Core
1. <b>Actions</b>: your bot's action (for every intent recognized by the bot).
e.g., outputing a text, a link, ...
2. <b>Stories</b>: defines <b>a sequence</b> of intents and actions.
Interaction b/w the user and bot in terms of intent and action taken by the bot.
3. <b>Templates</b>: defines all the actions.
4. <b>Slots</b>: Bot's memory. Stores the values that enable the bot to keep a track of the conversations
### Domain
A file (domain.yml) that consists of all the intents, entities, actions, slots and templates.
### Concepts
* Two systems: NLU and DP
  * NLU: understanding user's input
  * Dialogue Policies (DP): predicting the next action
* 
## Dense Note
[Note for Concepts](README_udemy_rasa_tutorial.md)

# APIs
1. [HTTP API](https://rasa.com/docs/rasa/2.x/http-api)
Besides basic functions (training, sending messages, running tests, ...), it offers authentication methods (Token Based Auth, JWT Based Auth)
2. [NLU-Only Server](https://rasa.com/docs/rasa/2.x/nlu-only-server)



