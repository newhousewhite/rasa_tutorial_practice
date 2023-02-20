# Tutorial 1: Conversational AI with RASA [3]

### Start a rasa bot project
```commandline
python -m rasa init --init-dir proj
```

## RASA NLU
### Train
Under proj/data/nlu.yml, fill training data. Then, fill config.yml. Then
```commandline
python -m rasa train nlu
```

To test,
```commandline
python -m rasa shell nlu
```

### To use custom embedding model
Run the following to create rasa embedding model at ./spacy.word2vec.model using your data
```commandline
mkdir external_data
ln -s /Users/jangwon/exp/udemy/complete_chatbot_course_using_rasa_framework_and_python/2.\ Rasa\ NLU\ -\ Custom\ Model\ Word2Vec/external_data/word2vec_shopping.txt.gz external_data/word2vec_shopping.txt.gz
pushd external_data
python -m spacy init vectors en word2vec_shopping.txt.gz spacy.word2vec.model
popd 
```

### To handle profanity
Below python package was used in the tutorial, but has python version issue with rasa.
```commandline
pip install profanity-filter
python -m spacy download en
```
Haven't tried yet, but https://github.com/vzhou842/profanity-check.git might be another option.

## Rasa Core
* rasa use data to learn conversation patterns
* <b>Response</b>: set of words/replies the knows. Picked based on the prediction by the policies.
  * <b>Utterances</b>: hard coded messages (text, images, buttons)
  * <b>Actions</b>: defined by python code. Includes
    * calling the DB
    * calling an API
    * writing to the DB
    * do some calculation (anything you can do with this)
    * rasa_sdk.Tracker: tracks the state of actions
* <b>Story</b>: defines example conversations
  * provides training data for the Dialogue Management (DM) System of Rasa
  * use the combination of both an intent and entities, not specificcontents of the messages
* <b>Domain</b>: all your bot should know. intents, responses, what info to remember, what entities to extract

### Rasa Story, Rules and Actions
```commandline
python -m rasa train
python -m rasa run actions
```
actions server and call server are different endpoints in rasa.

Update endpoints.yml
```commandline
python -m rasa shell
```

<b>Rules</b>: always follow the same path. You can ahve conditions with Rules or have rules for conversation start. 

c.f.) <b>Stories</b> uses a probabilistic model that is generalizable to unseen conversation paths.


# References
1. RASA learning: [conversational AI with RASA](https://learning.rasa.com/conversational-ai-with-rasa)
2. https://github.com/bikashkumars/rasa
3. Udemy: [Complete Chatbot Course Using Rasa Framework & Python](https://www.udemy.com/course/the-complete-chatbot-course-using-rasa-python-nlp)
