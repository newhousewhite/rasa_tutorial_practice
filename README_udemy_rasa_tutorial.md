# Tutorial 1: Conversational AI with RASA [3]

### Rasa version migration guide:
* https://rasa.com/docs/rasa/migration-guide/#custom-policies-and-custom-components

### Start a rasa bot project
```commandline
python -m rasa init --init-dir proj
```

## RASA API
Start REST API server
```commandline
python -m rasa run actions
python -m rasa run --enable-api --cors "*" --debug --auth-token FILL_ME
```
* ```--cors *``` is for cross-origin resource sharing. It'll accept traffic from any source

Client POST request examples:
```commandline
python clients/post_requests.py
```
Note that auth-token is set at the end of url with ```?token=$FILL_ME``` when requesting

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
Interactive mode
```commandline
python -m rasa interactive
```

<b>Rules</b>: always follow the same path. You can ahve conditions with Rules or have rules for conversation start. 

c.f.) <b>Stories</b> uses a probabilistic model that is generalizable to unseen conversation paths.

### Dialogue Policies
* Data augmentation: an amount of new storeis to create from the existing stories
* Rasa crate longer stories by putting together some shorter sotries
* Improve the performance of our models
* Allows dialogue maangement to ignore history of the conversation

#### Memoization Policy
* Mimics the stories from your training data by checking story matching in your stories.yml
  * If matching, confidence = 1.0
  * If not matching, predict None with confidence 0.0
* Usually combines with other policies, cuz users do not always follow our manually created stories.
* Optimized for its precision  & not for recall
  * e.g.) if a user asked time, you'd want to trigger action_check_time.


#### RulePolicy
* allows you to add business logic.
* specific intent can be followed by a specific action, regardless of what happened in the conversation.
* An intent can only be mapped to at most one action.

#### sklearn policy
* to predict the next action
* default model: LR (you can use RF, DL, ..., instead)

#### Embedding (TEDP) policy
* Transformer Embedding Dialogue (TED) Policy
* to perdict next action
* features used:
  * what the last action was
  * what intents & entities were predicted for the current user input
  * what slots are set.
  * takes previous states of dialogue based on max_history
* learns from training stories
* good at handles chitchat

#### Fallback and Human Handoff
* See [this](https://rasa.com/docs/rasa/fallback-handoff/)

#### Policy Priority
Form -> Fallback, TwoStageFallback -> Memoization, Augmented Memoization -> Mapping -> Embedding, Keras & Sklearn
* Of course, you can change the priority.

### Slots: Bot's Memory
* define slots through
  * entities: can remember important values by users through entities
  * custom actions: info from the outside for example results extracted from the external DB.
* types:
  * text (bot only checks if provided or not, not actual string content)
  * bool (value matters, e.g., Is_authenticated)
  * categorical
  * float
  * List (if you wanna store multiple values)
  * unfeaturized
* Conditional slots:
  * something like having both laptop and phone which are followed by different slot category and slots to fill.

## Interaction with mySQL DB
install mySQL server for mac, following [this guide](https://www.geeksforgeeks.org/how-to-install-mysql-on-macos/))
After adding path of your mysql (/usr/local/mysql/bin/mysql) to `$PATH` in ~/.bash_profile
```commandline
sudo mysql -u root -p   
# Password:  # then type your macbook password
# Enter password:    # then type your mysql password you entered during installation
```
To start mysql as a root, type below
```commandline
sudo mysql -u root -p
```
add users
```commandline
CREATE USER 'rasa-user'@'localhost' IDENTIFIED BY 'password123';
```
grant permission
```commandline
GRANT ALL PRIVILEGES ON *.* TO 'rasa-user'@'localhost' WITH GRANT OPTION;
```
configure mysql
```commandline
# find where your config files are
mysql --verbose --help | grep cnf
# this didn't help find my config files.  I may have to change config later
```
create DB
```commandline
CREATE DATABASE shopping_db;
```
write data to SQL DB
```commandline
python -m pip install mysql-connector-python
```
install mysql connector in mac
(ref: https://ruddra.com/install-mysqlclient-macos/)
For connecting any other application to MySQL, you need to install a connector. You can do it like this:
```commandline
brew install mysql-connector-c
echo 'export PATH="/usr/local/opt/mysql-client/bin:$PATH"' >> /Users/jangwon/.bash_profile
echo -e 'export LDFLAGS="-L/usr/local/opt/mysql-client/lib"' >> /Users/jangwon/.bash_profile
echo -e 'export CPPFLAGS="-I/usr/local/opt/mysql-client/include"' >> /Users/jangwon/.bash_profile
echo -e 'export PKG_CONFIG_PATH="/usr/local/opt/mysql-client/lib/pkgconfig"' >> /Users/jangwon/.bash_profile
xcode-select --install
brew install openssl
echo 'export PATH="/usr/local/opt/openssl@3/bin:$PATH"' >> /Users/jangwon/.bash_profile
echo -e 'export LDFLAGS="-L/usr/local/opt/openssl@3/lib"' >> /Users/jangwon/.bash_profile
echo -e 'export CPPFLAGS="-I/usr/local/opt/openssl@3/include"' >> /Users/jangwon/.bash_profile
echo -e 'export PKG_CONFIG_PATH="/usr/local/opt/openssl@3/lib/pkgconfig"' >> /Users/jangwon/.bash_profile
echo -e 'export LIBRARY_PATH=$LIBRARY_PATH:/usr/local/opt/openssl/lib/' >> /Users/jangwon/.bash_profile
brew unlink mysql
brew link --overwrite mysql-connector-c --force
echo 'export PATH="/usr/local/opt/mysql-client/bin:$PATH"' >> /Users/jangwon/.bash_profile
python -m pip install mysqlclient
brew unlink mysql-connector-c
brew link --overwrite mysql
python -m pip install mysqlclient
```
using mysql client in python: see [this youtube tutorial](https://www.youtube.com/watch?v=DdzIlzCfu4I)

# How to create messenger bot
## ngrok
see https://ngrok.com/docs/getting-started/ for mac OS and Linux
go to https://dashboard.ngrok.com/get-started/your-authtoken, and get your authtoken. Then configure your ngrok as follows:
```commandline
ngrok config add-authtoken FILL ME
```
Then, start your ngrok http
```commandline
cd server
bash run_ngrok.sh
```
Then, put your ngrok forwarding address to webhook of credentials.yml

Instead of `ngrok config add-authtoken`, 
## telegram
* BotFather -> /start -> jk_udemy_tutorial_bot ->  

# Debug Tips
* Question 1: Entity recognition doesn't work well.
  * A) Entity recognition looks at the context around the entity. So, it's important to add context around entity. If context is not provided in user's response, use custom slot mapping.

# References
1. RASA learning: [conversational AI with RASA](https://learning.rasa.com/conversational-ai-with-rasa)
2. https://github.com/bikashkumars/rasa
3. Udemy: [Complete Chatbot Course Using Rasa Framework & Python](https://www.udemy.com/course/the-complete-chatbot-course-using-rasa-python-nlp)
4. [Containers code for the learning center course](https://github.com/RasaHQ/conversational-ai-course-3.x)