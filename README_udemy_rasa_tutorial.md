# Tutorial 1: Conversational AI with RASA [3]

### Start a rasa bot project
```commandline
python -m rasa init --init-dir proj
```

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

# References
1. RASA learning: [conversational AI with RASA](https://learning.rasa.com/conversational-ai-with-rasa)
2. https://github.com/bikashkumars/rasa
3. Udemy: [Complete Chatbot Course Using Rasa Framework & Python](https://www.udemy.com/course/the-complete-chatbot-course-using-rasa-python-nlp)
